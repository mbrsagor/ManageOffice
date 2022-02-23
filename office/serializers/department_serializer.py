from rest_framework import serializers
from office.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'id',
            'name',
            'is_active',
            'created_at',
            'updated_at',
        ]

    def validate_name(self, value):
        if len(value) <= 3:
            raise serializers.ValidationError("Name should be more than 2 characters")
        return value
