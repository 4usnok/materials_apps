from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from course.models import Course, Lesson
from course.serializers import CourseSerializers, LessonSerializers


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD для модели 'Course'"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAuthenticated]


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


class LessonAPIUpdate(generics.UpdateAPIView):
    """Редактирование урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]


class LessonList(generics.RetrieveAPIView):
    """Просмотр отдельного урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]


class LessonAPIDestroy(generics.DestroyAPIView):
    """Удаление урока"""

    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
