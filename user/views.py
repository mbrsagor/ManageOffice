from rest_framework import views, status, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from utils.response import prepare_success_response, prepare_create_success_response, prepare_error_response


class ProfileAPIView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        try:
            queryset = Profile.objects.get(id=self.request.user.id)
            serializer = ProfileSerializer(queryset)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            queryset = User.objects.get(id=self.request.user.id)
            serializer = UserSerializer(queryset)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)


class ProfileUpdateAPIView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def put(self, request, pk):
        profile = Profile.objects.get(id=pk)
        if profile:
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_create_success_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(prepare_error_response('The user ID not found'), status=status.HTTP_403_FORBIDDEN)
