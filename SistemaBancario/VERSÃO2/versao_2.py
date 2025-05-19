from datetime import datetime, timedelta, date
import utils
menu = """
Qual operação quer realizar?
[d] Deposito
[s] Saque
[e] Extrato
[c] Criar Usuario
[u] Criar Conta
[q] Sair
"""

saldo = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
while True:
    # print(menu)
    opcao = input(menu)
    if opcao == 'd':
            if LIMITE_TRANSACOES <= 0:
                print('Limite de transações atingido.')
                continue
            else:
                saldo = utils.depositar(saldo)
                LIMITE_TRANSACOES -= 1
                print("Deposito realizado com sucesso!")
                break
    elif opcao == 's':
        if LIMITE_TRANSACOES <= 0:
            print('Limite de transações atingido.')
            continue
        elif LIMITE_SAQUES > 0:
            saldo, extrato = utils.sacar(saldo)
        else:
            print('Limite diario de saques atingido.')
    elif opcao == 'e':
        print(utils.extrato)
        print('================================')
    elif opcao == 'c':
        print('Criar usuario:')
        utils.criar_usuario()
        print('Usuario criado com sucesso!')
    elif opcao == 'u':
        print('Criar conta:')
        utils.criar_conta_corrente()
        print('Conta criada com sucesso!')
    elif opcao == 'q': break
    else: print("Comando inválido!")

