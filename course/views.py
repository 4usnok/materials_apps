from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from course.models import Course, Lesson, Subscription
from course.paginators import PageNumberPagination
from course.serializers import CourseSerializers, LessonSerializers
from course.tasks import send_info_about_update_course
from users.permissions import IsModer, IsOwner

from rest_framework.response import Response
from rest_framework.views import APIView


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD для модели 'Course'"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_permissions(self):
        """Права для разрешения доступа модераторам и владельцам"""
        if self.action in ["update", "retrieve", "partial_update"]:
            # Права для редактирования курса, доступа к определенному курсу
            # и возможности изменять некоторые поля курса
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]
        elif self.action == "create":
            # Права для создания имеет авторизованный пользователь, но не модератор
            self.permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action == "destroy":
            # Права для удаления имеет авторизованный пользователь - владелец
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save(owner=self.request.user)
        course.save()

    def get_queryset(self):
        """Права доступа"""
        queryset = super().get_queryset()
        if not self.request.user.groups.filter(
            name="moders"
        ).exists():  # если не входит в группу модеров
            return queryset.filter(
                owner=self.request.user
            )  # показать для владельцев только их объекты
        return queryset  # А, если входит, то весь список

    @action(detail=True, methods=("patch",))
    def course_update(self, request, pk):
        """Обновление курса"""
        course = get_object_or_404(Course, pk=pk)

        # Проверка прав
        if course.owner != request.user:
            return Response({"error": "У вас нет прав для редактирования этого курса"})

        # Обновление данных
        serializer = self.get_serializer(
            course,
            data=request.data,  # данные из запроса
            partial=True,  # разрешаем частичное обновление
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Отправка уведомления если обновил НЕ владелец
        send_info_about_update_course.delay(course.owner.email)

        return Response(data=serializer.data)


class LessonAPIView(generics.ListAPIView):
    """Просмотр списка уроков"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        """Права доступа"""
        queryset = super().get_queryset()
        if not self.request.user.groups.filter(
            name="moders"
        ).exists():  # если не входит в группу модеров
            return queryset.filter(
                owner=self.request.user
            )  # показать для владельцев только их объекты
        return queryset  # А, если входит, то весь список


class LessonAPICreate(generics.CreateAPIView):
    """Создание урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        lesson = serializer.save(owner=self.request.user)
        lesson.save()


class LessonAPIUpdate(generics.UpdateAPIView):
    """Редактирование урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated, IsModer | IsOwner]

    def perform_update(self, serializer):
        lesson = serializer.save(owner=self.request.user)
        lesson.user = self.request.user
        lesson.save()


class LessonList(generics.RetrieveAPIView):
    """Просмотр отдельного урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonAPIDestroy(generics.DestroyAPIView):
    """Удаление урока"""

    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_destroy(self, instance):
        instance.delete()


class SubscriptionActivate(APIView):
    """Активация подписки"""

    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        """Добавление или удаление подписки"""
        user = self.request.user
        course_item = get_object_or_404(Course, pk=self.request.data.get("course_id"))

        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "подписка добавлена"
        return Response({"message": message})
