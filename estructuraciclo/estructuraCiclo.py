## for es una estructura de ciclo
##que nos permite interar elementos o variables
##for numero in range(1,11):
 ##   print(numero)

## while tambien es una estructura de ciclo 
## int es un metodo que transforma un dato tipo texto a un 
## dato numerico real o entero 
## imput es un metodo de python que pide un dato
## por consola
# condicion=True
# while condicion==True:
#     numero=int(input('ingresa el numero ganador'))
#     if numero==10:
#         print('ganaste el premio')
#         condicion=False
#     else:
#         print('sientate chato')
## crear un programa que me pida mi edad
##si ingreso una edad incorrecta el programa seguira pidiendo mi edad
##si es la edad correctra me mostrara un mensaje correcto y se 
## terminara la ejecucion
# condicion=True
# while condicion==True:
#     edad=int(input('ingrese su edad: '))
#     if edad==20:
#         print('su edad es correcto')
#         condicion=False
#     else:
#         print('no es su edad intente de nuevo')

## averiguar sobre funciones

## ejemplo class
# password='juansitomc.,24'
# condicion=True
# intentos=1
# while condicion==True:
#     print('este es tu ', intentos, 'intentos')
#     newPassword=input('ingresa el password correcto: ')
#     if newPassword==password:
#         print('vienbenido al sistema :)')
#         condicion=Fals
#     else:
#         print('intenta de nuevo gil')
#         intentos+=1
## escribir  un progrrama que muestre la tabla de multiplicar del 1 al 12
# eval=True
# while eval==True:
#     numeros=int(input('ingrese el numero:  '))
#     if numeros==0:
#         print('saliendo del programa')
#         break
#     else:
#         for numero in range (1,11):
#             print(numero, '*',numeros, '=', numero*numeros)

# if numeros¡=0:
#     for numero in range (1,11):
#         print(numero, '*',numeros, '=', numero*numeros)
# else:
#     print('saliendo del programa')
#     break
# menssaje='hola'
#          #0123
#          #['h','o','l','a']
# for letra in menssaje:
#     print(letra)

##mostrar por consola las vocales
##tiene el mensaje 

# menssaje=input('ingrese un mesaje: ')
# contador=0
# for letra in menssaje:
#     if letra=='a':
#         contador+=1
# print('en este menssaje tienes: ' , contador ,'vocales')

# condicion=True
# numeros=int(input('ingrese el numero:  '))
# for n in range(2,numeros): 
#     if numeros%n==0:
#         print('no es primo ')
#         break
#     elif numeros%3==0:
#         print('no es primo ')
#         break
#     else:
#         print('es prmo')
#         break

# numeros=int(input('ingrese el numero:  '))
# for n in range(2,numeros): 
#     if numeros%n==0 or numeros%3==0:
#         print('no es primo ')
#         break
#     else:
#         print('es prmo')
#         break

# from re import T


# condicion=True
# while condicion==True:
#     numero=int(input('ingrese un numero: '))
#     if numero%2==0 or numero%3==0:
#         print('no es primo')
#     else:
#         print('es primo')
#         condicion=False

## escribir un programa que muestre el eco de todo lo que el usuario
## introdusca hasta que el usuario escriba "salir" que terminara
  
# condicion=True
# while condicion==True:
#     letra=input('ingrese cualquier letra o numero: ')
#     if letra=='salir':
#         print('salio del programa')
#         condicion=False
#     else:
#         print('sigue intentando')

# palabra=''
# while palabra!='salir':
#     palabra=input('escriba algo: ')
#     print(palabra)

# from operator import truediv



# letra=input('ingrese el numero:  ')
# for contador in letra:
#     if letra!='salir':
#         print('salio del programa')
#         break
#     else:
#         print('sigua intentando')
#         break

# from asyncio.windows_events import INFINITE


# contador=INFINITE
# for num in range(0, contador):
#     palabra=input('ingresa algo: ')
#     if palabra=='salir':
#         break

## pedir un texto y contar la cantidad de vocales

# from array import array

# contadorVocales=0
# menssaje=input('ingrese un mesaje: ')
# array=['a','e','i','o','u']
# for letra in menssaje:
#     if letra in array:
#         contadorVocales+=1
# print('en este menssaje tienes: ' , contadorVocales,'vocales')

# sentence=input('ingrese oracion: ')
# handlerVocals=0
# for words in sentence:
#     match words:
#         case 'a':
#             handlerVocals+=1
#         case 'e':
#             handlerVocals+=1
#         case 'i':
#             handlerVocals+=1
#         case 'o':
#             handlerVocals+=1
#         case 'u':
#             handlerVocals+=1    
# print('la cantidad de vocales es: ', handlerVocals)

#Calculadora 
import time


time.sleep(1)

time.sleep(0)

numero1 = int(input("primer número: "))
numero2 = int(input(f"segundo número: "))
print(f"De acuerdo, has escogido el {numero1} y el {numero2}")
time.sleep(1)

simbolo = input(f" (Escribe el numero)\n 1 Sumar\n 2 Restar\n 3 Multiplicar\n 4 Dividir\n 5 salir")

if simbolo == '1' or simbolo == "1":
    print(f"{numero1} + {numero2} =",(numero1+numero2))
elif simbolo == '2' or simbolo == "2":
    print(f"{numero1} - {numero2} =",(numero1-numero2))
elif simbolo == '3' or simbolo == "3":
    print(f"{numero1} * {numero2} =",(numero1*numero2))
elif simbolo == '4' or simbolo == "4":
    print(f"{numero1} / {numero2} =",(numero1/numero2))
elif simbolo == '5' or simbolo == "5":
    print(f"fin")
    
else:
    print(f"No has escrito ninguna letra correcta\nS|s para sumar R|r para restar M|m para multiplicar o D|d para dividir")
    