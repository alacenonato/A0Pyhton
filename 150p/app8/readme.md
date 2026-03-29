Bora 🔥 — agora você vai começar a mexer com **estrutura de dados + lógica de sistema real**.

---

# 🧩 PROJETO 8 — Lista de Tarefas (To-Do List CLI)

## 🎯 Objetivo

Criar um sistema de tarefas no terminal com:

✔ Adicionar tarefas
✔ Listar tarefas
✔ Marcar como concluída
✔ Remover tarefa
✔ Menu interativo

👉 Isso aqui já é base de **CRUD (Create, Read, Update, Delete)**

---

# 🧠 CONCEITOS IMPORTANTES

Você vai treinar:

* Listas
* Dicionários
* Funções
* Loop com menu
* Manipulação de estado

---

# 💻 VERSÃO COMPLETA (CLI + Tratamento de erro)

```python
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
        print("Tarefa adicionada com sucesso!")

    except Exception as e:
        print(f"Erro: {e}")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n===== SUAS TAREFAS =====")
    for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i} - {tarefa['titulo']} [{status}]")


def concluir_tarefa(tarefas):
    try:
        listar_tarefas(tarefas)

        indice = int(input("Digite o número da tarefa: "))

        tarefas[indice]["concluida"] = True
        print("Tarefa concluída!")

    except (ValueError, IndexError):
        print("Entrada inválida!")


def remover_tarefa(tarefas):
    try:
        listar_tarefas(tarefas)

        indice = int(input("Digite o número da tarefa: "))

        tarefas.pop(indice)
        print("Tarefa removida!")

    except (ValueError, IndexError):
        print("Entrada inválida!")


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
```

---

# 🔥 DESAFIOS (EVOLUÇÃO)

## 🧩 Desafio 1 — Salvar tarefas em arquivo (JSON)

👉 Persistência de dados (nível intermediário)

---

## 🧩 Desafio 2 — Prioridade de tarefa

Ex:

* Alta 🔴
* Média 🟡
* Baixa 🟢

---

## 🧩 Desafio 3 — Data de vencimento

👉 Trabalhar com datas

---

## 🧩 Desafio 4 — Filtro de tarefas

Ex:

* Mostrar só concluídas
* Mostrar pendentes

---

# 🚀 IDEIA PROFISSIONAL

Isso aqui pode virar:

* 🗂️ Sistema de produtividade
* 📊 App de gestão pessoal
* 📱 API para app mobile

---

# 🧠 MISSÃO

Faça:

✅ Teste todas as opções
✅ Quebre o código (testar erro)
✅ Melhore algo
✅ Suba no GitHub

---

# 🔥 PRÓXIMO PASSO

Posso te entregar:

👉 Versão com JSON (persistência)
👉 Interface gráfica (PySide6)
👉 Versão web (Flask)
👉 Ou versão profissional com banco de dados

---

Se quiser continuar:

👉 fala: **“Quero versão com JSON”**
ou
👉 **“Quero versão GUI”**
ou
👉 **“Quero versão Flask”** 😎

# MAIS E MAIS


