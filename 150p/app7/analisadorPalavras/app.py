from flask import Flask, render_template, request, send_file
import string
from collections import Counter
import io

app = Flask(__name__)

STOPWORDS = {
    "de", "da", "do", "das", "dos", "a", "o", "e", "é",
    "em", "um", "uma", "para", "com", "não", "na", "no"
}


def analisar_texto(texto):
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    palavras = texto_limpo.split()

    palavras_filtradas = [p for p in palavras if p not in STOPWORDS]

    total_palavras = len(palavras_filtradas)
    total_caracteres = len(texto)
    total_frases = texto.count('.') + texto.count('!') + texto.count('?')

    frequencia = Counter(palavras_filtradas)
    frequencia_ordenada = frequencia.most_common()
    mais_comum = frequencia.most_common(1)

    return {
        "palavras": total_palavras,
        "caracteres": total_caracteres,
        "frases": total_frases,
        "frequencia": frequencia_ordenada,
        "mais_comum": mais_comum
    }


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None
    texto = ""

    if request.method == "POST":
        try:
            texto = request.form.get("texto", "")

            arquivo = request.files.get("arquivo")

            if arquivo and arquivo.filename != "":
                texto = arquivo.read().decode("utf-8")

            if not texto.strip():
                raise ValueError("Texto vazio!")

            resultado = analisar_texto(texto)

        except Exception as e:
            erro = str(e)

    return render_template("index.html", resultado=resultado, erro=erro, texto=texto)


@app.route("/exportar", methods=["POST"])
def exportar():
    try:
        texto = request.form.get("texto", "")

        if not texto.strip():
            raise ValueError("Texto vazio!")

        resultado = analisar_texto(texto)

        buffer = io.StringIO()
        buffer.write("=== RELATÓRIO ===\n")
        buffer.write(f"Palavras: {resultado['palavras']}\n")
        buffer.write(f"Caracteres: {resultado['caracteres']}\n")
        buffer.write(f"Frases: {resultado['frases']}\n\n")

        if resultado["mais_comum"]:
            palavra, qtd = resultado["mais_comum"][0]
            buffer.write(f"Mais frequente: {palavra} ({qtd}x)\n\n")

        buffer.write("Frequência:\n")
        for palavra, qtd in resultado["frequencia"]:
            buffer.write(f"{palavra}: {qtd}\n")

        buffer.seek(0)

        return send_file(
            io.BytesIO(buffer.getvalue().encode("utf-8")),
            as_attachment=True,
            download_name="relatorio.txt",
            mimetype="text/plain"
        )

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)