# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.






# Entrada
def pregunta():
    valor = input(">>> ")
    return valor


# Procesamiento
def comprobacion(valor):
    if valor == "salir":
        pass
    else:
        return False


# Salida

def main():
    print ("Hola vamos a realizar un bucle y hasta que no escribas salir este bucle no se va a parar")
    comprobar = False
    while comprobar == False:
        valor = pregunta()
        comprobar = comprobacion(valor)
        
main()







