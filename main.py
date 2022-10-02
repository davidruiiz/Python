#Ejercicios de entrada y salida

#1) Utiliza el método input() para realizar las siguientes tarea

#Pide un número por teclado, muestra el resultado y su tipo 
num1=(input("Introduce un número: "))
print(num1, type(num1))

#Pide un número por teclado y asegurate de que capturemos la información en formato int
num2=int(input("Introduce un número entero: ")) #si no recibe un número entero aparecerá un error
print(type(num2))

#Pide un número por teclado y asegurate de que capturemos la información en formato float
num3=float(input("Introduce un número real: ")) #si no recibe un número real aparecerá un error
print(type(num3))


#2) Vamos a formatear números:

#Pide un numero entero por teclado
entero=int(input("Introduce un número entero: "))

#Muéstralo con el formato de 5 dígitos rellenos con 0s por delante
print("{:05d}".format(entero))

#Pide un número flotante por teclado
flotante=float(input("Introduce un número real: "))

#Muéstralo con 5 dígitos para la parte entera y 3 dígitos para la parte decimal
print("{:09.3f}".format(flotante))#se imprimirán 9 caracteres (incluido el punto decimal, de esos 9, 3 serán decimales)


#3) Vamos a ponernos creativos. ¿Cuántas formas tienes de mostrar esta información?
#La altura es de 1,80 metros y el peso es de 80,135 KG
#Siendo la altura y el peso dos variables que se recojan con 2 inputs
altura=float(input("Introduce la altura en metros: "))
peso=float(input("Introduce el peso en kilos: "))
print("La altura es de", altura,"metros y el peso es de", peso,"KG")
print("La altura es de {0} metros y el peso es de {1} KG".format(altura,peso))
    