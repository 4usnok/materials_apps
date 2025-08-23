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
* Модель курса `Course`
* Модель урока `Lesson`
* Модель подписки `Subscription`

2. Содержит `serializers.py`:
* Сериализатор для модели `Lesson` -> `LessonSerializers`
* Сериализатор для модели `Course` -> `CourseSerializers`
* Сериализатор для модели `Course` -> `CourseSerializers`
3. Содержит `views.py`:
* `CourseViewSet` -> ViewSet CRUD для модели `Course`
* `LessonAPIView` -> Просмотр списка уроков
* `LessonAPICreate` -> Создание урока
* `LessonAPIUpdate` -> Редактирование урока
* `LessonList` -> Просмотр отдельного урока
* `LessonAPIDestroy` -> Удаление урока
* `SubscriptionActivate` -> Активация подписки
4. Содержит `permissions.py` -> классы прав доступа для групп админки
5. Содержит `paginators.py` -> для создания пагинации просмотра объектов
6. Содержит `tests.py` -> для тестов
7. Содержит `validators.py` -> для создания валидации
8. Содержит `tasks.py` -> для периодических задач:
* `send_info_about_update_course` -> функция для отправки сообщения на электронную почту
* `check_login_user` -> функция изменения статуса на неактивный, в случае, если пользователь не был онлайн не меньше месяца


## Приложение `users`
Приложение предназначенное для работы с пользователями и платежами
1. Содержит `models.py`:
* Модель пользователя `User`
* Модель платежа `Payments`
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
4. Содержит `services.py` -> для сервисных функций:
* Содержит сервисную функцию `create_product` -> для создания продукта
* Содержит сервисную функцию `create_price` -> для создания цены
* Содержит сервисную функцию `create_session_to_url` -> для создания сессии для получения ссылки на оплату
5. Содержит `permission.py` -> для прав доступа:
* Содержит `has_permission` -> для разрешения доступа только модераторам
* Содержит `IsOwner` -> для разрешения доступа только владельцам


## Прочие файлы
1. `.env.sample` -> Заполняется в первую очередь(предназначен для заполнений host, port, пароля от бд, названия бд и тд.)
2. `payments_fixture.json` -> содержит json-файлы модели `Payments`
3. `users_fixture.json` -> содержит json-файлы модели `User`
4. `Readme.md` -> содержит описание проекта

# Полезные команды
* Запуск сервера: `python manage.py runserver`,
* Создание суперюзера(админка): `python manage.py createsuperuser`,
* Создание миграций: `python manage.py makemigrations`,
* Сохранение миграций: `python manage.py migrate`,
* Откат всех миграций: `python manage.py migrate name_migration`, где `name_migration` -> название миграции.
* Создание фикстуры для модели пользователей `User`: `python -Xutf8 manage.py dumpdata users.User --output users_fixture.json --indent 4`
* Создание фикстуры для модели платежей `Payments`: `python -Xutf8 manage.py dumpdata users.Payments --output payments_fixture.json --indent 4`
* Создания файла с покрытием `.coverage`: `coverage run --source='.' manage.py test`
* Посмотреть покрытие unit-тестами: `coverage report`
* Запуск обработчика очереди (worker) для получения задач и их выполнения: `celery -A config worker -l INFO`
