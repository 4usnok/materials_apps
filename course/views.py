from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from course.models import Course, Lesson
from course.paginators import PageNumberPagination
from course.serializers import CourseSerializers, LessonSerializers
from users.permissions import IsModer, IsOwner


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
        queryset = super().get_queryset()
        if not self.request.user.groups.filter(
            name="moders"
        ).exists():  # если не входит в группу модеров
            return queryset.filter(
                owner=self.request.user
            )  # показать для владельцев только их объекты
        return queryset  # А, если входит, то весь список


class LessonAPIView(generics.ListAPIView):
    """Просмотр списка уроков"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
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
        lesson = instance.save(owner=self.request.user)
        lesson.user = self.request.user
        lesson.save()
