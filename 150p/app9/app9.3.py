from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich import box

console = Console()


def gerar_tabuada(numero, inicio, fim):
    table = Table(
        title=f"Tabuada do {numero}",
        box=box.DOUBLE,
        style="cyan"
    )

    table.add_column("Operação", justify="center")
    table.add_column("Resultado", justify="center", style="green")

    for i in range(inicio, fim + 1):
        table.add_row(f"{numero} x {i}", str(numero * i))

    console.print(table)


def tabuada_completa(inicio, fim):
    for n in range(1, 11):
        gerar_tabuada(n, inicio, fim)


def menu():
    console.print(Panel.fit(
        "[bold yellow]SISTEMA DE TABUADA[/bold yellow]\n"
        "[1] Tabuada de um número\n"
        "[2] Tabuada completa (1 a 10)\n"
        "[0] Sair",
        border_style="blue"
    ))


while True:
    menu()

    opcao = Prompt.ask("\nEscolha uma opção", choices=["1", "2", "0"])

    if opcao == "0":
        console.print("\n[bold red]Encerrando sistema...[/bold red]")
        break

    try:
        inicio = IntPrompt.ask("Início da tabuada")
        fim = IntPrompt.ask("Fim da tabuada")

        if inicio > fim:
            console.print("[bold red]Erro: início maior que fim![/bold red]")
            continue

        if opcao == "1":
            numero = IntPrompt.ask("Digite o número")
            gerar_tabuada(numero, inicio, fim)

        elif opcao == "2":
            tabuada_completa(inicio, fim)

        continuar = Prompt.ask(
            "\nDeseja continuar?",
            choices=["s", "n"],
            default="s"
        )

        if continuar == "n":
            console.print("[bold red]Finalizando...[/bold red]")
            break

    except Exception:
        console.print("[bold red]Erro: entrada inválida![/bold red]")