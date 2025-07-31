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
    path('lesson/', LessonAPIView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonAPICreate.as_view(), name='lesson_create'),
    path('lesson/update/<int:pk>', LessonAPIUpdate.as_view(), name='lesson_update'),
    path('lesson/destroy/<int:pk>', LessonAPIDestroy.as_view(), name='lesson_destroy'),
    path('lesson/update/<int:pk>', LessonList.as_view(), name='lesson_update'),
] + router.urls