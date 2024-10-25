#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=int(input("Introduce un valor entre 1-10: "))
var2=int(input("Introduce otro valor entre 1-10: "))

if var1>10 or var1<0 or var2>10 or var2<0:
    print("Una variable o las dos estan fuera de los limites")
else:

    if var1>var2:
        print(f"El valor {var1} es mas grande que {var2}")
    if var1<var2:
        print(f"El valor {var2} es mas grande que {var1}")
    if var1==var2:
        print("Los dos valores son iguales")
        