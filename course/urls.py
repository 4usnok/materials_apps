from django.urls import path
from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig
from course.views import CourseViewSet
from lesson.views import LessonAPIView, LessonAPICreate, LessonAPIUpdate, LessonAPIDestroy, LessonList

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
urlpatterns = router.urls

urlpatterns = [
    path('course/', LessonAPIView.as_view(), name='course_list'),
    path('course/create/', LessonAPICreate.as_view(), name='course_create'),
    path('course/update/<int:pk>', LessonAPIUpdate.as_view(), name='course_update'),
    path('course/destroy/<int:pk>', LessonAPIDestroy.as_view(), name='course_destroy'),
    path('course/update/<int:pk>', LessonList.as_view(), name='course_update'),
] + router.urls