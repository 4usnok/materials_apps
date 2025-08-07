from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import (PaymentsAPICreate, PaymentsAPIDestroy,
                         PaymentsAPIUpdate, PaymentsListAPIView,
                         UserViewSet, PaymentsDetailList)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    # payments
    path("payments/", PaymentsListAPIView.as_view(), name="payments-list"),
    path("payments/create/", PaymentsAPICreate.as_view(), name="payments-create"),
    path(
        "payments/update/<int:pk>", PaymentsAPIUpdate.as_view(), name="Payments-update"
    ),
    path(
        "payments/destroy/<int:pk>",
        PaymentsAPIDestroy.as_view(),
        name="Payments-destroy",
    ),
    path("payments/detail/<int:pk>", PaymentsDetailList.as_view(), name="Payments-detail"),
] + router.urls
