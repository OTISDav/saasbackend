from django.db import models
from django.conf import settings

class Video(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='videos')
    url = models.URLField(max_length=500)  # L'URL de la vidéo
    title = models.CharField(max_length=255)  # Le titre de la vidéo
    download_path = models.CharField(max_length=500, blank=True, null=True)  # Chemin où la vidéo a été téléchargée
    downloaded_at = models.DateTimeField(auto_now_add=True)  # Date de téléchargement

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    class Meta:
        ordering = ['-downloaded_at']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
