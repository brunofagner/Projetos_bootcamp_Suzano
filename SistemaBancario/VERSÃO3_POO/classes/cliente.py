import conta
import transacao

class Cliente:
    def __init__(self, endereco: str):
        """
        Inicializa um novo cliente.
        :param endereco: O endereço do cliente.
        :param contas: Lista de contas associadas ao cliente.
        """
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta: conta.Conta, transacao: transacao.Transacao):
        """
        Realiza uma transação em uma conta.
        :param conta: A conta na qual a transação será realizada.
        :param transacao: A transação a ser realizada.
        """
        transacao.registrar(conta)


    def adicionar_conta(self, conta: conta.Conta):
        """
        Adiciona uma nova conta ao cliente.
        :param conta: A conta a ser adicionada.
        """
        if conta not in self._contas:
            self._contas.append(conta)