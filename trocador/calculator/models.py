from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Agua(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k')

	class Meta:
		verbose_name='Agua'
		verbose_name_plural='Aguas'


class Butano(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k')

class CO2(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k')

class Metano(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k')

class Pentano(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k')

class RC318(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k')

class Resultado(models.Model):
	resultado = models.CharField(max_length=7000)	

