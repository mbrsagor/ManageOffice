from rest_framework import serializers

from base.models.office import Office


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = (
            'id', 'name', 'employee', 'code', 'logo', 'created_at', 'updated_at'
        )
