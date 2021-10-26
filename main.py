# Reto 3: Python Basics
# Cena de restaurante
from collections import OrderedDict as od

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
billetes = od({
    "MONEDA_UNO" : 0.01,
    "MONEDA_D0S" : 0.02,
    "MONEDA_CINCO" : 0.05,
    "MONEDA_DIEZ" : 0.1,
    "MONEDA_VEINTE" : 0.2,
    "MONEDA_CINCUENTA" : 0.5,
    "MONEDA_UN_E" : 1,
    "MONEDA_DOS_E" : 2,
    "BILLETE_CINCO" : 5,
    "BILLETE_DIEZ" : 10,
    "BILLETE_VEINTE" : 20,
    "BILLETE_CINCUENTA" : 50,
    "BILLETE_CIEN" : 100,
    "BILLETE_QUINIENTOS" : 500
})

carta = {'tortilla':5, 'montadito':2.2, "chuleta":8, "combinado":11, "agua":1,"copa_vino":1.5, "botella_vino":6, "cana":1}
orden = []

def carta_printer(dict):
    temp = []
    for item, precio in dict.items():
        temp.append(f"{item}.................€{precio}")
    return "\n".join(temp)

def calcula_billetes(importe):
    # lista temporal de los billetes, orden revertido para empezar de los valores altos hacia los bajos
    b = list(billetes.items())
    b.reverse()

    # diccionario pago para almacenar la seleccion y cuantia de billetes
    pago = {}

    for item in b:
        if importe == 0:
            break

        for i in range(4,0,-1):
            if importe - (item[1] * i) >= 0:
                importe = importe - (item[1] * i)
                pago[item[0]] = i

    if 0 < importe < 0.1:
        pago['MONEDA_UNO'] = 1
    return pago

if __name__ == '__main__':
    # print(billetes)
    print(f"Buenas noches, esta es la carta\n{carta_printer(carta)}")
    # orden.extend(input("¿Que quiere cenar? ").split())
    # print(orden)

    print(f"su importe es {calcula_billetes(0.09)}")


