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
	exibition = Resultado()
	form = Calculo(request.POST or None)
	template_name = 'cascoetubos/calculo_cascoetubos.html'
	if form.is_valid():
		if True:#bool(nome_fluido1) or bool(nome_fluido2):
			cur=sqlite3.connect('db.sqlite3').cursor()
			dic1={'k':0,'cp':0,'Pr':0,'Viscos':0,'Viscos_tw':0}
			dic2={'k':0,'cp':0,'Pr':0,'Viscos':0,'Viscos_tw':0}
			temp_m1=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1'])/2
			temp_m2=(form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/2
			temp_w=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1']+form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/4
			propried_get(temp_m1,temp_w,tuple([form.cleaned_data['nome_fluido1']]),dic1)
			propried_get(temp_m2,temp_w,tuple([form.cleaned_data['nome_fluido2']]),dic2)
	if form.is_valid():
		resultado = heat_friction_shell(
			# Fluido1
			{'Vazao':form.cleaned_data['Vazao1'],
			'T_entr':form.cleaned_data['T_entr1'],
			'T_said':form.cleaned_data['T_said1'],
			'k':dic1['k'] if bool(dic1['k']) else form.cleaned_data['k1'],
			'cp':dic1['cp'] if bool(dic1['cp']) else form.cleaned_data['cp1'],
			'Pr':dic1['Pr'] if bool(dic1['Pr']) else form.cleaned_data['Pr1'],
			'Viscos':dic1['Viscos'] if bool(dic1['Viscos']) else form.cleaned_data['Viscosidade1'],
			'Densidade':dic1['Densidade'] if bool(dic1['Densidade']) else form.cleaned_data['Densidade1'],
			'Diam_ext':form.cleaned_data['Diam_ext1'],
			'Diam_int':form.cleaned_data['Diam_int1'],
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
			'Diam_ext':form.cleaned_data['Diam_ext2'],
			'Diam_int':form.cleaned_data['Diam_int2'],
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
			'Bfl_spac':form.cleaned_data['Bfl_spac'],
			'Bfl_prct':form.cleaned_data['Bfl_prct'],
			'Num_pass_tb':form.cleaned_data['Num_pass_tb'],
			'Pt':form.cleaned_data['Pt'],
			'Num_passes_casco':form.cleaned_data['Num_passes_casco'],
			'Efic_bomb1':form.cleaned_data['Efic_bomb1'],
			'Efic_bomb2':form.cleaned_data['Efic_bomb2']})
			

		res = Resultado()
		res.result_casc_tb = resultado
		res.save()
		exibition = res.result_casc_tb
		
	context = {'form': form,
				'model': exibition,}

	return render(request, template_name, context)



