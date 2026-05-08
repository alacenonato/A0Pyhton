import sys
import random
from PySide6.QtWidgets import (
    QApplication, QSpinBox, QWidget, QVBoxLayout,
    QPushButton, QLabel, QListWidget,
    QSpinBox
)

class GeradorNomeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gerador de Nomes Ficticios")
        self.setGeometry(200, 200, 500, 600)

        # Banco de nomes
        self.nomes = [
            "Aron", "Luna", "Kael", "Mira", "Drake",
            "Zane", "Nora", "Theo", "Lyra", "Raven"
        ]

        self.sobrenomes = [
            "Darkwood", "Silvermoon", "Blackstone",
            "Stormborn", "Nightfall", "Ironheart",
            "Shadowalker" "Flamecrest", "Winterbane"
        ]

        layout = QVBoxLayout()

        # Quantidade
        self.quantidade = QSpinBox()
        self.quantidade.setMinimum(1)
        self.quantidade.setMaximum(20)
        self.quantidade.setPrefix("Quantidade:")

        layout.addWidget(self.quantidade)

        # Botão
        self.btn_gerar = QPushButton("Gerar Nomes")
        layout.addWidget(self.btn_gerar)

        # Resultado principal
        self.resultado = QLabel("Nomes aparecerão aqui")
        layout.addWidget(self.resultado)

        # Histórico
        self.historico = QListWidget()
        layout.addWidget(self.historico)

        self.setLayout(layout)

        # Evento
        self.btn_gerar.clicked.connect(self.gerar_nomes)

    # --------------------------------------

    def gerar_nomes(self):
        qtd = self.quantidade.value()

        nomes_gerados = set()

        while len(nomes_gerados) < qtd:
            nome = random.choice(self.nomes)
            sobrenome = random.choice(self.sobrenomes)

            completo = f"{nome} {sobrenome}"

            nomes_gerados.add(completo)

        nomes_lista = list(nomes_gerados)

        self.resultado.setText(
            "✨ " + " | ".join(nomes_lista)
        )
        
        # Historico
        for nome in nomes_lista:
            self.historico.addItem(nome)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    janela = GeradorNomeApp()
    janela.show()

    sys.exit(app.exec())

