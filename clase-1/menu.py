# Menú de ejemplo en Python

while True:
    print("\nMENU")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Opción 5")
    print("6. Opción 6")
    print("7. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        print("Has elegido la opción 1")
    elif opcion == 2:
        print("Has elegido la opción 2")
    elif opcion == 3:
        print("Has elegido la opción 3")
    elif opcion == 4:
        print("Has elegido la opción 4")
    elif opcion == 5:
        print("Has elegido la opción 5")
    elif opcion == 6:
        print("Has elegido la opción 6")
    elif opcion == 7:
        print("Saliendo del menú...")
        break
    else:
        print("Opción inválida")
