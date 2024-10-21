#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
import pdb
# Entrada
def pregunta():
    try: # De esta forma mato 2 pajaros de un tiro uso int para que solo ingrese numeros enteros y encima compruebo que el valor introducido sea un numero
        valor = int(input(">>> "))
    except:
        print("Por favor solo introduzca valores númericos")
        return pregunta()
    return valor


# Procesamiento

def suma(num1, num2):
    devuelto = num1 + num2
    return devuelto




# Salida

def main():
    resultado = 0
    valor = 1
    print ("Hola vamos a realizar un bucle y hasta que no escribas salir este bucle no se va a parar")
    while valor != 0:
        valor = pregunta()
        if valor > 0:
            resultado = suma(valor, resultado)
        if valor == 0:
            break
        #pdb.set_trace()


    print(f"La suma total es: {resultado}")
        
main()




