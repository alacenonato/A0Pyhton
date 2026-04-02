import random

# ==================
# Gerar Jogos
# ==================

def gerar_jogo(qtd_numeros):
    return sorted(random.sample(range(1, 61), qtd_numeros))

def gerar_varios_jogos(qtd_jogos, qtd_numeros):
    return [gerar_jogo(qtd_numeros) for _ in range(qtd_jogos)]

# =====================
# Resultado Oficial 
# =====================
def gerar_resultado():
    return sorted(random.sample(range(1, 61), 6))

# =========================
# Verificar Acertos
# =========================
def verificar_acertos(jogo, resultado):
    acertos = len(set(jogo) & set(resultado))

    if acertos == 6:
        status = "SENA 🥇"
    elif acertos == 5:
        status = "QUINA 🥈"
    elif acertos == 4:
        status = "QUADRA 🥉"
    else:
        status = "-"
    
    return acertos, status

# =========================
# Formatar Jogo
# =========================
def formatar(jogo):
    return " ".join(f"{n:02d}" for n in jogo)

# =========================
# Ranking
# =========================
def ranking(jogos, resultado):
    resultado_final = []

    for i, jogo in enumerate(jogos, 1):
        acertos, status = verificar_acertos(jogo, resultado)

        resultado_final.append({
            "id": i,
            "jogo": jogo,
            "acertos": acertos,
            "status": status}
        )
    
    # ordenar por número de acertos (maior primeiro)
    resultado_final.sort(key = lambda x: x["acertos"], reverse=True)

    return resultado_final

# ==========================
# MAIN
# ==========================
def main():
    print("=== 🎰 SIMULADOR MEGA-SENA ===\n")

    try:
        qtd_jogos = int(input("Quantos jogos deseja gerar? "))
        qtd_numeros = int(input("Quantos números pro jogo (6 a 15)? "))

        if qtd_numeros < 6 or qtd_numeros >15 :
            print("Erro: escolha entre 6 a 15 números.")
            return

        # gerar jogos
        jogos = gerar_varios_jogos(qtd_jogos, qtd_numeros)
        
        print("\n🎯 Seus jogos:")
        for i, jogo in enumerate(jogos, 1):
            print(f"Jogo {i}: {formatar(jogo)}")
        
        # gerar resultado oficial
        resultado = gerar_resultado()
        print("\n🏆 Resultado oficial:")
        print(formatar(resultado))

        # ranking
        resultado_rank = ranking(jogos, resultado)
        
        print("\n📊 Resultado dos jogos:\n")
        for item in resultado_rank:
            print(
                f"Jogo {item['id']}: {formatar(item['jogo'])} "
                f"→ {item['acertos']} acertos {item['status']}"
            )
        
        # melhor jogo
        melhor = resultado_rank[0]
        print("\n🔥 Melhor jogo:")
        print(
            f"Jogo {melhor['id']} com {melhor['acertos']} acertos {melhor['status']}"
        )

    except ValueError:
        print("Digite valores válidos")


if __name__ == "__main__":
    main()
