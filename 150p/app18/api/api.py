from flask import Flask, request, jsonify
from database import *
from services import nome_valido, telefone_valido

app = Flask(__name__)

# garantir que a tabela exista
criar_tabela()

# LISTAR TODOS
@app.route("/contatos", methods=["GET"])
def listar_contatos():
    contatos = listar_contatos_db()

    resultado = [
        {"id": c[0], "nome": c[1], "telefone": c[2]}
        for c in contatos
    ]

    return jsonify(resultado)

# BUSCAR
@app.route("/contatos/buscar", methods=["GET"])
def buscar_contatos():
    termo = request.args.get("q", "")
    dados = buscar_contatos_db(termo)

    resultado = [
        {"id": c[0], "nome": c[1], "telefone": c[2]}
        for c in dados
    ] 

    return jsonify(resultado)

# ADICIONAR
@app.route("/contatos", methods=["POST"])
def adicionar_contato():
    data = request.json

    nome = data.get("nome")
    telefone = data.get("telefone")

    if not nome_valido(nome):
        return jsonify({"erro": "Nome inválido"}), 400
    
    if not telefone_valido(telefone):
        return jsonify({"erro": "Telefone inválido"}), 400
    
    inserir_contatos(nome, telefone)

    return jsonify({"mensagem": "Contato adicionado"}), 201

# EDITAR
@app.route("/contatos/<int:id>", methods=["PUT"])
def editar_contato(id):
    data = request.json

    nome = data.get("nome")
    telefone = data.get("telefone")

    if not nome_valido(nome) or not telefone_valido(telefone):
        return jsonify({"erro": "Dados inválidos"}), 400
    
    atualizar_contato(id, nome, telefone)

    return jsonify({"mensagem": "Contato atualizado"})

# REMOVER
@app.route("/contatos/<int:id>", methods=["DELETE"])
def remover_contato(id):
    deletar_contato(id)
    return jsonify({"mensagem": "Contato removido"})

if __name__ == "__main__":
    app.run(debug=True)
