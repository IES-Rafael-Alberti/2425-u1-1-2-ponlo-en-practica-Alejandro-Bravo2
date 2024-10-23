#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

def pregunta():
    try:
        numero = int(input("Ingrese un número mayor que 1 (0 para salir): "))
    except:
        print("Por favor solo introduzca números")
        return pregunta()
    return numero



def es_primo(n):
    """Comprueba si el número es primo"""
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True

def main():
    """Cuenta la cantidad de números primos ingresados por el usuario."""
    contador_primos = 0
    numero = pregunta()
    while numero != 0:
        if es_primo(numero) == True:
            contador_primos += 1
        numero = pregunta()
    print(f"La cantidad de números primos es: {contador_primos}")

if __name__ == "__main__":
    main()