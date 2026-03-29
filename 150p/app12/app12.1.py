def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_status(media):
    if media >= 7:
        return "Aprovado ✅"
    elif media >= 5:
        return "Recuperação ⚠️"
    else:
        return "Reprovado ❌"
    
def main():
    print("=== Sistema de Notas ===")

    nome = input("Nome do aluno:")
    
    notas = []

    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    media = calcular_media(notas)
    status = verificar_status(media)

    print("\n--- Resultado ---")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")

if __name__ == "__main__":
    main()
