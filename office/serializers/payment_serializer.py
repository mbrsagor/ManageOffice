from rest_framework import serializers

from office.models import Payment
from user.serializers import UserSerializer
from office.serializers.bank_serailizer import BankSerializer


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'title',
            'user',
            'bank_name',
            'pay_purpose',
            'status',
            'amount',
            'month',
            'created_at',
            'updated_at',
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        response['bank_name'] = BankSerializer(instance.bank_name).data
        return response


    # def validate_month(self, value):
    #     if len(value) <= 10:
    #         raise serializers.ValidationError("Salary has been already payment")
