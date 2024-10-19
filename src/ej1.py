#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.




# Entrada
def pregunta():
    guarda = input("Dime una palabra: ")
    return guarda

#Procesamiento
def veces(n):
    for i in range(10):
        print (n)
    



#Salida
def main():
    palabra = pregunta()
    veces(palabra)

main()