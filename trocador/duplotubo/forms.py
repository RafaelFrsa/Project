# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from trocador.duplotubo.models import Agua, Butano, CO2, Metano, Pentano, RC318

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
			attrs={"class":"form-control", "placeholder":"Vazão em Kg/s",'maxlength':'15'
			}
			)
	 ) 
	 T_entr1 = forms.FloatField(label='Temperatura de Entrada',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Tempreratura de entrada em °C",'maxlength':'15'
			}
			)
	 )  
	 T_said1 = forms.FloatField(label='Temperatura de Saída',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Tempreratura de saída em °C",'maxlength':'15'
			}
			)
	 )   
	 k1 = forms.FloatField(label='Condutividade Térmica',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Condutividade Térmica em W/m.k"
			}
			)
	 )   
	 cp1 = forms.FloatField(label='Capacidade calorífica',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Capacidade calorifica em °C"
			}
			)
	 )   
	 Pr1 = forms.FloatField(label='Número de Prandtl',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Número de Prandtl"
			}
			)
	 )   
	 Viscosidade1 = forms.FloatField(label='Viscosidade Dinâmica',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Viscosidade Dinâmica em Pa.s"
			}
			)
	 )   
	 Densidade1 = forms.FloatField(label='Densidade',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Densidade em kg/m3"
			}
			)
	 )   
	 Diam_ext1 = forms.FloatField(label='Diâmetro Externo',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Diâmetro Externo em mm"

			}
			)
	 )   
	 Diam_int1 = forms.FloatField(label='Diâmetro Interno',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Diâmetro Iterno em mm"
			}
			)
	 )   
	 Viscos_tw1 = forms.FloatField(label='Viscosidade da Temperatura da Parede',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Viscosidade da Temperatura da Parede"
			}
			)
	 )   
	 Vazao2 = forms.FloatField(label='Vazão',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control" , "placeholder":"Vazão em Kg/s"
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
			attrs={"class":"form-control", "placeholder":"Capacidade calorífica em °C"
			}
			)
	 )    
	 k2 = forms.FloatField(label='Condutividade Térmica',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Condutividade Térmica em W/m.k"
			}
			)
	 )    
	 cp2 = forms.FloatField(label='Capacidade calorífica',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder":"Capacidade calorífica em °C"
			}
			)
	 )    
	 Pr2 = forms.FloatField(label='Número de Prandtl',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Número de Prandtl"
			}
			)
	 )   
	 Viscosidade2 = forms.FloatField(label='Viscosidade Dinâmica',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Viscosidade Dinâmica em Pa.s"
 
			}
			)
	 )   
	 Densidade2 = forms.FloatField(label='Densidade_banco',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Viscosidade em kg/m3"
			}
			)
	 )   
	 Diam_ext2 = forms.FloatField(label='Diâmetro Externo',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control" , "placeholder": "Diâmetro Externo em mm"
			}
			)
	 )   
	 Diam_int2 = forms.FloatField(label='Diâmetro Interno',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control" , "placeholder": "Diâmetro Interno em mm"
			}
			)
	 )   
	 Viscos_tw2 = forms.FloatField(label='Viscosidade da Temperatura da Parede',required=False,
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Viscosidade da Temperatura da Parede"

			}
			)
	 )   
	 K = forms.FloatField(label='Condutividade Térmica do Material',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Condutividade Térmica do em W/m.k " 
			}
			)
	 )    
	 L = forms.FloatField(label='Comprimento',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Comprimento em m"
			}
			)
	 )   
	 R_fi = forms.FloatField(label='Fator de Incrustação Interno',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Fator de Incrustação Interno em m2.k/w"
			}
			)
	 )   
	 R_fo = forms.FloatField(label='Fator de Incrustação Externo',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Fator de Incrustação Externo em m2.k/w"
			}
			)
	 )   
	 Calor_const = forms.BooleanField(label='Termicamente Isolado', required=False)
	 Contracorrente = forms.BooleanField(label='Escoamento Contracorrente', required=False)
	 ef_b1 = forms.FloatField(label='Eficiência da Bomba Interna',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Eficiência da Bomba Interna em %"

			}
			)
	 )   
	 ef_b2 = forms.FloatField(label='Eficiência da Bomba Externa',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Eficiência da Bomba Externa em %"

			}
			)
	 )   
	 Num_tubs = forms.FloatField(label='Número de Tubos',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Eficiência da Bomba Externa em %"
			}
			)
	 )   
	 Alet_num = forms.FloatField(label='Quantidade de Aletas',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Quantidade de Aletas"
			}
			)
	 )   
	 Alet_alt = forms.FloatField(label='Altura das Aletas',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Altura das aletas em mm"
			}
			)
	 )   
	 Alet_k = forms.FloatField(label='Condutividade das Aletas',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Condutividade das Aletas"
			}
			)
	 )   
	 Alet_esp = forms.FloatField(label='Espessura das Aletas',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Espessura das Aletas em mm"
			}
			)
	 )   
	 Alet_type = forms.FloatField(label='Tipo de Aletas',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Tipo de Aletas"
			}
			)
	 )   
	 Alet_tubes = forms.BooleanField(label='Tubos Aletados?', required=False)
	 Multi_tubes = forms.BooleanField(label='Tubos Multiplos?', required=False)
	 arranj_ser_paral = forms.BooleanField(label='Arranjo Série e Paralelo', required=False)
	 T_I_Paralelo = forms.BooleanField(label='Tubo Interno Paralelo', required=False)
	 R_A_Paralelo = forms.BooleanField(label='Tubo Externo Paralelo', required=False)
	 Num_ramos = forms.FloatField(label='Número de Ramos',
	 		widget=forms.NumberInput(
			attrs={"class":"form-control", "placeholder": "Número de Ramos"
			}
			)
	 )  






		



