#Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando 
# el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de 
# longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada 
# línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total 
# (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
import re


def pregunta():
    frase = input("Dame el título de tu libro: ")
    return frase


def bucle(frase):
    numero = re.findall(r'-?\d+\.?\d*', frase)
    return numero



def main():
    contador = 0
    numero = 0
    todos_Numeros = []
    frase = pregunta()
    while frase != "*":
        frase = pregunta()
        if frase == "/":
            contador += 1
        else:
            numero = bucle(frase)
            todos_Numeros.append(numero)
    print(f"Se han completado {contador} líneas y en esas líneas habían: ")
    print(*todos_Numeros[::], sep=", ")

main()

###FALTAN COSAS