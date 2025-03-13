from django.urls import path
from .views import ReporteListCreate, ReporteDetail, UploadExcelView
from . import views

urlpatterns = [
    path('reportes/', ReporteListCreate.as_view(), name='reporte-list-create'),  # Para listar y crear
    path('reportes/<int:pk>/', ReporteDetail.as_view(), name='reporte-detail'),  # Para obtener, actualizar o borrar un reporte
    path('upload-excel/', UploadExcelView.as_view(), name='upload-excel'),  # Para cargar excel
]
