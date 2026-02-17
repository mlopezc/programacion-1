from persona import Persona
class Carro:
    def __init__(self, marca, modelo, color, dueno: Persona):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.dueno = dueno
        self.encendido = False

    def encender(self):
        self.encendido = True
        print("El carro está encendido")

    def apagar(self):
        self.encendido = False
        print("El carro está apagado")

    def describir(self):
        print(
            "Carro:", self.marca,
            self.modelo,
            "- Color:", self.color,
            "- Dueño:", self.dueno.nombre
        )
