from rest_framework import serializers
from office.models import Designation


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = [
            'id',
            'name',
            'is_active',
            'created_at',
            'updated_at',
        ]

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name should be more than 1 characters")
        return value
