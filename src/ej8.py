#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.




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
    triangulo = ["1"]
    contador = int(1)
    if (num1) > 0:
        while contador != num1:
            valor = (contador + 2) 
            triangulo.append(valor)
            print(*triangulo[::-1],sep=" ")
            contador = contador + 2
    else:
        print("Por favor introduzca valores mayores a 0")




#Salida

def main():
    num1 = pregunta()
    comprobacion(num1)

main()
