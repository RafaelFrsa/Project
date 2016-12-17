from django.shortcuts import render
from trocador.duplotubo.forms import Calculo
from django.http import HttpResponse  
from trocador.duplotubo.metodo_kern import *;
from trocador.duplotubo.models import *
from trocador.duplotubo.forms import *




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

def calculo_duplotubo(request):
	#import pdb; pdb.set_trace()
	form = Calculo(request.POST)
	if form.is_valid():
		resultado = yut(# Fluido1
			{'Vazao':form.cleaned_data['Vazao1'],
			'T_entr':form.cleaned_data['T_entr1'],
			'T_said':form.cleaned_data['T_said1'],
			'k':form.cleaned_data['k1'],
			'cp':form.cleaned_data['cp1'],
			'Pr':form.cleaned_data['Pr1'],
			'Viscos':form.cleaned_data['Viscosidade1'],
			'Densidade':form.cleaned_data['Densidade1'],
			'Diam_ext':form.cleaned_data['Diam_ext1'],
			'Diam_int':form.cleaned_data['Diam_int1'],
			'Annulus':0,
			'Liquido':1,
			'Viscos_tw':form.cleaned_data['Viscos_tw1']},
			# Fluido2
			{'Vazao':form.cleaned_data['Vazao2'],
			'T_entr':form.cleaned_data['T_entr2'],
			'T_said':form.cleaned_data['T_said2'],
			'k':form.cleaned_data['k2'],
			'cp':form.cleaned_data['cp2'],
			'Pr':form.cleaned_data['Pr2'],
			'Viscos':form.cleaned_data['Viscosidade2'],
			'Densidade':form.cleaned_data['Densidade2'],
			'Diam_ext':form.cleaned_data['Diam_ext2'],
			'Diam_int':form.cleaned_data['Diam_int2'],
			'Annulus':1,
			'Liquido':1,
			'Viscos_tw':form.cleaned_data['Viscos_tw2']},
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
		#result=str(resultado)
		res = Resultado()
		res.resultado = resultado
		res.save()
	context = {'form': form}

	return render(request, 'calculo_duplotubo.html', context)



def Formulario(request):
	form = ChoiceForm(request.POST or None)

	if request.method == 'POST':
		form.save()
	return render(request, 'modelform.html', {'form':form})