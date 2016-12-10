#-*- coding: cp1252 -*- 
from django import forms
#from gen.core.operacao import soma

class Calculo(forms.Form):

	Vazao1 = forms.FloatField(label='Vazão') 
	T_entr1 = forms.FloatField(label='Temperatura de Entrada') 
	T_said1 = forms.FloatField(label='Temperatura de Saída') 
	k1 = forms.FloatField(label='Condutividade Térmica_banco') 
	cp1 = forms.FloatField(label='Capacidade calorífica_banco') 
	Pr1 = forms.FloatField(label='Número de Prandtl') 
	Viscosidade1 = forms.FloatField(label='Viscosidade_banco')
	Densidade1 = forms.FloatField(label='Densidade_banco')
	Diam_ext1 = forms.FloatField(label='Diâmetro Externo')
	Diam_int1 = forms.FloatField(label='Diâmetro Interno')
	Viscos_tw1 = forms.FloatField(label='Viscosidade_da_temp_parede_banco')
	Vazao2 = forms.FloatField(label='Vazão')
	T_entr2 = forms.FloatField(label='Temperatura de Entrada') 
	T_said2 = forms.FloatField(label='Temperatura de Saída') 
	k2 = forms.FloatField(label='Condutividade Térmica_banco') 
	cp2 = forms.FloatField(label='Capacidade calorífica_banco') 
	Pr2 = forms.FloatField(label='Número de Prandtl')
	Viscosidade2 = forms.FloatField(label='Viscosidade_banco')
	Densidade2 = forms.FloatField(label='Densidade_banco')
	Diam_ext2 = forms.FloatField(label='Diâmetro Externo_banco')
	Diam_int2 = forms.FloatField(label='Diâmetro Interno_banco')
	Viscos_tw2 = forms.FloatField(label='Viscosidade_da_temp_parede_banco')
	K = forms.FloatField(label='Condutividade Térmica do Material') 
	L = forms.FloatField(label='Comprimento')
	R_fi = forms.FloatField(label='Fator de Incrustação Interno')
	R_fo = forms.FloatField(label='Fator de Incrustação Externo')
	Calor_const = forms.BooleanField(label='Termicamente Isolado')
	Contracorrente = forms.BooleanField(label='Escoamento Contracorrente')
	ef_b1 = forms.FloatField(label='Eficiência da Bomba Interna')
	ef_b2 = forms.FloatField(label='Eficiência da Bomba Externa')
	Num_tubs = forms.FloatField(label='Número de Tubos')
	Alet_num = forms.FloatField(label='Quantidade de Aletas')
	Alet_alt = forms.FloatField(label='Altura das Aletas')
	Alet_k = forms.FloatField(label='Condutividade das Aletas')
	Alet_esp = forms.FloatField(label='Espessura das Aletas')
	Alet_type = forms.FloatField(label='Tipo das Aletas')
	Alet_tubes = forms.FloatField(label='Tubos Aletados?')
	Multi_tubes = forms.FloatField(label='Tubos Multiplos?')
	arranj_ser_paral = forms.FloatField(label='Arranjo Série e Paralelo')
	T_I_Paralelo = forms.FloatField(label='Tubo Interno Paralelo')
	R_A_Paralelo = forms.FloatField(label='Tubo Externo Paralelo')
	Num_ramos = forms.FloatField(label='Número de Ramos')





