import random

def gerar_jogo(quantidade):
    return sorted(random.sample(range(1,61), quantidade))

def gerar_varios_jogos(qtd_jogos, qtd_numeros):
    jogos = []
    for _ in range(qtd_jogos):
        jogos.append(gerar_jogo(qtd_numeros))
    return jogos

def formatar_jogo(jogo):
    return " | ".join(f"{num:02d}" for num in jogo)

def main():
    print("=== 🎰 GERADOR MEGA-SENA ===")

    while True:
        try:
            qtd_jogos = int(input("Quantos jogos deseja gerar? "))
            qtd_numeros = int(input("Quantos números por jogo (6 a 15)? "))

            if qtd_numeros < 6 or qtd_numeros > 15:
                print("Erro: escolha entre 6 a 15 números.")
                continue

            jogos = gerar_varios_jogos(qtd_jogos, qtd_numeros)
      
            print("\n🎯 Jogos Gerados:\n")
            for i, jogo in enumerate(jogos, 1):
                print(f"Jogo {i}: {formatar_jogo(jogo)}")

        except ValueError:
            print("Digite valores válidos.")

        continuar = input("\nGerar novamente? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == '__main__':
    main()
