import random
import string

tamanho = int(input("Digite o tamanho da senha:"))

caracteres = string.ascii_letters

senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

print("Senha gerada:", senha)

