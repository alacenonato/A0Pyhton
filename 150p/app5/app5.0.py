import random

numero_secreto = random.randint(1, 100)

tentativa = int(input("Adivinhe o número (1 a 100)"))

if tentativa == numero_secreto:
    print("Acertou! 🎉")
else:
    print(f"Errou! O número era {numero_secreto}")