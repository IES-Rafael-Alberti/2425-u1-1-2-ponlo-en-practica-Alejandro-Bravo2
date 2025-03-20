
#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
# imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el 
# número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

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

def sumita(num2:int):
    lista_Sumar = [int(n) for n in str(num2)]
    resultado = sum(lista_Sumar)
    return resultado




# Salida

def main():
    valor = 1
    contador = 0
    print ("Hola vamos a realizar un bucle y hasta que no escribas salir este bucle no se va a parar")
    while valor != -1:
        valor = pregunta()
        resultado = valor % 2
        if resultado == 0:
            contador += 1
        if valor > 0:
            resultado = sumita(valor)
            print(f"La suma de todos los digítos de ese número es: {resultado} y la cantidad de números pares son: {contador}")
            

if __name__ == "__main__":
    main()