from abc import ABC, abstractmethod
from classes.conta import Conta
class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta: Conta):
        """
        Método abstrato para registrar uma transação em uma conta.
        :param conta: A conta na qual a transação será registrada.
        """
        pass


