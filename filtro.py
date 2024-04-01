
def filtrar_productos(precios, umbral, operacion='mayor'):
    if operacion == 'mayor':
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio > umbral}
    elif operacion == 'menor':
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio < umbral}
    else:
        return "Lo sentimos, no es una operación válida"
    
    return productos_filtrados

if __name__ == "__main__":
    import sys

    precios = {'Notebook': 700000,
               'Teclado': 25000,
               'Mouse': 12000,
               'Monitor': 250000,
               'Escritorio': 135000,
               'Tarjeta de Video': 1500000}

    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        productos_filtrados = filtrar_productos(precios, umbral)
        print("Los productos mayores al umbral son:", ", ".join(productos_filtrados.keys()))
    elif len(sys.argv) == 3:
        umbral = int(sys.argv[1])
        operacion = sys.argv[2]
        productos_filtrados = filtrar_productos(precios, umbral, operacion)
        if isinstance(productos_filtrados, str):
            print(productos_filtrados)
        else:
            print("Los productos", operacion + "es al umbral son:", ", ".join(productos_filtrados.keys()))
    else:
        print("Uso incorrecto. Debe proporcionar un umbral y opcionalmente 'mayor' o 'menor'.")
