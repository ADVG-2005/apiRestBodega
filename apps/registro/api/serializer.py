from rest_framework.serializers import ModelSerializer
from apps.registro.models import Materiales

class RegistroSerializer(ModelSerializer):
    class Meta:
        model = Materiales
        fields = ['id','nombre','categoria','cantidad','fechaIngreso']
