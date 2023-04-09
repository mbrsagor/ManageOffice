from rest_framework import viewsets, views, generics, permissions, status
from django_filters import rest_framework as filters
from rest_framework.response import Response

from office.models import Task, Project
from utils import response, employee_info
from office.serializers.task_serializer import TaskSerializer
from pagination.default_pagination import StandardResultsSetPagination


class TaskFilter(filters.FilterSet):
    project_name = filters.ModelChoiceFilter(field_name='project_name', queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = ['project']


class TaskViewSet(viewsets.ModelViewSet):
    """
    Create Task API CRUD API
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        return serializer.save(assigned_by=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(assigned_by=self.request.user)


class TaskFilterView(generics.ListAPIView):
    """
    Task list API endpoint
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter


class CompleteTaskListAPIView(views.APIView):
    """
    Complete task API listview
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            complete_task = Task.objects.filter(status=employee_info.Evolution.DONE)
            serializer = TaskSerializer(complete_task, many=True)
            return Response(response.prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                response.prepare_error_response(e),
                status=status.HTTP_400_BAD_REQUEST
            )
