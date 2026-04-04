import random

def escolher_computador():
    return random.choice(["pedra", "papel", "tesoura"])

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    
    vitorias = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }

    if vitorias[jogador] == computador:
        return "jogador"
    else:
        return "computador"
    
def jogar():
    while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou sair): ")

        if jogador == "sair":
            print("Encerrando jogo... ")
            break

        if jogador not in ["pedra", "papel", "tesoura"]:
            print("Opção inválida!")
            continue

        computador = escolher_computador()
        resultado = determinar_vencedor(jogador, computador)

        print(f"Computador: {computador}")

        if resultado == "empate":
            print("Empate!")
        elif resultado == "jogador":
            print("Você venceu!")
        else:
            print("Você perdeu!")

jogar()
