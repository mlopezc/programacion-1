class Persona:
    def __init__(self, nombre: str, edad: int, pais: str):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def presentarse(self):
        print(
            "Hola, mi nombre es", self.nombre,
            "tengo", self.edad, "años",
            "y soy de", self.pais
        )

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def es_costarricense(self):
        return self.pais == "Costa Rica"