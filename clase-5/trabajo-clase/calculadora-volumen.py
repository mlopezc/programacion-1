import volumen
def menu():
    mensaje = '''
    Por favor ingrese la opción deseada:  
    1) Calcular volumen Cubo
    2) Calcular volumen Paralelepipedo
    3) Calcular volumen Cilindro
    4) Calcular volumen Esfera
    5) Calcular volumen Cono
    6) Salir
    ''' 
    opcion = int(input(mensaje))
    while opcion != 6:
        match opcion:
            case 1:
                volumen.procesar_volumen_cubo()
            case 2:
                volumen.procesar_volumen_paralelepipedo()
            case 3:
                volumen.procesar_volumen_cilindro()
            case 4:
                print("No Implementado aún")
            case  5:
                print("No Implementado aún")
            case  _:
                print("Opción inválida")
        opcion = int(input(mensaje))
    print("Chau!")


menu()