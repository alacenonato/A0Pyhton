import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
QPushButton, QLabel, QSpinBox, QListWidget
)

class DadosApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simulador de Dados")
        self.setGeometry(200, 200, 400, 500)

        layout = QVBoxLayout()

        # Seleção de quantidade de dados
        self.spin = QSpinBox()
        self.spin.setMinimum(1)
        self.spin.setMaximum(6)
        self.spin.setPrefix("Dados: ")
        layout.addWidget(self.spin)

        # Botão rolar
        self.btn_rolar = QPushButton("Rolar Dados")
        layout.addWidget(self.btn_rolar)

        # Resultado
        self.resultado = QLabel("Resultado: -")
        layout.addWidget(self.resultado)

        # Soma
        self.soma = QLabel("Soma: -")
        layout.addWidget(self.soma)

        # Histórico
        self.historico = QListWidget()
        layout.addWidget(self.historico)

        self.setLayout(layout)

        # Evento
        self.btn_rolar.clicked.connect(self.rolar_dados)

    def rolar_dados(self):
        qtd = self.spin.value()
        resultados = [ random.randint(1,6) for _ in range(qtd)]
        soma = sum(resultados)

        # Mostra resultado
        self.resultado.setText(f"Resultado: {resultados}")
        self.soma.setText(f"Soma: {soma}")

        # Histórico
        self.historico.addItem(f"{resultados} - soma: {soma}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = DadosApp()
    janela.show()
    sys.exit(app.exec())




