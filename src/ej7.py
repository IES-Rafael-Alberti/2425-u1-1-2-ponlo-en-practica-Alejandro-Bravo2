#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

#Entrada

def entrada():
    try:
        num = int(input("Dime un número: "))
    except:
        print("Por favor solo dame valores numericos")
        return entrada()
    return num



#Procesamiento

def multiplicador(n:int):
    for i in range(1, 11):
        print (f"{n} x {i} = {n * i}")


#Salida

def main():
    num = entrada()
    multiplicador(num)

if __name__ == "__main__":
    main()