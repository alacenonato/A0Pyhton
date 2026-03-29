from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def gerar_senha(tamanho, usar_numeros, usar_simbolos):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    senha = []

    if usar_numeros:
        senha.append(random.choice(numeros))
    if usar_simbolos:
        senha.append(random.choice(simbolos))

    caracteres = letras
    if usar_numeros:
        caracteres += numeros
    if usar_simbolos:
        caracteres += simbolos

    while len(senha) < tamanho:
        senha.append(random.choice(caracteres))

    random.shuffle(senha)
    return ''.join(senha)

def avaliar_senha(senha):
    tamanho = len(senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_simbolo = any(c in string.punctuation for c in senha)

    if tamanho >= 12 and tem_numero and tem_simbolo:
        return "Forte 💪"
    elif tamanho >= 8:
        return "Média ⚖️"
    else:
        return "Fraca ❌"

@app.route("/", methods=["GET", "POST"])
def index():
    senhas = []
    if request.method == "POST":
        try:
            tamanho = int(request.form["tamanho"])
            quantidade = int(request.form["quantidade"])
        except:
            return render_template("index.html", senhas=["Digite valores válidos!"])

        usar_numeros = "numeros" in request.form
        usar_simbolos = "simbolos" in request.form

        for i in range(quantidade):
            senha = gerar_senha(tamanho, usar_numeros, usar_simbolos)
            nivel = avaliar_senha(senha)
            senhas.append(f"Senha {i+1}: {senha} ({nivel})")

    return render_template("index.html", senhas=senhas)

if __name__ == "__main__":
    app.run(debug=True)