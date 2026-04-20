from services import *
from database import criar_tabela
from rich import print

def menu():
    criar_tabela()

    while True:
        print("\n[bold cyan]=== AGENDA ===[/bold cyan]")
        print("[1] Adicionar")
        print("[2] Listar")
        print("[3] Buscar")
        print("[4] Editar")
        print("[5] Remover")
        print("[6] Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            editar()
        elif opcao == "5":
            remover()
        elif opcao == "6":
            print("[bold red]Saindo... [/bold red]")
            break
        else:
            print("[red]Opção inválid[/red]")

if __name__ == "__main__":
        menu()
