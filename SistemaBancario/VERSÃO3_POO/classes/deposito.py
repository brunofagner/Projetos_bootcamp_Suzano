import transacao

class Saque(transacao.Transacao):
    def __init__(self, valor: float):
        """
        Inicializa uma nova transação de saque.
        :param valor: O valor a ser sacado.
        """
        self.valor = valor