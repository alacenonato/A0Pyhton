import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
)
from PySide6.QtCore import QTimer, Qt


class Cronometro(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cronômetro Profissional")
        self.setGeometry(100, 100, 300, 200)

        self.tempo = 0

        # Timer (atualiza a cada 1 segundo)
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_tempo)

        # Layout principal
        layout = QVBoxLayout()

        # Label do tempo
        self.label = QLabel("00:00:00")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 40px; font-weight: bold;")
        layout.addWidget(self.label)

        # Botões
        botoes_layout = QHBoxLayout()

        self.btn_start = QPushButton("Iniciar")
        self.btn_pause = QPushButton("Pausar")
        self.btn_reset = QPushButton("Resetar")

        botoes_layout.addWidget(self.btn_start)
        botoes_layout.addWidget(self.btn_pause)
        botoes_layout.addWidget(self.btn_reset)

        layout.addLayout(botoes_layout)

        self.setLayout(layout)

        # Eventos
        self.btn_start.clicked.connect(self.iniciar)
        self.btn_pause.clicked.connect(self.pausar)
        self.btn_reset.clicked.connect(self.resetar)

    def formatar_tempo(self):
        h = self.tempo // 3600
        m = (self.tempo % 3600) // 60
        s = self.tempo % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def atualizar_tempo(self):
        self.tempo += 1
        self.label.setText(self.formatar_tempo())

    def iniciar(self):
        self.timer.start(1000)

    def pausar(self):
        self.timer.stop()

    def resetar(self):
        self.timer.stop()
        self.tempo = 0
        self.label.setText("00:00:00")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Cronometro()
    janela.show()
    sys.exit(app.exec())