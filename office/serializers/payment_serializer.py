from rest_framework import serializers

from office.models import Payment


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

    # def validate_title(self, value):
    #     if len(value) <= 10:
    #         raise serializers.ValidationError("Name should be more than 10 characters")
