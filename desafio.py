menu = """
Como eu posso te ajuda hoje? 

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500 
extrato = " "
numero_saques = 0
LIMITE_DE_SAQUE = 3 

while True: 
    opcao = input(menu)

    if opcao == "d":
       valor_str = input("Informe o valor do depósito: ")

       try:
        valor = float(valor_str)
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

       except ValueError:
           print("Informe um valor válido...")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        execedeu_saldo = valor > saldo 
        execedeu_limite = valor > limite 
        execedeu_saques = numero_saques >= LIMITE_DE_SAQUE

        if execedeu_saldo: 
            print("Operação falhou! Você não tem saldo sufuciente")
        elif execedeu_limite: 
            print("Operação falhou! Ops...eu acho que você não tem esse valor")
        elif execedeu_saques: 
            print("Operação falhou! Uhmmm...Seu limite de saques diarios foi atigindo")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor é inválido")

    elif opcao == "e":
        print("\n===========Extrato===========")
        print("Nenhuma movimentação por aqui ;( " if not extrato.strip() else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")
       
    elif opcao == "q":
        print("Operação encerrada com sucesso! ;) ")
        break
    
    else: 
        print("Opção inválida! selecione uma das opções acima")