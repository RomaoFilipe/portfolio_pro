from rest_framework import generics
from app.projects.models import Project
from .serializers import ProjectSerializer

class ProjectListAPI(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
