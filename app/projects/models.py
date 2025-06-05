from django.db import models

CATEGORIES = [
    ("programming", "Programming"),
    ("3d", "3D Design"),
    ("multimedia", "Multimedia"),
]

class Project(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    technologies = models.CharField(max_length=300, help_text="Comma separated")
    description = models.TextField()
    image = models.ImageField(upload_to="projects/images/")
    video = models.FileField(upload_to="projects/videos/", blank=True, null=True)
    model_3d = models.FileField(upload_to="projects/3d/", blank=True, null=True)
    repo_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
