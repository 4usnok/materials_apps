from django.urls import path
from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig
from course.views import (
    CourseViewSet,
    LessonAPICreate,
    LessonAPIDestroy,
    LessonAPIUpdate,
    LessonAPIView,
    LessonList,
    SubscriptionActivate,
)

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("lessons/", LessonAPIView.as_view(), name="lessons_list"),
    path("lessons/create/", LessonAPICreate.as_view(), name="lessons_create"),
    path("lessons/update/<int:pk>", LessonAPIUpdate.as_view(), name="lessons_update"),
    path(
        "lessons/destroy/<int:pk>", LessonAPIDestroy.as_view(), name="lessons_destroy"
    ),
    path("lessons/detail/<int:pk>", LessonList.as_view(), name="lessons_detail"),
    path("subscription/", SubscriptionActivate.as_view(), name="subscription_activate"),
] + router.urls
