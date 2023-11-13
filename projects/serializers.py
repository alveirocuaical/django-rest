from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    
    identifier = serializers.CharField(source='id')
    project_title = serializers.CharField(source='title')
    project_description = serializers.CharField(source='description')
    project_technology = serializers.CharField(source='technology')
    project_created_at = serializers.DateTimeField(source='created_at')

    
    class Meta:
        model = Project
        fields = ('identifier', 'project_title', 'project_description', 'project_technology', 'project_created_at')       
        read_only_fields = ('created_at',)
        
