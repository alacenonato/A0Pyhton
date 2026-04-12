from funcoes import *

def menu():
    agenda = carregar_dados()

    while True:
        print("\n=== AGENDA ===")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contatos")
        print("4. Editar contato")
        print("5. Remover contato")
        print("6. Sair")

        opcao = input("Escolha:")

        if opcao == "1":
            adicionar_contato(agenda)
        elif opcao == "2":
            listar_contatos(agenda)
        elif opcao == "3":
            buscar_contato(agenda)
        elif opcao == "4":
            editar_contato(agenda)
        elif opcao == "5":
            remover_contato(agenda)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
        menu()
