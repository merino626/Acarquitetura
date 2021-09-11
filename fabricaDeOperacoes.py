from operacoes import Divisao, Soma, Multiplicacao, Subtracao


class OperacaoFabrica():
    def criar(self, operador):
        objeto_operacao = None
        if operador == "soma":
            objeto_operacao = Soma()
        elif operador == "divisao":
            objeto_operacao = Divisao()
        elif operador == "subtracao":
            objeto_operacao =  Subtracao()
        elif operador == "multiplicacao":
            objeto_operacao = Multiplicacao()
        return objeto_operacao
