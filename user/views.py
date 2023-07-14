from rest_framework.response import Response
from rest_framework import views, status, permissions, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from utils import response
from .models import Profile
from utils.message import LOGOUT_MSG, NO_ID
from .serializers import ProfileSerializer, UserSerializer, RegistrationSerializer, PasswordChangeSerializer


class UserRegistrationAPIView(views.APIView):
    """
    Name: user registration API
    Method: POST
    URL: /api/user/registration/
    """
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(response.prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(response.prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(response.prepare_error_response(str(ex)), status=status.HTTP_403_FORBIDDEN)


class LoginAPIView(ObtainAuthToken):
    """
    Name: user login API
    Method: POST
    URL: /api/user/login/
    """
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])
            user = serializer.validated_data['user']
            return Response(response.prepare_signin_success_response(token.key, user.pk), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(response.prepare_error_response(str(ex)), status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(views.APIView):
    """
    Name: user profile API
    Method: GET
    URL: /api/user/profile/
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        try:
            profile = Profile.objects.get(id=self.request.user.id)
            serializer = ProfileSerializer(profile)
            return Response(response.prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            user = User.objects.get(id=self.request.user.id)
            if user is not None:
                serializer = UserSerializer(user)
                return Response(response.prepare_success_response(serializer.data), status=status.HTTP_200_OK)
            return Response(response.prepare_error_response(str(e)), status=status.HTTP_200_OK)


class ProfileUpdateAPIView(views.APIView):
    """
    Name: user profile update API
    Method: PUT
    URL: /api/user/profile/<pk>/
    """
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, pk):
        try:
            profile = Profile.objects.get(id=pk)
            if profile is not None:
                serializer = ProfileSerializer(profile, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(user=request.user)
                    return Response(response.prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
                return Response(response.prepare_create_success_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(response.prepare_error_response(NO_ID), status=status.HTTP_403_FORBIDDEN)
        except Exception as ex:
            return Response(response.prepare_error_response(str(ex)), status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    """
    Name: user change password API
    Method: PUT
    URL: /api/user/password-change/<pk>/
    """
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PasswordChangeSerializer

    def update(self, request, *args, **kwargs):
        try:
            serializer = PasswordChangeSerializer()
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=self.request.user)
                return Response(response.prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(response.prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(response.prepare_error_response(str(ex)), status=status.HTTP_403_FORBIDDEN)


class LogoutAPIView(views.APIView):
    """
    Name: user logout API
    Method: GET
    URL: /api/user/logout/
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        try:
            request.user.auth_token.delete()
            return Response(response.prepare_success_response(LOGOUT_MSG), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(response.prepare_error_response(str(ex)), status=status.HTTP_400_BAD_REQUEST)
