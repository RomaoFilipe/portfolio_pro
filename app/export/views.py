from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit
import zipfile
import os
from django.conf import settings
from django.shortcuts import render

def export_pdf(request):
    html = render_to_string("export/export_template.html", {"title": "My Portfolio PDF"})
    pdf = pdfkit.from_string(html, False)
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=portfolio.pdf"
    return response

def export_zip(request):
    zip_filename = "portfolio.zip"
    zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)

    with zipfile.ZipFile(zip_path, "w") as zipf:
        # Example: add static file or images
        zipf.write(os.path.join(settings.MEDIA_ROOT, "example.jpg"), "example.jpg")

    with open(zip_path, "rb") as f:
        response = HttpResponse(f.read(), content_type="application/zip")
        response["Content-Disposition"] = f"attachment; filename={zip_filename}"

    return response
