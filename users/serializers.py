from django.utils.timezone import now
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

    subscript_result = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        read_only_fields = ["user", "course"]

    def get_subscript_result(self, obj):
        if obj.is_active:
            return 'подписка добавлена'
        else:
            return 'подписка удалена'


