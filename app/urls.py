

from django.urls import path
from app import views


urlpatterns = [
    path('', views.home),
    path('flower/<int:pk>/', views.FlowerDetailView.as_view(), name='flower-detail'),

    path('flower/<int:flower_id>/action/', views.LikeFlowerView.as_view(), name='like-flower')
]
