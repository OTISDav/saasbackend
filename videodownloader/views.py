from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Video
from .serializers import VideoSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import youtube_dl

class DownloadVideoView(APIView):
    def post(self, request):
        url = request.data.get('url')
        if url:
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                title = info_dict.get('title', None)
                video = Video.objects.create(
                    user=request.user,
                    url=url,
                    title=title,
                    download_path=info_dict.get('filename', ''),
                )
                serializer = VideoSerializer(video)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "URL missing"}, status=status.HTTP_400_BAD_REQUEST)

class UserVideoListView(generics.ListAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Video.objects.filter(user=self.request.user)