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
password='juansitomc.,24'
condicion=True
intentos=1
while condicion==True:
    print('este es tu ', intentos, 'intentos')
    newPassword=input('ingresa el password correcto: ')
    if newPassword==password:
        print('vienbenido al sistema :)')
        condicion=False
    else:
        print('intenta de nuevo gil')
        intentos+=1
