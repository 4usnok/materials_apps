from rest_framework import serializers

from users.models import Payments, User, Product, Price


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class PriceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ["currency", "unit_amount"]


class SessionSerializers(serializers.Serializer):
    session = serializers.CharField(max_length=50)
