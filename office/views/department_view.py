from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from office.models import Department
from office.serializers.department_serializer import DepartmentSerializer
from office.pagination import StandardResultsSetPagination
from office.filter import DepartmentFilter


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    Department CRUD API endpoint
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination
    filterset_class = DepartmentFilter
    filter_backends = (filters.DjangoFilterBackend,)

    # API URL: /api/v1/department/
    """
        {
            "name": "Department Name",
            "is_active": true
        }
    """
