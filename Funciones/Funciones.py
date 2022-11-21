##funciones
## 2 tipos de funciones
## funciones propias de python
# print() ## sirve para mostrar mensajes o resultaods 
# int() ##convierte el string a numeros enteros
# input() ## esta funcion sirve para pedir datos al usuario

## funciones creadas
##creando funcion
# from unittest import result


# def suma(a,b):
#     resultado=a+b
#     return resultado
##uso de funcion
# print(suma(4,6))
 
# numero='10' ##'10'
# int(numero)## 10
## int es el nomnre de la funcion () y dentro de parentesis van los 
## parametros
# sentence=input('ingrese una oracion: ')
# sentence2=input('ingrese una oracion: ')
# def countVocals(texto):
#     vocales=['a','e','i','o','u']
#     contadorVocales=0
#     for letras in texto:
#         if letras in vocales:
#             contadorVocales+=1
#     return contadorVocales
# print('la cantidad de vocales es : ',countVocals(sentence))
# print('la cantidad de vocales es : ',countVocals(sentence2))

## crear una funcion de operaciones  aritmeticos matematicos ,

## operadorMatematico(num1,num2, operacion)

## operadorMatematico(4,5, 'sumate esto')
## por consola la suma de 4/4
## por consola es un error

# def mensaje(nombre, apellido,accion):
#     if accion== 'saludo':
#         mensaje='hola' , nombre,apellido, 'como estas'
#     elif accion=='despedida':
#         mensaje='adios', nombre,apellido
#     return mensaje

# respuesta=mensaje('juansito', 'hivallanca', 'saludo')
# print(respuesta)

# sentence=input('enter centemce')
# vocales=['a','e','i','o','u']
# contador=0
# def countVocal(oracion,vocal):
#     contador=0
#     for word in oracion:
#         if word in vocal:
#             contador+=1
#     return contador
# print(countVocal(sentence,vocales))

## operadorMatematico(4,5,'suma')
## por consola la suma de 5+6
## 1.UTILIZAR LA PALABRA RECERVADA def
## 2.asignamos un nombre de la funcion--descriptivo
## 3.siempre tiene que recivir parametros
    #()--no recive parametros
    #(nombre)--que la funcion esta recibiendo un parametro
    #(edad,nombre)
# 4.siempre la funcion tiene que retornar un tipo de dato
# from sqlite3 import DateFromTicks


# def saludo(nombre):
#     respuesta=f'hola como estas {nombre}'
#     return respuesta

#como uso
# arrayAmigos=['ronal','claudio','diego','jose','mozitar','kevin','lilian']
# for amigo in range(0,len(arrayAmigos)):
#     print(saludo(arrayAmigos[amigo]))

## crear una funcion que me retorne los n numeros fibonaci
# 1 1 2 3 5 8
# ## crear una funcioon que me retorne el factorial de un momento n
# 5=5*4*3*2*1
# 7=7*6*5*4*3*2*1
# ##crear una funcion que me diga si una palabra es palidromo
# ada
# ala 
# reconocer
# replace indexof splip reduce
# operacion='resta'
# n1=80
# n2=50
# if operacion=='suma':
#     print(n1+n2)
# if operacion=='resta':
#     print(n1-n2)

def operaciones(n1,n2,operador):
    if operador=='suma':
        total=n1+n2
    if operador=='resta':
        total=n1-n2
    if operador=='multiplicacion':
        total=n1*n2
    if operador=='division':
        total=n1/n2
    return total

#llamando la funcion
respuesta=operaciones(10,8,'suma')
respuesta2=operaciones(100,8,'resta')
print(f'la suma es  {respuesta}')
print(f'la suma es {respuesta2}')
