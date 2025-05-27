import cliente
import datetime

class PessoaFisica(cliente.Cliente):
    def __init__(self, endereco: str, contas: list, cpf: str, nome: str = "", data_nascimento: datetime.date = None):
        """
        Inicializa uma nova pessoa física.
        :param endereco: O endereço da pessoa física.
        :param contas: Lista de contas associadas à pessoa física.
        :param cpf: O CPF da pessoa física.
        :param nome: O nome da pessoa física (opcional).
        :param data_nascimento: A data de nascimento da pessoa física (opcional).
        """
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self) -> str:
        """
        Retorna o CPF da pessoa física.
        :return: O CPF da pessoa física.
        """
        return self._cpf

    @property
    def nome(self) -> str:
        """
        Retorna o nome da pessoa física.
        :return: O nome da pessoa física.
        """
        return self._nome
    @property
    def data_nascimento(self) -> datetime.date:
        """
        Retorna a data de nascimento da pessoa física.
        :return: A data de nascimento da pessoa física.
        """
        return self._data_nascimento