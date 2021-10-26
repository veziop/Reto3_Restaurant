# Reto 3: Python Basics
# Cena de restaurante
# from collections import OrderedDict as od

MONEDA_UNO = 0.01
MONEDA_D0S = 0.02
MONEDA_CINCO = 0.05
MONEDA_DIEZ = 0.1
MONEDA_VEINTE = 0.2
MONEDA_CINCUENTA = 0.5
MONEDA_UN_E = 1
MONEDA_DOSE_ = 2
BILLETE_CINCO = 5
BILLETE_DIEZ = 10
BILLETE_VEINTE = 20
BILLETE_CINCUENTA = 50
BILLETE_CIEN = 100
BILLETE_QUINIENTOS = 500

#creacion de un diccionario especial capaz de recordar el orden del contenido
# billetes = od({
#     "MONEDA_UNO" : 0.01,
#     "MONEDA_D0S" : 0.02,
#     "MONEDA_CINCO" : 0.05,
#     "MONEDA_DIEZ" : 0.1,
#     "MONEDA_VEINTE" : 0.2,
#     "MONEDA_CINCUENTA" : 0.5,
#     "MONEDA_UN_E" : 1,
#     "MONEDA_DOS_E" : 2,
#     "BILLETE_CINCO" : 5,
#     "BILLETE_DIEZ" : 10,
#     "BILLETE_VEINTE" : 20,
#     "BILLETE_CINCUENTA" : 50,
#     "BILLETE_CIEN" : 100,
#     "BILLETE_QUINIENTOS" : 500
# })

billetes = (
    ("MONEDA_UNO", 0.01),
    ("MONEDA_D0S", 0.02),
    ("MONEDA_CINCO", 0.05),
    ("MONEDA_DIEZ", 0.1),
    ("MONEDA_VEINTE", 0.2),
    ("MONEDA_CINCUENTA", 0.5),
    ("MONEDA_UN_E", 1),
    ("MONEDA_DOS_E", 2),
    ("BILLETE_CINCO", 5),
    ("BILLETE_DIEZ", 10),
    ("BILLETE_VEINTE", 20),
    ("BILLETE_CINCUENTA", 50),
    ("BILLETE_CIEN", 100),
    ("BILLETE_QUINIENTOS", 500)
)

carta = {'tortilla':5,
         'montadito':2.2,
         'milanesa': 9,
         "chuleta":8,
         "combinado":11,
         "agua":0.8,
         "copa_de_vino":1.5,
         "botella_de_vino":6,
         "cana":1}

orden = []

def carta_printer(dict):
    temp = []
    for item, precio in dict.items():
        t = item + '.'*(26-len(item)) + '€' + str(precio)
        temp.append(t)
    return "\n".join(temp)

def calcula_billetes(importe):
    # lista temporal de los billetes, orden revertido para empezar de los valores altos hacia los bajos
    # EDIT: diccionario ordenado no es necesario, una tupla es mas eficiente
    # b = list(billetes.items())
    # b.reverse()

    # diccionario pago para almacenar la seleccion y cuantia de billetes
    pago = {}

    for item in billetes[::-1]:
        if importe == 0:
            break
        importe = round(importe, 2)

        for i in range(4,0,-1):
            if importe - (item[1] * i) >= 0:
                importe = importe - (item[1] * i)
                pago[item[0]] = i

    # para el error del calculo, a menudo el importe restante es 0.009999995 o similar
    if 0 < importe < 0.1:
        pago['MONEDA_UNO'] = 1

    return pago

def checkeo_orden(orden):
    # funcion para chequear que los elementos del pedido están en el menu
    temp = [item for item in orden if item not in carta]
    return temp

def calculo_importe():
    return sum([carta[item] for item in orden])

def toma_del_pedido():
    global orden
    orden = input("¿Que quiere cenar? Ingrese exactamente como lo pone en la carta, separado con espacios\n").lower().split()

    # orden.extend(input("¿Que quiere cenar? ").split())

if __name__ == '__main__':
    # print(billetes)
    print(f"Buenas noches, esta es la carta\n{carta_printer(carta)}")

    # while not checkeo_orden(orden):
    #     toma_del_pedido()
    #     total = calculo_importe()
    try:
        toma_del_pedido()
    except:
        print("Error: asegurese que ingresa bien el texto")

    total = calculo_importe()

    print(f"su importe es €{total}\n")
    print(f"para pagar exacto:") #{calcula_billetes(total)}")
    for par in calcula_billetes(total).items():
        print(f"{par[1]} de {par[0]}")
    print("Gracias por su visita.")

