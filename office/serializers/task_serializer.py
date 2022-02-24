from rest_framework import serializers

from office.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'task_name',
            'project_name',
            'assigned_by',
            'assigned_users',
            'assigned_date',
            'status',
            # 'total_working_day',
            'created_at',
            'updated_at'
        ]
