from django.urls import path
from .views import TransferRawDataToDatosTransformados, GetTransformedData

urlpatterns = [
    path('transfer/', TransferRawDataToDatosTransformados.as_view(), name='transfer_raw_to_datos_transformados'),
    path('info/', GetTransformedData.as_view(), name='get_transformed_data'),
]