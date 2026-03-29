import random
import string

def avaliar_senha(senha):
    tamanho = len(senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_simbolo = any(c in string.punctuation for c in senha)

    if tamanho >= 12 and tem_numero and tem_simbolo:
        return "Forte 💪"
    elif tamanho >= 8:
        return "Média ⚖️"
    else:
        return "Fraca ❌"


def gerar_senha(tamanho, usar_numeros, usar_simbolos):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    senha = []

    # Garante pelo menos 1 número
    if usar_numeros:
        senha.append(random.choice(numeros))

    # Garante pelo menos 1 símbolo
    if usar_simbolos:
        senha.append(random.choice(simbolos))

    # Conjunto de caracteres
    caracteres = letras
    if usar_numeros:
        caracteres += numeros
    if usar_simbolos:
        caracteres += simbolos

    # Completa o restante da senha
    while len(senha) < tamanho:
        senha.append(random.choice(caracteres))

    # Embaralha para não ficar previsível
    random.shuffle(senha)

    return ''.join(senha)


print("=== GERADOR DE SENHAS PROFISSIONAL ===")

tamanho = int(input("Tamanho da senha: "))
usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
quantidade = int(input("Quantas senhas deseja gerar? "))

salvar = input("Deseja salvar em arquivo? (s/n): ").lower() == 's'

senhas_geradas = []

for i in range(quantidade):
    senha = gerar_senha(tamanho, usar_numeros, usar_simbolos)
    nivel = avaliar_senha(senha)

    print(f"\nSenha {i+1}: {senha}")
    print(f"Nível: {nivel}")

    senhas_geradas.append(f"{senha} - {nivel}")

# Salvar em arquivo
if salvar:
    with open("senhas.txt", "w") as arquivo:
        for linha in senhas_geradas:
            arquivo.write(linha + "\n")

    print("\nSenhas salvas em 'senhas.txt'")