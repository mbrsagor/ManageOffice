from rest_framework import viewsets, views, generics, permissions, status
from django_filters import rest_framework as filters
from rest_framework.response import Response

from office.models import Task, Project
from office.serializers.task_serializer import TaskSerializer
from office.pagination import StandardResultsSetPagination
from utils.employee_info import Evolution
from utils.response import prepare_success_response, prepare_error_response


class TaskFilter(filters.FilterSet):
    project_name = filters.ModelChoiceFilter(field_name='project_name', queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = ['project_name']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination


class TaskFilterView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter


class CompleteTaskListAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            complete_task = Task.objects.filter(status=Evolution.DONE)
            serializer = TaskSerializer(complete_task, data=request.data)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                prepare_error_response(e),
                status=status.HTTP_400_BAD_REQUEST
            )
