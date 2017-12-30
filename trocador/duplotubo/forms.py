# -*- coding: utf-8 -*-

from django import forms
#from django.forms import ModelForm
from trocador.core.models import Agua, Butano, CO2, Metano, Pentano, RC318

Opcoes = (('manual', 'Manual'),
    ('Agua', 'Água'),
    ('Butano', 'Butano'),
    ('CO2', 'CO2'), 
    ('Metano', 'Metano'),
    ('Pentano', 'Pentano'),   
    ('RC318', 'RC318'),)

Tipos_de_aletas=(('retangular','Retangular'),
                ('circular','Anular'),
                ('studded','Studded'),)

#data={'nome_fluido1':'Agua','nome_fluido2':'Agua','Vazao1':0,'T_entr1':1,'T_said1':1,'k1':2,'cp1':1,'Pr1':1,'Viscos1':12,'Densidade1':12,'Diam_ext1':13,'Diam_int1':11,'Viscos_tw1':14,'Vazao2':12,'T_entr2':15,'T_said2':16,'k2':121,'cp2':143,'Pr2':154,'Viscos2':3,'Densidade2':4,'Diam_ext2':42,'Diam_int2':44,'Viscos_tw2':43,'K':31,'L':34,'R_fi':33,'R_fo':46,'Calor_cnste':51,'Contracorrente':53,'Efic_bomb1':55,'Efic_bomb2':342,'Num_tubs':312,'Alet_per_tube':432,'Alet_alt':32231,'Alet_K':43221,'Alet_espes':3422,'Tubo_aletado':12341,'Alet_type':'retangular','Multi_tube':True,'arranj_ser_paral':True,'T_I_Paralelo':True,'R_A_Paralelo':False,'Num_ramos':1}



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
    Diam_ext1 = forms.FloatField(label='Diâmetro Externo',label_suffix=1000,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Diâmetro Externo em mm"

        }
        )
    )   
    Diam_int1 = forms.FloatField(label='Diâmetro Interno',label_suffix=1000,
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
    Diam_ext2 = forms.FloatField(label='Diâmetro Externo',label_suffix=1000,
            widget=forms.NumberInput(
        attrs={"class":"form-control" , "placeholder": "Diâmetro Externo em mm"
        }
        )
    )   
    Diam_int2 = forms.FloatField(label='Diâmetro Interno',label_suffix=1000,
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
    Efic_bomb1 = forms.FloatField(label='Eficiência da Bomba Interna',initial=100,label_suffix=100,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": " % de Eficiência da Bomba Interna "

        }
        )
    )   
    Efic_bomb2 = forms.FloatField(label='Eficiência da Bomba Externa', initial=100,label_suffix=100,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": " % de Eficiência da Bomba Externa "

        }
        )
    )   
    Num_tubs = forms.FloatField(label='Número de Tubos', initial=1,required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Número de Tubos"
        }
        )
    )   
    Alet_per_tube = forms.IntegerField(label='Quantidade de Aletas',
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Quantidade de Aletas"
        }
        )
    )   
    Alet_alt = forms.FloatField(label='Altura das Aletas',label_suffix=1000,
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
    Alet_espes = forms.FloatField(label='Espessura das Aletas',label_suffix=1000,
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
    Num_ramos = forms.FloatField(label='Número de Ramos', initial=1,required=False,
            widget=forms.NumberInput(
        attrs={"class":"form-control", "placeholder": "Número de Ramos"
        }
        )
    )  
