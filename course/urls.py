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
    path('', LessonAPIView.as_view(), name='lesson_list'),
    path('create/', LessonAPICreate.as_view(), name='lesson_create'),
    path('update/<int:pk>', LessonAPIUpdate.as_view(), name='lesson_update'),
    path('destroy/<int:pk>', LessonAPIDestroy.as_view(), name='lesson_destroy'),
    path('detail/<int:pk>', LessonList.as_view(), name='lesson_detail'),
] + router.urls