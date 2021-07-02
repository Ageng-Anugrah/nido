from rest_framework.serializers import ModelSerializer
from app_profile.models import UserProfile
from app_auth.serializers import (
    UserSerializer
)


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'photo',
            'user',
            'photo',
            'phone_number',
            'secondary_email',
            'line_id',
            'birth_date',
            'birth_place',
            'home_address',
            'current_address',
        )
