# Reto 3: Python Basics
# Cena de restaurante

MONEDA_UNO = 0.01
MONEDA_D0S = 0.02
MONEDA_CINCO = 0.05
MONEDA_DIEZ = 0.1
MONEDA_VEINTE = 0.2
MONEDA_CINCUENTA = 0.5
BILLETE_CINCO = 5
BILLETE_DIEZ = 10
BILLETE_VEINTE = 20
BILLETE_CINCUENTA = 50
BILLETE_CIEN = 100
BILLETE_QUINIENTOS = 500

carta = {'tortilla':5, 'montadito':2.2, "chuleta":8, "combinado":11, "agua":1,"copa_vino":1.5, "botella_vino":6, "cana":1}
orden = []

def carta_printer(dict):
    temp = []
    for item, precio in dict.items():
        temp.append(f"{item}.............€{precio}")
    return "\n".join(temp)

def calcula_billetes(importe):
    pass


if __name__ == '__main__':
    print(f"Buenas noches, esta es la carta\n{carta_printer(carta)}")
    orden.extend(input("¿Que quiere cenar? ").split())
    print(orden)

