menu = '''
[ D ] Depositar
[ S ] Sacar
[ E ] Extrato
[ Q ] Sair
=>'''

saldo = 0
limite = 500
extrato = ''
numeros_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'D':
        valor = float(input('INFORME O VALOR DO DEPOSITO:'))

        if valor > 0 :
            saldo += valor
            extrato += f'Depósito:R${valor:.2f}\n'

        else:
            print('Operação falhou! o valor informado é invalido.')
    elif opcao == 'S':
        valor = float(input('Informe o valor do saque: '))
        execedeu_saldo =  valor > saldo

        execedeu_limite = valor > limite

        execedeu_saques = numeros_saques >= LIMITES_SAQUES

        if execedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif execedeu_limite:
            print('Operação falhou! O valor de saque exede o limite.')

        elif execedeu_saques:
            print('Operação falhou! Número de saques exedido')

        elif valor > 0 :
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numeros_saques += 1

        else:
            print('Operação falhou! O valor informado é invalido.')

    elif opcao == 'E':
        print('################ EXTRATO ###################')
        print('Não foram reaizados movimnetações.' if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print('=============================================')

    elif opcao == 'Q' :
        break

    else:
        print('Opreção inválida, por favor selecione novamnete a operação desejada.')











