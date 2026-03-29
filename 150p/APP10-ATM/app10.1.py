import datetime

# ==== Dados Iniciais ====
saldo = 1000.0
senha_correta = "1234"
extrato = []
limite_saque_diario = 500.0
saque_realizado_hoje = 0.0

ARQUIVO_EXTRATO = "extrato.txt"

# ==== Funções ====
def salvar_extrato():
    with open(ARQUIVO_EXTRATO, "w") as f:
        for item in extrato:
            f.write(item + "\n")

def mostrar_saldo():
    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")

def depositar():
    global saldo

    try: 
        valor = float(input("Digite o valor para depósito: "))

        if valor <= 0:
            print("❌ Valor inválido!")
            return
        
        saldo += valor

        registro = f"{data_hora()} - Depósito: +R$ {valor:.2f}"
        extrato.append(registro)

        salvar_extrato()

        print("✅ Depósito realizado!")
        mostrar_saldo()
    
    except:
        print("❌ Entrada inválida!")

def sacar():
    global saldo, saque_realizado_hoje

    try:
        valor = float(input("Digite o valor para saque: "))

        if valor <= 0:
            print("❌ Valor inválido!")
            return
        
        if valor > saldo:
            print("❌ Valor insuficiente!")
            return
        
        if saque_realizado_hoje + valor > limite_saque_diario:
            print("❌ Limite diário de saque atingido!")
            return
        
        saldo -= valor
        saque_realizado_hoje += valor

        registro = f"{data_hora()} - Saque: -R$ {valor:.2f}"
        extrato.append(registro)
        
        salvar_extrato()

        print("✅ Saque realizado!")
        mostrar_saldo()

    except:
        print("❌ Entrada inválida!")

def ver_extrato():
    print("\n📄 === EXTRATO ===")

    if not extrato:
        print("Nenhuma movimentação.")
    else:
        for item in extrato:
            print(item)

def data_hora():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def login():
    tentativas = 3

    while tentativas > 0:
        print(f"="*30)
        senha = input("Digite sua senha: ")

        if senha == senha_correta:
            print("✅ Acesso liberado!")
            return True
        else:
            tentativas -=1
            print(f"❌ Senha incorreta! Tentativas restantes: {tentativas}")
    
    print("🚫 Conta bloqueada!")
    return False

# ===== SISTEMA PRINCIPAL =====

if not login():
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
        mostrar_saldo()
    
    elif opcao == "2":
        depositar()

    elif opcao == "3":
        sacar()

    elif opcao == "4":
        ver_extrato()

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("❌ Opção inválida!")