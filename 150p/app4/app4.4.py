import sys
import random
import string
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QTextEdit, QCheckBox, QFileDialog
)
from PySide6.QtGui import QClipboard

# Funções de senha
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

# Classe do App
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de Senhas 🔐")
        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("""
            QWidget { background-color: #1e1e2f; color: #ffffff; font-family: Arial; font-size: 14px; }
            QPushButton { background-color: #4caf50; border: none; padding: 8px; border-radius: 5px; }
            QPushButton:hover { background-color: #45a049; }
            QLineEdit, QTextEdit { background-color: #2e2e3e; color: #ffffff; border: 1px solid #555555; border-radius: 5px; padding: 4px; }
            QCheckBox { padding: 2px; }
        """)

        layout = QVBoxLayout()

        self.tamanho_input = QLineEdit()
        self.tamanho_input.setPlaceholderText("Tamanho da senha")
        self.quantidade_input = QLineEdit()
        self.quantidade_input.setPlaceholderText("Quantidade de senhas")

        self.check_numeros = QCheckBox("Incluir números")
        self.check_simbolos = QCheckBox("Incluir símbolos")

        self.botao_gerar = QPushButton("Gerar Senhas")
        self.botao_gerar.clicked.connect(self.gerar)

        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)

        self.botao_salvar = QPushButton("Salvar em arquivo")
        self.botao_salvar.clicked.connect(self.salvar)

        self.botao_copiar = QPushButton("Copiar última senha")
        self.botao_copiar.clicked.connect(self.copiar_senha)

        layout.addWidget(QLabel("Gerador de Senhas 🔐"))
        layout.addWidget(self.tamanho_input)
        layout.addWidget(self.quantidade_input)
        layout.addWidget(self.check_numeros)
        layout.addWidget(self.check_simbolos)
        layout.addWidget(self.botao_gerar)
        layout.addWidget(self.resultado)
        layout.addWidget(self.botao_copiar)
        layout.addWidget(self.botao_salvar)

        self.setLayout(layout)

    def gerar(self):
        self.resultado.clear()
        try:
            tamanho = int(self.tamanho_input.text())
            quantidade = int(self.quantidade_input.text())
        except:
            self.resultado.setText("Digite valores válidos!")
            return

        self.senhas = []

        for i in range(quantidade):
            senha = gerar_senha(tamanho, self.check_numeros.isChecked(), self.check_simbolos.isChecked())
            nivel = avaliar_senha(senha)
            texto = f"Senha {i+1}: {senha} ({nivel})"
            self.resultado.append(texto)
            self.senhas.append(texto)

    def salvar(self):
        if not hasattr(self, 'senhas') or not self.senhas:
            self.resultado.append("\nNenhuma senha gerada ainda!")
            return

        caminho, _ = QFileDialog.getSaveFileName(self, "Salvar Senhas", "senhas.txt", "Text Files (*.txt)")
        if caminho:
            with open(caminho, "w") as f:
                for linha in self.senhas:
                    f.write(linha + "\n")
            self.resultado.append(f"\nSalvo em {caminho}!")

    def copiar_senha(self):
        if hasattr(self, 'senhas') and self.senhas:
            clipboard = QApplication.clipboard()
            ultima_senha = self.senhas[-1].split(": ")[1].split(" ")[0]
            clipboard.setText(ultima_senha)
            self.resultado.append("\nSenha copiada para a área de transferência!")

# Execução
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = App()
    janela.show()
    sys.exit(app.exec())