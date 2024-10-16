print("1: Pitufos")
print("2: Avatar")
print("3: Piratas del Caribe")
print("4: E.T.")

pelicula=input("Introduce el numero de una pelicula: ")

if pelicula=="1" or pelicula=="4":
    print("El precio es 9€")
if pelicula=="2":
    print("El precio es 11€")
if pelicula=="3":
    print("El precio es 8€")
else:
    print("Error")