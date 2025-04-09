saldo = 0
limite_saque = 3
limite_saque_valor = 500


def sacar(valor):
    global saldo
    global limite_saque
    global limite_saque_valor
    if valor <= saldo and limite_saque > 0 and limite_saque_valor >= valor:
        saldo -= valor
        limite_saque -= 1
        limite_saque_valor -= valor
        print("\nValor de R$ {valor} sacado, seu saldo agora é de: R$ {saldo}\n".format(valor=valor, saldo=saldo))
    elif valor >= saldo:
        print("\nValor a ser sacado é maior que o saldo da conta\n")
    elif limite_saque <= 0:
        print('\nSeu limite de saques diários foi atingido\n')
    elif limite_saque_valor <= valor:
        print('\nSeu limite de valor de saque diário foi atingido, mas você ainda pode sacar R$ {limite}\n'.format(limite=limite_saque_valor))
    else:
        print('\nValor não pode ser sacado\n')

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print("\nValor de R$ {valor} depositado, seu saldo agora é de R$ {saldo}\n".format(valor=valor, saldo=saldo))

def extrato():
    print('\nSeu extrato é de R$ {saldo}\n'.format(saldo=saldo))

opcao = -1
valor = 0

while opcao != 0:
    opcao = int(input("[1] Extrato \n[2] Sacar \n[3] Depositar \n[0] Sair \n: "))

    if opcao == 1:
        extrato()
    elif opcao == 2:
        valor = int(input("\nQuanto deseja sacar: "))
        sacar(valor)
    elif opcao == 3:
        valor = int(input("\nQuanto deseja depositar: "))
        depositar(valor)
else:
    print("\nObrigado por utilizar o nosso sistema bancário.\n")