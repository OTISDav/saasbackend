from rest_framework import serializers
from .models import SocialMediaPost

class SocialMediaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaPost
        fields = ['id', 'user', 'platform', 'message', 'file', 'created_at']
