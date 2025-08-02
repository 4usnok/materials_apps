from rest_framework import serializers

from course.models import Course, Lesson


class CourseSerializers(serializers.ModelSerializer):
    quant_les = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_quant_les(self, obj):
        return obj.lesson_set.count()

class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'