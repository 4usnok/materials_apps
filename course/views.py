from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission

from course.models import Course, Lesson
from course.serializers import CourseSerializers, LessonSerializers
from users.permissions import ModeratorRights


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD для модели 'Course'"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    def get_permissions(self):
        """Права для разрешения доступа модераторам"""
        if (
            self.action == "list"
            or self.action == "update"
            or self.action == "retrieve"
            or self.action == "partial_update"
        ):
            # Права для просмотра списка курсов, редактирования курса, доступа к одному курсу
            # и возможности изменять некоторые поля курса
            self.permission_classes = [IsAuthenticated, ModeratorRights]
        elif self.action == "create" or self.action == "destroy":
            # Права для создания нового курса или удаления
            self.permission_classes = [IsAuthenticated]


class LessonAPIView(generics.ListAPIView):
    """Просмотр списка уроков"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated, ModeratorRights]


class LessonAPICreate(generics.CreateAPIView):
    """Создание урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]


class LessonAPIUpdate(generics.UpdateAPIView):
    """Редактирование урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated, ModeratorRights]


class LessonList(generics.RetrieveAPIView):
    """Просмотр отдельного урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated, ModeratorRights]


class LessonAPIDestroy(generics.DestroyAPIView):
    """Удаление урока"""

    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
