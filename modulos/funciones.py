def operaciones(n1,n2,operador):
    if operador=='suma':
        total=n1+n2
    if operador=='resta':
        total=n1-n2
    if operador=='por':
        total=n1*n2
    if operador=='entre':
        total=n1/n2
    return total
def saludo():
    mensaje='hola weyy'
    return mensaje