import os
from colorama import Fore, Style, init # type: ignore

init(autoreset=True)

historico = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def linha():
    print(Fore.CYAN + "=" * 40)


def titulo(txt):
    linha()
    print(Fore.YELLOW + Style.BRIGHT + txt.center(40))
    linha()


def menu():
    titulo("CONVERSOR DE TEMPERATURA")
    print(Fore.GREEN + "1 - Converter temperatura")
    print(Fore.BLUE + "2 - Ver histórico")
    print(Fore.RED + "3 - Sair")
    linha()


def entrada_float(msg):
    while True:
        try:
            return float(input(Fore.WHITE + msg))
        except ValueError:
            print(Fore.RED + "❌ Digite um número válido!")


def entrada_unidade(msg):
    while True:
        unidade = input(Fore.WHITE + msg).upper()
        if unidade in ["C", "F", "K"]:
            return unidade
        else:
            print(Fore.RED + "❌ Unidade inválida! Use C, F ou K.")


def converter(temp, origem, destino):
    if origem == destino:
        return temp

    if origem == "C":
        if destino == "F":
            return (temp * 9/5) + 32
        elif destino == "K":
            return temp + 273.15

    elif origem == "F":
        if destino == "C":
            return (temp - 32) * 5/9
        elif destino == "K":
            return (temp - 32) * 5/9 + 273.15

    elif origem == "K":
        if destino == "C":
            return temp - 273.15
        elif destino == "F":
            return (temp - 273.15) * 9/5 + 32


def converter_temperatura():
    titulo("NOVA CONVERSÃO")

    temp = entrada_float("Digite a temperatura: ")
    origem = entrada_unidade("Origem (C/F/K): ")
    destino = entrada_unidade("Destino (C/F/K): ")

    resultado = converter(temp, origem, destino)

    print(Fore.GREEN + f"\n✅ Resultado: {resultado:.2f} {destino}")

    historico.append(f"{temp} {origem} → {resultado:.2f} {destino}")


def ver_historico():
    titulo("HISTÓRICO")

    if not historico:
        print(Fore.YELLOW + "Nenhuma conversão realizada ainda.")
    else:
        for i, item in enumerate(historico, 1):
            print(Fore.CYAN + f"{i}. {item}")

    linha()


# 🔁 LOOP PRINCIPAL
while True:
    limpar_tela()
    menu()

    opcao = input(Fore.WHITE + "Escolha uma opção: ")

    if opcao == "1":
        converter_temperatura()
        input(Fore.MAGENTA + "\nPressione ENTER para continuar...")

    elif opcao == "2":
        ver_historico()
        input(Fore.MAGENTA + "\nPressione ENTER para continuar...")

    elif opcao == "3":
        print(Fore.RED + "\nSaindo do sistema... 👋")
        break

    else:
        print(Fore.RED + "❌ Opção inválida!")
        input(Fore.MAGENTA + "Pressione ENTER para tentar novamente...")