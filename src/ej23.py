#Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando 
# el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de 
# longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada 
# línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total 
# (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
import pdb

def pregunta():
    frase = input("Dame el título de tu libro: ")
    return frase

def contar_Numeros(frase, cantidad:0):
    frase_Partida = frase.split()
    pdb.set_trace()
    partes = [str(n) for n in str(frase_Partida)]
    partes.pop(0)
    partes.reverse()
    partes.pop(0)
    partes.remove("'")
    partes.reverse()
    partes.remove("'")
    for char in partes:
        if char.isdigit():
            cantidad += 1
    return cantidad
def main():
    Cantidad_Frases = int(0)
    contador = 0
    frase = "a"
    while frase != "*":
        frase = pregunta()
        if frase != "/":
            contador = contar_Numeros(frase, contador)
        elif frase == "/":
            Cantidad_Frases += 1
            print(f"Línea completa. Aparecen {contador} dígitos numéricos.")
            contador = 0
    print(f"Fin. Se leyeron {Cantidad_Frases} líneas completas.")


if __name__ == "__main__":
    main()
