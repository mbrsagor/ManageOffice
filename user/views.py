from rest_framework import views, status, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Profile
from .serializers import ProfileSerializer, UserSerializer


class ProfileAPIView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        try:
            queryset = Profile.objects.get(id=self.request.user.id)
            serializer = ProfileSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            queryset = User.objects.get(id=self.request.user.id)
            serializer = UserSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)

