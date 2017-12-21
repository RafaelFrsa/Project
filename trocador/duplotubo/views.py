from django.shortcuts import render
from trocador.duplotubo.forms import Calculo
from django.http import HttpResponse  
from trocador.duplotubo.metodo_kern import *;
from trocador.duplotubo.models import *
from trocador.duplotubo.forms import *
from django.db import connection
import sqlite3
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
                query1,query2,temp1,temp2=trecho(Agua,temp_w)
                prop1=eval('query1.Viscos');prop2=eval('query2.Viscos')
            else:
                query1,query2,temp1,temp2=trecho(Agua,temp)
                prop1=eval('query1.%s'%propriedade);prop2=eval('query2.%s'%propriedade)
            fluido[propriedade]=(prop2-prop1)*(temp-temp1)/(temp2-temp1) + prop1 if prop2>prop1 else -(prop1-prop2)*(temp-temp1)/(temp2-temp1) + prop1
        except: pass
    fluido['Pr']=fluido['cp']*fluido['Viscos']/fluido['k']
    return fluidos

@login_required
def calculo_duplotubo(request):
	#import pdb; pdb.set_trace()
	exibition = Resultado()
	template_name = 'duplotubo/calculo_duplotubo.html'
	form = Calculo(request.POST or None)

	if form.is_valid():
		if form.cleaned_data['nome_fluido1']=='manual': 
			fiul1={'Vazao':form.cleaned_data['Vazao1'],
			'T_entr':form.cleaned_data['T_entr1'],
			'T_said':form.cleaned_data['T_said1'],
			'k':form.cleaned_data['k1'],
			'cp':form.cleaned_data['cp1'],
			'Pr':form.cleaned_data['Pr1'],
			'Viscos':form.cleaned_data['Viscosidade1'],
			'Densidade':form.cleaned_data['Densidade1'],
			'Diam_ext':form.cleaned_data['Diam_ext1']/1000.0,
			'Diam_int':form.cleaned_data['Diam_int1']/1000.0,
			'Annulus':0,
			'Liquido':1,
			'Viscos_tw':form.cleaned_data['Viscos_tw1']}

		if form.cleaned_data['nome_fluido2']=='manual': 
			fiul2={'Vazao':form.cleaned_data['Vazao2'],
			'T_entr':form.cleaned_data['T_entr2'],
			'T_said':form.cleaned_data['T_said2'],
			'k':form.cleaned_data['k2'],
			'cp':form.cleaned_data['cp2'],
			'Pr':form.cleaned_data['Pr2'],
			'Viscos':form.cleaned_data['Viscosidade2'],
			'Densidade':form.cleaned_data['Densidade2'],
			'Diam_ext':form.cleaned_data['Diam_ext2']/1000.0,
			'Diam_int':form.cleaned_data['Diam_int2']/1000.0,
			'Annulus':1,
			'Liquido':1,
			'Viscos_tw':form.cleaned_data['Viscos_tw2']}
		elif form.cleaned_data['nome_fluido2']!='manual' or form.cleaned_data['nome_fluido1']!='manual':

			cur=sqlite3.connect('db.sqlite3').cursor()
			dic1={'k':0,'cp':0,'Pr':0,'Viscos':0,'Viscos_tw':0}
			dic2={'k':0,'cp':0,'Pr':0,'Viscos':0,'Viscos_tw':0}
			temp_m1=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1'])/2
			temp_m2=(form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/2
			temp_w=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1']+form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/4
			propried_get(tuple([form.cleaned_data['nome_fluido1']]),temp_m1,temp_w,dic1)
			propried_get(tuple([form.cleaned_data['nome_fluido2']]),temp_m2,temp_w,dic2)

	context={'form': form}
	if form.is_valid():
		if form.cleaned_data['nome_fluido1']=='manual' and form.cleaned_data['nome_fluido2']!='manual':
			fluido1, fluido2, material = yut(fiul1,

				{'Vazao':form.cleaned_data['Vazao2'],
				'T_entr':form.cleaned_data['T_entr2'],
				'T_said':form.cleaned_data['T_said2'],
				'k':dic2['k'] if bool(dic2['k']) else form.cleaned_data['k2'],
				'cp':dic2['cp'] if bool(dic2['cp']) else form.cleaned_data['cp2'],
				'Pr':dic2['Pr'] if bool(dic2['Pr']) else form.cleaned_data['Pr2'],
				'Viscos':dic2['Viscos'] if bool(dic2['Viscos']) else form.cleaned_data['Viscosidade2'],
				'Densidade':dic1['Densidade'] if bool(dic1['Densidade']) else form.cleaned_data['Densidade2'],
				'Diam_ext':form.cleaned_data['Diam_ext2']/1000.0,
				'Diam_int':form.cleaned_data['Diam_int2']/1000.0,
				'Annulus':1,'Liquido':1,
				'Viscos_tw':dic2['Viscos_tw'] if bool(dic2['Viscos_tw']) else form.cleaned_data['Viscos_tw2']},

				{'K':form.cleaned_data['K'],
				'L':form.cleaned_data['L'],
				'R_fi':form.cleaned_data['R_fi'],
				'R_fo':form.cleaned_data['R_fo'],
				'Calor_cnste':form.cleaned_data['Calor_const'],
				'Contracorrente':form.cleaned_data['Contracorrente'],
				'Efic_bomb1':form.cleaned_data['ef_b1']/100.0,
				'Efic_bomb2':form.cleaned_data['ef_b2']/100.0,
				'Num_tubs':form.cleaned_data['Num_tubs'],
				'Alet_per_tube':form.cleaned_data['Alet_num'],
				'Alet_alt':form.cleaned_data['Alet_alt']/1000.0,
				'Alet_K':form.cleaned_data['Alet_k'],
				'Alet_espes':form.cleaned_data['Alet_esp']/1000.0,
				'Alet_type':form.cleaned_data['Alet_type'],
				'Tubo_aletado':form.cleaned_data['Alet_tubes'],
				'Multi_tube':form.cleaned_data['Multi_tubes'],
				'arranj_ser_paral':form.cleaned_data['arranj_ser_paral'],
				'T_I_Paralelo':form.cleaned_data['T_I_Paralelo'],
				'R_A_Paralelo':form.cleaned_data['R_A_Paralelo'],
				'Num_ramos':form.cleaned_data['Num_ramos']})

		if form.cleaned_data['nome_fluido2']=='manual' and form.cleaned_data['nome_fluido1']!='manual':
			fluido1, fluido2, material = yut(	
				{'Vazao':form.cleaned_data['Vazao2'],
				'T_entr':form.cleaned_data['T_entr2'],
				'T_said':form.cleaned_data['T_said2'],
				'k':dic2['k'] if bool(dic2['k']) else form.cleaned_data['k2'],
				'cp':dic2['cp'] if bool(dic2['cp']) else form.cleaned_data['cp2'],
				'Pr':dic2['Pr'] if bool(dic2['Pr']) else form.cleaned_data['Pr2'],
				'Viscos':dic2['Viscos'] if bool(dic2['Viscos']) else form.cleaned_data['Viscosidade2'],
				'Densidade':dic1['Densidade'] if bool(dic1['Densidade']) else form.cleaned_data['Densidade2'],
				'Diam_ext':form.cleaned_data['Diam_ext2']/1000.0,
				'Diam_int':form.cleaned_data['Diam_int2']/1000.0,
				'Annulus':1,
				'Liquido':1,
				'Viscos_tw':dic2['Viscos_tw'] if bool(dic2['Viscos_tw']) else form.cleaned_data['Viscos_tw2']},

				fiul2,

				{'K':form.cleaned_data['K'],
				'L':form.cleaned_data['L'],
				'R_fi':form.cleaned_data['R_fi'],
				'R_fo':form.cleaned_data['R_fo'],
				'Calor_cnste':form.cleaned_data['Calor_const'],
				'Contracorrente':form.cleaned_data['Contracorrente'],
				'Efic_bomb1':form.cleaned_data['ef_b1']/100.0,
				'Efic_bomb2':form.cleaned_data['ef_b2']/100.0,
				'Num_tubs':form.cleaned_data['Num_tubs'],
				'Alet_per_tube':form.cleaned_data['Alet_num'],
				'Alet_alt':form.cleaned_data['Alet_alt']/1000.0,
				'Alet_K':form.cleaned_data['Alet_k'],
				'Alet_espes':form.cleaned_data['Alet_esp']/1000.0,
				'Alet_type':form.cleaned_data['Alet_type'],
				'Tubo_aletado':form.cleaned_data['Alet_tubes'],
				'Multi_tube':form.cleaned_data['Multi_tubes'],
				'arranj_ser_paral':form.cleaned_data['arranj_ser_paral'],
				'T_I_Paralelo':form.cleaned_data['T_I_Paralelo'],
				'R_A_Paralelo':form.cleaned_data['R_A_Paralelo'],
				'Num_ramos':form.cleaned_data['Num_ramos']})

		elif form.cleaned_data['nome_fluido1']=='manual' and form.cleaned_data['nome_fluido2']=='manual':
			fluido1, fluido2, material = yut(fiul1,fiul2,
				{'K':form.cleaned_data['K'],
				'L':form.cleaned_data['L'],
				'R_fi':form.cleaned_data['R_fi'],
				'R_fo':form.cleaned_data['R_fo'],
				'Calor_cnste':form.cleaned_data['Calor_const'],
				'Contracorrente':form.cleaned_data['Contracorrente'],
				'Efic_bomb1':form.cleaned_data['ef_b1']/100.0,
				'Efic_bomb2':form.cleaned_data['ef_b2']/100.0,
				'Num_tubs':form.cleaned_data['Num_tubs'],
				'Alet_per_tube':form.cleaned_data['Alet_num'],
				'Alet_alt':form.cleaned_data['Alet_alt']/1000.0,
				'Alet_K':form.cleaned_data['Alet_k'],
				'Alet_espes':form.cleaned_data['Alet_esp']/1000.0,
				'Alet_type':form.cleaned_data['Alet_type'],
				'Tubo_aletado':form.cleaned_data['Alet_tubes'],
				'Multi_tube':form.cleaned_data['Multi_tubes'],
				'arranj_ser_paral':form.cleaned_data['arranj_ser_paral'],
				'T_I_Paralelo':form.cleaned_data['T_I_Paralelo'],
				'R_A_Paralelo':form.cleaned_data['R_A_Paralelo'],
				'Num_ramos':form.cleaned_data['Num_ramos']})


		else:
			fluido1, fluido2, material = yut(
				# Fluido1
				{'Vazao':form.cleaned_data['Vazao1'],
				'T_entr':form.cleaned_data['T_entr1'],
				'T_said':form.cleaned_data['T_said1'],
				'k':dic1['k'] if bool(dic1['k']) else form.cleaned_data['k1'],
				'cp':dic1['cp'] if bool(dic1['cp']) else form.cleaned_data['cp1'],
				'Pr':dic1['Pr'] if bool(dic1['Pr']) else form.cleaned_data['Pr1'],
				'Viscos':dic1['Viscos'] if bool(dic1['Viscos']) else form.cleaned_data['Viscosidade1'],
				'Densidade':dic1['Densidade'] if bool(dic1['Densidade']) else form.cleaned_data['Densidade1'],
				'Diam_ext':form.cleaned_data['Diam_ext1']/1000.0,
				'Diam_int':form.cleaned_data['Diam_int1']/1000.0,
				'Annulus':0,
				'Liquido':1,
				'Viscos_tw':dic1['Viscos_tw'] if bool(dic1['Viscos_tw']) else form.cleaned_data['Viscos_tw1']},
				# Fluido2
				{'Vazao':form.cleaned_data['Vazao2'],
				'T_entr':form.cleaned_data['T_entr2'],
				'T_said':form.cleaned_data['T_said2'],
				'k':dic2['k'] if bool(dic2['k']) else form.cleaned_data['k2'],
				'cp':dic2['cp'] if bool(dic2['cp']) else form.cleaned_data['cp2'],
				'Pr':dic2['Pr'] if bool(dic2['Pr']) else form.cleaned_data['Pr2'],
				'Viscos':dic2['Viscos'] if bool(dic2['Viscos']) else form.cleaned_data['Viscosidade2'],
				'Densidade':dic1['Densidade'] if bool(dic1['Densidade']) else form.cleaned_data['Densidade2'],
				'Diam_ext':form.cleaned_data['Diam_ext2']/1000.0,
				'Diam_int':form.cleaned_data['Diam_int2']/1000.0,
				'Annulus':1,
				'Liquido':1,
				'Viscos_tw':dic2['Viscos_tw'] if bool(dic2['Viscos_tw']) else form.cleaned_data['Viscos_tw2']},
				# Material
				{'K':form.cleaned_data['K'],
				'L':form.cleaned_data['L'],
				'R_fi':form.cleaned_data['R_fi'],
				'R_fo':form.cleaned_data['R_fo'],
				'Calor_cnste':form.cleaned_data['Calor_const'],
				'Contracorrente':form.cleaned_data['Contracorrente'],
				'Efic_bomb1':form.cleaned_data['ef_b1']/100.0,
				'Efic_bomb2':form.cleaned_data['ef_b2']/100.0,
				'Num_tubs':form.cleaned_data['Num_tubs'],
				'Alet_per_tube':form.cleaned_data['Alet_num'],
				'Alet_alt':form.cleaned_data['Alet_alt']/1000.0,
				'Alet_K':form.cleaned_data['Alet_k'],
				'Alet_espes':form.cleaned_data['Alet_esp']/1000.0,
				'Alet_type':form.cleaned_data['Alet_type'],
				'Tubo_aletado':form.cleaned_data['Alet_tubes'],
				'Multi_tube':form.cleaned_data['Multi_tubes'],
				'arranj_ser_paral':form.cleaned_data['arranj_ser_paral'],
				'T_I_Paralelo':form.cleaned_data['T_I_Paralelo'],
				'R_A_Paralelo':form.cleaned_data['R_A_Paralelo'],
				'Num_ramos':form.cleaned_data['Num_ramos']})

			res = Resultado()
			res.result_fl = fluido1
			res.result_pres = fluido2
			res.result_geral = material
			res.save()

		context = {'form': form,
					'Vazao1':fluido1['Vazao'][0],
					'Vazao2':fluido1['Vazao'][1],
					'Tentr1': fluido1['Temperatura de Entrada'][0],
					'Tentr2': fluido1['Temperatura de Entrada'][1],
					'Tsaid1': fluido1['Temperatura de Saida'][0],
					'Tsaid2': fluido1['Temperatura de Saida'][1],
					'Velocidade_Media_Escoamento1':fluido1['Velocidade Media de Escoamento'][0],
					'Velocidade_Media_Escoamento2':fluido1['Velocidade Media de Escoamento'][1],
					'Numero_Reynolds1':fluido1['Numero de Reynolds'][0],
					'Numero_Reynolds2':fluido1['Numero de Reynolds'][1],
					'Numero_Nusselts1':fluido1['Numero de Nusselts'][0],
					'Numero_Nusselts2':fluido1['Numero de Nusselts'][1],
					'dTlmtd':material['Var. Log. de Temperatura (dTm)'],
					'Coeficiente_Pelicula1':fluido1['Coeficiente de Pelicula (h)'][0],
					'Coeficiente_Pelicula2':fluido1['Coeficiente de Pelicula (h)'][1],

					'DP1':fluido2['DP'][0],
					'DP2':fluido2['DP'][1],
					'DPrb1':fluido2['DPrb'][0],
					'DPrb2':fluido2['DPrb'][1],
					'DP_total1':fluido2['DPtotal'][0],
					'DP_total2':fluido2['DPtotal'][1],
					'Potencia_Bombeamento1': fluido2['Potencia de Bombeamento'][0],
					'Potencia_Bombeamento2': fluido2['Potencia de Bombeamento'][1],
					'DP_Bocais1':fluido2['DPnl (bocais)'][0],
					'DP_Bocais2':fluido2['DPnl (bocais)'][1],

					'Area_Troca_Termica_Total':material['Area de Troca Termica Total'],
					'Calor_Trocado':material['Calor Trocado (Heat Duty)'],
					'Coef_Trans_Calor_Limpo':material['Coef. de Trans. de Calor Limpo (Uc)'],
					'Coef_Trans_Calor_Incrustado':material['Coef. de Trans. de Calor Incrustado (Ud)'],
					'Fator_Limpeza':material['Fator de Limpeza (CF)'],
					'Area_Grampo_Tubular':material['Area por Grampo Tubular'],
					'Numero_Grampos':str(material['Numero de Grampos']),
                    'Excesso_Area':str(material['Excesso de Area (Over-Surface Design)']),
                    }
				
	return render(request, template_name, context)
