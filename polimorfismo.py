
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre


    def avanza(self):
        print("Estoy caminando")


class Ciclista(Persona):            #La clase Ciclista extiende a la superclase Persona

    def __init__(self, nombre):     #Incializamos la subclase Ciclista
        super().__init__(nombre)    #Inicializamos la superclase Persona

    def avanza(self):
        print("Me desplazo en mi bicicleta")


def main():
    persona = Persona("Raul")
    persona.avanza()

    ciclista = Ciclista("Daniel")
    ciclista.avanza()

if __name__ == "__main__":
    main()