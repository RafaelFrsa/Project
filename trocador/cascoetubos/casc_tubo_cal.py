# -*- coding: cp1252 -*-
import sys

from math import *
from dupl_tubo import *

def heat_friction_shell(fluido1,fluido2,material):
    calor_vazao(fluido1,fluido2)
    Ang=material['Angulo_tubos'];Ds=fluido1['Diam_int'];Do=fluido2['Diam_ext']
    d_i=fluido2['Diam_int']
    fluido1['Area_s']=Ds*material['Bfl_spac']*(material['Pt']-Do)/material['Pt']
    fluido1['Re']=fluido2['Diam_ext']*fluido1['Vazao']/fluido1['Viscos']/fluido1['Area_s']
    Res=fluido1['Re'];
    Gs=fluido1['Vazao']/fluido1['Area_s']
    fluido1['G']=Gs
    material['Diam_feixe_tubos']= (Ds - 9.525*10**-3) if Ds<0.3 else (Ds-12.7*10**-3) if (Ds>=300 and Ds<=100) else (Ds-15.875*10**-3)
    Dctl= material['Diam_feixe_tubos'] - Do
    Bc=material['Bfl_prct'];#Fractional Baffle cut, porcentagem da chicana que está cortada
    teta_ds=2*acos(1-2*Bc);
    B=material['Bfl_spac'];Ns=material['Num_passes_casco']
    delta_sb=(0.8+0.002*Ds/1000.+0.75)*10**-3
    delta_tb = 0.4*10**-3 if Do>0.03175 else 0.4 if (2*B)<0.9144 else 0.2
    S_b=B*(Ds-material['Diam_feixe_tubos']);
    S_sb=Ds*delta_sb*(pi-0.5*teta_ds);
    S_tb=pi*Do*delta_tb;
    Pt_eff=material['Pt'] if Ang==30 else material['Pt']/(2**0.5);
    Pt_linha=material['Pt'] if Ang==90 else material['Pt']*cos(radians(Ang))
    S_m=B*((Ds-material['Diam_feixe_tubos'])+((material['Diam_feixe_tubos']-Do)/(Pt_eff))*(material['Pt']-Do))
    material['Num_bfl']=int(material['L']/B) if material['L']%B!=0 else (material['L']/B-1)
    nb=material['Num_bfl']
    np=material['Num_pass_tb']
    CTP=0.93 if np==1 else 0.9 if np==2 else 0.85 if np==3 else 0.85
    CL=1.0 if Ang==90 or Ang==45 else 0.87
    PR=material['Pt']/(Do)
    material['Num_tubos_Preliminar']=int(0.785*(CTP/CL)*((Ds**2)/(pow((PR*Do),2))))+1
    nt=material['Num_tubos_Preliminar']
    Bout=0.8*B if material['L']%B!=0 else B
    Bin=0.8*B if material['L']%B!=0 else B
    Nc=int(Ds*(1-2*Bc)/Pt_linha)+1
    Nss=Nc*0.2 if Res>100 else Nc*0.1
    Ncw=int(0.8*Bc*fluido1['Diam_int']/Pt_linha)+1
#####Cálculo de Jc
    teta_ctl=2*acos((Ds*(1-2*Bc))/Dctl)
    Fc=1+(sin(teta_ctl)-teta_ctl)/pi
    Fw=(1-Fc)/2.
    Jc=0.55+0.72*Fc
##Cálculo de Jl
    rs=S_sb/(S_sb+S_tb);rl=(S_sb+S_tb)/S_m
    Jl=0.44*(1-rs)+(1-0.44*(1-rs))*exp(-2.2*rl)
##Cálculo de Jb
    rss=Nss/Nc
    Cj=1.35 if Res<100 else 1.25
    Cr=4.5 if Res<100 else 3.7
    Jb=1 if rss>=0.5 else exp(-Cj*(S_b/S_m)*(1-pow(2*rss,1/3.)))
##Cálculo de Jr
    Nct=(nb+1)*(Nc+Ncw)
    Jr=pow(10/Nct,0.18) if Res<20 else (7.5*10**-3*Res+0.25) if (Res>=20 and Res<100) else 1.0
##Cálculo de Js
    n1=0.6 if Res>=100 else 1/3.
    n2=0.2 if Res>=100 else 1.0
    Js=(nb-1+pow(Bin/B,(1-n1))+pow(Bout/B,(1-n1)))/(nb-1+Bin/B + Bout/B)
    fluido1['Area_w']=0.125*pow(Ds,2)*(teta_ds-sin(teta_ds))-0.25*nt*Fw*pi*pow(Do,2)
    S_w=fluido1['Area_w']
##Cálculo dos Fatores de Correção para Queda de Pressão
    Rl=exp(-1.33*(1+rs)*pow(rl,(0.8-0.15*(1+rs))))
    Rb=exp(-Cr*(S_b/S_m)*(1-pow(2*rss,1/3.)))
    Rs=0.5*(pow((B/Bin),(2-n2))+pow((B/Bout),(2-n2)))
    Dw=4*S_w/(pi*Do*nt*0.5*(1-Fc)+Ds*teta_ds)
    if Res>=10**4:
        APw_ideal=pow(fluido1['Vazao'],2)*(2+0.6*Ncw)/(2*fluido1['Densidade']*fluido1['Area_s']*S_w)
        if Ang==30:
            a1,a2,a3,a4,b1,b2,b3,b4=.321,-.388,1.450,.519,.372,-.123,7.00,0.5
        if Ang==45:
            a1,a2,a3,a4,b1,b2,b3,b4=.370,-.396,1.930,0.5,0.303,-0.126,6.59,0.520
        if Ang==90:
            a1,a2,a3,a4,b1,b2,b3,b4=0.370,-.395,1.187,.370,0.391,-.148,6.30,0.378
    elif Res>10**3 and Res<10**4:
        APw_ideal=pow(fluido1['Vazao'],2)*(2+0.6*Ncw)/(2*fluido1['Densidade']*fluido1['Area_s']*S_w)
        if Ang==30:
            a1,a2,a3,a4,b1,b2,b3,b4=0.321,-.388,1.450,.0519,.486,-.152,7.00,0.5
        if Ang==45:
            a1,a2,a3,a4,b1,b2,b3,b4=0.370,-0.396,1.930,0.5,0.333,-0.136,6.59,0.52
        if Ang==90:
            a1,a2,a3,a4,b1,b2,b3,b4=.107,-0.266,1.187,0.370,0.0815,0.022,6.30,0.378
    elif Res>10**2 and Res<10**3:
        APw_ideal=pow(fluido1['Vazao'],2)*(2+0.6*Ncw)/(2*fluido1['Densidade']*fluido1['Area_s']*S_w)
        if Ang==30:
            a1,a2,a3,a4,b1,b2,b3,b4=.593,-.477,1.450,0.519,4.570,-.0,476,7.00,0.5
        if Ang==45:
            a1,a2,a3,a4,b1,b2,b3,b4=.730,-0.5,1.930,0.5,3.5,-.476,6.59,0.520
        if Ang==90:
            a1,a2,a3,a4,b1,b2,b3,b4=0.408,-.46,1.187,0.370,6.09,-.602,6.30,0.378
    elif Res>10 and Res<10**2:
        APw_ideal=26*(fluido1['Viscos']*fluido1['Vazao']/(pow(fluido1['Densidade']*fluido1['Area_s']*S_w,0.5)))*(Ncw/(fluido1['Densidade']-Do)+B/pow(Dw,2))+(fluido1['Vazao']/(fluido1['Densidade']*fluido1['Area_s']*S_w))
        if Ang==30:
            a1,a2,a3,a4,b1,b2,b3,b4=1.36,-.657,1.450,.519,45.1,-.973,7.00,0.5
        if Ang==45:
            a1,a2,a3,a4,b1,b2,b3,b4=0.498,-.656,1.930,0.5,26.2,-.913,6.59,0.520
        if Ang==90:
            a1,a2,a3,a4,b1,b2,b3,b4=0.9,-.631,1.187,0.370,32.1,-.963,6.30,0.378
    else:
        APw_ideal=26*(fluido1['Viscos']*fluido1['Vazao']/(pow(fluido1['Densidade']*fluido1['Area_s']*S_w,0.5)))*(Ncw/(fluido1['Densidade']-Do)+B/pow(Dw,2))+(fluido1['Vazao']/(fluido1['Densidade']*fluido1['Area_s']*S_w))
        if Ang==30:
            a1,a2,a3,a4,b1,b2,b3,b4=1.4,-.667,1.450,0.519,48.0,-1.0,7.0,0.5
        if Ang==45:
            a1,a2,a3,a4,b1,b2,b3,b4=1.550,-.667,1.930,0.5,32.0,-1.0,6.59,0.52
        if Ang==90:
            a1,a2,a3,a4,b1,b2,b3,b4=.970,-.667,1.187,0.370,35.0,-1,6.3,0.378
    a=a3/(1+0.14*pow(Res,a4))
    ji=a1*pow(1.33/(material['Pt']/Do),a)*pow(Res,a2)
    h_id=ji*(fluido1['cp'])*(Gs)*(pow((fluido1['k']/(fluido1['cp']*fluido1['Viscos'])),2/3.))*(pow(fluido1['Viscos']/fluido1['Viscos_tw'],0.14))
####Observação do Serth, correlações para cálculos para os fatores de correção
    h_o=h_id*Jc*Jl*Jb*Js*Jr
    fluido1['H_ID']=h_id;fluido1['Ji']=ji
    fluido1['Fator_Correcao_Geral_Calor']=Jc*Jl*Jb*Js*Jr
    fluido1['Coeficient_calor']=h_o
    fluido1['Nu']=h_o*Do/fluido1['k']
    ## Número de Reynolds Tubo 2
    A_t=pi*fluido2['Diam_int']**2/4;A_tp=nt*A_t/np
    fluido2['G']=fluido2['Vazao']/A_tp;fluido2['Vel_mf']=fluido2['G']/fluido2['Densidade']
    fluido2['Re']=fluido2['Vel_mf']*fluido2['Densidade']*fluido2['Diam_int']/fluido2['Viscos']
    nusselt_tube(fluido2,fluido1,material)
    f=pow((1.58*log(fluido2['Re'])-3.28),-2.)
    fluido2['Coeficient_calor']=fluido2['Nu']*fluido2['k']/fluido2['Diam_int']
    ############### Equações de Queda de Pressão e Dimensionamento #################
    b=b3/(1+0.14*pow(Res,b4))
    f_i=b1*pow(1.33/(material['Pt']/Do),b)*pow(Res,b2)
    fluido1['f_i']=f_i
    fluido1['Nc,nb,ncw']=Nc,nb,Ncw;fluido1[u'\u0394Pw_ideal']=APw_ideal
    AP_ideal=(2*f_i*Nc*pow(Gs,2)/(fluido1['Densidade']*pow(fluido1['Viscos']/fluido1['Viscos_tw'],0.14)))
    APf=((nb-1)*AP_ideal*Rb+nb*APw_ideal)*Rl+2*AP_ideal*(1+Ncw/Nc)*Rb*Rs
    fluido1[u'\u0394P do Casco']=APf
    fluido1[u'\u0394P_Central_Chicanas']=(nb-1)*Rl*Rb*AP_ideal #Serth 6.9 pg 212
    fluido1[u'\u0394P_Janela_Chicanas']=nb*APw_ideal*Rl #Serth 6.14 pg 213
    fluido1[u'\u0394P_Entrada_Saida']=2*AP_ideal*(1+Ncw/Nc)*Rb*Rs #Serth 6.15 pg 213
    s1=fluido1['Densidade']/1000.0;s2=fluido1['Densidade']/1000.0
    APn1=(7.5*10**-4)*(Ns*(fluido1['G']**2))/s1 if Res>2000 else ((1.5*10**-3)*(Ns*(fluido1['G']**2))/s1)
    APn2=(7.5*10**-4)*(Ns*(fluido2['G']**2))/s2 if Res>2000 else ((1.5*10**-3)*(Ns*(fluido2['G']**2))/s2)
    fluido1[u'\u0394Ptotal']=APf+APn1
    ###Para o segundo a partir de agora ######!!!!
    fluido2['f']=f
    APf2=(4*f*material['L']*np/fluido2['Diam_int']+4*np)*(fluido2['Densidade']*fluido2['Vel_mf']/2)
    fluido2[u'\u0394Ptotal']=APf2+APn2
    fluido1['Potencia_bomb']=fluido1['Vazao']*fluido1[u'\u0394Ptotal']/(material['Efic_bomb1']*fluido1['Densidade'])
    fluido2['Potencia_bomb']=fluido2['Vazao']*fluido2[u'\u0394Ptotal']/(material['Efic_bomb2']*fluido2['Densidade'])
    F=correction_factor(fluido1,fluido2,material)
    dTm=check_dtm(fluido1,fluido2,material)
    U_o=(Do/(d_i*fluido2['Coeficient_calor'])+(Do*log(Do/d_i)/(2*material['K']))+1/h_o)**-1
    Q=fluido1['Vazao']*fluido1['cp']*abs(fluido1['T_entr']-fluido1['T_said'])
    U_f=(1/U_o+material['R_fi']+material['R_fo'])**-1
    OS=(U_o/U_f)-1
    area_c=Q/(U_o*F*dTm)
    area_f=Q/(U_f*F*dTm)
    fluido1['Vel_mf']=fluido1['G']/fluido1['Densidade']
    material['Num_tubos']=area_f/(material['L']*pi*Do)
    fluido1['dPN']=APn1
    fluido2['dPN']=APn2
    material['area_c']=area_c
    material['area_f']=area_f
    material['Q']=Q
    material['Uc']=U_o
    material['Ud']=U_f
    material['dTm']=dTm
    material['S_m']=S_m
    material['S_b']=S_b
    material['S_sb']=S_sb
    material['S_tb']=S_tb
    material['OS']=OS

    return fluido1, fluido2, material











