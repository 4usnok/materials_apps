# lms-приложение: платформа для онлайн обучения

SPA веб-приложение, где бэкенд-сервер возвращает клиенту JSON-структуры. 
LMS-система, в которой каждый желающий может размещать свои полезные материалы или курсы.

# Инструкция по установке и использованию разработанного функционала приложения
1. Клонируйте репозиторий:
```
git clone https://github.com/4usnok/DZ5_DRF_materials_apps.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
# Содержание проекта
## Приложение `course`
Приложение предназначенное для работы с курсом и уроками
1. Содержит `models.py`:
* модель курса `Course`
* модель курса `Lesson`
2. Содержит `serializers.py`:
* Сериализатор для модели `Lesson` -> `LessonSerializers`
* Сериализатор для модели `Course` -> `CourseSerializers`
3. Содержит `views.py`:
* `CourseViewSet` -> ViewSet CRUD для модели `Course`
* `LessonAPIView` -> Просмотр списка уроков
* `LessonAPICreate` -> Создание урока
* `LessonAPIUpdate` -> Просмотр отдельного урока
* `LessonAPIDestroy` -> Удаление урока

## Приложение `users`
Приложение предназначенное для работы с пользователями и платежами
1. Содержит `models.py`:
* модель пользователя `User`
* модель пользователя `Payments`
2. Содержит `serializers.py`:
* Сериализатор для модели `User` -> `UserSerializers`
* Сериализатор для модели `Payments` -> `PaymentsSerializers`
3. Содержит `views.py`:
* `UserViewSet` -> ViewSet CRUD для модели `User`
* `PaymentsListAPIView` -> Фильтрация и сортировка платежей
* `PaymentsAPICreate` -> Создание платежа
* `PaymentsAPIUpdate` -> Редактирование платежа
* `PaymentsDetailList` -> Просмотр отдельного платежа
* `PaymentsAPIDestroy` -> PaymentsAPIDestroy

# Полезные команды
Полезные команды
* Запуск сервера: `python manage.py runserver`,
* Создание суперюзера(админка): `python manage.py createsuperuser`,
* Создание миграций: `python manage.py makemigrations`,
* Сохранение миграций: `python manage.py migrate`,
* Откат всех миграций: `python manage.py migrate name_migration`, где `name_migration` -> название миграции.
* Создание фикстуры для модели пользователей `User`: `python -Xutf8 manage.py dumpdata users.User --output users_fixture.json --indent 4`
* Создание фикстуры для модели платежей `Payments`: `python -Xutf8 manage.py dumpdata users.Payments --output payments_fixture.json --indent 4`