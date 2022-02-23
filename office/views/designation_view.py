from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from office.models import Designation
from office.serializers.designation_serializer import DesignationSerializer
from office.pagination import StandardResultsSetPagination
from office.filter import DesignationFilter


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination
    filterset_class = DesignationFilter
    filter_backends = (filters.DjangoFilterBackend,)

    # API URL: /api/v1/designation/
    """
        {
            "name": "CEO",
            "is_active": true
        }
    """
