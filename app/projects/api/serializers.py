from rest_framework import serializers
from app.projects.models import Project



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
