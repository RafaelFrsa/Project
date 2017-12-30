from django.shortcuts import render
from trocador.duplotubo.forms import Calculo
from trocador.duplotubo.metodo_kern import *
from trocador.duplotubo.models import *
from trocador.duplotubo.forms import *
from trocador.core.models import *
from django.contrib.auth.decorators import login_required
import pdb 

def propried_get(Table,temp,temp_w,fluido):
    def trecho(Table,temp):
        query1=Table.objects.filter(temperature__gte=temp)[0] 
        query2=Table.objects.filter(temperature__lte=temp)[len(Table.objects.filter(temperature__lte=temp))-1] 
        temp1=query1.temperature;temp2=query2.temperature
        return query1,query2,temp1,temp2
    for propriedade in fluido.keys():
        try:
            if propriedade=='Viscos_tw':
                query1,query2,temp1,temp2=trecho(Agua,temp_w)
                prop1=eval('query1.Viscos');prop2=eval('query2.Viscos')
            else:
                query1,query2,temp1,temp2=trecho(Agua,temp)
                prop1=eval('query1.%s'%propriedade);prop2=eval('query2.%s'%propriedade)
            fluido[propriedade]=(prop2-prop1)*(temp-temp1)/(temp2-temp1) + prop1 if prop2>prop1 else -(prop1-prop2)*(temp-temp1)/(temp2-temp1) + prop1
        except: pass
    fluido['Pr']=fluido['cp']*fluido['Viscos']/fluido['k']
    return fluido

def atribut(formulario,dicionario,identificador=''):
    for dado in formulario.cleaned_data.keys():
        chave=dado.replace(identificador,'')
        if chave in dicionario.keys() and bool(formulario.cleaned_data[dado]):
            dicionario[chave]=formulario.cleaned_data[dado]
            if formulario.fields[dado].label_suffix:
                dicionario[chave]=formulario.cleaned_data[dado]/float(formulario.fields[dado].label_suffix)
    return  dicionario

@login_required
def calculo_duplotubo(request):
    fluidoInterno={'Vazao':0,'T_entr':0,'T_said':0,'cp':0,'k':0,'Pr':0,'Viscos':0,'Densidade':0,'Diam_ext':0,'Diam_int':0,'Annulus':0,'Liquido':1,'Viscos_tw':0}
    fluidoExterno={'Vazao':0,'T_entr':0,'T_said':0,'cp':0,'k':0,'Pr':0,'Viscos':0,'Densidade':0,'Diam_ext':0,'Diam_int':0,'Annulus':1,'Liquido':1,'Viscos_tw':0}
    material={'K':0,'L':1, 'R_fi':0,'R_fo':0,'Calor_cnste':0,'Contracorrente':0,'Num_tubs':0,'Alet_per_tube':0,'Alet_alt':0,'Alet_K':0,'Alet_espes':0,'Alet_type':0,'Tubo_aletado':0,'Multi_tube':0,'Efic_bomb1':0,'Efic_bomb2':0,'arranj_ser_paral':0,'T_I_Paralelo':0,'R_A_Paralelo':0,'Num_ramos':0}
    exibition = Resultado()
    template_name = 'duplotubo/calculo_duplotubo.html'
    form = Calculo(request.POST or None)
    context={'form': form}
    if form.is_valid():
        temp_m1=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1'])/2
        temp_m2=(form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/2
        temp_w=(form.cleaned_data['T_entr1']+form.cleaned_data['T_said1']+form.cleaned_data['T_entr2']+form.cleaned_data['T_said2'])/4
        atribut(form,fluidoInterno,identificador="1")
        atribut(form,fluidoExterno,identificador='2')
        atribut(form,material)
        if form.cleaned_data['nome_fluido1']!='manual':
            propried_get(eval(form.cleaned_data['nome_fluido1']),temp_m1,temp_w,fluidoInterno)
        if form.cleaned_data['nome_fluido2']!='manual':
            propried_get(eval(form.cleaned_data['nome_fluido2']),temp_m2,temp_w,fluidoExterno)
        #pdb.set_trace()
        result_fluido, result_press, result_gerais = yut(fluidoInterno,fluidoExterno,material)
        res = Resultado(result_fl = result_fluido,result_pres = result_press,result_geral = result_gerais)
        res.save()
        context = {'form': form,
                    'Vazao1':result_fluido['Vazao'][0],
                    'Vazao2':result_fluido['Vazao'][1],
                    'Tentr1': result_fluido['Temperatura de Entrada'][0],
                    'Tentr2': result_fluido['Temperatura de Entrada'][1],
                    'Tsaid1': result_fluido['Temperatura de Saida'][0],
                    'Tsaid2': result_fluido['Temperatura de Saida'][1],
                    'Velocidade_Media_Escoamento1':result_fluido['Velocidade Media de Escoamento'][0],
                    'Velocidade_Media_Escoamento2':result_fluido['Velocidade Media de Escoamento'][1],
                    'Numero_Reynolds1':result_fluido['Numero de Reynolds'][0],
                    'Numero_Reynolds2':result_fluido['Numero de Reynolds'][1],
                    'Numero_Nusselts1':result_fluido['Numero de Nusselts'][0],
                    'Numero_Nusselts2':result_fluido['Numero de Nusselts'][1],
                    'dTlmtd':result_gerais['Var. Log. de Temperatura (dTm)'],
                    'Coeficiente_Pelicula1':result_fluido['Coeficiente de Pelicula (h)'][0],
                    'Coeficiente_Pelicula2':result_fluido['Coeficiente de Pelicula (h)'][1],

                    'DP1':result_press['DP'][0],
                    'DP2':result_press['DP'][1],
                    'DPrb1':result_press['DPrb'][0],
                    'DPrb2':result_press['DPrb'][1],
                    'DP_total1':result_press['DPtotal'][0],
                    'DP_total2':result_press['DPtotal'][1],
                    'Potencia_Bombeamento1': result_press['Potencia de Bombeamento'][0],
                    'Potencia_Bombeamento2': result_press['Potencia de Bombeamento'][1],
                    'DP_Bocais1':result_press['DPnl (bocais)'][0],
                    'DP_Bocais2':result_press['DPnl (bocais)'][1],

                    'Area_Troca_Termica_Total':result_gerais['Area de Troca Termica Total'],
                    'Calor_Trocado':result_gerais['Calor Trocado (Heat Duty)'],
                    'Coef_Trans_Calor_Limpo':result_gerais['Coef. de Trans. de Calor Limpo (Uc)'],
                    'Coef_Trans_Calor_Incrustado':result_gerais['Coef. de Trans. de Calor Incrustado (Ud)'],
                    'Fator_Limpeza':result_gerais['Fator de Limpeza (CF)'],
                    'Area_Grampo_Tubular':result_gerais['Area por Grampo Tubular'],
                    'Numero_Grampos':str(result_gerais['Numero de Grampos']),
                    'Excesso_Area':str(result_gerais['Excesso de Area (Over-Surface Design)']),}
    return render(request, template_name, context)