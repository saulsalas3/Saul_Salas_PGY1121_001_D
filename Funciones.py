import numpy as np

def llenar(ar):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if len(str(x)) < 2:
                ar[f][c] = '0' + str(x)
            else:
                ar[f][c] = str(x)


def mostrar(ar):
    for f in range(10):
        fila = ''
        for c in range(10):
            fila = fila + '  |  ' + ar[f][c]
        print(fila)


def comprar(ar,num_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(num_asiento):
                ar[f][c] = '--'


def comprobar(ar,num_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(num_asiento):
                if ar[f][c] == '--':
                    return False
    return True




