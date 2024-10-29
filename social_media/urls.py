# social_media/urls.py

from django.urls import path
from .views import publish_to_twitter, publish_to_linkedin

urlpatterns = [
    path('publish/twitter/', publish_to_twitter, name='publish_to_twitter'),
    path('publish/linkedin/', publish_to_linkedin, name='publish_to_linkedin'),
]
