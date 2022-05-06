from rest_framework import serializers
from .models import *

class TaskSer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Task
