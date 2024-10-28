# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
# (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

def pregunta():
    frase = input("Dame una frase: ")
    return frase



def separador(frase):
    palabras = frase.split(" ")
    if palabras: # De esta forma evitamos que palabras este vacio, lo que hace es comprobar que palabra tenga contenido o no
        return max(palabras, key=len) #max sirve para buscar el elemento mas grande y key=len lo que hace es contar las letras de cada palabra.
    else:
        return None


def main():
    frase = pregunta()
    larga = separador(frase)
    if larga:
        print(f"La palabra más larga de la frase es {larga}")
    else:
        print("No se ingresó ninguna palabra")

if __name__ == "__main__":
    main()