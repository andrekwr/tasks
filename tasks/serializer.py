from rest_framework import serializers
from tasks.model import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "pub_date", "description")