from rest_framework.serializers import ModelSerializer
from app_auth.models import (
    User
)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'npm', 'generation')
