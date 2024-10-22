#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

# Entrada

def pregunta():
    palabra = input("Dime una palabra: ")
    return palabra



# Procesamiento

def repetir(nombre):
    for i in nombre[::-1]:
        print (i)


# Salida


def main():
    palabra = pregunta()
    repetir(palabra)


if __name__ == "__main__":
    main()