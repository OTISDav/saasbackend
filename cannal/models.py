from django.db import models
from django.conf import settings

# Modèle pour les canaux Telegram
class CanalTelegram(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    proprietaire = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='canaux_possedes')
    date_creation = models.DateTimeField(auto_now_add=True)
    est_vendu = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

# Modèle pour la vente de canaux
class VenteCanal(models.Model):
    canal = models.OneToOneField(CanalTelegram, on_delete=models.CASCADE, related_name='vente')
    acheteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='canaux_achetes')
    date_vente = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Vente de {self.canal.nom}"

# Modèle de transaction pour enregistrer les paiements
class Transaction(models.Model):
    vente = models.ForeignKey(VenteCanal, on_delete=models.CASCADE, related_name='transactions')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_transaction = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.montant}"
