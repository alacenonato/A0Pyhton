import sys
import string
from collections import Counter
from PySide6.QtWidgets import ( 
    QApplication, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QPushButton, QFileDialog, QMessageBox
)

# Palavras comuns (stopwords)

STOPWORDS= {
    "de", "da", "do", "das", "dos", "a", "o", "e", "é",
    "em", "um", "uma", "para", "com", "não", "na", "no"
}

# -----------------------------
# FUNÇÃO DE ANÁLISE
# -----------------------------

def analisar_texto(texto):
    texto_limpo = texto.translate(str.maketrans('','', string.punctuation))
    palavras = texto_limpo.split()

    # Remover stopwords
    palavras_filtradas = [ p for p in palavras if p not in STOPWORDS]

    total_palavras = len(palavras_filtradas)
    total_caracteres = len(texto)
    total_frases = texto.count('.') + texto.count('!') + texto.count('?')

    frequencia = Counter(palavras_filtradas)
    frequencia_ordenada = frequencia.most_common()

    palavras_mais_comum = frequencia.most_common(1)

    return {
        "palavras": total_palavras,
        "caracteres": total_caracteres,
        "frases": total_frases,
        "frequencia": frequencia_ordenada,
        "mais_comum": palavras_mais_comum

    }

# -----------------------------
# FUNÇÃO DE ANÁLISE
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

        self.btn_carregar = QPushButton("Carregar arquivo.txt")
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