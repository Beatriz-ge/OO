"""O importe abaixo cria métodos abstratos em python"""
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    """Classe abstrata (não pode ser instanciada diretamente), que representa formas genéricas"""
    def __init__(self, tipo):
        self._tipo = tipo

    @abstractmethod
    def calcular_area(self):
        """Classe que recebe as instâncias da construtora e calcula a área"""

    def get_tipo(self):
        """Retorna uma string que descreve o tipo da forma geométrica"""
        return self._tipo

class Circulo(FormaGeometrica):
    """Subclasse que herda os métodos da classe mãe para o objeto Circulo"""
    def __init__(self, raio):
        super().__init__('Círculo')
        self._raio = raio

    def calcular_area(self):
        """Calcula a área do circulo"""
        return 3.14 * self._raio ** 2

    def get_raio(self):
        """Retorna o valor do raio"""
        return self._raio

class Quadrado(FormaGeometrica):
    """Subclasse que herda os métodos da classe mãe para o objeto Quadrado"""
    def __init__(self, lado):
        super().__init__('Quadrado')
        self._lado = lado

    def calcular_area(self):
        """Calcula área do Quadrado"""
        return self._lado ** 2

    def get_lado(self):
        """Retorna o valor do lado"""
        return self._lado

class Triangulo(FormaGeometrica):
    """Subclasse que herda os métodos da classe mãe para o objeto Triangulo"""
    def __init__(self, base, altura):
        super().__init__('Triângulo')
        self._base = base
        self._altura = altura

    def calcular_area(self):
        """Calcula área do Triangulo"""
        return 0.5 * self._base * self._altura

    def get_base(self):
        """Retorna o valor da base"""
        return self._base

    def get_altura(self):
        """Retorna o valor da altura"""
        return self._altura
