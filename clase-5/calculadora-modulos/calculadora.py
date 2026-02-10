import sumar
import restar
import multiplicar
import dividir
def calculadora():
    print("=== CALCULADORA POR MÓDULOS ===")

    num1 = float(input("Ingrese el primer número: "))
    operador = input("Ingrese el operador (+, -, *, /): ")
    num2 = float(input("Ingrese el segundo número: "))

    if operador == "+":
        print("Resultado:", sumar.sumar(num1, num2))

    elif operador == "-":
        print("Resultado:", restar.restar(num1, num2))

    elif operador == "*":
        print("Resultado:", multiplicar.multiplicar(num1, num2))

    elif operador == "/":
        print("Resultado:", dividir.dividir(num1, num2))

    else:
        print("Operador no válido")

calculadora()