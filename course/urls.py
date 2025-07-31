from django.urls import path
from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig
from course.views import CourseViewSet
from lesson.views import LessonAPIView, LessonAPICreate, LessonAPIUpdate, LessonAPIDestroy, LessonList

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
urlpatterns = router.urls

urlpatterns = [] + router.urls