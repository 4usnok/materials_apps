from django.contrib import admin

from course.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ("id", "title")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_filter = ("id", "title")
