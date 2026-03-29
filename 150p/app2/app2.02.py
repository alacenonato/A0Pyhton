import os

historico = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def linha():
    print("=" * 40)


def titulo(txt):
    linha()
    print(txt.center(40))
    linha()


def menu():
    titulo("CONVERSOR DE TEMPERATURA")
    print("1 - Converter temperatura")
    print("2 - Ver histórico")
    print("3 - Sair")
    linha()


def entrada_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("❌ Digite um número válido!")


def entrada_unidade(msg):
    while True:
        unidade = input(msg).upper()
        if unidade in ["C", "F", "K"]:
            return unidade
        else:
            print("❌ Unidade inválida! Use C, F ou K.")


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

    print(f"\n✅ Resultado: {resultado:.2f} {destino}")

    historico.append(f"{temp} {origem} → {resultado:.2f} {destino}")


def ver_historico():
    titulo("HISTÓRICO")

    if not historico:
        print("Nenhuma conversão realizada ainda.")
    else:
        for i, item in enumerate(historico, 1):
            print(f"{i}. {item}")

    linha()


# 🔁 LOOP PRINCIPAL
while True:
    limpar_tela()
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        converter_temperatura()
        input("\nPressione ENTER para continuar...")

    elif opcao == "2":
        ver_historico()
        input("\nPressione ENTER para continuar...")

    elif opcao == "3":
        print("\nSaindo do sistema... 👋")
        break

    else:
        print("❌ Opção inválida!")
        input("Pressione ENTER para tentar novamente...")


'''
O que você acabou de construir (IMPORTANTE)

Isso aqui já é nível iniciante forte, porque você usou:

🧠 Funções organizadas

🔁 Loop infinito (while True)

🛡️ Tratamento de erro (try/except)

📜 Histórico (lista)

🖥️ Interface estruturada (UX básica)

👉 Isso já parece um mini sistema real, não só um exercício.

🧪 Teste esse fluxo:

Converter várias temperaturas

Ver histórico

Tentar digitar letras → deve bloquear

Tentar opções inválidas no menu

🚀 Próximo nível (recomendado)

Se você quiser evoluir MUITO com esse mesmo projeto:

👉 posso te guiar para:

💾 Salvar histórico em arquivo (JSON)

🎨 Interface mais bonita (cores no terminal)

🖱️ Interface gráfica com Tkinter

🌐 Criar uma API com Flask

👉 Me chama assim:

👉 “quero deixar com cores no terminal”
👉 “quero salvar histórico em arquivo”
👉 “quero transformar em app com botão”

Vou evoluindo com você passo a passo até nível profissional.

'''