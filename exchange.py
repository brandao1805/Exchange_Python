print("\n")
print("FEI Crypto Exchange, onde a inovação digital se encontra com o futuro financeiro.\n")

money = 0
bit = 0
eth = 0
rip = 0
                                                                              #EXTENSÕES
from datetime import datetime

import random
                                                                              #DEF ATUALIZAR COTAÇÃO
def atualizar_cotacao():
    global bit, eth, rip
    # Inicializar as cotações com valores reais
    bit = 355.510  #valor inicial do Bitcoin
    eth = 19.269   #valor inicial do Ethereum
    rip = 2      #valor inicial do Ripple
    #variação máxima e mínima de 5%
    max_variation = 0.05
    min_variation = -0.05
    #gerar uma variação aleatória para cada criptomoeda
    bit_variation = random.uniform(min_variation, max_variation)
    eth_variation = random.uniform(min_variation, max_variation)
    rip_variation = random.uniform(min_variation, max_variation)
    #atualizar as cotações com base na variação
    bit += bit * bit_variation
    eth += eth * eth_variation
    rip += rip * rip_variation
    #arredondar para 4 casas decimais
    bit = round(bit, 4)
    eth = round(eth, 4)
    rip = round(rip, 4)

                                                                              #DEF EXTRATO
transactions = []

def adcação(transactions, type, valor, money, cota, taxa, reais, bit, eth, rip):
    datehr = datetime.now().strftime("%d-%m-%Y %H:%M")
    transaction = f"{datehr} {type} {valor:.2f} {money} {cota:.2f} {taxa:.2f} {reais:.2f} {bit:.4f} {eth:.4f} {rip:.4f}"
    transactions.append(transaction)
    with open('ext.txt', 'a') as extrato:
        extrato.write(transaction + '\n')

def consext():
    with open('ext.txt', 'r') as extrato:
        print(extrato.read())

def atualizar_saldo(cpf, new_money):
    with open('exchange.txt', 'r+') as arquivo:
        linhas = arquivo.readlines()
        for i in range(0, len(linhas), 4):
            if linhas[i+1].strip() == cpf:
                linhas[i+3] = f"{new_money}\n"
                break
        arquivo.seek(0)
        arquivo.writelines(linhas)

                                                                              #APRESENTAÇÃO
while True:
    option = int(input("Já existe um cadastro? Para descobrir todas as oportunidades que nossa plataforma oferece, faça login., 1 -> SIM // 2 -> NÃO: "))
    print("\n")  # PULAR LINHA
                                                                                  #CADASTRO
    if option == 2:
        print("Nossa plataforma foi feita para atender às suas necessidades, caso você seja um investidor experiente que está procurando diversificar seu portfólio ou um iniciante curioso que está explorando novas oportunidades financeiras. Estamos aqui para ajudá-lo a navegar pelo mundo das criptomoedas de maneira segura e eficiente, com uma interface amigável e ferramentas de compra e venda sofisticadas.\n")
        name = input("Insira seu nome completo: ")
        cpf = input("Insira as numerações do seu CPF: ")
        senha = input("Crie sua senha de 6 dígitos: ")
        with open('exchange.txt', 'a') as arquivo:
            arquivo.write(name + '\n')
            arquivo.write(cpf + '\n')
            arquivo.write(senha + '\n')
            arquivo.write(f"{money}\n")
        print("\n")  # PULAR LINHA
        print("É com grande prazer que anunciamos a sua chegada à nossa comunidade.\nAtenciosamente, A Equipe da FEI Crypto Exchange")
                                                                                  #LOGIN
    elif option == 1:
        print("Bem-vindo de volta à FEI Crypto Exchange!\nÉ maravilhoso tê-lo conosco novamente. Esperamos que sua ausência tenha sido produtiva para você e que você esteja preparado para continuar explorando as incríveis oportunidades do mundo das criptomoedas.\n")
        cpf = input("Insira as numerações do seu CPF: ")
        senha = input("Insira sua senha: ")
        user_correct = False

        infos = []
        with open('exchange.txt', 'r') as arquivo:
            for linha in arquivo:
                infos.append(linha.strip())
        for i in range(1, len(infos), 4):
            if cpf == infos[i] and senha == infos[i + 1]:
                user_correct = True
                money = float(infos[i + 2])
                print("Login realizado com sucesso na FEI Crypto Exchange! Você agora está conectado ao seu perfil.\n")
                break
        
        if not user_correct:
            print("CPF ou senha incorretos...\n")
            continue

                                                            #OPÇÕES
    while True:
        print("Opções Disponíveis:")
        print("1. Consultar saldo")
        print("2. Consultar extrato")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Comprar criptomoedas")
        print("6. Vender criptomoedas")
        print("7. Atualizar cotação")
        print("8. Sair")
        
        user_option = int(input("Escolha uma opção: "))
        print("\n")  # PULAR LINHA
        
                                                                               #CONSULTAR SALDO
        if user_option == 1:
            senha = input("Digite sua senha: ")
            print("\n")  # PULAR LINHA
            found = False
            with open('exchange.txt', 'r') as arquivo:
                infos = [linha.strip() for linha in arquivo]
            for i in range(1, len(infos), 4):
                if cpf == infos[i] and senha == infos[i + 1]:
                    found = True
                    break
            if found:
                print("Saldo detalhado")
                print(f"Reais: R$ {money:.2f}")
                print(f"Bitcoin: BTC {bit:.4f}")
                print(f"Ethereum: ETH {eth:.4f}")
                print(f"Ripple: XRP {rip:.4f}")
                print("\n")  # PULAR LINHA
            else:
                print("Senha incorreta.\n")

                                                                              #CONSULTAR EXTRATO
        elif user_option == 2:
            senha = input("Digite sua senha: ")
            if senha == infos[infos.index(cpf) + 1]:
                print("-" * 100)
                consext()
                print("-" * 100)

                                                                              #DEPOSITAR
        elif user_option == 3:
            deposito = float(input("Digite o valor que deseja depositar: R$ "))
            money += deposito
            atualizar_saldo(cpf, money)
            print("Depósito realizado com sucesso!")
            adcação(transactions, "DEPOSITO", deposito, money, 0, 0, money, bit, eth, rip)
            print("\n")  # PULAR LINHA

                                                                              #SACAR
        elif user_option == 4:
            saque = float(input("Digite o valor que deseja sacar: R$ "))
            if saque > money:
                print("Saldo em conta insuficiente.")
                print("\n")  # PULAR LINHA
            else:
                money -= saque
                atualizar_saldo(cpf, money)
                print("Saque realizado com sucesso!")
                adcação(transactions, "SAQUE", saque, money, 0, 0, money, bit, eth, rip)
                print("\n")  # PULAR LINHA

                                                                              #COMPRA
        elif user_option == 5:
            senha = input("Digite sua senha: ")
            print("\n")      # PULAR LINHA
            if senha == infos[infos.index(cpf) + 1]:
                moedas = int(input("Escolha sua moeda: 1. ₿itcoin / 2. Ethereum / 3. Ripple: "))

                #atualizar a cotação antes da compra
                atualizar_cotacao()

                #exibe a cotação atualizada
                if moedas == 1:
                    print(f"Cotação atual do Bitcoin (BTC): {bit:.4f}")
                    cota = bit
                elif moedas == 2:
                    print(f"Cotação atual do Ethereum (ETH): {eth:.4f}")
                    cota = eth
                elif moedas == 3:
                    print(f"Cotação atual do Ripple (XRP): {rip:.4f}")
                    cota = rip

                quantidade = float(input("Digite a quantidade que deseja comprar: "))

                valor = quantidade * cota

                if valor > money:
                    print("Saldo insuficiente para realizar a compra.")
                    print("\n")  # PULAR LINHA
                else:
                    if moedas == 1:
                        taxa = 0.02  
                    elif moedas == 2:
                        taxa = 0.01  
                    elif moedas == 3:
                        taxa = 0.01  

                    valor_taxa = valor * taxa
                    valor_final = valor - valor_taxa
                    money -= valor
                    atualizar_saldo(cpf, money)

                    if moedas == 1:
                        bit += quantidade
                        adcação(transactions, "COMPRA", valor, money, cota, taxa * 100, money, bit, eth, rip)
                        print(f"Compra de Bitcoin realizada com sucesso! Você comprou {quantidade:.6f} BTC")#BITCOIN
                    elif moedas == 2:
                        eth += quantidade
                        adcação(transactions, "COMPRA", valor, money, cota, taxa * 100, money, bit, eth, rip)
                        print(f"Compra de Ethereum realizada com sucesso! Você comprou {quantidade:.6f} ETH")#ETHEREUM
                    elif moedas == 3:
                        rip += quantidade
                        adcação(transactions, "COMPRA", valor, money, cota, taxa * 100, money, bit, eth, rip)
                        print(f"Compra de Ripple realizada com sucesso! Você comprou {quantidade:.6f} XRP")#RIPPLE
                    print("\n")  # PULAR LINHA
            else:
                print("Senha incorreta.\n")


                                                                              #VENDA
        elif user_option == 6:
            senha = input("Digite sua senha: ")
            print("\n")       # PULAR LINHA
            if senha == infos[infos.index(cpf) + 1]:
                moedas = int(input("Escolha sua moeda para vender: 1. ₿itcoin / 2. Ethereum / 3. Ripple: "))
                if moedas == 1:
                    quantidade = float(input("Digite a quantidade de Bitcoin que deseja vender: "))
                    if quantidade > bit:
                        print("Quantidade de Bitcoin insuficiente para realizar a venda.")
                        print("\n")  # PULAR LINHA
                    else:
                        cota = bit  #utiliza a cotação atual do Bitcoin
                        valor_venda = quantidade * cota
                        taxa = 0.03  #taxa 3% venda bitcoin
                        valor_taxa = valor_venda * taxa
                        valor_final = valor_venda - valor_taxa
                        money += valor_final
                        bit -= quantidade
                        atualizar_saldo(cpf, money)
                        adcação(transactions, "VENDA", valor_final, money, cota, taxa * 100, money, bit, eth, rip)
                        print(f"Venda de Bitcoin realizada com sucesso! Você recebeu R$ {valor_final:.2f}")
                        print("\n")  # PULAR LINHA

                elif moedas == 2:
                    quantidade = float(input("Digite a quantidade de Ethereum que deseja vender: "))#ETHEREUM
                    if quantidade > eth:
                        print("Quantidade de Ethereum insuficiente para realizar a venda.")
                        print("\n")  # PULAR LINHA
                    else:
                        cota = eth  #utiliza a cotação atual do Ethereum
                        valor_venda = quantidade * cota
                        taxa = 0.02  #taxa 2% venda ethereum
                        valor_taxa = valor_venda * taxa
                        valor_final = valor_venda - valor_taxa
                        money += valor_final
                        eth -= quantidade
                        atualizar_saldo(cpf, money)
                        adcação(transactions, "VENDA", valor_final, money, cota, taxa * 100, money, bit, eth, rip)
                        print(f"Venda de Ethereum realizada com sucesso! Você recebeu R$ {valor_final:.2f}")
                        print("\n")  # PULAR LINHA

                elif moedas == 3:
                    quantidade = float(input("Digite a quantidade de Ripple que deseja vender: "))#RIPPLE
                    if quantidade > rip:
                        print("Quantidade de Ripple insuficiente para realizar a venda.")
                        print("\n")  # PULAR LINHA
                    else:
                        cota = rip  #utiliza a cotação atual do Ripple
                        valor_venda = quantidade * cota
                        taxa = 0.01  #taxa 1% venda ripple
                        valor_taxa = valor_venda * taxa
                        valor_final = valor_venda - valor_taxa
                        money += valor_final
                        rip -= quantidade
                        atualizar_saldo(cpf, money)
                        adcação(transactions, "VENDA", valor_final, money, cota, taxa * 100, money, bit, eth, rip)
                        print(f"Venda de Ripple realizada com sucesso! Você recebeu R$ {valor_final:.2f}")
                        print("\n")  # PULAR LINHA
            else:
                print("Senha incorreta.\n")

                                                                              #COTAÇÃO
        elif user_option == 7:
            senha = input("Digite sua senha: ")
            print("\n")
            if senha == infos[infos.index(cpf) + 1]:
                atualizar_cotacao()
                #exibir mensagem com as novas cotações
                print("Cotações atualizadas com sucesso:")
                print(f"Bitcoin (BTC): {bit:.4f}")
                print(f"Ethereum (ETH): {eth:.4f}")
                print(f"Ripple (XRP): {rip:.4f}")
                print("\n")  # PULAR LINHA
            else:
                print("Senha incorreta.")
                print("\n")  # PULAR LINHA

                                                                              #SAIR
        elif user_option == 8:
            print("Logout com sucesso, até a próxima!\nFEI Crypto Exchange")
            break
        else:
            print("Opção inválida")