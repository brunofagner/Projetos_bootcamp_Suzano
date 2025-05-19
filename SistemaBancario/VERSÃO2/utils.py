numero_conta = 0
def depositar(saldo, /):
    """
    Função para realizar um depósito na conta.
    """
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato = insert_extrato(extrato, valor, 'd', saldo)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"Novo saldo: R$ {saldo:.2f}")
    else:
        print("Valor inválido para depósito.")
    return saldo

def sacar(*, saldo):
    """
    Função para realizar um saque da conta.
    """
    valor = float(input("Digite o valor do saque: "))
    if 0 < valor <= 500 and valor <= saldo:
        saldo -= valor
        extrato = insert_extrato(extrato, valor, 's', saldo)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Novo saldo: R$ {saldo:.2f}")
    else:
        print("Valor inválido para saque ou saldo insuficiente.")
    # return saldo, extrato




extrato = '''
===============Extrato=================
'''
def insert_extrato(extrato, valor=1, tipo='e', saldo=0):
    """
    Função para inserir uma transação no extrato.
    """
    from datetime import datetime
    if tipo == 'd':
        extrato += f"""
        ===============================
        Deposito no valor de: R$ {valor:.2f}
        Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        Saldo atual: R$ {saldo:.2f}
        ===============================
        """
    elif tipo == 's':
        extrato += f"""
        ===============================
        Saque no valor de: R$ {valor:.2f}
        Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        Saldo atual: R$ {saldo:.2f}
        ===============================
        """
    elif tipo == 'e':
        extrato += f"""
        ===============================
        Extrato solicitado
        Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        Saldo atual: R$ {saldo:.2f}
        ===============================
        """
    return extrato

usuarios = []
def criar_usuario():
    """
    Função para criar um novo usuário.
    """
    from datetime import datetime
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    idade = (datetime.now() - data_nascimento).days // 365
    cpf = input("Digite seu CPF: ").replace('.', '').replace('-', '')
    # Verifica se o CPF já está cadastrado
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado.")
        return None
    endereco = input("Digite seu endereço: ")
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'idade': idade,
        'cpf': cpf,
        'endereco': endereco
    }

    if idade < 18:
        print("Você deve ter pelo menos 18 anos para criar uma conta.")
        return None
    else:
        usuarios.append(usuario)
        print(f"Usuário {nome} criado com sucesso!")
        return nome

def criar_conta_corrente():
    """
    Função para criar uma conta corrente.
    """
    cpf_usuario = input("Digite o cpf do usuário: ")
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            conta_corrente = {
                'agencia': '001',
                'numero_conta': numero_conta + 1,
                'saldo': 0,
                'usuario': usuario
            }
            global numero_conta
            numero_conta += 1
            print(f"Conta corrente criada com sucesso! {conta_corrente}")
            return conta_corrente
    print("Usuário não encontrado.")
    return None