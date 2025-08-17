from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from course.models import Lesson, Course
from users.models import User, Subscription


class LessonsCreateTestCase(APITestCase):

    def setUp(self):
        """ Подготовка данных """
        self.user = User.objects.create_user(
            username="kakas@gmail.com",
            email="kaka@gmail.com",
            password="kakas123",
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


    def test_create_lesson(self):
        """ Тестирование создания урока """
        url = reverse("course:lessons_create")
        data = {
                "title": "Основы Python",
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
            Lesson.objects.filter(title='Основы Python').exists()
        )


    def test_retrieve_lesson(self):
        """ Тестирование просмотра отдельного урока """
        url = reverse("course:lessons_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = {
                "course": self.course,
                "url_on_video": "https://www.youtube.com/",
                "title": "Основы Django",
                "owner": self.user.id
            }

        # проверка статус кода
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # проверка содержимого json
        self.assertEqual(data.get("title"), self.lesson.title)


    def test_update_lesson(self):
        """ Тестирование редактирования урока """
        url = reverse("course:lessons_update", args=(self.lesson.pk,))
        update_data = {
                "title": "Основы ООП",
                "owner": self.user.id
            }

        # отправляем обновлённые данные
        response = self.client.patch(url, update_data)
        data = response.json()

        # проверка статус кода
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # проверка содержимого json
        self.assertEqual(data.get("title"), "Основы ООП")


    def test_delete_lesson(self):
        """ Тестирование удаления урока """
        url = reverse("course:lessons_destroy", args=(self.lesson.pk,))
        response = self.client.delete(url)

        # проверка статус кода
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # проверка количества уроков после удаления
        self.assertEqual(Lesson.objects.count(), 0)

    def test_list_lessons(self):
        """ Тестирование просмотра списка уроков """
        url = reverse("course:lessons_list")
        response = self.client.get(url)

        # проверка статус кода
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_activate_subscription(self):
        """ Тестирование активированной подписки """
        url = reverse("course:subscription_activate")

        # данные для активированной подписки
        data_for_activate = {
                "course_id": self.course.id,
                "subscription_activate": True
             }
        response_for_activ_subs = self.client.post(
            url,
            data_for_activate,
            format='json'
        )

        # тестирование статус кода активации подписки
        self.assertEqual(
            response_for_activ_subs.status_code, status.HTTP_200_OK
        )
        # тестирование активированной подписки
        response_data = response_for_activ_subs.json()
        print(response_data)

        self.assertTrue(
            response_data
        )

    def test_delete_subscription(self):
        """ Тестирование удаления подписки """
        Subscription.objects.create(user=self.user, course=self.course) # создадим подписку
        url = reverse("course:subscription_activate")

        # данные для деактивации подписки
        data_for_deactivate_subs = {
                "course_id": self.course.id,
                "subscription_activate": False
             }
        response_for_activ_subs = self.client.post(
            url,
            data_for_deactivate_subs,
            format='json'
        )

        # тестирование статус кода деактивации подписки
        self.assertEqual(
            response_for_activ_subs.status_code, status.HTTP_200_OK
        )
        # тестирование деактивированной подписки
        response_data_deactivate = response_for_activ_subs.json()
        print(response_data_deactivate)
        self.assertFalse(
            response_data_deactivate.get("subscription_activate"), "подписка удалена"
        )

    def test_unauthorized_access(self):
        """ Тестирование ошибки 401 для неавторизованных пользователей """
        self.client.force_authenticate(user=None)
        url = reverse("course:lessons_detail", args=(self.lesson.pk,))
        response = self.client.get(url)

        # тестирование статус для неавторизованного пользователя
        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED
        )

