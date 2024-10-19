# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
# número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

#Entrada
def pregunta():
    try:
        num1 = int(input("Dime la cantidad a invertir: "))
        num2 = float(input("Dime el interes anual: "))
        num3 = int(input("Dime el número de años que quieres tener tu dinero en el fondo: "))
    except:
        print("Por favor introduzca valores númericos")
        return pregunta()
    return num1, num2, num3




#Procesamiento





#Salida

