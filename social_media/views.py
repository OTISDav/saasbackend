from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import requests
import os
from requests_oauthlib import OAuth1
from .models import SocialMediaPost
from .serializers import SocialMediaPostSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def publish_to_twitter(request):
    message = request.data.get('message')

    if not message:
        return Response({"error": "Le message est requis."}, status=status.HTTP_400_BAD_REQUEST)

    # Détails de l'authentification Twitter
    access_token = "1453983449262530564-gcC4sJqfWpi9LoK2VcEk2abLmqEen8"
    access_token_secret = "ayXKkqubjY1sPhFSmYTd6hmFmyXSnspQQN793s25Onpgc"
    consumer_key = "YRsItz3ap8CM1uW4dISQuVwsL"
    consumer_secret = "mZyTaofRb2fqLKMgwBfSLkmWMJpEIHX8FgX9kqkqQDCDta4ynC"

    # Appel à l'API Twitter
    url = "https://api.twitter.com/1.1/statuses/update.json"
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    payload = {'status': message}
    response = requests.post(url, auth=auth, params=payload)

    if response.status_code == 200:
        # Créer l'objet SocialMediaPost
        post = SocialMediaPost.objects.create(user=request.user, platform="Twitter", message=message)
        return Response({"message": "Publication sur Twitter réussie.", "post": SocialMediaPostSerializer(post).data}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Erreur lors de la publication sur Twitter."}, status=status.HTTP_400_BAD_REQUEST)
# social_media/views.py


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def publish_to_linkedin(request):
    message = request.data.get('message')
    file = request.FILES.get('file')  # Récupérer un fichier s'il est fourni

    if not message:
        return Response({"error": "Le message est requis."}, status=status.HTTP_400_BAD_REQUEST)

    # Détails de l'authentification LinkedIn
    access_token = "<votre_token_d'accès_linkedin>"

    # Appel à l'API LinkedIn pour publier un message
    url = "https://api.linkedin.com/v2/shares"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "content": {
            "contentEntities": [],
            "title": message
        },
        "owner": "urn:li:person:YOUR_USER_ID",
        "subject": message,
        "text": {
            "text": message
        }
    }

    # Si un fichier est fourni, l'ajouter à la requête
    if file:
        # Sauvegarder le fichier dans le système de fichiers avant de le télécharger sur LinkedIn
        file_path = os.path.join("social_media_files", file.name)
        with open(file_path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)

        # Associer le fichier à la publication LinkedIn ici (implémentation spécifique à LinkedIn)
        # Ajouter l'URL ou d'autres détails du fichier à l'API LinkedIn

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        # Créer l'objet SocialMediaPost
        post = SocialMediaPost.objects.create(user=request.user, platform="LinkedIn", message=message, file=file)
        return Response({"message": "Publication sur LinkedIn réussie.", "post": SocialMediaPostSerializer(post).data}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Erreur lors de la publication sur LinkedIn."}, status=status.HTTP_400_BAD_REQUEST)
# social_media/views.py