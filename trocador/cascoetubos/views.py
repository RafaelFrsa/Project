from django.shortcuts import render
from trocador.cascoetubos.forms import Calculo
from django.http import HttpResponse  
from trocador.cascoetubos.casc_tubo_cal import *;
from trocador.cascoetubos.models import *
from trocador.cascoetubos.forms import *
from django.contrib.auth.decorators import login_required


@login_required
def calculo_cascoetubos(request):
	#import pdb; pdb.set_trace()
	form = Calculo(request.POST)
	if form.is_valid():
		resultado = heat_friction_shell(
			# Fluido1
			{'Vazao':form.cleaned_data['Vazao1'],
			'T_entr':form.cleaned_data['T_entr1'],
			'T_said':form.cleaned_data['T_said1'],
			'k':form.cleaned_data['cp1'],
			'cp':form.cleaned_data['k1'],
			'Pr':form.cleaned_data['Pr1'],
			'Viscos':form.cleaned_data['Viscosidade1'],
			'Densidade':form.cleaned_data['Densidade1'],
			'Diam_ext':form.cleaned_data['Diam_ext1'],
			'Diam_int':form.cleaned_data['Diam_int1'],
			'Annulus':1,
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
			'Annulus':0,
			'Liquido':1,
			'Viscos_tw':form.cleaned_data['Viscos_tw2']},
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
	context = {'form': form}

	return render(request, 'calculo_cascoetubos.html', context)



