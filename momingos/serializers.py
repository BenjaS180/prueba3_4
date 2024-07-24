from rest_framework import serializers
from .models import DatosTransformados

class DatosTransformadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosTransformados
        fields = ['id', 'nombre_completo', 'edad_nominal']
