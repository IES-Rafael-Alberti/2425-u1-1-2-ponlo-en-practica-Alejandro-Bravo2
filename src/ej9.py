#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

#Entrada
def pregunta():
    contraseña = input("Dime tu contraseña: ")
    contraseña2 = input("Dime tu contraseña de tu usuario: ")
    return contraseña, contraseña2




#Procesamiento

def comprobacion(n,m):
    if n == m:
        print("Has introducido la contraseña correctamente")
    else:
        print("Has introducido mal su contraseña")


#Salida

def main():
    c1,c2 = pregunta()
    comprobacion(c1,c2)
    
    
main()