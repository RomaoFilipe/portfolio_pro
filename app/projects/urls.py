from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name="projects"),
    path("add/", views.project_add, name="project_add"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
