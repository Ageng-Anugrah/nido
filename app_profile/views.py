from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app_profile.models import UserProfile
from app_profile.serializers import UserProfileSerializer
from rest_framework import permissions
# Create your views here.


class ListCreatePhoto(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DetailProfileAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.AllowAny, )
    lookup_field = 'user__npm'
