from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# =========================
# LÓGICA
# =========================
def gerar_jogo(qtd):
    return sorted(random.sample(range(1, 61), qtd))

def gerar_varios(qtd_jogos, qtd_nums):
    return [gerar_jogo(qtd_nums) for _ in range(qtd_jogos)]

def gerar_resultado():
    return sorted(random.sample(range(1, 61), 6))

def verificar(jogo, resultado):
    acertos = len(set(jogo) & set(resultado))

    if acertos == 6:
        status = "SENA"
    elif acertos == 5:
        status = "QUINA"
    elif acertos == 4:
        status = "QUADRA"
    else:
        status = "-"

    return acertos, status

# =========================
# ROTAS
# =========================

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API Mega-Sena funcionando 🚀"
    })


# 🔹 Gerar jogos
@app.route("/gerar", methods=["POST"])
def gerar():
    data = request.get_json()

    qtd_jogos = data.get("qtd_jogos", 1)
    qtd_numeros = data.get("qtd_numeros", 6)

    if qtd_numeros < 6 or qtd_numeros > 15:
        return jsonify({"erro": "Números devem estar entre 6 e 15"}), 400

    jogos = gerar_varios(qtd_jogos, qtd_numeros)

    return jsonify({
        "jogos": jogos
    })


# 🔹 Resultado oficial
@app.route("/resultado", methods=["GET"])
def resultado():
    return jsonify({
        "resultado": gerar_resultado()
    })


# 🔹 Simulação completa
@app.route("/simular", methods=["POST"])
def simular():
    data = request.get_json()

    qtd_jogos = data.get("qtd_jogos", 1)
    qtd_numeros = data.get("qtd_numeros", 6)

    jogos = gerar_varios(qtd_jogos, qtd_numeros)
    resultado = gerar_resultado()

    ranking = []

    for i, jogo in enumerate(jogos, 1):
        acertos, status = verificar(jogo, resultado)

        ranking.append({
            "jogo_id": i,
            "numeros": jogo,
            "acertos": acertos,
            "status": status
        })

    ranking.sort(key=lambda x: x["acertos"], reverse=True)

    melhor = ranking[0]

    return jsonify({
        "resultado_oficial": resultado,
        "ranking": ranking,
        "melhor_jogo": melhor
    })


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":
    app.run(debug=True)