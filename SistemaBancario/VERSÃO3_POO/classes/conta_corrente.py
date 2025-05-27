import classes.conta

class ContaCorrente(classes.conta.Conta):
    def __init__(self, saldo: float, numero: int, agencia: str, 
                 cliente: classes.cliente.Cliente, historico: classes.historico.Historico,
                 limite: float, limite_saque: float):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saque = limite_saque
