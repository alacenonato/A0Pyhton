import json
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()
ARQUIVO = "dados.json"
LOG = "historico.txt"

# === UTIL ===
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

# === VALIDAÇÕES ===
def ler_texto(msg):
    while True:
        texto = input(msg).strip()
        if texto:
            return texto
        console.print("[red]Entrada não pode ser vazia[/red]")
    
def ler_nota(msg):
    while True:
        try:
            n= float(input(msg))
            if 0 <= n <= 10:
                return n
            console.print("[red]Nota dever ser entre 0 e 10[/red]")
        except:
            console.print("[red]Entrada inválida[/red]")

def ler_opcao():
    return Prompt.ask("Escolha uma opção: ")

# === REGRAS ===
def calcular_media(notas):
    return sum(notas)/ len(notas)

def status(media):
    if media >= 7:
        return "[green]Aprovado[/green]"
    elif media >=5:
        return "[yellow]Recuperação[/yellow]"
    return "[red]Reprovado[/red]"

# === TURMAS ===
def criar_turma(dados):
    nome = ler_texto("Nome da turma: ")
    if nome in dados["turmas"]:
        console.print("[red]Turma já existe[/red]")
        return
    
    dados["turmas"][nome] = []
    salvar_dados(dados)
    log(f"Turma criada: {nome}")

# === ALUNOS ===
def adicionar_aluno(dados):
    turma = ler_texto("Turma: ")

    if turma not in dados["turmas"]:
        console.print("[red]Turma não encontrada[/red]")
        return
    
    nome = ler_texto("Nome do aluno: ")
    qtd = int(input("Quantidade de notas: "))

    notas = []
    for i in range(qtd):
        notas.append(ler_nota(f"Nota {i+1}"))

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

