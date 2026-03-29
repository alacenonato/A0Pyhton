import random 
import string

print("=== Gerador de Senhas ===")

tamanho = int(input("Tamanho da senha: "))

usar_numeros = input("Incluir números? (s/n):").lower() == 's'
usar_simbolos = input("Incluir símbolos? (s/n)").lower() == 's'

caracteres = string.ascii_letters #print(caracteres)

if usar_numeros:
    caracteres += string.digits #print(caracteres)

if usar_simbolos:
    caracteres += string.punctuation #print(caracteres)

senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

print("\nSenha gerada: ", senha)

