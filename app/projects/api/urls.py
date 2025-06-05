from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.ProjectListAPI.as_view(), name="api_projects"),
]
