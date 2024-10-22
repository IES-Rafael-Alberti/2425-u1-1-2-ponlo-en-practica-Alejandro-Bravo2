#Solicitar al usuario el ingreso de una frase y de una letra 
# (que puede o no estar en la frase). Recorrer la frase, carácter a
# carácter, comparando con la letra buscada. Si el carácter no coincide,
# indicar que no hay coincidencia en esa posición (imprimiendo la posición) y 
# continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.



# Entrada
def pregunta():
    frase = input("Dime una frase: ")
    vocal = input("Dime una letra: ")
    return frase, vocal



# Procesamiento
def comprobar(frase, vocal):
    contador = 0
    for vocal in frase:
        contador = contador + 1
    return contador

def Anti_Tontos(vocal):
    if len(vocal) != 1:
        return False
    else:
        return True



# Salida


def main():
    frase, vocal = pregunta()
    dudoso = Anti_Tontos(vocal)
    if dudoso == True:
        contador = comprobar(frase, vocal)
        print(f"La letra introducida ha sido repetida {contador} veces en la frase")
    else:
        print("Te he dicho que escribas solo una letra no más")
    
    
main()