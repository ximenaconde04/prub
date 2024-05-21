from django.db import models

# Create your models here.

class Taller(models.Model):
    ponente = models.CharField(max_length=50)
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.codigo, self.nombre)

class Alumno(models.Model):
    numeroControl = models.CharField(max_length=12)
    nombreCompleto = models.CharField(max_length=50)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.numeroControl, self.nombreCompleto)

class InscripcionTaller(models.Model):
    fechaInscripcion = models.DateTimeField(auto_now_add=True)
    taller = models.ForeignKey(Taller, on_delete=models.DO_NOTHING)
    alumno = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING)
    completado = models.BooleanField(default=False)
    fechaCompletado = models.DateTimeField(null=True)

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.taller.nombre, self.alumno.nombreCompleto)