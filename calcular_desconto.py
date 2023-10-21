from time import sleep
import os

# Função para obter os valores digitados para apenas um produto
def valor_um_produto():
    while True:
        valor = input('Informe o preço do produto: R$')
        try:
            valor = float(valor)
            if valor <= 0:
                print('>> Valor não permitido. Tente novamente.\n')
                continue
            break
        except:
            print(f'>> O valor "{valor}" não é permitido. Tente novamente.\n')
            continue
    return valor


# Função para estipular a quantidade de produtos que serão digitados
def quantidade_produtos():
    while True:
        quantidade = input('Informe a quantidade de produtos: ')
        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                print('Valor não permitido. Tente novamente.\n')
                continue
            break
        except:
            print('Valor não permitido. Tente novamente.\n')
            continue
    return quantidade


# Função para obter o número que designará a porcentagem
def porcentagem():
    while True:
        porcentagem = input('\nInforme a porcentagem de desconto (%): ')
        try:
            porcentagem = int(porcentagem)
            if porcentagem <= 0 or porcentagem > 100:
                print('>> Valor não permitido. Tente novamente.')
                continue
            break
        except:
            print(
                f'>> O valor "{porcentagem}" não é permitido. Tente novamente.')
            continue
    return porcentagem


# Função para calcular o desconto de apenas um produto
def calculo_desconto(valor, porcentagem):
    desconto = (valor * porcentagem) / 100
    valor_final = valor - desconto
    return valor_final


# Função para obter os valores digitados para os produtos, com base na quantidade informada
def valor_varios_produtos(quantidade):
    lista_produtos = []
    for prod in range(quantidade):
        while True:
            valor = input(f'\nInforme o valor do {prod+1}º produto: R$')
            try:
                valor = float(valor)
                if valor <= 0:
                    print('>> Valor não permitido. Tente novamente.')
                    continue
                break
            except:
                print(
                    f'>> O valor "{valor}" não é permitido. Tente novamente.')
                continue
        lista_produtos.append(valor)
    total = sum(lista_produtos)
    return lista_produtos, total


# Função para calcular o desconto da opção para vários produtos
def calculo_desconto_produtos(total, porcentagem):
    desconto = (total * porcentagem) / 100
    valor_final = total - desconto
    return valor_final


# Função para mostrar o resultadom com base nas opções escolhidas
def resultado(opcao):
    if opcao == 1:
        os.system('cls')
        print('\n\t----CÁLCULO DE UM PRODUTO----')
        valor = valor_um_produto()
        porcem = porcentagem()
        valor_final = calculo_desconto(valor, porcem)
        os.system('cls')
        print('\nRESULTADO:')
        print(
            f'Preço: R${valor:.2f}\nDesconto: {porcem}%\nValor final: R${valor_final:.2f}')
    else:
        os.system('cls')
        print('\n\t----CÁLCULO DE VÁRIOS PRODUTOS----')
        quantidade = quantidade_produtos()
        lista, valor = valor_varios_produtos(quantidade)
        porcem = porcentagem()
        valor_final = calculo_desconto_produtos(valor, porcem)

        print('\nQUANTIDADE DE PRODUTOS:')
        for num, produtos in enumerate(lista):
            print(f'{num+1:3} - R${produtos:.2f}')
        os.system('cls')
        print('\nRESULTADO:')
        print(
            f'Soma dos produtos: R${valor:.2f}\nDesconto: {porcem}%\nValor final: R${valor_final:.2f}')


# Função para mostrar o menu de escolha
def menu():
    print('\n\t----MENU----')
    print('\nInforme um dos números correspondentes: ')
    print('\t1 - Calcular o desconto com apenas um produto')
    print('\t2 - Calcular o desconto com vários produtos')
    while True:
        op = input('\nInforme o número de uma das opções acima: ')
        try:
            op = int(op)
            if op <= 0 or op >= 3:
                print('>> Valor não permitido. Tente novamente.')
                continue
            else:
                os.system('cls')
                resultado(op)
            break
        except:
            print('>> Valor não permitido. Tente novamente.')
            continue


# While que mantem o programa. Chama a função Menu e a
# opção de escolha em permanecer no programa
while True:
    os.system('cls')
    menu()
    while True:
        sair = input('\nDeseja finalizar o programa? (S/N): ')
        if sair == 'N' or sair == 'n':
            os.system('cls')
            menu()
        elif sair == 'S' or sair == 's':
            print('Programa Finalizado!')
            print('\nAdeus')
            sleep(2)
            break
        else:
            print(f'>> O valor "{sair}" não é permitido.')
    break
