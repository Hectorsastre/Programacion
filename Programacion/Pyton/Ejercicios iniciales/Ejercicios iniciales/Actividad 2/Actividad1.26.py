#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra=input("Introduce una letra: ")
if str.isupper (letra):
    print(f"La letra {letra} es mayuscula")
elif str.islower(letra):
    print(f"La letra {letra} es minuscula")
else:
    print("¿Que es eso?")
