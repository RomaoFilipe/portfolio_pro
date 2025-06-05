from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all().order_by("-created_at")
    return render(request, "projects/project_list.html", {"projects": projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "projects/project_detail.html", {"project": project})

def project_add(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("projects")
    return render(request, "projects/project_add.html", {"form": form})
