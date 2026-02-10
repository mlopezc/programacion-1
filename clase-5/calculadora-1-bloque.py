print("=== CALCULADORA BÁSICA ===")

# Entrada de datos
num1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (+, -, *, /): ")
num2 = float(input("Ingrese el segundo número: "))

# Proceso
if operador == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operador == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operador == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operador == "/":
    if num2 == 0:
        print("Error: No se puede dividir entre cero")
    else:
        resultado = num1 / num2
        print("Resultado:", resultado)

else:
    print("Operador no válido")
