from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # Utilise la méthode authenticate pour valider l'utilisateur
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Identifiants incorrects. Veuillez réessayer.")
        else:
            raise serializers.ValidationError("Le nom d'utilisateur et le mot de passe sont obligatoires.")

        data['user'] = user
        return data