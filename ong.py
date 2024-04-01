
def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def calcular_productoria(lista):
    productoria = 1
    for num in lista:
        productoria *= num
    return productoria

def calcular(**kwargs):
    for key, value in kwargs.items():
        if key.startswith("fact"):
            resultado = calcular_factorial(value)
            print(f"El factorial de {value} es {resultado}")
        elif key.startswith("prod"):
            resultado = calcular_productoria(value)
            print(f"La productoria de {value} es {resultado}")

if __name__ == "__main__":
    calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
