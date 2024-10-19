#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

#Entrada

def pregunta():
    try:
        num = int(input("Dime tu edad: "))
    except:
        print("Por favor introduzca un número")
        return pregunta
    return num


#Procesamiento

def comprobacion(n):
    seguridad = False
    if n < 130 and n > 0:
        seguridad = True
        return seguridad
    else:
        print("Por favor introduzca tu verdadera edad")


def multiple(n, m:int):
    if n == True:
        print("Desde que naciste hasta ahora han transcurrido:")
        for i in range (m):
            print (f"Año: {i}")



#Salida

def main():
    nombre = pregunta()
    seguridad = comprobacion(nombre)
    multiple(seguridad, nombre)

main()