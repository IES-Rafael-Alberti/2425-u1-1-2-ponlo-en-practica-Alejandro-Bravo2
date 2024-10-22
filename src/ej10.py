#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

import pdb
#Entrada

def pregunta():
    try:
        num1 = int(input("Dame un número entero: "))
        
    except:
        print("Por favor introduzca un valor numerico")
        return pregunta
    return num1


#Procesamiento

def es_primo(n):
    """ Divide n entre rango entre 2 hasta n, en caso de haber alguno que de como resultado de la división 0, devuelve falso.
    """
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True
        
#Salida

def main():
    n = pregunta()
    valor = es_primo(n)
    if valor == True:
        print("Es primo")
    else:
        print("No es primo")
        
if __name__ == "__main__":
    main()