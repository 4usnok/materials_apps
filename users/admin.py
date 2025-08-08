from django.contrib import admin

from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")

@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_filter = ("id", "user")
