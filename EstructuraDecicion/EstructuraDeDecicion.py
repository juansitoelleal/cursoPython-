## operacion match
# operacion='suma'
# match operacion:
#     case 'suma':
#         print('realize una suma')
#     case 'resta':
#         print('realize una reata')
#     case 'multiplicacion':
#         print('realize una multiplicacion')
#     case _:
#         print('no hay operacion')
## una variable con mensajae hola mundo
## pedimpos al ususario que ingrase un texto 
## si texto es hola 
## mostraras el mensaje complto
## si el texto ingresado es como estas 
## extraeras del mensaje la palabra  mundo
## si se ingresa otro texto
## mosgtrara por defecto el mensaje de error


mensaje='hola mundo'
texto=input('ingrese un texto: ')       
if texto=='hola':
    print(mensaje[:])
elif texto=='como estas':
    print(mensaje[4:])
elif texto=='saludo':
    print(mensaje[:5])
else:
    print('error')
