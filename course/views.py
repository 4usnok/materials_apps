from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from course.models import Course, Lesson
from course.serializers import CourseSerializers, LessonSerializers
from users.permissions import IsModer, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD для модели 'Course'"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    def get_permissions(self):
        """Права для разрешения доступа модераторам и владельцам """
        # ["update", "retrieve", "partial_update"]
        if self.action in ["update", "retrieve", "partial_update"]:
            # Права для редактирования курса, доступа к определенному курсу
            # и возможности изменять некоторые поля курса
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]
        elif self.action in ["create", "destroy"]:
            # Права для создания нового курса или удаления
            self.permission_classes = [IsAuthenticated, ~IsModer, IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save(owner=self.request.user)
        course.user = self.request.user
        course.save()

    def perform_update(self, serializer):
        course = serializer.save(owner=self.request.user)
        course.user = self.request.user
        course.save()

    def perform_destroy(self, instance):
        course = instance.save(owner=self.request.user)
        course.user = self.request.user
        course.save()


class LessonAPIView(generics.ListAPIView):
    """Просмотр списка уроков"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]


class LessonAPICreate(generics.CreateAPIView):
    """Создание урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        lesson = serializer.save(owner=self.request.user)
        lesson.user = self.request.user
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
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        lesson = instance.save(owner=self.request.user)
        lesson.user = self.request.user
        lesson.save()
