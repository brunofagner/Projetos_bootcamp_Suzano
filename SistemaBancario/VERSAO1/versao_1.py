from datetime import datetime, timedelta, date

menu = """
Qual operação quer realizar?
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair
"""
extrato = '''
===============Extrato=================
'''
saldo = 0
limite_saques = 3
limite_transacoes = 10
while True:
    # print(menu)
    opcao = input(menu)
    if opcao == 'd':
            if limite_transacoes <= 0:
                print('Limite de transações atingido.')
                continue
            valor = float(input('Informe o valor maior que 0 para depositar:'))
            if valor <= 0: print("Valor invalido")
            else:
                saldo += valor
                limite_transacoes -= 1
                print('Deposito realizado com sucesso!')
                extrato += f"""
================================
Deposito no valor de: R$ {valor:.2f}
Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
Saldo atual: R$ {saldo:.2f}
================================
                            """
                break
    elif opcao == 's':
        if limite_transacoes <= 0:
            print('Limite de transações atingido.')
            continue
        elif limite_saques > 0:
            valor = float(input('Informe o valor maior que 0 e menor que R$500,00:'))
            if valor <= 0 or valor >= 500: print("Valor invalido!")
            elif valor > saldo: print("Saldo insuficiente!")
            else:
                saldo -= valor
                limite_saques -= 1
                limite_transacoes -= 1
                print("Saque realizado com sucesso!")
                extrato += f"""
================================
Saque no valor de: R$ {valor}
Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
Saldo atual: R$ {saldo}
================================
                            """            
        else:
            print('Limite diario de saques atingido.')
    elif opcao == 'e':
        print(extrato)
        print('================================')
    elif opcao == 'q': break
    else: print("Comando inválido!")

