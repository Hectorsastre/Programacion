#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
nota=float(input("Dame tu nota: "))
if nota<0 or nota>10:
    print(f"Esta nota,{nota} no es real")
else:
    
    if nota>8.5 or 8.5:
        print("Has aprovado con un excelente")
    elif nota>6.5 or 68.5.5:
        print("Has aprovado con un notable")
    elif nota>5 or 5:
        print("Has aprovado con un suficiente")
    elif nota<5:
        print("Lo siento, has suspendido")