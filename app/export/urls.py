from django.urls import path
from . import views

urlpatterns = [
    path("pdf/", views.export_pdf, name="export_pdf"),
    path("zip/", views.export_zip, name="export_zip"),
]
