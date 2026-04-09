import time

segundos = int(input("Digite o tempo em segundos: "))

while segundos > 0:
    print(f"Tempo restante: {segundos}")
    time.sleep(1)
    segundos -= 1

print("Tempo esgotado!")

