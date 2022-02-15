from rest_framework import viewsets, permissions

from base.models.office import Office
from base.serializers.office_serializer import OfficeSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAdminUser, ]
