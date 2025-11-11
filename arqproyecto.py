decimal=int(input("Ingresa un número decimal de 2 digitos porfavor: "))

valores=[128, 64, 32, 16, 8, 4, 2, 1]
binario=""

for valor in valores:
    if decimal >= valor:
        binario += "1"
        decimal -= valor
    else:
        binario += "0"

print("El número", decimal, "en binario de 8 bits es: ", binario)