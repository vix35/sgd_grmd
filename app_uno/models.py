from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Velocidad_de_quiebre(models.Model):
    sector = models.CharField(max_length=20)
    punto = models.CharField(max_length=20)
    fecha = models.CharField(max_length=50)
    turno = models.CharField(max_length=20)
    condicion_geomecanica = models.CharField(max_length=200)
    velocidad_recomendada = models.CharField(max_length=20)
    observaciones_SGO = models.CharField(blank=True, max_length=200)
    poligono_control_sismico_asociado = models.CharField(max_length=200)
    id_para_control_SGP_focos = models.CharField(blank=True, max_length=200)
    porcentaje_ext_primario = models.FloatField()

class DBF(models.Model):
    material = models.CharField(max_length=200)
    unidad = models.CharField(max_length=200)
    valor = models.FloatField(max_length=200, null=True)
    fecha = models.CharField(max_length=200)

class Plan_diario(models.Model):
    sector = models.CharField(max_length=20)
    punto = models.CharField(max_length=20)
    fecha = models.CharField(max_length=50)
    TPD = models.FloatField()
    fecha_plan_subido = models.DateField(auto_now_add=True)

# class Zona_mineralurgicas(models.Model):
#
# class Cipe(models.Model):
#
# class Dilucion(models.Model):
