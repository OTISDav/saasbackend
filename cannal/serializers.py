from rest_framework import serializers
from .models import CanalTelegram, VenteCanal, Transaction

class CanalTelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanalTelegram
        fields = ['id', 'nom', 'description', 'prix', 'proprietaire', 'date_creation', 'est_vendu']

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
