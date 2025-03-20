# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

#Entrada

def pregunta():
    try:
        num1 = int(input("Dime tu edad: "))
    except:
        print("Por favor ingresa un número")
        return pregunta()
    return num1
#Procesamiento

def comprobacion(n):
    valorfinal = []
    if n > 0:
        for i in range(1, n, 2):
            """Valor inicial: 1,valor final: n , valor incremento: 2
            """
            valor = str(i)
            valorfinal.append(valor)
    else:
        print("Por favor escriba un número mayor a 0")
    return valorfinal    
#Salida
        
def main():
    num1 = pregunta()
    valorfinal = comprobacion(num1)
    print (*valorfinal, sep=" , ")
if __name__ == "__main__":
    main()