from rest_framework import viewsets
from course.models import Course
from course.serializers import CourseSerializers


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
