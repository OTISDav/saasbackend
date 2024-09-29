from django.urls import path
from .views import GenerateCVView, UserCVListView

urlpatterns = [
    path('generate/', GenerateCVView.as_view(), name='generate_cv'),
    path('my_cvs/', UserCVListView.as_view(), name='user_cvs'),  # Nouvel endpoint
]
