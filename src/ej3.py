# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

#Entrada

def pregunta():
    num1 = int(input("Dame un número entero: "))
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
    print (*valorfinal, sep=" , ")
    
#Salida
        
def main():
    num1 = pregunta()
    comprobacion(num1)

main()