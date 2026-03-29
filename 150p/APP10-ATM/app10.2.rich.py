from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print
import datetime

console = Console()

# ====== DADOS ======
saldo = 1000.0
senha_correta = "1234"
extrato = []
limite_saque_diario = 500.0
saque_realizado_hoje = 0.0

ARQUIVO_EXTRATO = "extrato.txt"


# ====== FUNÇÕES ======

def data_hora():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def salvar_extrato():
    with open(ARQUIVO_EXTRATO, "w") as f:
        for item in extrato:
            f.write(item + "\n")


def mostrar_saldo():
    console.print(Panel(f"[bold green]Saldo atual: R$ {saldo:.2f}[/bold green]"))


def depositar():
    global saldo

    try:
        valor = float(console.input("[cyan]Digite o valor para depósito:[/cyan] "))

        if valor <= 0:
            console.print("[red]Valor inválido![/red]")
            return

        saldo += valor
        registro = f"{data_hora()} - Depósito: +R$ {valor:.2f}"
        extrato.append(registro)
        salvar_extrato()

        console.print("[green]Depósito realizado com sucesso![/green]")
        mostrar_saldo()

    except:
        console.print("[red]Entrada inválida![/red]")


def sacar():
    global saldo, saque_realizado_hoje

    try:
        valor = float(console.input("[cyan]Digite o valor para saque:[/cyan] "))

        if valor <= 0:
            console.print("[red]Valor inválido![/red]")
            return

        if valor > saldo:
            console.print("[red]Saldo insuficiente![/red]")
            return

        if saque_realizado_hoje + valor > limite_saque_diario:
            console.print("[red]Limite diário atingido![/red]")
            return

        saldo -= valor
        saque_realizado_hoje += valor

        registro = f"{data_hora()} - Saque: -R$ {valor:.2f}"
        extrato.append(registro)
        salvar_extrato()

        console.print("[green]Saque realizado![/green]")
        mostrar_saldo()

    except:
        console.print("[red]Entrada inválida![/red]")


def ver_extrato():
    table = Table(title="📄 Extrato Bancário")

    table.add_column("Data/Hora", style="cyan")
    table.add_column("Movimentação", style="magenta")

    if not extrato:
        console.print("[yellow]Nenhuma movimentação.[/yellow]")
        return

    for item in extrato:
        data, resto = item.split(" - ")
        table.add_row(data, resto)

    console.print(table)


def login():
    tentativas = 3

    while tentativas > 0:
        senha = console.input("[cyan]Digite sua senha:[/cyan] ")

        if senha == senha_correta:
            console.print("[green]Acesso liberado![/green]")
            return True
        else:
            tentativas -= 1
            console.print(f"[red]Senha incorreta! Tentativas restantes: {tentativas}[/red]")

    console.print("[bold red]Conta bloqueada![/bold red]")
    return False


def menu():
    console.print(Panel.fit(
        "[bold cyan]CAIXA ELETRÔNICO[/bold cyan]\n\n"
        "[1] Ver saldo\n"
        "[2] Depositar\n"
        "[3] Sacar\n"
        "[4] Extrato\n"
        "[5] Sair",
        title="Menu",
        border_style="blue"
    ))


# ====== EXECUÇÃO ======

console.print(Panel("[bold blue]Bem-vindo ao Caixa Eletrônico[/bold blue]"))

if not login():
    exit()

while True:
    menu()
    opcao = console.input("[yellow]Escolha uma opção:[/yellow] ")

    if opcao == "1":
        mostrar_saldo()

    elif opcao == "2":
        depositar()

    elif opcao == "3":
        sacar()

    elif opcao == "4":
        ver_extrato()

    elif opcao == "5":
        console.print("[bold]Saindo...[/bold]")
        break

    else:
        console.print("[red]Opção inválida![/red]")