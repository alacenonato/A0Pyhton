def mostrar_menu():
    print("\n===== TO-DO LIST =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")

def adicionar_tarefa(tarefas):
    try:
        titulo = input("Digite a tarefa: ").strip()

        if not titulo:
            raise ValueError("Tarefa não pode ser vazia!")
        
        tarefa = {
            "titulo": titulo,
            "concluida": False
        }

        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso")

    except Exception as e:
        print(f"Erro: {e}")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n=== Suas Tarefas ==="
    )

    print("\n===== SUAS TAREFAS =====")
    for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i} - {tarefa['titulo']} [{status}]")

def concluir_tarefa(tarefas):
    try:
        listar_tarefas(tarefas)

        indice = int(input("Digite o número da tarefa: "))

        tarefas[indice]["concluida"] = True
        print("Tarefa concluida")

    except (ValueError, IndexError):
        print("Entrada inválida!")
        
def remover_tarefa(tarefas):
    try:
        listar_tarefas(tarefas)

        indice = int(input("Digite o número da tarefa: "))

        tarefas.pop(indice)
        print("Tarefa removida!")

    except (ValueError, IndexError):
        print("Entrada inválida")

def main():
    tarefas = []

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
