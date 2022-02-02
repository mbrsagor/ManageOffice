import datetime

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.utils import datetime_to_epoch
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Profile

SUPERUSER_LIFETIME = datetime.timedelta(minutes=90)


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'}),
    password2 = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Confirm Password'},
                                      write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'pin', 'role', 'password', 'password2'
        )

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('password2')
        if password != confirm_password:
            raise ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            pin=validated_data['pin'],
            role=validated_data['role'],
            password=validated_data['password'],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'pin', 'email', 'role', 'last_login', 'is_superuser', 'is_staff'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'date_of_birth', 'gender', 'nid_number', 'phn_num', 'emergency_phn_num',
            'address', 'employee', 'bank_account', 'bank_name', 'eduction', 'documents',
            'profile_picture', 'created_at', 'updated_at'
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        token['user_id'] = user.id
        token['name'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_active'] = user.is_active
        if user:
            token.payload['exp'] = datetime_to_epoch(token.current_time + SUPERUSER_LIFETIME)
            return token


class PasswordChangeSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'id', 'old_password', 'new_password', 'confirm_password'
        )

    def validate(self, attrs):
        """
        When user given new password & confirm password wrong the method will call.
        :param attrs: new password and confirm password
        :return: user_id
        """
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Sorry! password not match'})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        """
        When user input new password this method will save the password database.
        :param instance:
        :param validated_data:
        :return:
        """
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
