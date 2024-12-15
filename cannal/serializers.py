from rest_framework import serializers
from .models import CanalTelegram, VenteCanal, Transaction

class CanalTelegramSerializer(serializers.ModelSerializer):
    proprietaire = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    proprietaire_nom = serializers.CharField(source='proprietaire.username', read_only=True)  # Ajout du nom du propriétaire
    class Meta:
        model = CanalTelegram
        fields = '__all__'
        # fields = ['id', 'nom', 'description', 'prix', 'proprietaire', 'date_creation', 'est_vendu']

class VenteCanalSerializer(serializers.ModelSerializer):
    canal = CanalTelegramSerializer()

    class Meta:
        model = VenteCanal
        fields = ['id', 'canal', 'acheteur', 'date_vente']

class TransactionSerializer(serializers.ModelSerializer):
    vente = VenteCanalSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'vente', 'montant', 'date_transaction']
