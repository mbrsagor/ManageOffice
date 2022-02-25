from rest_framework import serializers

from office.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'name', 'description', 'budget', 'client_name', 'reference_name', 'date_line',
            'payment_status', 'is_active', 'status', 'document', 'image', 'start_day', 'created_at', 'updated_at'
        ]
