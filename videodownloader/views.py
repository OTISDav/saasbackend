import os
from rest_framework.response import Response
from rest_framework import status
from .models import Video
from .serializers import VideoSerializer
from rest_framework import generics
import yt_dlp as youtube_dl
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def download_video(request):
    # On attend une URL de la vidéo dans le corps de la requête
    url = request.data.get('url')

    if not url:
        return Response({"error": "L'URL est requise."}, status=status.HTTP_400_BAD_REQUEST)

    # Chemin du dossier Téléchargements de l'utilisateur
    user_home_dir = os.path.expanduser("~")
    downloads_dir = os.path.join(user_home_dir, "Téléchargements", "OtisTelechargement")

    # Création du dossier "OtisTelechargement" s'il n'existe pas
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)

    # Utilisation de yt-dlp pour obtenir des informations sur la vidéo et la télécharger
    try:
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            'outtmpl': f'{downloads_dir}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4'
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)  # Télécharger la vidéo
            video_title = info_dict.get('title', None)
            download_url = ydl.prepare_filename(info_dict)  # Chemin complet de la vidéo téléchargée

            uploader_name = info_dict.get('uploader', None) #le nom du uploader

    except Exception as e:
        return Response({"error": "Impossible de récupérer ou télécharger la vidéo. Veuillez vérifier l'URL."}, status=status.HTTP_400_BAD_REQUEST)

    # Créer un objet vidéo pour l'utilisateur connecté
    video = Video.objects.create(
        title=video_title,
        url=url,
        user=request.user,
        uploader = uploader_name
    )

    # Sérialisation et réponse
    serializer = VideoSerializer(video)
    return Response({"video": serializer.data, "downloadUrl": download_url, "title": video_title}, status=status.HTTP_201_CREATED)

class UserVideoListView(generics.ListAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Video.objects.filter(user=self.request.user)
