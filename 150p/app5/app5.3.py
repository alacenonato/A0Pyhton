import random 

def escolher_dificuldade():
    print("\nEscolha a dificuldade:")
    print("1 - Fácil (1 a 50)")
    print("2 - Médio (1 a 100)")
    print("3 - Difícil (1 a 200)")

    opcao = input("Opção: ")

    if opcao == "1":
        return 50
    elif opcao == "2":
        return 100
    elif opcao == "3":
        return 200
    else:
        print("Opção inválida! Usando padrão (1 a 100).")
        return 100
    
def calcular_pontos(tentativas, max_tentativas):
    # Quanto menos tentativas, maior a pontuação
    return max(0, (max_tentativas - tentativas + 1) * 10)


def jogar():
    limite = escolher_dificuldade()
    numero_secreto = random.randint(1, limite)

    max_tentativas = 5  # 🔥 Desafio 1
    tentativas = 0
    historico = []  # 🔥 Desafio 3

    print(f"\nAdivinhe o número entre 1 e {limite}")
    print(f"Você tem {max_tentativas} tentativas!\n")

    while tentativas < max_tentativas:
        try:
            tentativa =int(input("Digite sue palpite: "))
        except:
            print("Digite um número válido!")
            continue

        tentativas += 1
        historico.append(tentativa)

        if tentativa == numero_secreto:
            pontos = calcular_pontos(tentativas, max_tentativas)
            print(f"\n🎉 Acertou em {tentativas} tentativas!")
            print(f"⭐ Pontuação: {pontos}")
            break
        elif tentativa < numero_secreto:
            print("🔼 Tente um número MAIOR")
        else:
            print("🔽 Tente um número MENOR")

        print(f"Tentativas restantes: {max_tentativas - tentativas}")

    else:
        print(f"\n💀 Você perdeu! O número era {numero_secreto}")

    # 🔥 Mostrar histórico
    print("\n📜 Histórico de tentativas:", historico)


def main():
    while True:
        jogar()

        # 🔥 Desafio 5
        continuar = input("\nQuer jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por jogar! 👋")
            break


# Executar jogo
main()