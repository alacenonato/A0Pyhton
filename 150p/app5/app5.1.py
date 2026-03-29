import random
numero_secreto = random.randint(1, 100)

while True:
    tentativa = int(input("Adivinhe o número (1 a 100):"))

    if tentativa == numero_secreto:
        print("Parabéns! Você acertou 🎉")
        break
    elif tentativa < numero_secreto:
        print("Tente um número MAIOR 🔼")
    else:
        print("Tente um número MENOR 🔽")