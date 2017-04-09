# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from trocador.cascoetubos.models import Agua, Butano, CO2, Metano, Pentano, RC318

Opcoes = (
	('', 'Manual'),
    ('duplotubo_agua', 'Água'),
    ('duplotubo_butano', 'Butano'),
    ('duplotubo_co2', 'CO2'), 
    ('duplotubo_metano', 'Metano'),
    ('duplotubo_pentano', 'Pentano'),   
    ('duplotubo_rc318', 'RC318'),     
    
)


class Calculo(forms.Form):

	# Fluido 1
	nome_fluido1 = forms.ChoiceField(label='Componente', choices=Opcoes, required=False, 
	 		widget=forms.Select(
	 		attrs={'class':'btn btn-default dropdown-toggle', 'type':'button', 'role':'separator'}
	 		)
	 	)
	nome_fluido2 = forms.ChoiceField(label='Componente', choices=Opcoes, required=False,
	 	widget=forms.Select(
	 		attrs={'class':'btn btn-default dropdown-toggle'}
	 		)
	 	)
	Vazao1 = forms.FloatField(label='Vazão', 
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Vazão em Kg/s"
			}
			)
		) 
	T_entr1 = forms.FloatField(label='Temperatura de Entrada',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Tempreratura de entrada em °C"

			}
			)
		) 
	T_said1 = forms.FloatField(label='Temperatura de Saída',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Tempreratura de saída em °C"

			}
			)
		) 
	cp1 = forms.FloatField(label='Capacidade calorífica',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
 		)
	k1 = forms.FloatField(label='Condutividade Térmica',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Condutividade Térmica em W/m.k"
			}
			)
		) 

	Pr1 = forms.FloatField(label='Número de Prandtl',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Número de Prandtl"
			}
			)
		)  
	Viscosidade1 = forms.FloatField(label='Viscosidade',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Viscosidade Dinâmica em Pa.s"
			}
			)
		) 
	Densidade1 = forms.FloatField(label='Densidade',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Densidade em kg/m3"
			}
			)
		)
	Diam_ext1 = forms.FloatField(label='Diâmetro Externo',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Diâmetro externo em mm"
			}
			)
		)
	Diam_int1 = forms.FloatField(label='Diâmetro Interno',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Diâmetro interno em mm"
			}
			)
		) 
	 
	Viscos_tw1 = forms.FloatField(label='Viscosidade da temperatura da parede',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Viscosidade de temperatura da parede"
			}
			)
		) 

	# Fluido 2
	Vazao2 = forms.FloatField(label='Vazao',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Vazão em Kg/s"
			}
			)
		) 
	T_entr2 = forms.FloatField(label='Temperatura de Entrada',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Tempreratura de entrada em °C"

			}
			)
		)
	T_said2 = forms.FloatField(label='Temperatura de Saída',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Tempreratura de saída em °C"

			}
			)
		) 
	cp2 = forms.FloatField(label='Capacidade calorífica',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Tempreratura de saída em °C"
			}
			)
		) 
	k2 = forms.FloatField(label='Condutividade Térmica',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Condutividade Térmica em W/m.k"
			}
			)
		)  
	Pr2 = forms.FloatField(label='Número de Prandtl',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Número de Prandtl"
			}
			)
		) 
	Viscosidade2 = forms.FloatField(label='Viscosidade', required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Viscosidade Dinâmica em Pa.s"
			}
			)
		) 
	
	Densidade2 = forms.FloatField(label='Densidade',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Densidade em kg/m3"
			}
			)
		) 
	Diam_ext2 = forms.FloatField(label='Diâmetro Externo',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Diâmetro Externo em mm"
			}
			)
		) 
	Diam_int2 = forms.FloatField(label='Diâmetro Interno',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Diâmetro Interno em mm"
			}
			)
		)
	Viscos_tw2 = forms.FloatField(label='Viscosidade de temperatura da parede',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Viscosidade de temperatura da parede"
			}
			)
		) 

	# Material
	K = forms.FloatField(label='Condutividade Térmica do Material',
	widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Condutividade Térmica em W/m.k"
			}
			)
		)  
	L = forms.FloatField(label='Comprimento',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Comprimento em m"

			}
			)
		) 
	R_fi = forms.FloatField(label='Fator de Incrustação Interno',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Fator de incrustação interno em m2.K/W"

			}
			)
		) 
	R_fo = forms.FloatField(label='Fator de Incrustação Externo',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Fator de incrustação externo em m2.K/W"
			}
			)
		) 
	Calor_const = forms.BooleanField(label='Termicamente Isolado', required=False)
	Contracorrente = forms.BooleanField(label='Escoamento Contracorrente', required=False)
	Angulo_tubos = forms.FloatField(label='Angulo dos Tubos',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Angulo dos Tubos"
			}
			)
		)
	Bfl_spac = forms.FloatField(label='Distância Entre Chicanas',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":" Distância Entre Chicanas em mm"
			}
			)
		)
	Bfl_prct = forms.FloatField(label='Porcentagem de Abertura das Chicanas',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":" Porcentagem de Abertura das Chicanas"

			}
			)
		)
	Num_pass_tb = forms.FloatField(label='Número de Passes do Tubo',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Número dos passes do tubo"
			}
			)
		)
	Pt = forms.FloatField(label='Pt',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)
	Num_passes_casco = forms.FloatField(label='Número dos passes do casco',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Número dos passes do casco"
			}
			)
		)
	Efic_bomb1 = forms.FloatField(label='Eficiencia da Bomba 1',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Eficiencia da Bomba 1"

			}
			)
		)
	Efic_bomb2 = forms.FloatField(label='Eficiencia da Bomba 2',
		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Eficiencia da Bomba 2"
			}
			)
		)







