from django.shortcuts import render
from trocador.cascoetubos.forms import Calculo
from django.http import HttpResponse  
from trocador.cascoetubos.casc_tubo_cal import *;
from trocador.cascoetubos.models import *
from trocador.cascoetubos.forms import *
import sqlite3
from django.contrib.auth.decorators import login_required



def propried_get(temp_m,temp_w,table,fluido):
	con = sqlite3.connect('db.sqlite3');
	cur = con.cursor();
	def inter_temp(temp,table,prop):
		sql2='SELECT %s,temp FROM %s '\
	          'WHERE temp >= %.5f LIMIT 1;'
		sql1='SELECT %s,temp FROM %s '\
	          'WHERE temp <= %.5f '\
	          'ORDER BY temp DESC LIMIT 1;'
		y1=float(cur.execute(sql1%(prop,table[0],temp,)).fetchall()[0][0])
		y2=float(cur.execute(sql2%(prop,table[0],temp,)).fetchall()[0][0])
		temp1=float(cur.execute(sql1%(prop,table[0],temp,)).fetchall()[0][1])
		temp2=float(cur.execute(sql2%(prop,table[0],temp,)).fetchall()[0][1])
		if y2>y1:
			prop=(y2-y1)*(temp-temp1)/(temp2-temp1) + y1
		else:
			prop=-(y1-y2)*(temp-temp1)/(temp2-temp1) + y1
		return prop

	sql_stmnt='SELECT %s FROM %s WHERE temp == %s;'
	if temp_m in cur.execute('SELECT * FROM %s;'%table).fetchall():
	    fluido['Densidade']=float(cur.execute(sql_stmnt%('densidade',table,temp_m)).fetchone()[0])
	    fluido['Viscos']=float(cur.execute(sql_stmnt%('Viscos',table,temp_m)).fetchone()[0])
	    fluido['cp']=float(cur.execute(sql_stmnt%('cp',table,temp_m)).fetchone()[0])
	    fluido['Viscos_tw']=float(cur.execute(sql_stmnt%('Viscos',table,temp_m)).fetchone()[0])
	    fluido['k']=float(cur.execute(sql_stmnt%('k',table,temp_w)).fetchone()[0])
	    fluido['Pr']=fluido['cp']*fluido['Viscos']/fluido['k']
	else:
	    fluido['Densidade']=inter_temp(temp_m,table,'densidade')
	    fluido['Viscos']=inter_temp(temp_m,table,'Viscos')
	    fluido['cp']=inter_temp(temp_m,table,'cp')
	    fluido['Viscos_tw']=inter_temp(temp_w,table,'Viscos')
	    fluido['k']=inter_temp(temp_m,table,'k')
	    fluido['Pr']=fluido['cp']*fluido['Viscos']/fluido['k']
	return fluido


@login_required
def calculo_cascoetubos(request):
	#import pdb; pdb.set_trace()
	#exibition = Resultado()
	form = Calculo(request.POST or None)
	template_name = 'cascoetubos/calculo_cascoetubos.html'
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
			propried_get(temp_m1,temp_w,tuple([form.cleaned_data['nome_fluido1']]),dic1)
			propried_get(temp_m2,temp_w,tuple([form.cleaned_data['nome_fluido2']]),dic2)

	context={'form': form}
	if form.is_valid():
		if form.cleaned_data['nome_fluido1']=='manual' and form.cleaned_data['nome_fluido2']!='manual':
			fluido1, fluido2, material = heat_friction_shell(fiul1,

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

				{'K':form.cleaned_data['K'],'L':form.cleaned_data['L'],'R_fi':form.cleaned_data['R_fi'],
				'R_fo':form.cleaned_data['R_fo'],'Calor_cnste':form.cleaned_data['Calor_const'],
				'Contracorrente':form.cleaned_data['Contracorrente'],'Angulo_tubos':form.cleaned_data['Angulo_tubos'],
				'Bfl_spac':form.cleaned_data['Bfl_spac']/1000.0,'Bfl_prct':form.cleaned_data['Bfl_prct']/100.0,
				'Num_pass_tb':form.cleaned_data['Num_pass_tb'],'Pt':form.cleaned_data['Pt']/1000,
				'Num_passes_casco':form.cleaned_data['Num_passes_casco'],'Efic_bomb1':form.cleaned_data['Efic_bomb1']/100.0,
				'Efic_bomb2':form.cleaned_data['Efic_bomb2']/100.0})

		if form.cleaned_data['nome_fluido2']=='manual' and form.cleaned_data['nome_fluido1']!='manual':
			fluido1, fluido2, material = heat_friction_shell(	
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
				'Angulo_tubos':form.cleaned_data['Angulo_tubos'],
				'Bfl_spac':form.cleaned_data['Bfl_spac']/1000.0,
				'Bfl_prct':form.cleaned_data['Bfl_prct']/100.0,
				'Num_pass_tb':form.cleaned_data['Num_pass_tb'],
				'Pt':form.cleaned_data['Pt'],
				'Num_passes_casco':form.cleaned_data['Num_passes_casco'],
				'Efic_bomb1':form.cleaned_data['Efic_bomb1']/100.0,
				'Efic_bomb2':form.cleaned_data['Efic_bomb2']/100.0})

		elif form.cleaned_data['nome_fluido1']=='manual' and form.cleaned_data['nome_fluido2']=='manual':
			fluido1, fluido2, material = heat_friction_shell(fiul1,fiul2,
				{'K':form.cleaned_data['K'],
				'L':form.cleaned_data['L'],
				'R_fi':form.cleaned_data['R_fi'],
				'R_fo':form.cleaned_data['R_fo'],
				'Calor_cnste':form.cleaned_data['Calor_const'],
				'Contracorrente':form.cleaned_data['Contracorrente'],
				'Angulo_tubos':form.cleaned_data['Angulo_tubos'],
				'Bfl_spac':form.cleaned_data['Bfl_spac']/1000.0,
				'Bfl_prct':form.cleaned_data['Bfl_prct']/100.0,
				'Num_pass_tb':form.cleaned_data['Num_pass_tb'],
				'Pt':form.cleaned_data['Pt']/1000,
				'Num_passes_casco':form.cleaned_data['Num_passes_casco'],
				'Efic_bomb1':form.cleaned_data['Efic_bomb1']/100.0,
				'Efic_bomb2':form.cleaned_data['Efic_bomb2']/100.0})


		else:

			fluido1, fluido2, material = heat_friction_shell(
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
				'Angulo_tubos':form.cleaned_data['Angulo_tubos'],
				'Bfl_spac':form.cleaned_data['Bfl_spac']/1000.0,
				'Bfl_prct':form.cleaned_data['Bfl_prct']/100.0,
				'Num_pass_tb':form.cleaned_data['Num_pass_tb'],
				'Pt':form.cleaned_data['Pt']/1000,
				'Num_passes_casco':form.cleaned_data['Num_passes_casco'],
				'Efic_bomb1':form.cleaned_data['Efic_bomb1']/100.0,
				'Efic_bomb2':form.cleaned_data['Efic_bomb2']/100.0})
				

			res = Resultado()
       		res.result_fl = fluido1
       		res.result_pres = fluido2
       		res.result_geral = material
       		res.save()

		context = {'form': form,
					'Vazao1':str(fluido1['Vazao']),
					'Vazao2':str(fluido2['Vazao']),
					'Tentr1': str(fluido1['T_entr']),
					'Tentr2': str(fluido2['T_entr']),
					'Tsaid1': str(fluido1['T_said']),
					'Tsaid2': str(fluido2['T_said']),
					'Velocidade_Media_Escoamento1':str(fluido1['Vel_mf']),
					'Velocidade_Media_Escoamento2':str(fluido2['Vel_mf']),
					'Numero_Reynolds1':str(fluido1['Re']),
					'Numero_Reynolds2':str(fluido2['Re']),
					'Numero_Nusselts1':str(fluido1['Nu']),
					'Numero_Nusselts2':str(fluido2['Nu']),
					'dTlmtd':material['dTm'],
					'Coeficiente_Pelicula1':str(fluido1['Coeficient_calor']),
					'Coeficiente_Pelicula2':str(fluido2['Coeficient_calor']),

					'DP1':str(fluido1[u'\u0394P do Casco']/1000.0),
					'DP2':str(fluido2[u'\u0394Ptotal']/1000.0),
					'DP_Central_Chicanas':str(fluido1[u'\u0394P_Central_Chicanas']/1000.0),
					'DP_Janela_Chicanas':str(fluido1[u'\u0394P_Janela_Chicanas']/1000.0),
					'DP_Entrada_Saida':str(fluido1[u'\u0394P_Entrada_Saida']/1000.0),
					'DP_total1':str(fluido1[u'\u0394Ptotal']/1000.0),
					'DP_total2':str(fluido2[u'\u0394Ptotal']/1000.0),
					'Potencia_Bombeamento1': str(fluido1['Potencia_bomb']/1000.0),
					'Potencia_Bombeamento2': str(fluido2['Potencia_bomb']/1000.0),
					'DP_Bocais1':str(fluido1['dPN']/1000.0),
					'DP_Bocais2':str(fluido2['dPN']/1000.0),

					'Area_superficie_Limpa':material['area_c'],
					'Area_superficie_Incrustada':material['area_f'],
					'Calor_Trocado':material['Q']/1000.0,
					'Coef_Trans_Calor_Limpo':material['Uc'],
					'Coef_Trans_Calor_Incrustado':material['Ud'],
					'Numero_Chicanas':str(material['Num_bfl']),
					'Numero_Tubos':str(int(material['Num_tubos'])+1),
					'Area_Escoamento_Cruzado':str(material['S_m']),
                    'Bypass_Area_Escoamento':str(material['S_b']),
                    'Area_Vazamento_CascoChicanas':str(material['S_sb']),
                    'Area_Vazamento_TubosChicanas':str(material['S_tb']),
                    'Fator_Corr_Geral_Coef_Calor':str(fluido1['Fator_Correcao_Geral_Calor']),
                    'Excesso_Area':str(material['OS']*100),
                    'Numero_Tubos_Preeliminar':str(material['Num_tubos_Preliminar']),
					}

	return render(request, template_name, context)



