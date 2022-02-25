from rest_framework import serializers

from office.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id', 'name', 'phn_num', 'email', 'address', 'organization',
            'created_at', 'updated_at'
        ]
