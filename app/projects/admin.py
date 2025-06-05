from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "featured", "created_at")
    list_filter = ("category", "featured")
    search_fields = ("name", "technologies")
