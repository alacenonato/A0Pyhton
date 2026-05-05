import random
import json

def salvar():
    with open("nomes.json", "w") as f:
        json.dump(nomes, f)

def carregar():
    global nomes 
    try:
        with open("nomes.json", "r") as f:
            nomes = json.load(f)
    except:
        nomes = []

def adicionar_nomes():
    print("Digite os nomes (vazio para parar):")
    while True:
        nome = input("Nome:")
        if nome == "":
            break
        nomes.append(nome)
    salvar()

def sortear():
    if not nomes:
        print("Nenhum nome cadastrado.")
        return
    
    sorteado = random.choice(nomes)
    print(f"Sorteado: {sorteado}")

def sortear_varios():
    if not nomes:
        print("Lista vazia.")
    
    qtd = int(input("Quantos nomes sortear?"))

    if qtd > len(nomes):
        print("Quantidade maior que lista")
        return
    
    sorteados = random.sample(nomes, qtd)

    print("Sorteados:")
    for s in sorteados:
        print("-", s )



def menu():
    carregar()
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