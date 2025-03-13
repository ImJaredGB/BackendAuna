from rest_framework import generics, permissions
from .models import Reporte
from .serializers import ReporteSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.http import JsonResponse
import pandas as pd
from rest_framework.permissions import AllowAny

# Vista para listar y crear Reportes
class ReporteListCreate(generics.ListCreateAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

# Vista para obtener, actualizar o eliminar un reporte
class ReporteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    permission_classes = [permissions.AllowAny]

# Vista para cargar un archivo Excel y crear reportes desde él
class UploadExcelView(APIView):
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file provided'}, status=400)

        excel_file = request.FILES['file']

        try:
            df = pd.read_excel(excel_file)  # Leemos el archivo Excel

            # Iteramos por las filas y creamos los reportes
            for _, row in df.iterrows():
                dni = row.get('DNI')

                # Verificamos si el reporte ya existe con el mismo DNI
                if not Reporte.objects.filter(dni=dni).exists():
                    # Si no existe, creamos el nuevo reporte
                    Reporte.objects.create(
                        dni=dni,
                        nombre_apellidos=row.get('Apellidos y Nombres'),
                        sede=row.get('Sede'),
                        unidad_negocio=row.get('Sociedad'),
                        linea_movil=None,
                        modelo_movil=None,
                        imei_movil=None,
                        valor_movil=None,
                        accesorios_movil=None,
                        linea_fija=None,
                        modelo_fija=None,
                        imei_fija=None,
                        valor_fija=None,
                        accesorios_fija=None,
                        imagen_tomada=None,
                        imagen_subida=None,
                        firma_imagen=None,
                        fecha=None,
                        tipo_especialista="No definido",
                    )
                else:
                    print(f"El reporte con DNI {dni} ya existe, se omite la inserción.")

            return JsonResponse({'message': 'File processed successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)