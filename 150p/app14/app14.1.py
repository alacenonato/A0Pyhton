import random

def gerar_numero(minimo, maximo, quantidade):
    return random.sample(range(minimo, maximo + 1), quantidade)

def mostrar_estatisticas(numeros):
    print("\n Estatisticas:")
    print(f"Maior: {max(numeros)}")
    print(f"Menor: {min(numeros)}")
    print(f"Média: {sum(numeros)/len(numeros):.2f}")

def main():
    print("=== Gerador Avançado ===")

    while True:
        try:
            minimo = int(input("Mínimo: "))
            maximo = int(input("Máximo: "))
            quantidade = int(input("Quantidade de números: "))

            if minimo > maximo:
                print("Erro: mínimo maior que máximo.")
                continue

            if quantidade > (maximo - minimo + 1):
                print("Erro: quantidade maior que o intervalo disponível.")
                continue

            numeros = gerar_numero(minimo, maximo, quantidade)

            print(f"\nNúmeros gerado: {numeros}")
            mostrar_estatisticas(numeros)
        
        except ValueError:
            print("Digite apenas números válidos.")

        continuar = input("\nGerar novamente? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
