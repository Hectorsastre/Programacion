#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
from math import # en vez de usar "math.sqrt" en cada uno

x1=0
x2=0
a=int(input("Ingrese el coeficiente de la variable a: "))
b=int(input("Ingrese el coeficiente de la variable b: "))
c=int(input("Ingrese el término independiente: "))

if ((a**2)-4*a*c)<0:
  print("La solución requiere una raiz cuadrada negativa")
else:
  x1=(-b+sqrt(b**2-(4*a*c)))/(2*a)  # Fórmula parte positiva
  x2=(-b-sqrt(b**2-(4*a*c)))/(2*a)  # Fórmula negativa
  print("Las soluciones de la ecuación son:")
  if x1>0:
      print(f"La solucion de la ecuación es:¨{x1}")
  else:
      print(f"La solucion de la ecuación es:¨{x2}")