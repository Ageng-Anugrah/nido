from django.urls import path
from app_profile import views

urlpatterns = [
    path('photo/', views.ListCreatePhoto.as_view()),
    path('<user__npm>/', views.DetailProfileAPIView.as_view(), name='profile-detail'),
]