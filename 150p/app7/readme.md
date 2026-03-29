
Bora 🔥 — agora você vai dar mais um salto de lógica.

---

# 🧩 PROJETO 7 — Contador de Palavras

## 🎯 Objetivo

Criar um programa que analisa um texto e retorna:

✔ Quantidade de palavras
✔ Quantidade de caracteres
✔ Quantidade de frases
✔ Palavra mais frequente
✔ Frequência de todas as palavras

👉 Isso aqui já começa a entrar em **processamento de texto (muito usado no mercado)**

---

# 🧠 CONCEITOS IMPORTANTES

Você vai treinar:

* Strings
* Listas
* Dicionários (`dict`)
* Funções
* Limpeza de texto (muito importante)

---

# 💻 VERSÃO COMPLETA (CLI + Tratamento de erro)

```python
import string
from collections import Counter


def analisar_texto(texto):
    # Remover pontuação
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation))

    # Padronizar para minúsculas
    texto_limpo = texto_limpo.lower()

    palavras = texto_limpo.split()

    # Contagem
    total_palavras = len(palavras)
    total_caracteres = len(texto)
    total_frases = texto.count('.') + texto.count('!') + texto.count('?')

    frequencia = Counter(palavras)

    palavra_mais_comum = frequencia.most_common(1)

    return {
        "palavras": total_palavras,
        "caracteres": total_caracteres,
        "frases": total_frases,
        "frequencia": frequencia,
        "mais_comum": palavra_mais_comum
    }


def main():
    print("===== ANALISADOR DE TEXTO =====")

    try:
        texto = input("Digite um texto: ")

        if not texto.strip():
            raise ValueError("Texto vazio!")

        resultado = analisar_texto(texto)

        print(f"\nTotal de palavras: {resultado['palavras']}")
        print(f"Total de caracteres: {resultado['caracteres']}")
        print(f"Total de frases: {resultado['frases']}")

        if resultado["mais_comum"]:
            palavra, qtd = resultado["mais_comum"][0]
            print(f"Palavra mais frequente: '{palavra}' ({qtd}x)")

        print("\nFrequência de palavras:")
        for palavra, qtd in resultado["frequencia"].items():
            print(f"{palavra}: {qtd}")

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
```

---

# 🔥 DESAFIOS (EVOLUÇÃO)

## 🧩 Desafio 1 — Ignorar palavras comuns

Exemplo:

* de, a, o, e, da...

👉 Isso melhora muito análise real

---

## 🧩 Desafio 2 — Ordenar por frequência

Mostrar palavras mais usadas primeiro

---

## 🧩 Desafio 3 — Ler arquivo `.txt`

Em vez de digitar texto

---

## 🧩 Desafio 4 — Exportar relatório

Salvar análise em arquivo `.txt`

---

# 🚀 VERSÃO PROFISSIONAL (IDEIA)

Você pode transformar isso em:

* 📊 Analisador de texto (tipo mini BI)
* 🧠 Base para IA/NLP
* 📝 Ferramenta para contadores (analisar relatórios)

---

# 🧠 MISSÃO

Faça:

✅ Teste com textos grandes
✅ Modifique algo
✅ Suba no GitHub

---

# 🔥 PRÓXIMO PASSO

Posso fazer pra você também:

👉 Versão com interface gráfica (PySide6)
👉 Versão web (Flask)
👉 Versão que lê PDFs

---

Se quiser continuar:

👉 fala: **“Projeto 8”**
ou
👉 **“Quero versão GUI desse projeto”** 😎

# MAIS E MAIS 

Perfeito — agora você está criando algo **nível ferramenta real de mercado** 🔥
Vou te entregar a versão **GUI completa com PySide6**, incluindo TODOS os desafios:

---

# 🚀 PROJETO 7 — GUI COMPLETO (ANALISADOR DE TEXTO PRO)

## ✅ Funcionalidades incluídas:

✔ Interface gráfica
✔ Contagem de palavras, caracteres e frases
✔ Frequência de palavras (ordenada)
✔ Palavra mais frequente
✔ Ignorar palavras comuns (stopwords)
✔ Ler arquivo `.txt`
✔ Exportar relatório `.txt`
✔ Tratamento de erros completo

---

# 📦 INSTALAÇÃO

```bash
pip install PySide6
```

---

# 💻 CÓDIGO COMPLETO

```python
import sys
import string
from collections import Counter
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QPushButton, QFileDialog, QMessageBox
)

# Palavras comuns (stopwords)
STOPWORDS = {
    "de", "da", "do", "das", "dos", "a", "o", "e", "é",
    "em", "um", "uma", "para", "com", "não", "na", "no"
}


# -----------------------------
# FUNÇÃO DE ANÁLISE
# -----------------------------
def analisar_texto(texto):
    texto_limpo = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    palavras = texto_limpo.split()

    # Remover stopwords
    palavras_filtradas = [p for p in palavras if p not in STOPWORDS]

    total_palavras = len(palavras_filtradas)
    total_caracteres = len(texto)
    total_frases = texto.count('.') + texto.count('!') + texto.count('?')

    frequencia = Counter(palavras_filtradas)
    frequencia_ordenada = frequencia.most_common()

    palavra_mais_comum = frequencia.most_common(1)

    return {
        "palavras": total_palavras,
        "caracteres": total_caracteres,
        "frases": total_frases,
        "frequencia": frequencia_ordenada,
        "mais_comum": palavra_mais_comum
    }


# -----------------------------
# INTERFACE
# -----------------------------
class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Analisador de Texto PRO")
        self.setGeometry(200, 200, 600, 500)

        layout = QVBoxLayout()

        self.label = QLabel("Digite ou carregue um texto:")
        layout.addWidget(self.label)

        self.texto_input = QTextEdit()
        layout.addWidget(self.texto_input)

        # Botões
        self.btn_analisar = QPushButton("Analisar Texto")
        self.btn_analisar.clicked.connect(self.analisar)
        layout.addWidget(self.btn_analisar)

        self.btn_carregar = QPushButton("Carregar arquivo .txt")
        self.btn_carregar.clicked.connect(self.carregar_arquivo)
        layout.addWidget(self.btn_carregar)

        self.btn_exportar = QPushButton("Exportar relatório")
        self.btn_exportar.clicked.connect(self.exportar)
        layout.addWidget(self.btn_exportar)

        self.btn_limpar = QPushButton("Limpar")
        self.btn_limpar.clicked.connect(self.limpar)
        layout.addWidget(self.btn_limpar)

        # Saída
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

        self.resultado_atual = None

    # -----------------------------
    # ANALISAR
    # -----------------------------
    def analisar(self):
        texto = self.texto_input.toPlainText()

        try:
            if not texto.strip():
                raise ValueError("Texto vazio!")

            self.resultado_atual = analisar_texto(texto)

            self.output.clear()

            self.output.append(f"Palavras: {self.resultado_atual['palavras']}")
            self.output.append(f"Caracteres: {self.resultado_atual['caracteres']}")
            self.output.append(f"Frases: {self.resultado_atual['frases']}")

            if self.resultado_atual["mais_comum"]:
                palavra, qtd = self.resultado_atual["mais_comum"][0]
                self.output.append(f"\nMais frequente: '{palavra}' ({qtd}x)")

            self.output.append("\nTop palavras:")

            for palavra, qtd in self.resultado_atual["frequencia"][:10]:
                self.output.append(f"{palavra}: {qtd}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))

    # -----------------------------
    # CARREGAR ARQUIVO
    # -----------------------------
    def carregar_arquivo(self):
        try:
            caminho, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", "Text Files (*.txt)")

            if caminho:
                with open(caminho, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                    self.texto_input.setText(conteudo)

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar arquivo: {e}")

    # -----------------------------
    # EXPORTAR
    # -----------------------------
    def exportar(self):
        try:
            if not self.resultado_atual:
                raise ValueError("Nenhuma análise feita!")

            caminho, _ = QFileDialog.getSaveFileName(self, "Salvar relatório", "", "Text Files (*.txt)")

            if caminho:
                with open(caminho, "w", encoding="utf-8") as f:
                    f.write("=== RELATÓRIO ===\n")
                    f.write(f"Palavras: {self.resultado_atual['palavras']}\n")
                    f.write(f"Caracteres: {self.resultado_atual['caracteres']}\n")
                    f.write(f"Frases: {self.resultado_atual['frases']}\n\n")

                    if self.resultado_atual["mais_comum"]:
                        palavra, qtd = self.resultado_atual["mais_comum"][0]
                        f.write(f"Mais frequente: {palavra} ({qtd}x)\n\n")

                    f.write("Frequência:\n")
                    for palavra, qtd in self.resultado_atual["frequencia"]:
                        f.write(f"{palavra}: {qtd}\n")

                QMessageBox.information(self, "Sucesso", "Relatório salvo com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))

    # -----------------------------
    # LIMPAR
    # -----------------------------
    def limpar(self):
        self.texto_input.clear()
        self.output.clear()
        self.resultado_atual = None


# -----------------------------
# EXECUÇÃO
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = App()
    janela.show()
    sys.exit(app.exec())
```

---

# 🧠 O QUE VOCÊ ACABOU DE FAZER

Isso aqui já é **nível MUITO acima da maioria dos iniciantes**:

✔ Processamento de texto
✔ Interface gráfica real
✔ Manipulação de arquivos
✔ Tratamento de erros
✔ Estrutura de aplicação

👉 Isso já pode ir pro seu **portfólio profissional**

---

# 🔥 IDEIAS PRA TURBINAR (DIFERENCIAL)

Se quiser deixar absurdo:

* Tema escuro 🌙
* Gráfico de frequência (matplotlib)
* Suporte a PDF
* Exportar CSV
* Ranking top 100 palavras

---

# 🚀 PRÓXIMO PASSO

Se quiser manter o ritmo forte:

👉 **“Projeto 8”**
ou
👉 **“Quero transformar isso em app profissional com design bonito”** 😎

# MAIS E MAIS 

Bora 🔥 — agora você vai transformar isso em **aplicação web real com Flask** (isso aqui já é nível backend de mercado).

Vou te entregar uma versão completa do **Projeto 7 (Analisador de Texto) em Flask**, com:

---

# 🚀 PROJETO 7 — VERSÃO WEB (FLASK PRO)

## ✅ Funcionalidades:

✔ Interface web (HTML)
✔ Análise de texto
✔ Stopwords (ignorar palavras comuns)
✔ Frequência ordenada
✔ Upload de arquivo `.txt`
✔ Exportar relatório
✔ Tratamento de erros

---

# 📦 PASSO 1 — INSTALAR

```bash
pip install flask
```

---

# 📁 ESTRUTURA DO PROJETO

```
projeto7_flask/
│
├── app.py
├── templates/
│   └── index.html
└── static/
```

---

# 💻 app.py (BACKEND)

```python
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
```

---

# 🌐 templates/index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Analisador de Texto</title>
</head>
<body>

<h1>📊 Analisador de Texto</h1>

<form method="POST" enctype="multipart/form-data">
    <textarea name="texto" rows="10" cols="60">{{ texto }}</textarea><br><br>

    <input type="file" name="arquivo"><br><br>

    <button type="submit">Analisar</button>
</form>

{% if erro %}
    <p style="color:red;">Erro: {{ erro }}</p>
{% endif %}

{% if resultado %}
    <h2>Resultado:</h2>

    <p>Palavras: {{ resultado.palavras }}</p>
    <p>Caracteres: {{ resultado.caracteres }}</p>
    <p>Frases: {{ resultado.frases }}</p>

    {% if resultado.mais_comum %}
        <p>Mais frequente: {{ resultado.mais_comum[0][0] }} ({{ resultado.mais_comum[0][1] }}x)</p>
    {% endif %}

    <h3>Top palavras:</h3>
    <ul>
        {% for palavra, qtd in resultado.frequencia[:10] %}
            <li>{{ palavra }}: {{ qtd }}</li>
        {% endfor %}
    </ul>

    <form method="POST" action="/exportar">
        <input type="hidden" name="texto" value="{{ texto }}">
        <button type="submit">Exportar Relatório</button>
    </form>
{% endif %}

</body>
</html>
```

---

# ▶️ COMO RODAR

No terminal:

```bash
python app.py
```

Depois abra no navegador:

```
http://127.0.0.1:5000
```

---

# 🧠 O QUE VOCÊ APRENDEU (NÍVEL SUBIU 🔥)

Agora você já sabe:

✔ Criar aplicação web com Flask
✔ Trabalhar com rotas (`@app.route`)
✔ Receber formulário (POST)
✔ Upload de arquivos
✔ Gerar download (exportar)
✔ Template HTML (Jinja2)

👉 Isso já é **backend real**

---

# 🔥 PRÓXIMO NÍVEL (SE QUISER FICAR FORTE)

Posso evoluir isso pra:

👉 Layout bonito com Bootstrap
👉 API REST (sem interface)
👉 Banco de dados (histórico de análises)
👉 Login de usuário
👉 Deploy online

---

Se quiser continuar forte:

👉 fala: **“Projeto 8”**
ou
👉 **“Quero transformar isso em sistema SaaS”** 🚀
