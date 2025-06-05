from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("cms/", admin.site.urls),
    path("", include("app.core.urls")),
    path("projects/", include("app.projects.urls")),
    path("contact/", include("app.contacts.urls")),
    path("export/", include("app.export.urls")),
    path("api/", include("app.projects.api.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
