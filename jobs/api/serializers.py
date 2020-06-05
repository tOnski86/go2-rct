from rest_framework import serializers
from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Job
        fields = '__all__'

