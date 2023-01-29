from rest_framework import viewsets, generics, permissions
from django_filters import rest_framework as filters

from office.models import Project, Client
from office.serializers.project_serializer import ProjectSerializer
from pagination.default_pagination import StandardResultsSetPagination
from utils.employee_info import Evolution


class ProjectFilter(filters.FilterSet):
    """
    Filter project
    """
    date_line = filters.DateFilter(field_name='date_line')
    is_active = filters.BooleanFilter(field_name='is_active')
    budget = filters.NumericRangeFilter(field_name='budget')
    status = filters.ChoiceFilter(field_name='pay_purpose', choices=Evolution.task_status())
    client_name = filters.ModelChoiceFilter(field_name='client_name', queryset=Client.objects.all())

    class Meta:
        model = Project
        fields = ['client_name', 'date_line', 'is_active', 'status', 'budget']


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Create filter API
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


class ProjectFilterView(generics.ListAPIView):
    """
    Project filter API
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProjectFilter
