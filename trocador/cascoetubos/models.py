from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Agua(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP', blank=True)
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k', blank=True)

	class Meta:
		verbose_name='Agua'
		verbose_name_plural='Aguas'


class Butano(models.Model):
	
	temperature = models.FloatField('Temperatura')
	pressure = models.FloatField('Pressao')
	density= models.FloatField('Densidade')
	cp = models.FloatField('CP')
	viscosity = models.FloatField('Viscosidade')
	k = models.FloatField('k', blank=True)

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
	result_fl = models.CharField('Resultado FluidoDinamico', max_length=7000)	
	result_pres = models.CharField('Resultado Queda de Pressa', max_length=7000)
	result_geral = models.CharField('Resultado de Analise Geral', max_length=7000)

