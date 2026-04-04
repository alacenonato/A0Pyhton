import random
import json
import os

ARQUIVO = "dados.json"

# ====================
# MODELO PADRÃO (BASE SEGURA)
# ====================
# ✅ MELHORIA:
# Criamos um "molde" oficial dos dados
# Isso evita erro de chave faltando ou nome errado
MODELO_DADOS = {
    "vitorias": 0,
    "derrotas": 0,
    "empates": 0
}

# ====================
# UTIL / DADOS
# ====================
def validar_dados(dados):
    """
    Garante que o dicionário tem todas as chaves corretas.
    Corrige automaticamente se estiver errado.
    """
    for chave in MODELO_DADOS:
        if chave not in dados:
            # 🔧 MELHORIA:
            # Se faltar alguma chave, adiciona automaticamente
            dados[chave] = 0

    return dados


def carregar_dados():
    # Se não existir, cria novo
    if not os.path.exists(ARQUIVO):
        return MODELO_DADOS.copy()

    try:
        with open(ARQUIVO, "r") as f:
            dados = json.load(f)

            # ❌ SEU ERRO ORIGINAL:
            # Você salvou "empate" ao invés de "empates"
            # Isso quebrava o código depois
            
            # ✅ MELHORIA:
            # Validamos e corrigimos automaticamente
            dados = validar_dados(dados)

            return dados

    except Exception as e:
        print("Arquivo corrompido, recriando...", e)

        # ✅ MELHORIA:
        # Se o JSON estiver quebrado, recria do zero
        return MODELO_DADOS.copy()


def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)


def resetar_dados():
    # ❌ ERRO ORIGINAL:
    # "empate" (sem S) quebrava tudo depois
    
    # ✅ CORRETO:
    dados = MODELO_DADOS.copy()
    salvar_dados(dados)
    print("Histórico resetado!")


# =====================
# LÓGICA DO JOGO
# =====================
def escolher_computador():
    return random.choice(["pedra", "papel", "tesoura"])


def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"

    regras = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }

    # ❗ POSSÍVEL ERRO FUTURO (já prevenido antes):
    # Se jogador for inválido, isso daria KeyError
    # Mas você já protegeu com validação no input 👍

    if regras[jogador] == computador:
        return "jogador"

    return "computador"


# ======================
# JOGO PRINCIPAL
# ======================
def jogar():
    dados = carregar_dados()

    pontos_jogador = 0
    pontos_computador = 0

    print("\nMelhor de 3 - Começou!")

    while pontos_jogador < 2 and pontos_computador < 2:
        try:
            jogador = input("Escolha pedra, papel ou tesoura: ").lower()

            if jogador not in ["pedra", "papel", "tesoura"]:
                print("Opção inválida!")
                continue

            computador = escolher_computador()
            print(f"Computador escolheu: {computador}")

            resultado = determinar_vencedor(jogador, computador)

            if resultado == "empate":
                print("Empate!")

                # ❌ AQUI QUEBRAVA ANTES:
                # dados["empates"] não existia
                
                # ✅ AGORA SEGURO:
                dados["empates"] += 1

            elif resultado == "jogador":
                print("Você venceu a rodada!")
                pontos_jogador += 1
                dados["vitorias"] += 1
            else:
                print("Computador venceu!")
                pontos_computador += 1
                dados["derrotas"] += 1

            print(f"Placar: Você {pontos_jogador} x {pontos_computador} computador\n")

        except Exception as e:
            # ❗ MELHORIA:
            # Em desenvolvimento, é melhor NÃO esconder erro
            print("Erro inesperado:", e)
            raise  # remove isso depois se quiser

    # Resultado final
    if pontos_jogador > pontos_computador:
        print("Você ganhou a partida!")
    else:
        print("Você perdeu a partida!")

    salvar_dados(dados)


# ====================
# MENU
# ====================
def ver_historico():
    dados = carregar_dados()

    print("\n HISTÓRICO")
    print(f"Vitórias: {dados['vitorias']}")
    print(f"Derrotas: {dados['derrotas']}")
    print(f"Empates: {dados['empates']}\n")


def menu():
    while True:
        print("\n======= MENU ========")
        print("1 - Jogar")
        print("2 - Ver histórico")
        print("3 - Resetar histórico")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogar()
        elif opcao == "2":
            ver_historico()
        elif opcao == "3":
            resetar_dados()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


# ======================
# EXECUÇÃO
# ======================
if __name__ == "__main__":
    menu()