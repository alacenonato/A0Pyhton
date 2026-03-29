import os
from colorama import Fore, Style, init

init(autoreset=True)

historico = []

# 🎨 TEMAS
tema_atual = "dark"

temas = {
    "dark": {
        "titulo": Fore.YELLOW + Style.BRIGHT,
        "menu": Fore.CYAN,
        "texto": Fore.WHITE,
        "erro": Fore.RED,
        "sucesso": Fore.GREEN,
        "borda": Fore.BLUE
    },
    "light": {
        "titulo": Fore.BLUE + Style.BRIGHT,
        "menu": Fore.MAGENTA,
        "texto": Fore.BLACK,
        "erro": Fore.RED,
        "sucesso": Fore.GREEN,
        "borda": Fore.BLACK
    }
}


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cor(tipo):
    return temas[tema_atual][tipo]


# 🧱 CAIXA ASCII
def caixa(texto):
    largura = 42
    borda = cor("borda")

    print(borda + "┌" + "─" * largura + "┐")
    print(borda + "│" + texto.center(largura) + "│")
    print(borda + "└" + "─" * largura + "┘")


def menu():
    caixa("CONVERSOR DE TEMPERATURA")
    print(cor("menu") + " 1 → Converter temperatura")
    print(cor("menu") + " 2 → Ver histórico")
    print(cor("menu") + " 3 → Trocar tema")
    print(cor("menu") + " 4 → Sair")
    print(cor("borda") + "─" * 44)


def entrada_float(msg):
    while True:
        try:
            return float(input(cor("texto") + msg))
        except ValueError:
            print(cor("erro") + "❌ Digite um número válido!")


def entrada_unidade(msg):
    while True:
        unidade = input(cor("texto") + msg).upper()
        if unidade in ["C", "F", "K"]:
            return unidade
        else:
            print(cor("erro") + "❌ Use apenas C, F ou K.")


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
    caixa("NOVA CONVERSÃO")

    temp = entrada_float("Digite a temperatura: ")
    origem = entrada_unidade("Origem (C/F/K): ")
    destino = entrada_unidade("Destino (C/F/K): ")

    resultado = converter(temp, origem, destino)

    print(cor("sucesso") + f"\n✔ Resultado: {resultado:.2f} {destino}")

    historico.append(f"{temp} {origem} → {resultado:.2f} {destino}")


def ver_historico():
    caixa("HISTÓRICO")

    if not historico:
        print(cor("texto") + "Nenhuma conversão ainda.")
    else:
        for i, item in enumerate(historico, 1):
            print(cor("menu") + f"{i}. {item}")


def trocar_tema():
    global tema_atual
    caixa("ESCOLHER TEMA")

    print("1 → Dark")
    print("2 → Light")

    op = input("Escolha: ")

    if op == "1":
        tema_atual = "dark"
    elif op == "2":
        tema_atual = "light"
    else:
        print(cor("erro") + "Opção inválida!")


# 🔁 LOOP PRINCIPAL
while True:
    limpar_tela()
    menu()

    opcao = input(cor("texto") + "Escolha uma opção: ")

    if opcao == "1":
        converter_temperatura()
        input("\nPressione ENTER...")

    elif opcao == "2":
        ver_historico()
        input("\nPressione ENTER...")

    elif opcao == "3":
        trocar_tema()
        input("\nPressione ENTER...")

    elif opcao == "4":
        print(cor("erro") + "\nSaindo... 👋")
        break

    else:
        print(cor("erro") + "❌ Opção inválida!")
        input("Pressione ENTER...")