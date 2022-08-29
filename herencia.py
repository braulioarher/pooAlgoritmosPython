
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura

    
class Cuadrado(Rectangulo):     #La clase cuadrado extiende rectangulo

    def __init__(self, lado):               #Siempe que incializamos una subclase
        super().__init__(lado, lado)        #Debemos inicializar una superclase



if __name__ == "__main__":      #si este archivo se ejecuta directamente en la consola
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())
        
    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())

#Gerarquia en la vida real

#