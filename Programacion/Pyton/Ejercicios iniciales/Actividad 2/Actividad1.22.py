#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=float(input("Dame tu nota: "))
if nota<0 or nota>10:
    print(f"Esta nota,{nota} no es real")
else:
    
    if nota<5:
        print("Lo siento, has suspendido")
    else:
        print("Felicidades, has aprovado")
