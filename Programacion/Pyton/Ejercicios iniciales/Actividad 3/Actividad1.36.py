#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.
n=int(input("Introduce un número natural: "))
suma = 0
for resultado in range(1, n + 1):
    suma += resultado
print(f"La suma de los {n} primeros números naturales es: {suma}")