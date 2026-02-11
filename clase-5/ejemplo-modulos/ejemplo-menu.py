import animales
import animales2
def menu():
    mensaje = '''
    Por favor ingrese la opción deseada:  
    1) Imprimir Dinosaurio
    2) Imprimir Perro
    3) Imprimir Gato
    4) Imprimir Zorro
    5) Salir
    ''' 
    opcion = int(input(mensaje))
    while opcion != 5:
        match opcion:
            case 1:
                animales2.dinosaurio()
            case 2:
                animales.perro()
            case 3:
                animales.gato()
            case 4:
                animales.zorro()
            case  _:
                print("Opción inválida")
        opcion = int(input(mensaje))
        print("Chau!")


menu()