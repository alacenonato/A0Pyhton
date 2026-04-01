import json
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()
ARQUIVO = "dados.json"
LOG = "historico.txt"

# ================= UTIL =================

def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"turmas": {}}
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)


# ================= VALIDAÇÕES =================

def ler_texto(msg):
    while True:
        texto = input(msg).strip()
        if texto:
            return texto
        console.print("[red]Entrada não pode ser vazia[/red]")


def ler_nota(msg):
    while True:
        try:
            n = float(input(msg))
            if 0 <= n <= 10:
                return n
            console.print("[red]Nota deve ser entre 0 e 10[/red]")
        except:
            console.print("[red]Entrada inválida[/red]")


def ler_opcao():
    # return Prompt.ask("Escolha uma opção")
    return input("Escolha uma opção: ")

# ================= REGRAS =================

def calcular_media(notas):
    return sum(notas) / len(notas)


def status(media):
    if media >= 7:
        return "[green]Aprovado[/green]"
    elif media >= 5:
        return "[yellow]Recuperação[/yellow]"
    return "[red]Reprovado[/red]"


# ================= TURMAS =================

def criar_turma(dados):
    nome = ler_texto("Nome da turma: ")
    if nome in dados["turmas"]:
        console.print("[red]Turma já existe[/red]")
        return
    
    dados["turmas"][nome] = []
    salvar_dados(dados)
    log(f"Turma criada: {nome}")


# ================= ALUNOS =================

def adicionar_aluno(dados):
    turma = ler_texto("Turma: ")

    if turma not in dados["turmas"]:
        console.print("[red]Turma não encontrada[/red]")
        return

    nome = ler_texto("Nome do aluno: ")
    qtd = int(input("Quantidade de notas: "))

    notas = []
    for i in range(qtd):
        notas.append(ler_nota(f"Nota {i+1}: "))

    media = calcular_media(notas)

    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media,
        "status": status(media)
    }

    dados["turmas"][turma].append(aluno)
    salvar_dados(dados)
    log(f"Aluno adicionado: {nome}")


def listar_alunos(dados):
    turma = ler_texto("Turma: ")

    if turma not in dados["turmas"]:
        console.print("[red]Turma não encontrada[/red]")
        return

    tabela = Table(title=f"Turma: {turma}")
    tabela.add_column("Nome")
    tabela.add_column("Média")
    tabela.add_column("Status")

    for aluno in dados["turmas"][turma]:
        tabela.add_row(
            aluno["nome"],
            f"{aluno['media']:.2f}",
            aluno["status"]
        )

    console.print(tabela)


def editar_aluno(dados):
    turma = ler_texto("Turma: ")
    nome = ler_texto("Nome do aluno: ")

    for aluno in dados["turmas"].get(turma, []):
        if aluno["nome"] == nome:
            console.print(f"Notas atuais: {aluno['notas']}")

            novas_notas = []
            for i in range(len(aluno["notas"])):
                novas_notas.append(ler_nota(f"Nova nota {i+1}: "))

            aluno["notas"] = novas_notas
            aluno["media"] = calcular_media(novas_notas)
            aluno["status"] = status(aluno["media"])

            salvar_dados(dados)
            log(f"Aluno editado: {nome}")
            return

    console.print("[red]Aluno não encontrado[/red]")


def remover_aluno(dados):
    turma = ler_texto("Turma: ")
    nome = ler_texto("Nome do aluno: ")

    alunos = dados["turmas"].get(turma, [])

    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            salvar_dados(dados)
            log(f"Aluno removido: {nome}")
            return

    console.print("[red]Aluno não encontrado[/red]")


# ================= MENU =================

def menu():
    console.print("""
[bold cyan]
1 - Criar turma
2 - Adicionar aluno
3 - Listar alunos
4 - Editar aluno
5 - Remover aluno
6 - Sair
""")
    return ler_opcao()


# ================= MAIN =================

def main():
    dados = carregar_dados()

    while True:
        op = menu()

        if op == "1":
            criar_turma(dados)
        elif op == "2":
            adicionar_aluno(dados)
        elif op == "3":
            listar_alunos(dados)
        elif op == "4":
            editar_aluno(dados)
        elif op == "5":
            remover_aluno(dados)
        elif op == "6":
            console.print("[bold red]Saindo...[/bold red]")
            break
        else:
            console.print("[red]Opção inválida[/red]")


if __name__ == "__main__":
    main()