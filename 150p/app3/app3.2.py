import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)

class Conversor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conversor de Moeda")
        self.setGeometry(100, 100, 400, 400)

        # Widgets
        self.label = QLabel("Digite o valor em reais (R$):")
        self.input_valor = QLineEdit()
        self.botao = QPushButton("Converter")
        self.resultado = QLabel("")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_valor)
        layout.addWidget(self.botao)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

        # Evento
        self.botao.clicked.connect(self.converter)

    def converter(self):
        try:
            valor = float(self.input_valor.text())

            url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL"
            resposta = requests.get(url)
            dados = resposta.json()

            dolar = float(dados["USDBRL"]["bid"])
            euro = float(dados["EURBRL"]["bid"])
            libra = float(dados["GBPBRL"]["bid"])

            texto = (
                f"Dólar: $ {valor / dolar:.2f}\n"
                f"Euro: € {valor / euro:.2f}\n"
                f"Libra: £ {valor / libra:.2f}"
            )

            self.resultado.setText(texto)

        except:
            QMessageBox.critical(self, "Erro", "Digite um valor válido!")

# Rodar app
app = QApplication(sys.argv)
janela = Conversor()
janela.show()
sys.exit(app.exec())