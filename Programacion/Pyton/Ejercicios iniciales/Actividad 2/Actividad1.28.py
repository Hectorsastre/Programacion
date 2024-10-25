#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
letra=input("Introduce una letra: ")
if str.isdigit(letra):
    print("Eso no es una letra, es un numero")
else:
    if str.isupper (letra):
        print(f"La letra {letra} es mayuscula")
    elif str.islower (letra):
        print(f"La letra {letra} es minuscula")
    else:
        print("Eso no es una letra, es un simbolo")