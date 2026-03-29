saldo = 1000
senha_correta = "1234"
extrato = []

senha = input("Digite sua senha:")

if senha != senha_correta:
    print("Senha Incorreta!")
    exit()

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Seu saldo é: R$ {saldo}")

    elif opcao == "2":
        valor = float(input("Digite o valor para o depósito: "))
        saldo += valor
        extrato.append(f"Depósito: +R$ {saldo}")
        print("Depósito realizado!")

    elif opcao == "3":
        valor = float(input("Digite o valor para saque: "))

        if valor > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor
            extrato.append(f"Saque: -R$ {valor}")
            print("Saque realizado!")

    elif opcao == "4":
        print("\n=== Extrato ===")
        for item in extrato:
            print(item)

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
