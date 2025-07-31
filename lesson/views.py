from rest_framework import generics

from lesson.models import Lesson
from lesson.serializers import LessonSerializers

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

class LessonAPIDestroy(generics.DestroyAPIView):
    """ Удаление урока """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers

class LessonList(generics.RetrieveAPIView):
    """ Просмотр отдельного урока """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
