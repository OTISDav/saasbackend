from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CV
from .serializers import CVSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class GenerateCVView(APIView):
    def post(self, request):
        data = request.data
        cv = CV.objects.create(
            user=request.user,
            name=data.get('name'),
            email=data.get('email'),
            skills=data.get('skills'),
        )
        # Générer le PDF ici et le sauvegarder
        serializer = CVSerializer(cv)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserCVListView(generics.ListAPIView):
    serializer_class = CVSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CV.objects.filter(user=self.request.user)