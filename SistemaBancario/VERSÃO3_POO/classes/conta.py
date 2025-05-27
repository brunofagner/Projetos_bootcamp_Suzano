import cliente
import historico


class Conta:
    def __init__(self, numero: int, cliente: cliente.Cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = historico.Historico()

    @property
    def saldo(self) -> float:
        """
        Retorna o saldo da conta.
        :return: O saldo atual da conta.
        """
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente: cliente.Cliente, numero: int):
        return cls(numero, cliente)

    def sacar(self, valor: float) -> bool:
        '''
        Realiza um saque na conta.
        :param valor: O valor a ser sacado.
        :return: True se o saque for bem-sucedido, False caso contrário.
        '''
        if valor <= 0:
            return False
        if valor > self._saldo:
            return False
        return True
    
    def depositar(self, valor: float) -> bool:
        '''
        Realiza um depósito na conta.
        :param valor: O valor a ser depositado.
        :return: True se o depósito for bem-sucedido, False caso contrário.
        '''
        if valor <= 0:
            return False
        self._saldo += valor
        return True