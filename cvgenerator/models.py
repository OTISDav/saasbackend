from django.db import models
from django.conf import settings

class CV(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cvs')
    name = models.CharField(max_length=255)  # Nom de l'utilisateur pour le CV
    email = models.EmailField()  # Email à inclure dans le CV
    skills = models.TextField()  # Compétences sous forme de texte ou liste
    generated_at = models.DateTimeField(auto_now_add=True)  # Date de génération du CV
    pdf_file = models.FileField(upload_to='cv_pdfs/', blank=True, null=True)  # Fichier PDF généré pour le CV

    def __str__(self):
        return f"CV de {self.name} - {self.user.username}"

    class Meta:
        ordering = ['-generated_at']
        verbose_name = 'CV'
        verbose_name_plural = 'CVs'
