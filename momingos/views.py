from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DatosTransformados, RawData
from .serializers import DatosTransformadosSerializer
from datetime import date

class TransferRawDataToDatosTransformados(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Process each entry
            for entry in RawData.objects.all():
                nombre_completo = f"{entry.nombre} {entry.apellido}"
                
                if entry.edad:
                    edad_nominal = (date.today() - entry.edad).days // 365
                else:
                    edad_nominal = 0  # Use a default value of 0 if edad is None

                # Create or update the entry in DatosTransformados
                DatosTransformados.objects.update_or_create(
                    nombre_completo=nombre_completo,
                    defaults={'edad_nominal': edad_nominal}
                )

            return Response({"message": "Data transformed successfully."}, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class GetTransformedData(APIView):
    def get(self, request, *args, **kwargs):
        datos = DatosTransformados.objects.all()
        if not datos.exists():
            return Response({"message": "No transformed data available."}, status=200)

        serializer = DatosTransformadosSerializer(datos, many=True)
        return Response(serializer.data)
