from django.db import models


# Create your models here.

class EstudiantesAdsi(models.Model):

    cedula=models.IntegerField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    edad=models.IntegerField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
