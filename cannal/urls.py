from django.urls import path
from .views import CanalCreateView, CanalVendreView, CanalAcheterView, CanalListView

urlpatterns = [
    path('create/', CanalCreateView.as_view(), name='canal-create'),
    path('canaux/', CanalListView.as_view(), name='canal-list'),
    path('vendre/', CanalVendreView.as_view(), name='canal-vendre'),
    path('acheter/', CanalAcheterView.as_view(), name='canal-acheter'),
]
