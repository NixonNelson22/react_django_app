from backend.models import *
from rest_framework import serializers


class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = ['task_name', 'task_description']
