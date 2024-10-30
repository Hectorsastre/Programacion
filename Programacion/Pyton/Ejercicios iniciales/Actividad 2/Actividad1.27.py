#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla:
letra=input("Introduce una letra: ")
if str.isdigit(letra):
    print("Eso no es una letra, es un numero")
else:
    if str.isupper (letra):
        print(f"La letra {letra} es mayuscula")
    elif str.islower (letra):
        print(f"La letra {letra} es minuscula")
    else:
        print("Que es eso?")
    