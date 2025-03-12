#Juego del 7'5_Fase 3
import random#inserta la libreria
print("""Bienvenido al juego del 7 y 1/2:
1.-Por cada ronda reciviras una carta. 
2.-El valor de cada carta corresponde al índice o número que figura en una carta,
excepto la sota (10), el caballo (11) y el rey (12), 
estas cartas puntúan con medio punto (0.5).
3.-Plantate cuando quieras.
4.-El objetivo del juego es conseguir sumar la cantidad exacta de 7.5,
o bien, el número más cercano posible sin sobrepasar 7.5.
5.-Si te pasas, pierdes
Jugarás contra la BANCA
Mucha suerte jugador
----------------------------
""")
numero=[1,2,3,4,5,6,7,10,11,12]#lista de resultados posibles
numero_aleatorio=0#todas las variables a 0
continuar_final=0
puntos=100
puntos_b=100
alias=input("Introduce tu nombre de jugador: ")
while not continuar_final==1 or not puntos>=0:#para acabar el programa
    continuar=0
    continuar_b=0
    acumulado=0
    acumulado_b=0
    print(f"""Llevas {puntos} puntos acumulados
La BANCA tiene {puntos_b} puntos acumulados
- ------------------------ -
""")
    while continuar==0:#el while depende del chivato "continuar"
        pregunta=input(f"{alias}, quieres una carta?(s/n)")#s=si y n=no
        if pregunta=="n":
            print("""Se ha acabado la partida
                  """)
            continuar+=1#para el while
        if pregunta=="s":
            continuar+=0
            numero_aleatorio=random.choice(numero)#elige un numero aleatorio de la lista
            print(f"Tu carta es {numero_aleatorio}")
            if numero_aleatorio<=7 and numero_aleatorio>=1:#asigna el valos de las cartas del 1 a 7 
                acumulado+=numero_aleatorio
            else:#asigna el valor de la sota, el caballo y el rey
                acumulado+=0.5
        if acumulado>7.5:#para la partida si te pasas, dandola por perdida
            print("""Se ha acabado la partida
                  """)
            continuar+=1#para el while
        else:
            print(f"{alias},tu acumulado de puntos es de {acumulado} puntos, por ahora")
    print(f"""Tu acumulado es de {acumulado} puntos
- ------------------------ -
""")
    print("Ahora le toca a la BANCA")
    input("Presione ENTER para continuar")
    while continuar_b==0:#el while depende del chivato "continuar"
        if acumulado_b<=5:
            print("La BANCA pide una carta")
            numero_aleatorio=random.choice(numero)#elige un numero aleatorio de la lista
            print(f"La carta es {numero_aleatorio}")
            if numero_aleatorio<=7 and numero_aleatorio>=1:#asigna el valos de las cartas del 1 a 7 
                    acumulado_b+=numero_aleatorio
            else:#asigna el valor de la sota, el caballo y el rey
                    acumulado_b+=0.5
            if acumulado_b>7.5:#para la partida si te pasas, dandola por perdida
                print(f"El acumulado de la BANCA es de {acumulado_b} puntos")
                print("""Se ha acabado la partida
                      """)
                continuar_b+=1#para el while
            else:
                print(f"""BANCA,tu acumulado de puntos es de {acumulado_b} puntos, por ahora
- ------------------------ -
""")
                input("Presione ENTER para continuar")
        else:
            print("""La BANCA se planta
- ------------------------ -
""")
            continuar_b+=1
    print(f"El acumulado de la BANCA es de {acumulado_b} puntos")
    print(f"Tu acumulado era de {acumulado} puntos")
    input("Presione ENTER para continuar")
    
    if acumulado==7.5:#puntuacion perfecta
        print(f"Enhorabuena {alias}, has ganado la partida")
        puntos+=10
    if acumulado>=6 and acumulado<=7:#tiene que cumplir los dos factores y te da una puntuacion media
        print("Has sido un poco conservador")
        puntos+=5
    if acumulado<6:#puntuacion baja
        print(f"Quizás tendrías que arriesgar un poco ¿no {alias}?")
        puntos-=5
    if acumulado>7.5:#pierde el jugador
        print("Has perdido la partida!")
        puntos-=10
    if acumulado_b==7.5:#puntuacion perfecta
        print(f"Enhorabuena BANCA, has ganado la partida")
        input("Presione ENTER para continuar")
        puntos_b+=10
    if acumulado_b>=6 and acumulado_b<=7:#tiene que cumplir los dos factores y te da una puntuacion media
        print("La BANCA ha sido un poco conservadora")
        input("Presione ENTER para continuar")
        puntos_b+=5
    if acumulado_b<6:#puntuacion baja
        print(f"La BANCA no ha arriesgado")
        input("Presione ENTER para continuar")
        puntos_b-=5
    if acumulado_b>7.5:#pierde el jugador
        print("La BANCA perdido la partida!")
        input("Presione ENTER para continuar")
        puntos_b-=10
    if not acumulado<acumulado_b and acumulado<=7.5:
        print(f"""Has ganado a la BANCA {alias}!
              """)
    if acumulado>=8 and acumulado_b>=8:
        print("""Perdeis los dos
              """)
    if acumulado==acumulado_b:
        if acumulado>=8:
            print("""Perdeis los dos
                  """)
        else:
            print("""Un empate?
                  """)
    if acumulado<acumulado_b and acumulado_b<=7.5:
        print("""Ganó la BANCA
              """)
    repetir=input("Quieres repetir?(s/n) ")#s=si y n=no
    if repetir=="s":
        continuar_final+=0
    else:
        print(f"Te has ido con {puntos} puntos acumulados")
        print(f"Hasta otra, {alias}")
        continuar_final+=1#para el while
        puntos=0#para el primer while