# Reto 3: Python Basics
# Cena de restaurante
# Presentacion en consola de la carta, totalmente expansible.
# Toma del pedido.
# Calculo del importe total, iva incluido.
# Cómputo de los billetes para pagar exacto, sin vuelto.

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
         "croquetas":4,
         "entrecot":15,
         "plato_combinado":11,
         "agua":0.8,
         "copa_de_vino":1.5,
         "botella_de_vino":6,
         "cana":1}

orden = []

def carta_printer(dict):
    """"Funcion para presentar la carta bonita"""""
    temp = []
    for item, precio in dict.items():
        t = item + '.'*(26-len(item)) + '€' + str(precio)
        temp.append(t)
    return "\n".join(temp)

def calculo_billetes(importe):
    """Computo de los billetes para pagar exacto"""
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

    return pago

def checkeo_orden(orden):
    """Funcion para chequear que los elementos del pedido están en el menu"""
    temp = [item for item in orden if item not in carta]
    return temp

def calculo_importe():
    """Calculo del importe basado en el pedido del usuario y en los precios de la carta.
    Incluye iva y tambien lo facilita"""
    total = sum([carta[item] for item in orden])
    iva = total * 0.21
    return round(total + iva, 2), iva

def toma_del_pedido():
    global orden
    orden = input("""¿Que quiere cenar? Ingrese exactamente como lo pone en la carta, separado con espacios: """).lower().split()

if __name__ == '__main__':
    print(f"Buenas noches, esta es la carta\n{carta_printer(carta)}")

    while True:
        toma_del_pedido()
        if not checkeo_orden(orden):
            total = calculo_importe()
            break
        else:
            print('Por favor, inserte tal y como aparece en la carta')

    print(f"\nSu importe es €{total[0]}, con el IVA 21% incluido de €{total[1]}\n")
    print(f"Para pagar exacto por favor facilite:")

    for par in calculo_billetes(total[0]).items():
        print(f"{par[1]} de {par[0]}")

    print("\nGracias por su visita.")

