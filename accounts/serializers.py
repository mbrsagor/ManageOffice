from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'})
    confirm_password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Confirm Password'})

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'pin', 'employee', 'role', 'password', 'confirm_password'
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise ValueError({'password': 'Sorry! password not match'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            pin=validated_data['employee'],
            employee=validated_data['employee'],
            role=validated_data['role'],
            password=validated_data['password'],
            confirm_password=validated_data['confirm_password'],
        )
        return user
