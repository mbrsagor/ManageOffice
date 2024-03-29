from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    """User basic serializer"""
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name',
            'last_name', 'is_superuser', 'is_active'
        )


class RegistrationSerializer(serializers.ModelSerializer):
    """
    User create/registration serializer with validation
    """
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def validate_username(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("username should be more than 2 characters")
        return value

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Duplicate")
        return lower_email


class ProfileSerializer(serializers.ModelSerializer):
    """
    User profile serializer
    """
    class Meta:
        read_only_fields = ('user',)
        model = Profile
        fields = '__all__'


class PasswordChangeSerializer(serializers.ModelSerializer):
    """
    user can change his/her password after login
    """
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'pk', 'old_password', 'new_password', 'confirm_password'
        ]

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
