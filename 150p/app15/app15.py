import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").lower()

computador = random.choice(opcoes)

print(f"Computador escolher: {computador}")

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
    (jogador == "papel" and computador == "pedra") or \
    (jogador == "tesoura" and computador == "papel"):
    print("Você venceu!")
else:
    print("Você perdeu!")
