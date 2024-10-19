# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
# número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

#Entrada
def pregunta():
    try:
        num1 = int(input("Dime la cantidad a invertir: "))
        num2 = float(input("Dime el interes anual (ej: 2 == 0.02): "))
        num3 = int(input("Dime el número de años que quieres tener tu dinero en el fondo: "))
    except:
        print("Por favor introduzca valores númericos")
        return pregunta()
    return num1, num2, num3




#Procesamiento

def comprobacion(num1,num2,num3):
    if (num1 and num2 and num3 ) > 0:
        guardar = (num1 * (num2 / 100)) * num3
    else:
        print("Por favor introduzca valores mayores a 0")

    return guardar


#Salida

def main():
    num1,num2,num3 = pregunta()
    guardar = comprobacion(num1, num2, num3)
    print(f"La cantidad de dinero ganada en {num3} años ha sido {guardar}")

main()