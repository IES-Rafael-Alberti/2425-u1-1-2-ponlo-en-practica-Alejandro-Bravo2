#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

#Entrada

def pregunta():
    try:
        num1 = int(input("Dime un número entero: "))
    except:
        print("Por favor introduzca un número")
        return pregunta()
    return num1






#Procesamiento

def cuenta_Atras(n):
    todo = []
    if n > 1:
        for i in range (n, 0, -1):
            valor = str(i)
            todo.append(valor)
    else:
        print("Por favor introduzca un valor mayor a 1")
    return todo




#Salida

def main():
    num1 = pregunta()
    valor = cuenta_Atras(num1)
    print(*valor, sep=" , ")
    
main()