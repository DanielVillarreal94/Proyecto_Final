from django.db import models
from django.urls import reverse
# Create your models here.

class Docente(models.Model):
    cedula=models.IntegerField()
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    celular=models.CharField(max_length=30)
    titulo=models.CharField(max_length=30)
    correo=models.EmailField()
    foto=models.ImageField(upload_to='foto/')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('docente-list')


class Materia(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    materias=models.ManyToManyField('Materia')
    docente=models.ForeignKey('Docente', on_delete=models.PROTECT)   
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    celular=models.CharField(max_length=30)
    correo=models.EmailField()
    foto=models.ImageField(upload_to='foto/')

    def __str__(self):
        return self.nombre
    
    

class Nota(models.Model):
    docente=models.ForeignKey('Docente', on_delete=models.PROTECT)   
    estudiante=models.ForeignKey('Estudiante', on_delete=models.PROTECT)   
    materia=models.ForeignKey('Materia', on_delete=models.PROTECT) 
    logro=models.CharField(max_length=100, null=True)
    nota1=models.DecimalField(max_digits=3,decimal_places=2)
    nota2=models.DecimalField(max_digits=3,decimal_places=2)
    nota3=models.DecimalField(max_digits=3,decimal_places=2)

    def promedio(self):
        resultado=(self.nota1 + self.nota2 + self.nota3)/3
        res=round(resultado,2)
        return res
   
    def __str__(self):
        return self.logro

    def get_absolute_url(self):
        return reverse('nota-list')

