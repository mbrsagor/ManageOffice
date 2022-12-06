from rest_framework import serializers

from office.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ('assigned_by',)
        depth = 1
        fields = [
            'id',
            'task_name',
            'project',
            'assigned_by',
            'users',
            'assigned_date',
            'status',
            'created_at',
            'updated_at'
        ]

    def validate_task_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Task name should be more than 1 characters")
        return value
