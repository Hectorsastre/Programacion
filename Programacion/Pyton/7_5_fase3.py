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
----------------------------""")
numero=[1,2,3,4,5,6,7,10,11,12]#lista de resultados posibles
numero_aleatorio=0#todas las variables a 0
continuar_final=0
puntos=100
alias=input("Introduce tu nombre de jugador: ")
while not continuar_final==1 or not puntos>=0:#para acabar el programa
    continuar=0
    acumulado=0
    print(f"Llevas {puntos} puntos acumulados")
    while continuar==0:#el while depende del chivato "continuar"
        pregunta=input(f"{alias}, quieres una carta?(s/n)")#s=si y n=no
        if pregunta=="n":
            print("Se ha acabado la partida")
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
            print("Se ha acabado la partida")
            continuar+=1#para el while
        else:
            print(f"{alias},tu acumulado de puntos es de {acumulado} puntos, por ahora")
    print(f"Tu acumulado es de {acumulado} puntos")
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
    repetir=input("Quieres repetir?(s/n) ")#s=si y n=no
    if repetir=="s":
        continuar_final+=0
    else:
        print(f"Hasta otra, {alias}")
        continuar_final+=1#para el while
        puntos=0#para el primer while