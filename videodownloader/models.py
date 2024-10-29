from django.db import models
from django.conf import settings
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploader = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
