from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CanalTelegram, VenteCanal, Transaction
from .serializers import CanalTelegramSerializer
from django.utils import timezone


# Vue pour la Création d'un Canal
class CanalCreateView(APIView):
    def post(self, request):
        # Ajouter automatiquement le propriétaire comme utilisateur authentifié
        data = request.data.copy()
        data['proprietaire'] = request.user.id  # Associer le canal à l'utilisateur connecté

        serializer = CanalTelegramSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Vue pour la Vente d'un Canal
class CanalVendreView(APIView):
    def post(self, request, pk):
        try:
            canal = CanalTelegram.objects.get(pk=pk)
        except CanalTelegram.DoesNotExist:
            return Response({'erreur': 'Canal non trouvé.'}, status=status.HTTP_404_NOT_FOUND)

        if canal.est_vendu:
            return Response({'erreur': 'Ce canal est déjà vendu.'}, status=status.HTTP_400_BAD_REQUEST)

        # Créer la vente
        vente = VenteCanal.objects.create(canal=canal)
        canal.est_vendu = True
        canal.save()

        return Response({'message': 'Canal mis en vente avec succès'}, status=status.HTTP_200_OK)


# Vue pour l'Achat d'un Canal
class CanalAcheterView(APIView):
    def post(self, request, pk):
        try:
            canal = CanalTelegram.objects.get(pk=pk)
        except CanalTelegram.DoesNotExist:
            return Response({'erreur': 'Canal non trouvé.'}, status=status.HTTP_404_NOT_FOUND)

        if not canal.est_vendu:
            return Response({'erreur': 'Ce canal n\'est pas encore mis en vente.'}, status=status.HTTP_400_BAD_REQUEST)

        vente = canal.vente
        vente.acheteur = request.user
        vente.date_vente = timezone.now()
        vente.save()

        # Créer une transaction
        Transaction.objects.create(vente=vente, montant=canal.prix)

        return Response({'message': 'Achat du canal réussi'}, status=status.HTTP_200_OK)

# la liste des cannaux

class CanalListView(APIView):
    def get(self, request):
        # Récupérer tous les canaux
        canaux = CanalTelegram.objects.all()

        # Sérialiser les données
        serializer = CanalTelegramSerializer(canaux, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)