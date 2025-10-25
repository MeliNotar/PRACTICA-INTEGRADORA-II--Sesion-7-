import math

while True:
    numero = input("Ingrese un número entero: ")
    if numero.isdigit():
        numero_int = int(numero)
    else:
        print("No se ingresó un número entero. Programa finalizado.")
        break

    if numero_int == 0:
        print("Programa finalizado.")
        break

    texto = input("Ingrese una palabra o frase: ")

    cantidad_caracteres = len(texto)
    print(f"La frase tiene {cantidad_caracteres} caracteres.")

    factorial = math.factorial(cantidad_caracteres)
    print(f"El factorial de {cantidad_caracteres} es {factorial}.")

    if factorial % 2 == 0:
        print("El resultado del factorial es PAR.")
    else:
        print("El resultado del factorial es IMPAR.")
    
    print("-" * 40)