from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Confirm Password'}, write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'pin', 'employee', 'role', 'password', 'password2'
        )

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('password2')
        if password != confirm_password:
            raise ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            pin=validated_data['pin'],
            employee=validated_data['employee'],
            role=validated_data['role'],
            password=validated_data['password'],
        )
        return user
