from carro import Carro

class Toyota(Carro):
    def __init__(self, modelo, velocidad_maxima, puertas):
        print("Ejecutando constructor Toyota")
        super().__init__("Toyota", velocidad_maxima, puertas)
        self.__modelo = modelo

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        if not nuevo_modelo:
            raise ValueError("El modelo no puede estar vacío.")
        self.__modelo = nuevo_modelo

    def activar_modo_ecologico(self):
        print("Modo ECO activado para ahorrar combustible.")

    def __str__(self):
        return f"{super().__str__()}, Modelo: {self.modelo}"