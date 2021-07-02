from rest_framework.serializers import ModelSerializer
from app_bem.models import (
    BEM, BEMDepartement, BEMUser
)
from app_auth.serializers import (
    UserSerializer
)


class BEMSerializer(ModelSerializer):
    class Meta:
        model = BEM
        fields = ('id', 'name', 'year', 'logo_url',)


class BEMDepartementSerializer(ModelSerializer):
    bem = BEMSerializer()
    head = UserSerializer()

    class Meta:
        model = BEMDepartement
        fields = ('id', 'name', 'description', 'head', 'staff_amount', 'bem')


class BEMUserSerializer(ModelSerializer):
    user = UserSerializer()
    departement = BEMDepartementSerializer()

    class Meta:
        model = BEMUser
        fields = ('id', 'user', 'departement', 'role')
