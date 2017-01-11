from django.shortcuts import render
from trocador.duplotubo.forms import Calculo
from django.http import HttpResponse  
from trocador.duplotubo.metodo_kern import *;
from trocador.duplotubo.models import *
from trocador.duplotubo.forms import *
from django.db import connection
import sqlite3
#from trocador.duplotubo.test002 import *


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


def calculo_duplotubo(request):
	#import pdb; pdb.set_trace()
	exibition = Resultado()
	form = Calculo(request.POST or None)
	if form.is_valid():
		if True:#bool(nome_fluido1) or bool(nome_fluido2):
			cur=sqlite3.connect('db.sqlite3').cursor()
			diuty=cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
			fer=cur.execute("SELECT * FROM %s WHERE id=2;"%tuple([u'duplotubo_agua'])).fetchall()
			dic1={'k':0,'cp':0,'Pr':0,'Viscos':0,'Viscos_tw':0}
			dic2={'k':0,'cp':0,'Pr':0,'Viscos':0,'Viscos_tw':0}
			temp_m1=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1'])/2
			temp_m2=(form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/2
			temp_w=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1']+form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/4
			propried_get(temp_m1,temp_w,tuple([form.cleaned_data['nome_fluido1']]),dic1)
			propried_get(temp_m2,temp_w,tuple([form.cleaned_data['nome_fluido2']]),dic2)
		#if fluido1:
		#	Agua.objects.raw('SELECT * FROM %s', [Agua])
		resultado = yut(# Fluido1
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
			'Efic_bomb1':form.cleaned_data['ef_b1'],
			'Efic_bomb2':form.cleaned_data['ef_b2'],
			'Num_tubs':form.cleaned_data['Num_tubs'],
			'Alet_per_tube':form.cleaned_data['Alet_num'],
			'Alet_alt':form.cleaned_data['Alet_alt'],
			'Alet_K':form.cleaned_data['Alet_k'],
			'Alet_espes':form.cleaned_data['Alet_esp'],
			'Alet_type':form.cleaned_data['Alet_type'],
			'Tubo_aletado':form.cleaned_data['Alet_tubes'],
			'Multi_tube':form.cleaned_data['Multi_tubes'],
			'arranj_ser_paral':form.cleaned_data['arranj_ser_paral'],
			'T_I_Paralelo':form.cleaned_data['T_I_Paralelo'],
			'R_A_Paralelo':form.cleaned_data['R_A_Paralelo'],
			'Num_ramos':form.cleaned_data['Num_ramos']})
 		
		res = Resultado()
		res.result_dpl_tubo = resultado
		res.save()
		exibition = res.result_dpl_tubo
		
	context = {'form': form,
				'model': exibition,}

	return render(request, 'calculo_duplotubo.html', context)


# Create your views here.
# def joiner():
# 	form = Calculo(request.POST)
# 	fluido1={'Vazao':form.cleaned_data['Vazao1'],
# 			'T_entr':form.cleaned_data['T_entr1'],
# 			'T_said':form.cleaned_data['T_said1'],
# 			'k':form.cleaned_data['k1'],
# 			'cp':form.cleaned_data['cp1'],
# 			'Pr':form.cleaned_data['Pr1'],
# 			'Viscosidade':form.cleaned_data['Viscosidade1'],
# 			'Densidade':form.cleaned_data['Densidade1'],
# 			'Diam_ext':form.cleaned_data['Diam_ext1'],
# 			'Diam_int':form.cleaned_data['Diam_int1'],
# 			'Annulus':0,
# 			'Viscos_tw':form.cleaned_data['Viscos_tw1']}
# 	fluido2={'Vazao':form.cleaned_data['Vazao2'],
# 			'T_entr':form.cleaned_data['T_entr2'],
# 			'T_said':form.cleaned_data['T_said2'],
# 			'k':form.cleaned_data['k2'],
# 			'cp':form.cleaned_data['cp2'],
# 			'Pr':form.cleaned_data['Pr2'],
# 			'Viscosidade':form.cleaned_data['Viscosidade2'],
# 			'Densidade':form.cleaned_data['Densidade2'],
# 			'Diam_ext':form.cleaned_data['Diam_ext2'],
# 			'Diam_int':form.cleaned_data['Diam_int2'],
# 			'Annulus':1,
# 			'Viscos_tw':form.cleaned_data['Viscos_tw2']}
# 	material={'K':form.cleaned_data['K'],
# 			'L':form.cleaned_data['L'],
# 			'R_fi':form.cleaned_data['R_fi'],
# 			'R_fo':form.cleaned_data['R_fo'],
# 			'Calor_const':form.cleaned_data['Calor_const'],
# 			'Contracorrente':form.cleaned_data['Contracorrente'],
# 			'ef_b1':form.cleaned_data['ef_b1'],
# 			'ef_b2':form.cleaned_data['ef_b2']}
# 	return fluido1,fluido2,material