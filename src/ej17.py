#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

#Entrada
def pregunta():
    try:
        num1 = int(input("Dime un número entero: "))
    except:
        print("Por favor introduzca valores númericos")
        return pregunta()
    return num1




#Procesamiento
def comprobacion(num1):
    lista_Sumar = [int(n) for n in str(num1)]
    """Convierte el numero en cadena de texto para luego con el primer int(d) cambiarla a entero,
    esto sirve para dividir un número en muchas partes
    """
    resultado = sum(lista_Sumar) #Sumamos los numeros dentro de la lista
    return resultado



#Salida

def main():
    num1 = pregunta()
    digitos = comprobacion(num1)
    print(digitos)

if __name__ == "__main__":
    main()

#Las listas son lo mejor :)
