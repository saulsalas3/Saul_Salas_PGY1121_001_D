import numpy as np
from Funciones import *
from Asistente import *

ar = np.full((10,10),'---')
lista_asistentes = []
ciclo = True
def insertarEntrada(lista_asistentes,num_asiento):
    a = Asistente()
    a.rut = input("Ingrese rut: ")
    a.setNombre = input("Ingrese nombre: ")
    a.apellido = input("Ingrese apellido: ")
    a.num_asiento = num_asiento
    if num_asiento >= 1 and num_asiento <= 20:
        a.valor = 120000
    if num_asiento >= 21 and num_asiento <= 50:
        a.valor = 80000
    if num_asiento >= 51 and num_asiento <= 100:
        a.valor = 50000
    lista_asistentes.append(a)


def comprarEntrada(ar,num_asiento):
    try:
        ub = int(input("Ingrese cantidad de asientos (1-3): "))
        if ub >= 1 and ub <= 3:
            compra = 0
            while compra < ub:
                mostrar(ar)
                num_asiento = int(input("Ingrese numero de asiento: "))
                if num_asiento >= 1 and num_asiento <= 100:
                    desp = comprobar(ar,num_asiento)
                    if desp == True:
                        insertarEntrada(lista_asistentes,num_asiento)
                        comprar(ar,num_asiento)
                        compra = compra + 1
                    else:
                        print("Compra no disponible")
                else:
                    print("No existe el asiento")
        else:
            print("Debe ser entre 1 a 3")
    except:
        print("Ubicacion no valida")

llenar(ar)

def listarAsistente(lista_asistentes):
    for asistente in lista_asistentes:
        print(f"Nombre: {asistente.nombre}\ rut: {asistente.rut}\ valor: {asistente.valor}\ Asiento: {asistente.num_asiento}")


def total(lista_asistentes):
    pl = 0
    go = 0
    si = 0
    total_pl = 0
    total_go = 0
    total_si = 0
    for a in lista_asistentes:
        if a.valor == 120000:
            pl += 1
            total_pl += 120000
        if a.valor == 80000:
            go += 1
            total_go += 80000
        if a.valor == 50000:
            si += 1
            total_si += 50000
    print(f"Platinum: Cant: {pl}\ Total: {total_pl}")
    print(f"Gold: Cant: {go}\ Total: {total_go}")
    print(f"Silver: Cant: {si}\ Total: {total_si}")


def salir():
    print("Vuelva pronto")
    print("Saúl Salas")
    print("06/07/2023")
    return False



while ciclo:
    print("Concierto: Michael Jam")
    print("1) Comprar entradas")
    print("2) Mostrar ubicaciones")
    print("3) Ver listado de asistentes")
    print("4) Mostrar ganancias totales")
    print("5) Salir")
    try:
        op = int(input("Seleccione (1-5): "))
        match op:
            case 1:
                comprarEntrada(ar,lista_asistentes)
            case 2:
                mostrar(ar)
            case 3:
                listarAsistente(lista_asistentes)
            case 4:
                total(lista_asistentes)
            case 5:
                ciclo = salir()
            case _:
                print("Opcion no valida")
    except BaseException as error:
        print(f"Opcion no valida {error}")
