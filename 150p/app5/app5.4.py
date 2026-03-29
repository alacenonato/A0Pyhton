import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QLineEdit, QTextEdit, QComboBox
)

class Jogo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jogo da Adivinhação 🎮")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        # Título
        self.titulo = QLabel("Adivinhe o número!")
        self.layout.addWidget(self.titulo)

        # Dificuldade
        self.dificuldade = QComboBox()
        self.dificuldade.addItems(["Fácil (1-50)", "Médio (1-100)", "Difícil (1-200)"])
        self.layout.addWidget(self.dificuldade)

        # Input
        self.input_numero = QLineEdit()
        self.input_numero.setPlaceholderText("Digite seu palpite")
        self.layout.addWidget(self.input_numero)

        # Botão jogar
        self.botao = QPushButton("Tentar")
        self.botao.clicked.connect(self.tentar)
        self.layout.addWidget(self.botao)

        # Resultado
        self.resultado = QLabel("")
        self.layout.addWidget(self.resultado)

        # Histórico
        self.historico = QTextEdit()
        self.historico.setReadOnly(True)
        self.layout.addWidget(self.historico)

        # Tentativas
        self.tentativas_label = QLabel("")
        self.layout.addWidget(self.tentativas_label)

        # Pontuação
        self.pontuacao_label = QLabel("")
        self.layout.addWidget(self.pontuacao_label)

        # Novo jogo
        self.novo_jogo_btn = QPushButton("Novo Jogo 🔄")
        self.novo_jogo_btn.clicked.connect(self.novo_jogo)
        self.layout.addWidget(self.novo_jogo_btn)

        self.setLayout(self.layout)

        self.novo_jogo()

    def configurar_jogo(self):
        dificuldade = self.dificuldade.currentIndex()

        if dificuldade == 0:
            self.limite = 50
        elif dificuldade == 1:
            self.limite = 100
        else:
            self.limite = 200

        self.numero_secreto = random.randint(1, self.limite)
        self.max_tentativas = 5
        self.tentativas = 0
        self.historico_lista = []

        self.historico.clear()
        self.resultado.setText("")
        self.pontuacao_label.setText("")

        self.atualizar_tentativas()

    def novo_jogo(self):
        self.configurar_jogo()

    def atualizar_tentativas(self):
        restantes = self.max_tentativas - self.tentativas
        self.tentativas_label.setText(f"Tentativas restantes: {restantes}")

    def calcular_pontos(self):
        return max(0, (self.max_tentativas - self.tentativas + 1) * 10)

    def tentar(self):
        try:
            tentativa = int(self.input_numero.text())
        except:
            self.resultado.setText("Digite um número válido!")
            return

        self.tentativas += 1
        self.historico_lista.append(tentativa)
        self.historico.append(str(tentativa))

        if tentativa == self.numero_secreto:
            pontos = self.calcular_pontos()
            self.resultado.setText("🎉 Você acertou!")
            self.pontuacao_label.setText(f"Pontuação: {pontos}")
            return

        elif tentativa < self.numero_secreto:
            self.resultado.setText("🔼 Tente um número maior")
        else:
            self.resultado.setText("🔽 Tente um número menor")

        self.atualizar_tentativas()

        if self.tentativas >= self.max_tentativas:
            self.resultado.setText(f"💀 Fim de jogo! Número era {self.numero_secreto}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Jogo()
    janela.show()
    sys.exit(app.exec())