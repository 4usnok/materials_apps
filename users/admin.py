from django.contrib import admin

from course.models import Subscription
from users.models import User, Payments, Product, Price


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_filter = ("id", "user")


@admin.register(Subscription)
class PaymentsAdmin(admin.ModelAdmin):
    list_filter = ("user", "course")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ("name", "description", "link")


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_filter = ("unit_amount", "unit_amount", "currency")
