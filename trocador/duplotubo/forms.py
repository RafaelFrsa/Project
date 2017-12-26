# -*- coding: utf-8 -*-

from django import forms
#from django.forms import ModelForm
from trocador.core.models import Agua, Butano, CO2, Metano, Pentano, RC318

Opcoes = (
    ('manual', 'Manual'),
    ('core_agua', 'Água'),
    ('core_butano', 'Butano'),
    ('core_co2', 'CO2'), 
    ('core_metano', 'Metano'),
    ('core_pentano', 'Pentano'),   
    ('core_rc318', 'RC318'),     
    
)

Tipos_de_aletas=(('retangular','Retangular'),
                ('circular','Anular'),
                ('studded','Studded'),)



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
        attrs={"class":"form-control", "placeholder":"Vazão em kg/s",'maxlength':'15'
        }
        )
    ) 
    T_entr1 = forms.FloatField(label='Temperatura de Entrada',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder":"Temperatura em °C",'maxlength':'15'
        }
        )
    )  
    T_said1 = forms.FloatField(label='Temperatura de Saída',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder":"Temperatura em °C",'maxlength':'15'
        }
        )
    )   
    k1 = forms.FloatField(label='Condutividade Térmica',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder":"Condutividade Térmica em W/m.k",'maxlength':'15'
        }
        )
    )   
    cp1 = forms.FloatField(label='Calor Especifico',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder":"Calor Especifico em J/(kg.K)",'maxlength':'15'
        }
        )
    )   
    Pr1 = forms.FloatField(label='Número de Prandtl',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Número de Prandtl"
        }
        )
    )   
    Viscos1 = forms.FloatField(label='Viscosidade Dinâmica',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Viscosidade Dinâmica em Pa.s"
        }
        )
    )   
    Densidade1 = forms.FloatField(label='Densidade',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Densidade em kg/m³"
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
        attrs={"class":"form-control", "placeholder": "Diâmetro Interno em mm"
        }
        )
    )   
    Viscos_tw1 = forms.FloatField(label='Viscosidade na Temperatura da Parede',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder":"Viscosidade na Temperatura da Parede"
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
        attrs={"class":"form-control", "placeholder":"Temperatura em °C"
        }
        )
    )    
    T_said2 = forms.FloatField(label='Temperatura de Saída',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder":"Temperatura em °C"
        }
        )
    )    
    k2 = forms.FloatField(label='Condutividade Térmica',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder":"Condutividade Térmica W/m.k"
        }
        )
    )    
    cp2 = forms.FloatField(label='Calor Específico',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder":"Calor Específico em J/(kg.K)"
        }
        )
    )    
    Pr2 = forms.FloatField(label='Número de Prandtl',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Número de Prandtl"
        }
        )
    )   
    Viscos2 = forms.FloatField(label='Viscosidade Dinâmica',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Viscosidade Dinâmica em Pa.s"

        }
        )
    )   
    Densidade2 = forms.FloatField(label='Densidade',required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Densidade em kg/m³"
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
        attrs={"class":"form-control", "placeholder": "Condutividade Térmica em W/m.K " 
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
        attrs={"class":"form-control", "placeholder": "F. I. Interno em m².K/W "
        }
        )
    )   
    R_fo = forms.FloatField(label='Fator de Incrustação Externo',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "F. I. Externo em  m².K/W "
        }
        )
    )   
    Calor_cnste = forms.BooleanField(label='Termicamente Isolado?', required=False)
    Contracorrente = forms.BooleanField(label='Escoamento Contracorrente?', required=False)
    Efic_bomb1 = forms.FloatField(label='Eficiência da Bomba Interna',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": " % de Eficiência da Bomba Interna "

        }
        )
    )   
    Efic_bomb2 = forms.FloatField(label='Eficiência da Bomba Externa',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": " % de Eficiência da Bomba Externa "

        }
        )
    )   
    Num_tubs = forms.FloatField(label='Número de Tubos',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Número de Tubos"
        }
        )
    )   
    Alet_per_tube = forms.FloatField(label='Quantidade de Aletas',
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
    Alet_K = forms.FloatField(label='Condutividade das Aletas',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Condutividade das Aletas"
        }
        )
    )   
    Alet_espes = forms.FloatField(label='Espessura das Aletas',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Espessura das Aletas em mm"
        }
        )
    )
    Tubo_aletado = forms.BooleanField(label='Tubos Aletados?', required=False)
    Alet_type = forms.ChoiceField(label='Tipo de Aleta', choices=Tipos_de_aletas, required=False, 
            widget=forms.Select(
            attrs={'class':'btn btn-default dropdown-toggle', 'type':'button', 'role':'separator'}))  

    Multi_tube = forms.BooleanField(label='Tubos Multiplos ?', required=False)
    arranj_ser_paral = forms.BooleanField(label='Arranjo Série e Paralelo ?', required=False)
    T_I_Paralelo = forms.BooleanField(label='Tubo Interno Paralelo ?', required=False)
    R_A_Paralelo = forms.BooleanField(label='Tubo Externo Paralelo ?', required=False)
    Num_ramos = forms.FloatField(label='Número de Ramos',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Número de Ramos"
        }
        )
    )  