#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
c_notas=int(input("¿Cuántas notas quieres introducir? "))
for repeat in range(c_notas):
    nota = float(input(f"Introduce la nota {repeat + 1}: "))
    if nota>10 or nota<0:
        print("Esa nota no existe")
    else:
        if nota>= 6:
            print("Aprobado")
        else:
            print("Suspendido")