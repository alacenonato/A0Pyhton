import random

def gerar_jogo(quantidade):
    return sorted(random.sample(range(1,61), quantidade))

def main():
    print("=== Gerador de Mega-Sena ===")

    try:
        quantidade = int(input("Quantos números (6 a 15)? "))

        if quantidade < 6 or quantidade > 15:
            print("Erro: escolha entre 6 a 15 números.")
            return

        jogo = gerar_jogo(quantidade)
        print(f"Jogo gerado: {jogo}")

    except ValueError:
        print("Digite um número válido.")

if __name__ == "__main__":
    main()
