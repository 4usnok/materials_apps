from rest_framework import serializers

from course.models import Course, Lesson


class LessonSerializers(serializers.ModelSerializer):
    """Сериализатор для модели 'Lesson'"""

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializers(serializers.ModelSerializer):
    """Сериализатор для модели 'Course'"""

    quant_les = serializers.SerializerMethodField()
    conclusion_of_lessons = LessonSerializers(
        source="lesson_set", read_only=True, many=True
    )

    class Meta:
        model = Course
        fields = "__all__"

    def get_quant_les(self, obj):
        return obj.lesson_set.count()
