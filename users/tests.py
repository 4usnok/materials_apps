from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from course.models import Lesson, Course
from users.models import User


class SubscriptionCreateTestCase(APITestCase):

    def setUp(self):
        """ Подготовка данных """
        self.user = User.objects.create_user(
            username="kakas@gmail.com",
            email="kaka@gmail.com",
            password="kakas123",
            is_active=True
        )
        self.course = Course.objects.create(
            title="Программирование",
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            course=self.course,
            url_on_video="https://www.youtube.com/",
            title="Основы Django",
            owner=self.user
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_subscription(self):
        """ Тестирование активации подписки """
        url = reverse("users:subscription_activate")
        response = self.client.post(
            url,
            {"course_id": self.course.id},
            format='json'
        )

        # проверка статус кода
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
