from rest_framework import viewsets, generics, permissions
from django_filters import rest_framework as filters

from office.models import Task, Project
from office.serializers.task_serializer import TaskSerializer
from office.pagination import StandardResultsSetPagination


class TaskFilter(filters.FilterSet):
    project_name = filters.ModelChoiceFilter(field_name='project_name', queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = ['project_name']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination


class TaskFilterView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter
