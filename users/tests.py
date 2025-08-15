from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from course.models import Lesson, Course
from users.models import User


class LessonsCreateTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="kakas@gmail.com",
            email="kaka@gmail.com",
            password="kakas123",
            is_active=True
        )
        self.course = Course.objects.create(
            title="Программирование"
        )
        self.client = APIClient()

    def test_create_lesson(self):
        """ Тестирование создания урока """
        self.client.force_authenticate(user=self.user)
        url = reverse("course:lessons_create")
        data = {
                "title": "Основы python",
                "course": self.course.id,
                "url_on_video": "https://www.youtube.com/",
            }
        response = self.client.post(url, data)

        # проверка статус кода
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # проверка содержимого критичных полей post-запроса
        response_data = response.json()
        self.assertEqual(response_data["title"], "Основы Python")
        self.assertEqual(response_data["course"], self.course.id)

        # проверка записи в БД
        self.assertTrue(
            Lesson.objects.filter(title='Основы python').exists()
        )
    #
    #
    # def test_update_lesson(self):
    #     """ Тестирование редактирования урока """
    #     pass
    #
    # def test_obj_lesson(self):
    #     """ Тестирование просмотра одного урока """
    #     pass
    #
    # def test_delete_lesson(self):
    #     """ Тестирование удаления урока """
    #     pass
