import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe o número: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Acertou em {tentativas} tentativas! 🎉")
        break
    elif tentativa < numero_secreto:
        print("Maior 🔼")
    else:
        print("Menor 🔽")