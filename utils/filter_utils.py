from office.models import Task, Project
from django_filters import rest_framework as filters


class TaskFilter(filters.FilterSet):
    project_name = filters.ModelChoiceFilter(field_name='project_name', queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = ['project']
