import datetime
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
        fields = (
            '__all__'
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'date_of_birth', 'gender', 'nid_number', 'phn_num', 'emergency_phn_num',
            'address', 'employee', 'bank_account', 'bank_name', 'eduction', 'documents',
            'profile_picture', 'created_at', 'updated_at'
        ]


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
