#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice
frase= " A quien madruga Dios le ayuda"
print("A quien madruga Dios le ayuda")
palabra=frase.find(input("Dime una palabra: "))
if palabra>0:
    print("La palabra esta en la frase")
else:
    print("Esa palabra no es parte de la frase")