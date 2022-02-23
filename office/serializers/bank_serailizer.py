from rest_framework import serializers
from office.models import Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            'id',
            'name',
            'is_active',
            'created_at',
            'updated_at',
        ]

    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Name should be more than 5 characters")
        return value
