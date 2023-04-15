from django.db import models
import uuid

# Create your models here.
class EntrenamientosChirho(models.Model):
    id_chirho = models.UUIDField(default=uuid.uuid4, primary_key=True)
    nombrecurso_chirho = models.CharField(blank=False, max_length=50, verbose_name="Entrenamiento")


class MaquinariaEquipoChirho(models.Model):
    id_chirho = models.UUIDField(default=uuid.uuid4, primary_key=True)
    nombre_chirho = models.CharField(blank=False, max_length=50, verbose_name="Nombre de equipo")
    modelo_chirho = models.CharField(blank=False, max_length=50, verbose_name="Modelo de equipo")



    
