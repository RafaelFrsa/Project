#-*- coding: cp1252 -*- 
from django import forms


class Calculo(forms.Form):

	# Fluido 1
	Vazao1 = forms.FloatField(label='Vazão',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	T_entr1 = forms.FloatField(label='Temperatura de Entrada',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	T_said1 = forms.FloatField(label='Temperatura de Saída',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	cp1 = forms.FloatField(label='Capacidade calorífica_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
 		)
	k1 = forms.FloatField(label='Condutividade Térmica_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 

	Pr1 = forms.FloatField(label='Número de Prandtl',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)  
	Viscosidade1 = forms.FloatField(label='Viscosidade_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Densidade1 = forms.FloatField(label='Densidade_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)
	Diam_ext1 = forms.FloatField(label='Diâmetro Externo',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)
	Diam_int1 = forms.FloatField(label='Diâmetro Interno',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Anullus1 = forms.FloatField(label='Annulus',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Liquido1 = forms.FloatField(label='Liquido',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Viscos_tw1 = forms.FloatField(label='Vazão',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 

	# Fluido 2
	Vazao2 = forms.FloatField(label='Vazao',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	T_entr2 = forms.FloatField(label='Temperatura de Entrada',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)
	T_said2 = forms.FloatField(label='Temperatura de Saída',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	cp2 = forms.FloatField(label='cp',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	k2 = forms.FloatField(label='Condutividade Térmica_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)  
	Pr2 = forms.FloatField(label='Pr',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Viscosidade2 = forms.FloatField(label='Viscosidade', 
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	
	Densidade2 = forms.FloatField(label='Densidade_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Diam_ext2 = forms.FloatField(label='Diâmetro Externo_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Diam_int2 = forms.FloatField(label='Diâmetro Interno_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Anullus2 = forms.FloatField(label='Diâmetro Interno_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)
	Liquido2 = forms.FloatField(label='Diâmetro Interno_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)
	Viscos_tw2 = forms.FloatField(label='Viscosidade_da_temp_parede_banco',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 

	# Material
	K = forms.FloatField(label='Condutividade Térmica do Material',
	widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)  
	L = forms.FloatField(label='Comprimento',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	R_fi = forms.FloatField(label='Fator de Incrustação Interno',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	R_fo = forms.FloatField(label='Fator de Incrustação Externo',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Calor_const = forms.BooleanField(label='Termicamente Isolado', required=False)
	Contracorrente = forms.BooleanField(label='Escoamento Contracorrente', required=False)
	Num_tubs = forms.FloatField(label='Número de Tubos',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)
	Alet_per_tube = forms.FloatField(label='Quantidade de Aletas',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Alet_alt = forms.FloatField(label='Altura das Aletas',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Alet_k = forms.FloatField(label='Condutividade das Aletas',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Alet_esp = forms.FloatField(label='Espessura das Aletas',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Alet_type = forms.FloatField(label='Tipo das Aletas',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		) 
	Alet_tubes = forms.FloatField(label='Tubos Aletados?',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)  
	





