from rest_framework import serializers
from webapp.models.projects import Project
from webapp.models.tasks import Task
from webapp.models.statuses import Status
from webapp.models.task_types import Task_type


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'start_date',
                  'completion_date', 'is_deleted')
        read_only_fields = ('id', 'is_deleted')


class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class TaskTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_type
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class TasksSerializer(serializers.ModelSerializer):
    project = ProjectsSerializer(read_only=True)
    status = StatusesSerializer(many=True, read_only=True)
    task_types = TaskTypesSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'project', 'title', 'description', 'status', 'task_types', 'is_deleted', 'deleted_at',
                  'completion_date', 'created_at', 'updated_at')
        read_only_fields = ('id', 'project', 'status', 'task_types',
                            'created_at', 'updated_at', 'deleted_at')
