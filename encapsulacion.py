# Encapsulación

"""Una coordenada en dos dimensiones está compuesta por dos valores, el valor en el eje de las x y el valor en el eje de las y, ésto podría ser una clase. Un cuadrado está compuesto por cuatro coordenadas que son los cuatro vertices, ésto podría ser una clase que está compuesta por cuatro clases del objeto coordenada."""

# clase Coordenada

class Coordenada:

    # método constructor
    def __init__(self, x, y):
        # atributos privados
        self.__X = x
        self.__Y = y

    # métodos de lectura y escritura de cada atributo
    def getX(self):
        return self.__X
    
    def getY(self):
        return self.__Y
    
    def setX(self, x):
        self.__X = x

    def setY(self, y):
        self.__Y = y

    # método para mostrar la coordenada
    def mostrarCoordenada(self):
        print("(", self.__X, ",", self.__Y, ")")

# clase Cuadrado

class Cuadrado:

    # método constructor
    def __init__(self,v1, v2, v3, v4):
        # atributos privados
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4

    # métodos privados para mostrar los vértices
    def __mostrarCoordenadaV1(self):
        print("(", self.__V1.getX(), ",", self.__V1.getY(), ")")

    def __mostrarCoordenadaV2(self):
        print("(", self.__V2.getX(), ",", self.__V2.getY(), ")")

    def __mostrarCoordenadaV3(self):
        print("(", self.__V3.getX(), ",", self.__V3.getY(), ")")

    def __mostrarCoordenadaV4(self):
        print("(", self.__V4.getX(), ",", self.__V4.getY(), ")")

    # método para mostrar los vértices
    def mostrarVertices(self):
        print("El cuadrado está compuesto por los siguientes vértices: ")
        self.__mostrarCoordenadaV1()
        self.__mostrarCoordenadaV2()
        self.__mostrarCoordenadaV3()
        self.__mostrarCoordenadaV4()
    

# método principal del módulo
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

    # Qué ocurre si el método getX() lo hacemos privado: __getX()?
    # coordenada = Coordenada(3,4)
    # print("(", coordenada.getX(), ",", coordenada.getY(), ")")


if __name__ == "__main__":
    main()