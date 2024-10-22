#Crear un programa que permita al usuario ingresar los montos de las compras
# de un cliente (se desconoce la cantidad de datos que cargará, la cual puede
# cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario
# ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se
# debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a
# pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

#Entrada

def pregunta():
    dinerito = "0"
    try:
        dinerito = int((input("Dime cuanto te ha costado este articulo, para parar el programa ingrese 0: ")))
    except:
        print("Por favor escriba un número")
        return pregunta()
    return dinerito



# Procesamiento
resultado = 0
def comprobacion(dinero):
    if dinero > 1000:
        return dinero - (dinero / 10)
    else:
        return dinero

    
def Anti_Robo(dinero):
    if dinero > 0:
        return True
    else:
        return False







#Salida

def main():
    totalito = 0
    dinero = 1
    resultado = comprobacion(dinero)
    valor = Anti_Robo(dinero)
    if valor == True:
        while dinero != 0:
            dinero = pregunta()
            if dinero > 0:
                totalito += dinero
            else:
                print("Monto inválido. Ingrese un valor positivo.")
            resultado = comprobacion(totalito)
            print(f"Esta compra te va a costar: {resultado}")
    else:
        print("Por favor escriba números mayores a 0")         

if __name__ == "__main__":
    main()