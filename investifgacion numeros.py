##################mayor de tres numeros.

#print("coloque sus tres numeros:")

#a=int(input())
#b=int(input())
#c=int(input())

#numeromayor= max(a,b,c)

#print(numeromayor)


############################suma de digitos


#print("coloque el numero a sumar")


#numero = input()

#suma = 0
#for digito in numero:
    #suma += int(digito)

#print("La suma es:", suma)

#############################contador de palabras

#print("coloque una frase")

#frase= input()
#palabras= frase.split()

#cuantas= len(palabras)

#print("tu frase tiene:", cuantas, "palabras")

##########################Lista inversa

#lista= [10,5,7,8,9,3,4,2,1,6]

#ordenar= sorted(lista)

#reorden= ordenar[::-1]

#print(reorden)

#########################numeros aleatorios

#from random import random,uniform,randint,choice

#numeros= [randint(1,1000)for i in range(5)]

#print(numeros)

#########################adivinar numero
#from random import random,uniform,randint,choice

#print("inserta un numero para adivinar:")

#numero_ran= randint(1,10)

#while True:
    #numero=int(input())
    #if numero>numero_ran:
        #print("por favor, coloca un numero menor")
    #elif numero<numero_ran:
        #print("por favor, coloca un numero mayor")
    #else:
        #print("¡ingresaste el numero correcto!")
    
#########################secuencia personalizad

lista = list(range(1, 31))

multiplos = []

for numero in lista:
    if numero % 3 == 0:
        multiplos.append(numero)

print(multiplos)








