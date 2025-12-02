

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=400, blank=True)
    description = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
