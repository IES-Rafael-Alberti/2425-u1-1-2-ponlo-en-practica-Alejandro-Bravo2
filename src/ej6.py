import pdb
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

#Entrada
def pregunta():
    try:
        num1 = int(input("Dime un número entero: "))
    except:
        print("Por favor introduzca valores númericos")
        return pregunta()
    return num1




#Procesamiento

def comprobacion(num1):
    triangulo = ("*")
    if (num1) > 0:
        for i in range(0, num1 + 1):
            print (triangulo * i) # Multiplica la cadena triangulo para imprimirla por i veces
    else:
        print("Por favor introduzca valores mayores a 0")




#Salida

def main():
    num1 = pregunta()
    comprobacion(num1)

if __name__ == "__main__":
    main()