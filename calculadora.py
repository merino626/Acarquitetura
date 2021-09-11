from fabricaDeOperacoes import OperacaoFabrica


class Calculadora():
    def calcular(self, valor1, valor2, operacao):
        fabrica_operadores = OperacaoFabrica()
        tipo_operacao = fabrica_operadores.criar(operacao)
        if tipo_operacao:
            resultado = tipo_operacao.executar(valor1, valor2)
        else:
            resultado = f'Operação inválida: "{operacao}"'
        return resultado