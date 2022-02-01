from rest_framework import views, status, permissions
from rest_framework.response import Response

from .models import User
from .serializers import UserCreateSerializer
from utils.response import prepare_create_success_response, prepare_error_response
from services.auth_validation_service import create_use_validation


class UserRegistrationAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        validate_error = create_use_validation(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_404_NOT_FOUND)
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
