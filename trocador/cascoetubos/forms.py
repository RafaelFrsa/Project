#-*- coding: cp1252 -*- 
from django import forms
from django.forms import ModelForm
from trocador.cascoetubos.models import Agua, Butano, CO2, Metano, Pentano, Choice, RC318

Opcoes = (
	('', 'Manual'),
    ('duplotubo_agua', u'\xc1gua'),
    ('duplotubo_butano', 'Butano'),
    ('duplotubo_co2', 'CO2'), 
    ('duplotubo_metano', 'Metano'),
    ('duplotubo_pentano', 'Pentano'),   
    ('duplotubo_rc318', 'RC318'),     
    
)


class Calculo(forms.Form):

	# Fluido 1
	nome_fluido1 = forms.ChoiceField(label='Material', choices=Opcoes, required=False, 
	 		widget=forms.Select(
	 		attrs={'class':'btn btn-default dropdown-toggle', 'type':'button', 'role':'separator'}
	 		)
	 	)
	nome_fluido2 = forms.ChoiceField(label='Material', choices=Opcoes, required=False,
	 	widget=forms.Select(
	 		attrs={'class':'btn btn-default dropdown-toggle'}
	 		)
	 	)
	Vazao1 = forms.FloatField(label='Vazão',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	T_entr1 = forms.FloatField(label='Temperatura de Entrada',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	T_said1 = forms.FloatField(label='Temperatura de Saída',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	cp1 = forms.FloatField(label='Capacidade calorífica_banco',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
 		)
	k1 = forms.FloatField(label='Condutividade Térmica_banco',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 

	Pr1 = forms.FloatField(label='Número de Prandtl',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)  
	Viscosidade1 = forms.FloatField(label='Viscosidade_banco',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Densidade1 = forms.FloatField(label='Densidade_banco',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)
	Diam_ext1 = forms.FloatField(label='Diâmetro Externo',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)
	Diam_int1 = forms.FloatField(label='Diâmetro Interno',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	 
	Viscos_tw1 = forms.FloatField(label='Viscosidade_da_temp_parede_banco',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 

	# Fluido 2
	Vazao2 = forms.FloatField(label='Vazao',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	T_entr2 = forms.FloatField(label='Temperatura de Entrada',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)
	T_said2 = forms.FloatField(label='Temperatura de Saída',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	cp2 = forms.FloatField(label='cp',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	k2 = forms.FloatField(label='Condutividade Térmica_banco',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)  
	Pr2 = forms.FloatField(label='Pr',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Viscosidade2 = forms.FloatField(label='Viscosidade', required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	
	Densidade2 = forms.FloatField(label='Densidade_banco',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Diam_ext2 = forms.FloatField(label='Diâmetro Externo_banco',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Diam_int2 = forms.FloatField(label='Diâmetro Interno_banco',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)
	Viscos_tw2 = forms.FloatField(label='Viscosidade_da_temp_parede_banco',required=False,
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 

	# Material
	K = forms.FloatField(label='Condutividade Térmica do Material',
	widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)  
	L = forms.FloatField(label='Comprimento',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	R_fi = forms.FloatField(label='Fator de Incrustação Interno',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	R_fo = forms.FloatField(label='Fator de Incrustação Externo',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Calor_const = forms.BooleanField(label='Termicamente Isolado', required=False)
	Contracorrente = forms.BooleanField(label='Escoamento Contracorrente', required=False)
	Angulo_tubos = forms.FloatField(label='Angulo dos Tubos',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)
	Bfl_spac = forms.FloatField(label='Bfl_spac',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)
	Bfl_prct = forms.FloatField(label='Bfl_prct',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)
	Num_pass_tb = forms.FloatField(label='Número de Passes do Tubo',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
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
			attrs={"class":"form-control"
			}
			)
		)
	Efic_bomb1 = forms.FloatField(label='Eficiencia da Bomba 1',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)
	Efic_bomb2 = forms.FloatField(label='Eficiencia da Bomba 2',
		widget=forms.NumberInput(
			attrs={"class":"form-control"
			}
			)
		)







