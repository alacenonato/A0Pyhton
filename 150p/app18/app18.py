agenda = []

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    contato = {
        "nome": nome,
        "telefone": telefone
    }

    agenda.append(contato)
    print("Contato adicionado!")

def listar_contatos():
    if not agenda:
        print("Agenda vazia.")
        return

    for i, contato in enumerate(agenda):
        print(f"{i+1}. {contato['nome']} - {contato['telefone']}")

def buscar_contato():
    nome = input("Digite o nome para buscar: ")

    for contato in agenda:
        if nome.lower() in contato['nome'].lower():
            print(f"{contato['nome']} - {contato['telefone']}")

def remover_contato():
    listar_contatos()

    indice = int(input("Número do contato para remover: ")) -1

    if 0 <= indice < len(agenda):
        removido = agenda.pop(indice)
        print(f"Removido: {removido['nome']}")
    else:
        print("Indice inválido.")

def menu():
    while True:
        print("\n---AGENDA----")
        print("1. Adicionar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Remover")
        print("5. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            remover_contato()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
