from rest_framework import serializers

from users.models import Payments, User, Subscription


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"

class SubscriptionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"
