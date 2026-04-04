import sys
import random
import json
import os

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
)

ARQUIVO = "dados.json"

# ================
# DADOS 
# ================
def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"vitorias": 0, "derrotas": 0, "empates": 0}
    with open(ARQUIVO, "r") as f:
        return json.load(f)
    
def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent = 4)

def resetar_dados():
    salvar_dados("vitorias": 0, "derrotas": 0, "empates": 0)

# ================
# LÓGICA
# ================
def escolher_computador():
    return random.choice(["pedra", "papel", "tesoura"])

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    
    regras = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }

    if regras[jogador] == computador:
        return "jogador"
    return "computador"

# ==================
# APP
# ==================
class JogoApp(QWidget):
    def __int__(self):
        super().__init__()

        self.setWindowTitle("Pedra, Papel e Tesoura")
        self.resize(300, 300)

        self.dados = carregar_dados()
        self.pontos_jogador = 0
        self.pontos_computador = 0

        layout = QVBoxLayout()

        self.label_info = QLabel("Escolha sua jogada:")
        layout.addWidget(self.label_info)

        btn_pedra = QPushButton("Pedra")
        btn_pedra.clicked.connect(lambda: self.jogar("pedra"))
        layout.addWidget(btn_pedra)

        btn_papel = QPushButton("Papel")
        btn_papel.clicked.connect(lambda: self.jogar("papel"))
        layout.addWidget(btn_papel)

        btn_tesoura = QPushButton("Tesoura")
        btn_tesoura.clicked.connect(lambda: self.jogar("tesoura"))
        layout.addWidget(btn_tesoura)

        self.label_resultado = QLabel("")
        layout.addWidget