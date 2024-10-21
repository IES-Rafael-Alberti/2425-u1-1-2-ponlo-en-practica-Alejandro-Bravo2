#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

# Entrada
def pregunta():
    try: # De esta forma mato 2 pajaros de un tiro uso int para que solo ingrese numeros enteros y encima compruebo que el valor introducido sea un numero
        valor = int(input(">>> "))
    except:
        print("Por favor solo introduzca valores númericos")
        return pregunta()
    return valor


# Procesamiento

numeros = []
def biblioteca_Numeros(num):
    numeros.append(num)
    return numeros



# Salida

def main():
    valor = 1
    print ("Hola vamos a realizar un bucle y hasta que no escribas salir este bucle no se va a parar")
    while valor != 0:
        valor = pregunta()
        if valor > 0:
            biblioteca = biblioteca_Numeros(valor)
        if valor == 0:
            mayor = max(biblioteca)
            break


    print(f"El número mayor introducido ha sido: {mayor}")
        
main()
