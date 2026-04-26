import random

nomes = []

def adicionar_nomes():
    print("Digite os nomes (vazio para parar):")
    while True:
        nome = input("Nome:")
        if nome == "":
            break
        nomes.append(nome)

def sortear():
    if not nomes:
        print("Nenhum nome cadastrado.")
        return
    
    sorteado = random.choice(nomes)
    print(f"Sorteado: {sorteado}")

def menu():
    while True:
        print("\n=== SORTEADOR ===")
        print("1. Adicionar nomes")
        print("2. Sortear")
        print("3. Listar nomes")
        print("4. Sair")

        op = input("Escolha: ")

        if op == "1":
            adicionar_nomes()
        elif op == "2":
            sortear()
        elif op == "3":
            print(nomes)
        elif op == "4":
            break
        else:
            print("Opção inválida")

menu()