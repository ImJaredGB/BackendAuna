from django.db import models

class Reporte(models.Model):
    # Datos de Usuario (DNI PK)
    dni = models.IntegerField(primary_key=True)
    nombre_apellidos = models.CharField(max_length=255)
    sede = models.CharField(max_length=255)
    unidad_negocio = models.CharField(max_length=255)     

    #Linea Movil y Fija
    linea_movil = models.CharField(max_length=50, blank=True, null=True)
    modelo_movil = models.CharField(max_length=50, blank=True, null=True)
    imei_movil = models.BigIntegerField(blank=True, null=True)
    valor_movil = models.FloatField(blank=True, null=True)
    accesorios_movil = models.CharField(max_length=255, blank=True, null=True)

    linea_fija = models.CharField(max_length=50, blank=True, null=True)
    modelo_fija = models.CharField(max_length=50, blank=True, null=True)
    imei_fija = models.IntegerField(blank=True, null=True)
    valor_fija = models.FloatField(blank=True, null=True)
    accesorios_fija = models.CharField(max_length=255, blank=True, null=True)

    # Fotos y Firmas (Imagenes)
    imagen_tomada = models.ImageField(upload_to='fotos/tomadas/', blank=True, null=True)
    imagen_subida = models.ImageField(upload_to='fotos/subidas/', blank=True, null=True)
    firma_imagen = models.ImageField(upload_to='firmas/', blank=True, null=True)

    # Fecha y Tipo de Especialista
    fecha = models.DateField(auto_now_add=True)
    tipo_especialista = models.CharField(max_length=255)

    def __str__(self):
        return f"Usuario {self.nombre_apellidos} - DNI {self.dni}"

