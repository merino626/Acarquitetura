import unittest
from calculadora import Calculadora


class TesteCalculadora(unittest.TestCase):
   
    calculadora = Calculadora()

    def testa_soma(self):
        resultado = self.calculadora.calcular(5, 5, "soma")
        self.assertEqual(resultado, 10) 

    def testa_subtracao(self):
        resultado = self.calculadora.calcular(15, 5, "subtracao")
        self.assertEqual(resultado, 10)

    def testa_divisao(self):
        resultado = self.calculadora.calcular(50, 10, "divisao")
        self.assertEqual(resultado, 5)

    def testa_multiplicacao(self):
        resultado = self.calculadora.calcular(5, 5, "multiplicacao")
        self.assertEqual(resultado, 25)


if __name__ == "__main__":
    unittest.main()