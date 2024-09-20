from rest_framework.serializers import ModelSerializer
from apps.registro.models import Materiales

class RegistroSerializer(ModelSerializer):
    class Meta:
        model = Materiales
        fields = ['nombre','categoria','cantidad','fechaIngreso']
