from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    PaymentsAPICreate,
    PaymentsAPIDestroy,
    PaymentsAPIUpdate,
    PaymentsListAPIView,
    UserViewSet,
    PaymentsDetailList,
    UserCreateAPIView,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    # auth and register
    path(
        "register/", UserCreateAPIView.as_view(), name="register"
    ),
    path(
        "login/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # payments
    path("payments/", PaymentsListAPIView.as_view(), name="payments-list"),
    path("payments/create/", PaymentsAPICreate.as_view(), name="payments-create"),
    path(
        "payments/update/<int:pk>", PaymentsAPIUpdate.as_view(), name="payments-update"
    ),
    path(
        "payments/destroy/<int:pk>",
        PaymentsAPIDestroy.as_view(),
        name="payments-destroy",
    ),
    path(
        "payments/detail/<int:pk>", PaymentsDetailList.as_view(), name="payments-detail"
    ),
] + router.urls
