from rest_framework import viewsets, permissions

from office.models import Task
from office.serializers.task_serializer import TaskSerializer
from office.pagination import StandardResultsSetPagination


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
