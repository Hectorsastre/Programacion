#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif
frase=input("Dame una frase: ")

if len(frase)<11:
    print("La frase tiene menos de 11 caracteres")
elif len(frase)==11:
    print("La frase tiene 11 caracteres")
elif len(frase)>11:
    print("La frase tiene mas de 11 caracteres")