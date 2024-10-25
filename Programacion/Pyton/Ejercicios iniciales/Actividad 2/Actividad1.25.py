#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos
nota=float(input("Dame tu nota: "))
if nota<0 or nota>10:
    print(f"Esta nota,{nota} no es real")
else:
    
    if nota>8.5 or 8.5:
        print("Has aprovado con un excelente")
    elif nota>6.5 or 6.5:
        print("Has aprovado con un notable")
    elif nota>5 or 5:
        print("Has aprovado con un suficiente")
    elif nota<5:
        print("Lo siento, has suspendido")