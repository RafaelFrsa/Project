from __future__ import unicode_literals
from django.shortcuts import render
from trocador.cascoetubos.forms import Calculo
from trocador.cascoetubos.casc_tubo_cal import *
from trocador.cascoetubos.models import *
from trocador.cascoetubos.forms import *
from trocador.core.models import Agua, Butano, Pentano, RC318, CO2, Metano
from django.contrib.auth.decorators import login_required
 
def propried_get(Table,temp,temp_w,fluido):
	def trecho(Table,temp):
		query1=Table.objects.filter(temperature__gte=temp)[0] 
		query2=Table.objects.filter(temperature__lte=temp)[len(Table.objects.filter(temperature__lte=temp))-1] 
		temp1=query1.temperature;temp2=query2.temperature
		return query1,query2,temp1,temp2
	for propriedade in fluido.keys():
		try:
			if propriedade=='Viscos_tw':
				query1,query2,temp1,temp2=trecho(Table,temp_w)
				prop1=eval('query1.Viscos');prop2=eval('query2.Viscos')
			else:
				query1,query2,temp1,temp2=trecho(Table,temp)
				prop1=eval('query1.%s'%propriedade);prop2=eval('query2.%s'%propriedade)
			fluido[propriedade]=(prop2-prop1)*(temp-temp1)/(temp2-temp1) + prop1 if prop2>prop1 else -(prop1-prop2)*(temp-temp1)/(temp2-temp1) + prop1
		except: pass
	fluido['Pr']=fluido['cp']*fluido['Viscos']/fluido['k']
	return fluido

def atribut(formulario,dicionario,identificador=''):
	for dado in formulario.cleaned_data.keys():
		chave=dado.replace(identificador,'')
		if chave in dicionario.keys() and bool(formulario.cleaned_data[dado]):
			dicionario[str(chave)]=formulario.cleaned_data[dado]
			if formulario.fields[dado].label_suffix:
				dicionario[str(chave)]=float(formulario.cleaned_data[dado])/float(formulario.fields[dado].label_suffix)
	return	dicionario

@login_required
def calculo_cascoetubos(request):
	tubos_internos={'Vazao':0,'T_entr':0,'T_said':0,'cp':0,'k':0,'Pr':0,'Viscos':0,
	         'Densidade':0,'Diam_ext':0,'Diam_int':0,'Annulus':0,'Liquido':1,'Viscos_tw':0}
	casco={'Vazao':0,'T_entr':0,'T_said':0,'cp':0,'k':0,'Pr':0,'Viscos':0,
	         'Densidade':0,'Diam_ext':0,'Diam_int':0,'Annulus':1,'Liquido':1,'Viscos_tw':0}
	material={'K':0,'L':1, 'R_fi':0,'R_fo':0,'Calor_cnste':0,'Contracorrente':0,'Angulo_tubos':0,
          'Bfl_spac':0,'Bfl_prct':0,'Num_pass_tb':0,'Pt':0, 'Num_passes_casco':1,'Efic_bomb1':0,'Efic_bomb2':0}
	#import pdb; pdb.set_trace()
	template_name = 'cascoetubos/calculo_cascoetubos.html'
	form = Calculo(request.POST or None)
	context={'form': form}
	if form.is_valid():
		temp_m1=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1'])/2
		temp_m2=(form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/2
		temp_w=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1']+form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/4
		atribut(form,tubos_internos,identificador="2")
		atribut(form,casco,identificador='1')
		atribut(form,material)
		nome=form.cleaned_data['nome_fluido1']
		if form.cleaned_data['nome_fluido1']!='manual':
			propried_get(eval(form.cleaned_data['nome_fluido1']),temp_m1,temp_w,casco) 
		if form.cleaned_data['nome_fluido2']!='manual':
			propried_get(eval(form.cleaned_data['nome_fluido2']),temp_m2,temp_w,tubos_internos) 

		fluidodinamico, analis_press, analis_term = heat_friction_shell(casco,tubos_internos,material)
		res = Resultado(result_fl = fluidodinamico,result_pres = analis_press,result_geral = analis_term)
		res.save()

		context = {'form': form,'casco':casco,
					'Vazao1':str(casco['Vazao']),
					'Vazao2':str(tubos_internos['Vazao']),
					'Tentr1': str(casco['T_entr']),
					'Tentr2': str(tubos_internos['T_entr']),
					'Tsaid1': str(casco['T_said']),
					'Tsaid2': str(tubos_internos['T_said']),
					'Velocidade_Media_Escoamento1':str(casco['Vel_mf']),
					'Velocidade_Media_Escoamento2':str(tubos_internos['Vel_mf']),
					'Numero_Reynolds1':str(casco['Re']),
					'Numero_Reynolds2':str(tubos_internos['Re']),
					'Numero_Nusselts1':str(fluidodinamico['Numero de Nusselts'][0]),
					'Numero_Nusselts2':str(fluidodinamico['Numero de Nusselts'][1]),
					'dTlmtd':analis_term['DtTlmtd'],
					'Coeficiente_Pelicula1':str(casco['Coeficient_calor']),
					'Coeficiente_Pelicula2':str(tubos_internos['Coeficient_calor']),

					'DP1':str(casco['dP do Casco']/1000.0),
					'DP2':str(casco['dPtotal']/1000.0),
					'DP_Central_Chicanas':str(float(analis_press['DtP Central Chicanas'][0])/1000.0),
					'DP_Janela_Chicanas':str(float(analis_press['DtP Janela Chicanas'][0])/1000.0),
					'DP_Entrada_Saida':str(float(analis_press['DtP Entrada e Saida'][0])/1000.0),
					'DP_total1':str(float(analis_press['DtP total'][0])/1000.0),
					'DP_total2':str(float(analis_press['DtP total'][1])/1000.0),
					'Potencia_Bombeamento1': str(float(analis_press['Potencia de Bombeamento'][0])/1000.0),
					'Potencia_Bombeamento2': str(float(analis_press['Potencia de Bombeamento'][1])/1000.0),
					'DP_Bocais1':str(float(analis_press['DtP pelos Bocais'][0])/1000.0),
					'DP_Bocais2':str(float(analis_press['DtP pelos Bocais'][1])/1000.0),

					'Area_superficie_Limpa':analis_term['Area de superficie Limpa'],
					'Area_superficie_Incrustada':analis_term['Area de superficie Incrustada'],
					'Calor_Trocado':float(analis_term['Calor Trocado (Heat Duty)']),
					'Coef_Trans_Calor_Limpo':analis_term['Coef. de Trans. de Calor Limpo (Uc)'],
					'Coef_Trans_Calor_Incrustado':analis_term['Coef. de Trans. de Calor Incrustado (Ud)'],
					'Numero_Chicanas':str(analis_term['Numero de Chicanas']),
					'Numero_Tubos':str(analis_term['Numero de Tubos ']),
					'Area_Escoamento_Cruzado':str(analis_term['Area de Escoamento Cruzado']),
					'Bypass_Area_Escoamento':str(analis_term['Bypass Area de Escoamento']),
					'Area_Vazamento_CascoChicanas':str(analis_term['Area de Vazamento Casco-Chicanas']),
					'Area_Vazamento_TubosChicanas':str(analis_term['Area de Vazamento Tubos-Chicanas']),
					'Fator_Corr_Geral_Coef_Calor':str(analis_term['Fator de Corr. Geral Coef. Calor']),
					'Excesso_Area':str(analis_term['Excesso de Area (Over-Surface Design)']),
					'Numero_Tubos_Preeliminar':str(analis_term['Numero de Tubos Preeliminar']),}

	return render(request, template_name, context)