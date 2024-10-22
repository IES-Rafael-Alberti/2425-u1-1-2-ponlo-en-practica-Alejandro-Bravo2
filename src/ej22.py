#Crear un programa que solicite el ingreso de números enteros positivos, 
# hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y 
# cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.


#Entrada

def pregunta():
    dinerito = "0"
    try:
        dinerito = float((input("Dime cuanto te ha costado este articulo: ")))
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

pares = 0
impares = 0
def digitos(dinero):
    valor = str(dinero)
    parte_Entera, parte_Decimal = valor.split('.')
    pares = 0
    impares = 0

    for digito in parte_Entera:
        numero_Digito = int(digito)
        if numero_Digito % 2 == 0:
            pares += 1
        else:
            impares += 1

    if parte_Decimal:
        for digito in parte_Decimal:
            numero_Digito = int(digito)
            if numero_Digito % 2 == 0:
                pares += 1
            else:
                impares += 1

    return pares, impares



#Salida

def main():
    totalito = 0
    dinero = 1
    pares = 0
    impares = 0
    resultado = comprobacion(dinero)
    valor = Anti_Robo(dinero)
    print("Para finalizar el programa escriba 0")
    if valor == True:
        while dinero != 0:
            dinero = pregunta()
            if dinero > 0:
                totalito += dinero
                pares, impares = digitos(dinero)
            else:
                print("Monto inválido. Ingrese un valor positivo.")
        resultado = comprobacion(totalito)

        print(f"Esta compra te va a costar: {resultado} y tiene {pares} números pares y {impares} números impares")
    else:
        print("Por favor escriba números mayores a 0")         

if __name__ == "__main__":
    main()













