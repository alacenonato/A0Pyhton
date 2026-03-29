from flask import Flask, request, jsonify
from services.cpf_service import validar_cpf, gerar_cpf
from utils.helpers import limpar_cpf

app = Flask(__name__)

# Rota de status (health check)
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "message": "API de Cpf rodando"
    })

# Validar Cpf
@app.route("/cpf/validar", methods=["POST"])
def validar():
    data = request.get_json()

    if not data or "cpf" not in data:
        return jsonify({
            "erro": "Cpf não enviado"
        }), 400
    
    cpf = limpar_cpf(data["cpf"])
    valido, msg = validar_cpf(cpf)

    return jsonify({
        "cpf": cpf,
        "valido": valido,
        "mensagem": msg
    })

# Gerar Cpf
@app.route("/cpf/gerar", methods=["GET"])
def gerar():
    cpf = gerar_cpf()
    return jsonify({
        "cpf": cpf
    })

# Run
if __name__ == "__main__":
    app.run(debug=True)