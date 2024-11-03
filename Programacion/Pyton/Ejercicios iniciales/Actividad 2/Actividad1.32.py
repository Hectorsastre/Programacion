#32.  Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
frase= "A quien madruga Dios le ayuda"
palabra=print("A quien madruga Dios le ayuda")
palabra=input("Dime una palabra: ").lower()
if palabra in frase.lower():
    print(f"La palabra esta en la frase y en el indice {frase.lower().index(palabra)}")
else:
    print("Esa palabra no es parte de la frase")