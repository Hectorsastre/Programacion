# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:05:21 2025

@author: SastreCasellasHéctor
"""
import random
numero=[1,2,3,4,5,6,7,10,11,12]#lista de resultados posibles
numero_aleatorio=0#todas las variables a 0
continuar_final=0
puntos=100
puntos_b=100
while not continuar_final==1 or not puntos_b>=0:#para acabar el programa
    continuar=0
    acumulado_b=0
    print(f"La BANCA tiene {puntos_b} puntos acumulados")
    while continuar==0:#el while depende del chivato "continuar"
        if puntos_b<=5:
            print("La BANCA pide una carta")
            numero_aleatorio=random.choice(numero)#elige un numero aleatorio de la lista
        else:
            print("La BANCA se planta")
            continuar+=1
        print(f"Tu carta es {numero_aleatorio}")
        if numero_aleatorio<=7 and numero_aleatorio>=1:#asigna el valos de las cartas del 1 a 7 
                acumulado_b+=numero_aleatorio
        else:#asigna el valor de la sota, el caballo y el rey
                acumulado_b+=0.5
        if acumulado_b>7.5:#para la partida si te pasas, dandola por perdida
            print("Se ha acabado la partida")
            continuar+=1#para el while
        else:
            print(f"BANCA,tu acumulado de puntos es de {acumulado_b} puntos, por ahora")
    print(f"El acumulado de la BANCA es de {acumulado_b} puntos")
    if acumulado_b==7.5:#puntuacion perfecta
        print(f"Enhorabuena BANCA, has ganado la partida")
        puntos+=10
    if acumulado_b>=6 and acumulado_b<=7:#tiene que cumplir los dos factores y te da una puntuacion media
        print("La BANCA ha sido un poco conservadora")
        puntos+=5
    if acumulado_b<6:#puntuacion baja
        print(f"La BANCA no ha arriesgado")
        puntos-=5
    if acumulado_b>7.5:#pierde el jugador
        print("La BANCA perdido la partida!")
        puntos-=10
    if acumulado_b>=6.5 or acumulado_b<=8:
        continuar_final+=0
    else:
        print(f"Te has ido con {acumulado} acumulados")
        print(f"Hasta otra, {alias}")
        continuar_final+=1#para el while
        puntos_b=0#para el primer while