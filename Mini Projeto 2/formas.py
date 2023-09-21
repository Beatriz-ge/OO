from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self, tipo):
        self._tipo = tipo

    @abstractmethod
    def calcularArea(self):
        pass

    def getTipo(self):
        return self._tipo

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__('Círculo')
        self._raio = raio

    def calcularArea(self):
        return 3.14 * self._raio ** 2

    def getRaio(self):
        return self._raio

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__('Quadrado')
        self._lado = lado

    def calcularArea(self):
        return self._lado ** 2

    def getLado(self):
        return self._lado

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__('Triângulo')
        self._base = base
        self._altura = altura

    def calcularArea(self):
        return 0.5 * self._base * self._altura

    def getBase(self):
        return self._base

    def getAltura(self):
        return self._altura