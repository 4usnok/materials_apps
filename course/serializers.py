from rest_framework import serializers

from course.models import Course, Lesson, Subscription

from course.validators import validate_url


class LessonSerializers(serializers.ModelSerializer):
    """Сериализатор для модели 'Lesson'"""

    url_on_video = serializers.URLField(validators=[validate_url])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializers(serializers.ModelSerializer):
    """Сериализатор для модели 'Course'"""

    quant_les = serializers.SerializerMethodField()
    conclusion_of_lessons = LessonSerializers(
        source="lesson_set", read_only=True, many=True
    )
    subscription_activate = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_quant_les(self, obj):
        """Проверка количества уроков в курсе"""
        return obj.lesson_set.count()

    def get_subscription_activate(self, obj):
        """Проверка подписки на курс"""
        request = self.context.get("request")  # Получаем request из контекста
        if not request or not request.user.is_authenticated:
            return False
        # Проверяем подписку
        return Subscription.objects.filter(user=request.user, course=obj).exists()
