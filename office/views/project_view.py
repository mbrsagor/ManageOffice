from rest_framework import viewsets, generics, permissions, status
from django_filters import rest_framework as filters
from rest_framework.response import Response

from office.models import Project, Client
from utils.employee_info import Evolution
from office.serializers.project_serializer import ProjectSerializer
from utils.notification_manager import send_notification_single_user
from pagination.default_pagination import StandardResultsSetPagination


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

    def create(self, request, *args, **kwargs):
        # Static message and title
        title = "Add your title"
        message = "Your message added here or load sommewhere else"
        try:
            serializer = ProjectSerializer(data=self.request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                send_notification_single_user(self.request.user.device_token, title, message)
                return Response('Project added successfully', status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_200_OK)


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
