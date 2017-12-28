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
		if dado.replace(identificador,'') in dicionario.keys() and bool(formulario.cleaned_data[dado]):
			dicionario[dado.replace(identificador,'')]=formulario.cleaned_data[dado]
	if 'Annulus' in dicionario.keys():
		dicionario['Diam_int']=dicionario['Diam_int']/1000.0
		dicionario['Diam_ext']=dicionario['Diam_ext']/1000.0
	if 'Annulus' not in dicionario.keys():
		dicionario['Bfl_prct']=dicionario['Bfl_prct']/100.0
		dicionario['Bfl_spac']=dicionario['Bfl_spac']/1000.0
		dicionario['Efic_bomb1']=dicionario['Efic_bomb1']/100.0
		dicionario['Efic_bomb2']=dicionario['Efic_bomb2']/100.0
	return	dicionario

@login_required
def calculo_cascoetubos(request):
	fluidoInterno={'Vazao':0,'T_entr':0,'T_said':0,'cp':0,'k':0,'Pr':0,'Viscos':0,
	         'Densidade':0,'Diam_ext':0,'Diam_int':0,'Annulus':0,'Liquido':1,'Viscos_tw':0}
	fluidoExterno={'Vazao':0,'T_entr':0,'T_said':0,'cp':0,'k':0,'Pr':0,'Viscos':0,
	         'Densidade':0,'Diam_ext':0,'Diam_int':0,'Annulus':1,'Liquido':1,'Viscos_tw':0}
	material={'K':0,'L':1, 'R_fi':0,'R_fo':0,'Calor_cnste':0,'Contracorrente':0,'Angulo_tubos':0,
          'Bfl_spac':0,'Bfl_prct':0,'Num_pass_tb':0,'Pt':0, 'Num_passes_casco':1,'Efic_bomb1':0,'Efic_bomb2':0,}
	#import pdb; pdb.set_trace()

	template_name = 'cascoetubos/calculo_cascoetubos.html'
	form = Calculo(request.POST or None)
	context={'form': form}
	if form.is_valid():
		temp_m1=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1'])/2
		temp_m2=(form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/2
		temp_w=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1']+form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/4
		atribut(form,fluidoInterno,identificador="1")
		atribut(form,fluidoExterno,identificador='2')
		atribut(form,material)
		if form.cleaned_data['nome_fluido1']!='manual':
			propried_get(eval(form.cleaned_data['nome_fluido1']),temp_m1,temp_w,fluidoInterno) 
		if form.cleaned_data['nome_fluido2']!='manual':
			propried_get(eval(form.cleaned_data['nome_fluido2']),temp_m2,temp_w,fluidoExterno) 

		fluidodinamico, analis_press, analis_term = heat_friction_shell(fluidoInterno,fluidoExterno,material)

		res = Resultado(result_fl = fluidodinamico,result_pres = analis_press,result_geral = analis_term)
		res.save()

		context = {'form': form,
					'Vazao1':str(fluidoInterno['Vazao']),
					'Vazao2':str(fluidoExterno['Vazao']),
					'Tentr1': str(fluidoInterno['T_entr']),
					'Tentr2': str(fluidoExterno['T_entr']),
					'Tsaid1': str(fluidoInterno['T_said']),
					'Tsaid2': str(fluidoExterno['T_said']),
					'Velocidade_Media_Escoamento1':str(fluidoInterno['Vel_mf']),
					'Velocidade_Media_Escoamento2':str(fluidoExterno['Vel_mf']),
					'Numero_Reynolds1':str(fluidoInterno['Re']),
					'Numero_Reynolds2':str(fluidoExterno['Re']),
					'Numero_Nusselts1':str(fluidoInterno['Nu']),
					'Numero_Nusselts2':str(fluidoExterno['Nu']),
					'dTlmtd':analis_term['DtTlmtd'],
					'Coeficiente_Pelicula1':str(fluidoInterno['Coeficient_calor']),
					'Coeficiente_Pelicula2':str(fluidoExterno['Coeficient_calor']),

					'DP1':str(fluidoInterno['dP do Casco']/1000.0),
					'DP2':str(fluidoExterno['dPtotal']/1000.0),
					'DP_Central_Chicanas':str(fluidoInterno['dP_Central_Chicanas']/1000.0),
					'DP_Janela_Chicanas':str(fluidoInterno['dP_Janela_Chicanas']/1000.0),
					'DP_Entrada_Saida':str(fluidoInterno['dP_Entrada_Saida']/1000.0),
					'DP_total1':str(fluidoInterno['dPtotal']/1000.0),
					'DP_total2':str(fluidoExterno['dPtotal']/1000.0),
					'Potencia_Bombeamento1': str(fluidoInterno['Potencia_bomb']),
					'Potencia_Bombeamento2': str(fluidoExterno['Potencia_bomb']),
					'DP_Bocais1':str(float(analis_press['DtP pelos Bocais'][0])),
					'DP_Bocais2':str(float(analis_press['DtP pelos Bocais'][1])),

					'Area_superficie_Limpa':analis_term['Area de superficie Limpa'],
					'Area_superficie_Incrustada':analis_term['Area de superficie Incrustada'],
					'Calor_Trocado':float(analis_term['Calor Trocado (Heat Duty)']),
					'Coef_Trans_Calor_Limpo':analis_term['Coef. de Trans. de Calor Limpo (Uc)'],
					'Coef_Trans_Calor_Incrustado':analis_term['Coef. de Trans. de Calor Incrustado (Ud)'],
					'Numero_Chicanas':str(analis_term['Numero de Chicanas']),
					'Numero_Tubos':str(int(material['Num_tubos'])+1),
					'Area_Escoamento_Cruzado':str(analis_term['Area de Escoamento Cruzado']),
					'Bypass_Area_Escoamento':str(analis_term['Bypass Area de Escoamento']),
					'Area_Vazamento_CascoChicanas':str(analis_term['Area de Vazamento Casco-Chicanas']),
					'Area_Vazamento_TubosChicanas':str(analis_term['Area de Vazamento Tubos-Chicanas']),
					'Fator_Corr_Geral_Coef_Calor':str(analis_term['Fator de Corr. Geral Coef. Calor']),
					'Excesso_Area':str(analis_term['Excesso de Area (Over-Surface Design)']),
					'Numero_Tubos_Preeliminar':str(material['Num_tubos_Preliminar']),}

	return render(request, template_name, context)