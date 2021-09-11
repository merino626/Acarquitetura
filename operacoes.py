from abc import ABC, abstractmethod


class Operacao(ABC):
    @abstractmethod
    def executar(self, valor1, valor2):
        pass


class Divisao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 / valor2


class Soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2


class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 - valor2


class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 * valor2
