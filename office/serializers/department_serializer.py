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
