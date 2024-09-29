from django.urls import path
from .views import DownloadVideoView, UserVideoListView

urlpatterns = [
    path('download/', DownloadVideoView.as_view(), name='download_video'),
    path('my_videos/', UserVideoListView.as_view(), name='user_videos'),  # Nouvel endpoint
]
