def ler_quantidade():
    while True:
        try:
            q = int(input("Quantas notas deseja inserir: "))
            if q > 0:
                return q
            else:
                print("Digite um numero maior do que zero.")
        except ValueError:
            print("Entrada inválida.")

def salvar_resultado_aluno(nome, media, status):
    with open(f"aluno-{nome}.txt", "a") as f:
        f.write(f"{nome} - {media:.2f} - {status}\n")
                
def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Digite uma nota entra 0 a 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

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
    while True:
        nome = input("Nome do aluno:")
        #quantidade = int(input("Quantas notas deseja inserir? "))
        quantidade = ler_quantidade()

        notas = []

        for i in range(quantidade):
            nota = ler_nota(f"Digite a nota {i+1}: ")
            notas.append(nota)

        media = calcular_media(notas)
        status = verificar_status(media)

        print("\n--- Resultado ---")
        print(f"Aluno: {nome}")
        print(f"Média: {media:.2f}")
        print(f"Status: {status}")

        salvar = input("Deseja sair em arquivo[s/n]: ").lower()
        if salvar == 's':
            salvar_resultado_aluno(nome, media, status)
        
        sair = input("Deseja continuar?[s/n]: ").lower()
        if sair == 'n':
            break
        
if __name__ == "__main__":
    main()
