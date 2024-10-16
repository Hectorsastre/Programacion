# 9. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos=float(input("¿Cuantos segundos quieres calcular? "))
minutos=segundos/60
hora=minutos/60
print("Ha pasado",minutos,"minuto/s o",hora,"hora/s en total")
