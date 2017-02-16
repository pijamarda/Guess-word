from django.db import models

# Create your models here.

class Palabra(models.Model):
	word = models.CharField(max_length=200, unique=True)
	def __str__(self):
		return self.word

class Intento(models.Model):
	palabra = models.ForeignKey(Palabra)
	intentos = models.IntegerField(default=1)
	fecha = models.DateTimeField('fecha')

class Reportada(models.Model):
	word = models.CharField(max_length=200, unique=True)
	veces = models.IntegerField(default=1)

class Rendicion(models.Model):
	palabra = models.ForeignKey(Palabra)
	intentos = models.IntegerField(default=1)
	fecha = models.DateTimeField('fecha')