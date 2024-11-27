#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
cant_notas=int(input("¿Cuántas notas quieres introducir? "))
for repeat in range(cant_notas):
    nota=float(input(f"Introduce la nota {repeat + 1}: "))
    if nota>=5:
        print("Aprobado")
    else:
        print("Suspendido")