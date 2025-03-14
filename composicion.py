# Composición

"""Una coordenada en dos dimensiones está compuesta por dos valores, el valor en el eje de las x y el valor en el eje de las y, ésto podría ser una clase. Un cuadrado está compuesto por cuatro coordenadas que son los cuatro vertices, ésto podría ser una clase que está compuesta por cuatro clases del objeto coordenada."""

# clase Coordenada

class Coordenada:

    # método constructor
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # método para mostrar la coordenada
    def mostrarCoordenada(self):
        print("(", self.X, ",", self.Y, ")")

# clase Cuadrado

class Cuadrado:

    # método constructor
    def __init__(self,v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    # método para mostrar los vértices
    def mostrarVertices(self):
        print("El cuadrado está compuesto por los siguientes vértices: ")
        self.V1.mostrarCoordenada()
        self.V2.mostrarCoordenada()
        self.V3.mostrarCoordenada()
        self.V4.mostrarCoordenada()

# método principal
def main():
    # input
    x1 = int(input("Digite el valor de x: "))
    x2 = int(input("Digite el valor de y: "))

    # processing
    c1 = Coordenada(x1,x2)
    c1.mostrarCoordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()


if __name__ == "__main__":
    main()