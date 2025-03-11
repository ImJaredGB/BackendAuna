from rest_framework import generics
from .models import Reporte
from .serializers import ReporteSerializer

# Listar y crear Reportes
class ReporteListCreate(generics.ListCreateAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

# Detalles de un Reporte
class ReporteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
