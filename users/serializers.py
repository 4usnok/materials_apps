from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Payments, User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"
