from django.urls import path
from .views import download_video, UserVideoListView

urlpatterns = [
    path('download/', download_video, name='download_video'),
    path('my_videos/', UserVideoListView.as_view(), name='user_videos'),  # Nouvel endpoint
]
