
def procesar_volumen_cubo():
    lado = int(input("Por favor ingrese el lado del cubo"))
    resultado = calcular_volumen_cubo(lado)
    print(f"El Volumen del Cubo es: {resultado}")

def calcular_volumen_cubo(lado: int):
    return lado * lado * lado


def procesar_volumen_cilindro():
    radio = int(input("Por favor ingrese el radio del cilindro"))
    altura = int(input("Por favor ingrese la altura del cilindro"))
    resultado = calcular_volumen_cilindro(radio, altura)
    print(f"El Volumen del Cilindro es: {resultado}")

def calcular_volumen_cilindro(radio: int, altura: int):
    return radio * radio * altura

def procesar_volumen_paralelepipedo():
    lado = int(input("Por favor ingrese el lado del paralelepipedo"))
    base = int(input("Por favor ingrese la base del paralelepipedo"))
    altura = int(input("Por favor ingrese la altura del paralelepipedo"))
    resultado = calcular_volumen_paralelepipedo(lado, base, altura)
    print(f"El Volumen del paralelepipedo es: {resultado}")

def calcular_volumen_paralelepipedo(lado: int, base: int, altura: int):
    return lado * base * altura

