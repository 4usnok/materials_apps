from rest_framework import viewsets, generics
from course.models import Course, Lesson
from course.serializers import CourseSerializers, LessonSerializers


class CourseViewSet(viewsets.ModelViewSet):
    """ ViewSet CRUD для модели 'Course' """
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

class LessonAPIView(generics.ListAPIView):
    """ Просмотр списка уроков """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers

class LessonAPICreate(generics.CreateAPIView):
    """ Создание урока """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers

class LessonAPIUpdate(generics.UpdateAPIView):
    """ Редактирование урока """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers

class LessonList(generics.RetrieveAPIView):
    """ Просмотр отдельного урока """
    queryset = Lesson.objects.all()
    serializer_class = PaymentsSerializers

class LessonAPIDestroy(generics.DestroyAPIView):
    """ Удаление урока """
    queryset = Lesson.objects.all()
