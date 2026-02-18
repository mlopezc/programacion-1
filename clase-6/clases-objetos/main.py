from carro import Carro
from perro import Perro
from persona import Persona

def crear_perros():
   
    firulais = Perro("Firulais", "Cafe", "Zaguate", "Super Perro")
    snoopy = Perro("Snoopy", "Blanco", "Beagle", "Dog Chow")
    firulais.presentarse()
    snoopy.presentarse()
    firulais.vacunar()
    snoopy.vacunar()
    firulais.presentarse()
    snoopy.presentarse()

    nombre = input("Nombre ")
    color = input("Color ")
    raza = input("Raza ")
    alimento = input("Alimento ")


    otro_perro = Perro(nombre, color, raza, alimento)
    otro_perro.presentarse()

    # color_collar_snoopy = input("Deme el color del collar de Snoopy ")
    # tamano_collar_snoopy = input("Deme el tamaño del collar de Snoopy ")
    
    # snoopy.poner_collar(tamano_collar_snoopy, color_collar_snoopy)

    # snoopy.presentarse()

def crear_personas():
    charlie = Persona("Charlie Brown", 10, "USA")
    tommy = Persona("Tommy Pickles", 2, "USA")
    hugo = Persona("Hugo Pickles", 30, "Costa Rica")
    charlie.presentarse()
    tommy.presentarse()
    hugo.presentarse()
    charlie_es_mayor_edad = charlie.es_mayor_de_edad()
    print(charlie_es_mayor_edad)
    tommy_es_mayor_edad = tommy.es_mayor_de_edad()
    print(tommy_es_mayor_edad)
    hugo_es_mayor_edad = hugo.es_mayor_de_edad()
    print(hugo_es_mayor_edad)
    print(hugo.es_costarricense())

def crear_carros():
    
    frank = Persona("Frank Martin", 38, "USA")
    rav4 = Carro("Toyota", "Rav4", "Gris", frank)
    
    toretto = Persona("Dominick Toretto", 35, "USA")
    crv = Carro("Honda", "CRV", "Azul", toretto)


    rav4.encender()
    rav4.apagar()
    crv.encender()
    crv.apagar()
    crv.describir()
    rav4.describir()

def main():
    print("=====================================")
    crear_perros()
    print("=====================================")
    crear_personas()
    print("=====================================")
    crear_carros()
    print("=====================================")
    
main()