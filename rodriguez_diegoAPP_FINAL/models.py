from django.db import models

# Create your models here.
class Instituciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombreInstituciones = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    email = models.EmailField()
    def __str__(self):
        return self.nombreInstituciones


class Seminario(models.Model):
    id = models.AutoField(primary_key=True)
    institucion = models.ForeignKey(Instituciones, on_delete=models.CASCADE)
    nroPersonas = models.IntegerField()
    telefono = models.IntegerField()
    fechaInscripcion = models.DateField()
    horaInscripcion = models.TimeField()
    email = models.EmailField()
    estado = models.CharField(max_length=80)
    observacion = models.CharField(max_length=80)