import os


def contarLetra(string, letra):
    contador = 0
    string = string.upper()
    letra = letra.upper()
    for elemento in string:
        if elemento == letra:
            contador = contador + 1
    return contador


def Palindromo():
    numero = raw_input('Ingrese numero:')
    if numero.isdigit():
        d = [h for h in numero]
        if d == d[::-1]:
            print('el numero es palindromo')
            i = 1
        else:
            print('no es palindromo')
            i = 1
    else:
        i = 0
    return i


def Array():        
    minimo = input('min')
    maximo = input('max')
    if minimo < maximo:
        x = range(minimo, maximo+1)
        print(list(x))
        i = 1
    else:
        i=0
    return i
    


def LecturaTxt():
    direccion = raw_input('Indique la direccion exacta del archivo')
    nombre = raw_input('Indique el nombre del archivo')
    letra = raw_input('ingrese letra')
    f = open(os.path.join(direccion, nombre), 'r')
    mensaje = f.read()
    contador = contarLetra(mensaje, letra)
    if contador != 0:
        print 'la letra', letra, 'aparece', contador, 'veces'
        i = 1
    else:
        i = 0
    f.close()
    return i


##metodo = raw_input('Elija su metodo: a)Palindromo b)Array c)Lectura txt: ')
##if metodo == 'a':
##    Palindromo()
##elif metodo == 'b':
##    Array()
##elif metodo == 'c':
##    LecturaTxt()
