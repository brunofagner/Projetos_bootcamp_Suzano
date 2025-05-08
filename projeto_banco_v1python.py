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
while True:
    # print(menu)
    opcao = input(menu)
    if opcao == 'd':
        while True:
            valor = float(input('Informe o valor maior que 0 para depositar:'))
            if valor <= 0: print("Valor invalido")
            else: 
                saldo += valor
                print('Deposito realizado com sucesso!')
                extrato += f"""
================================
Deposito no valor de: R$ {valor:.2f}
Saldo atual: R$ {saldo:.2f}
================================
                            """
                break
    elif opcao == 's':
        if limite_saques > 0:
            valor = float(input('Informe o valor maior que 0 e menor que R$500,00:'))
            if valor <= 0 or valor >= 500: print("Valor invalido!")
            elif valor > saldo: print("Saldo insuficiente!")
            else:
                saldo -= valor
                limite_saques -= 1
                print("Saque realizado com sucesso!")
                extrato += f"""
================================
Saque no valor de: R$ {valor}
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
