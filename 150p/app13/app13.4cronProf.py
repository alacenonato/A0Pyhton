import sys
import json
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QHBoxLayout, QListWidget
)
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation
from PySide6.QtGui import QFont


class Cronometro(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cronômetro PRO")
        self.setGeometry(300, 200, 400, 400)

        self.tempo = 0
        self.laps = []

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_tempo)

        # Layout
        layout = QVBoxLayout()

        # Display tempo
        self.label = QLabel("00:00:00")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 32, QFont.Bold))
        layout.addWidget(self.label)

        # Lista de voltas
        self.lista_laps = QListWidget()
        layout.addWidget(self.lista_laps)

        # Botões
        btn_layout = QHBoxLayout()

        self.btn_start = QPushButton("▶ Start")
        self.btn_pause = QPushButton("⏸ Pause")
        self.btn_reset = QPushButton("⏹ Reset")
        self.btn_lap = QPushButton("⏱ Lap")

        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_pause)
        btn_layout.addWidget(self.btn_reset)
        btn_layout.addWidget(self.btn_lap)

        layout.addLayout(btn_layout)

        self.setLayout(layout)

        # Eventos
        self.btn_start.clicked.connect(self.iniciar)
        self.btn_pause.clicked.connect(self.pausar)
        self.btn_reset.clicked.connect(self.resetar)
        self.btn_lap.clicked.connect(self.marcar_lap)

        # Tema escuro
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: white;
            }
            QPushButton {
                background-color: #1f1f1f;
                border: 1px solid #333;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #007acc;
            }
            QListWidget {
                background-color: #1a1a1a;
                border: 1px solid #333;
            }
        """)

    def formatar_tempo(self):
        h = self.tempo // 3600
        m = (self.tempo % 3600) // 60
        s = self.tempo % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def atualizar_tempo(self):
        self.tempo += 1
        self.label.setText(self.formatar_tempo())
        self.animar_label()

    def animar_label(self):
        anim = QPropertyAnimation(self.label, b"geometry")
        anim.setDuration(200)
        anim.setStartValue(self.label.geometry())
        anim.setEndValue(self.label.geometry().adjusted(-5, -5, 5, 5))
        anim.start()

    def iniciar(self):
        self.timer.start(1000)

    def pausar(self):
        self.timer.stop()

    def resetar(self):
        self.timer.stop()
        self.tempo = 0
        self.label.setText("00:00:00")
        self.lista_laps.clear()
        self.laps = []

    def marcar_lap(self):
        tempo_atual = self.formatar_tempo()
        self.laps.append(tempo_atual)
        self.lista_laps.addItem(f"Lap {len(self.laps)}: {tempo_atual}")

    def salvar_historico(self):
        dados = {
            "data": str(datetime.now()),
            "laps": self.laps
        }
        with open("historico.json", "a") as f:
            f.write(json.dumps(dados) + "\n")

    def closeEvent(self, event):
        self.salvar_historico()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Cronometro()
    janela.show()
    sys.exit(app.exec())