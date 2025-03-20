#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado,
# 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción
# (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver 
# a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las 
# opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

import os
import time
#Entrada

def pregunta():
    print("1- Comenzar programa")
    print("2- Imprimir listado")
    print("3- Finalizar programa")
    valor = input("> ")
    return valor

# Procesamiento

def opciones(opc):
    if opc == 1:
        print("Hola mundo")
        return opciones
    elif opc == 2:
        print("Has elegido la opción 2, Hello World :)")
        return opciones
    elif opc == 3:
        pass
    else:
        return opciones







# Salida

def main():
    opc_Int = 0
    while opc_Int != (3):
        opc = pregunta()
        opc_Int = int(opc)
        opciones(opc_Int)
        time.sleep(2) # Para que espere 2 segundos antes de limpiar la consola
        os.system("clear") # Voy a limpiar la consola porque seguramente se vaya a llenar de muchos menus y queda feo


if __name__ == "__main__":
    main()

