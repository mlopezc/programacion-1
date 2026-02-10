def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b


def calculadora():
    print("=== CALCULADORA BÁSICA ===")

    num1 = float(input("Ingrese el primer número: "))
    operador = input("Ingrese el operador (+, -, *, /): ")
    num2 = float(input("Ingrese el segundo número: "))

    if operador == "+":
        print("Resultado:", sumar(num1, num2))

    elif operador == "-":
        print("Resultado:", restar(num1, num2))

    elif operador == "*":
        print("Resultado:", multiplicar(num1, num2))

    elif operador == "/":
        print("Resultado:", dividir(num1, num2))

    else:
        print("Operador no válido")


# Programa principal
calculadora()
