#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.

letras=[]
letra=""
continuar="s"
seguir=input("Quieres iniciar? (s/n) ")
while continuar=="s":
    letra=input("Introduce una letra: ")
    if letra not in letras:
        letras.append(letra)
    seguir=input("Quieres continuar? (s/n) ")
    if seguir=="s":
        continuar="s"
    else:
        continuar="n"
print(letras)