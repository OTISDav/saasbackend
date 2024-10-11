from rest_framework import status, generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterUserSerializer, LoginSerializer

class RegisterUserView(generics.CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            utilisateur = serializer.validated_data['user']
            refresh = RefreshToken.for_user(utilisateur)
            return Response({
                'message': 'Connexion réussie',
                'utilisateur': {
                    'id': utilisateur.id,
                    'nom_utilisateur': utilisateur.username,
                },
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
            }, status=status.HTTP_200_OK)
        else:
            # Affiche les erreurs pour comprendre ce qui ne va pas
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
