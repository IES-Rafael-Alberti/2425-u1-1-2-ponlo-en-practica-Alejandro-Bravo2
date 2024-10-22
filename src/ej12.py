#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
# Entrada

def pregunta():
    frase = input("Dime una frase: ")
    letra = input("Dime una letra: ")
    return frase, letra



# Procesamiento

def mostrar_Pantalla(frase,letra):
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    return contador



# Salida


def main():
    frase,letra = pregunta()
    contador = mostrar_Pantalla(frase, letra)
    print (f"El número de veces que se ha repetido esa letra en tu frase es {contador}")
    
if __name__ == "__main__":
    main()