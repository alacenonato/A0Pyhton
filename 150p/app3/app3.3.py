import sys
import requests
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QComboBox, QMessageBox, QTextEdit
)
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon

from openpyxl import Workbook
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class Conversor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conversor PRO")
        self.setGeometry(100, 100, 400, 500)

        # === Widgets ===
        self.label = QLabel("Valor em reais (R$):")
        self.input_valor = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(["USD", "EUR", "GBP"])

        self.botao = QPushButton("Converter")

        self.resultado = QLabel("")
        self.historico = QTextEdit()
        self.historico.setReadOnly(True)

        self.btn_excel = QPushButton("Exportar Excel")
        self.btn_pdf = QPushButton("Exportar PDF")

        # === Layout ===
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_valor)
        layout.addWidget(self.combo)
        layout.addWidget(self.botao)
        layout.addWidget(self.resultado)
        layout.addWidget(QLabel("Histórico:"))
        layout.addWidget(self.historico)
        layout.addWidget(self.btn_excel)
        layout.addWidget(self.btn_pdf)

        self.setLayout(layout)

        # === Eventos ===
        self.botao.clicked.connect(self.converter)
        self.btn_excel.clicked.connect(self.exportar_excel)
        self.btn_pdf.clicked.connect(self.exportar_pdf)

        # === Timer (auto atualização) ===
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_cotacao)
        self.timer.start(10000)  # 10 segundos

        self.cotacoes = {}

        # Tema escuro
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: white;
                font-size: 14px;
            }
            QPushButton {
                background-color: #1f1f1f;
                border: 1px solid #333;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #333;
            }
            QLineEdit {
                background-color: #1f1f1f;
                border: 1px solid #333;
            }
        """)

        self.atualizar_cotacao()

    def atualizar_cotacao(self):
        try:
            url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL"
            resposta = requests.get(url)
            dados = resposta.json()

            self.cotacoes = {
                "USD": float(dados["USDBRL"]["bid"]),
                "EUR": float(dados["EURBRL"]["bid"]),
                "GBP": float(dados["GBPBRL"]["bid"])
            }

        except:
            pass

    def converter(self):
        try:
            valor = float(self.input_valor.text())
            moeda = self.combo.currentText()

            cotacao = self.cotacoes.get(moeda)

            if not cotacao:
                raise Exception("Cotação não disponível")

            convertido = valor / cotacao

            texto = f"{moeda}: {convertido:.2f}"
            self.resultado.setText(texto)

            # Histórico
            registro = f"{datetime.now().strftime('%H:%M:%S')} - R$ {valor} → {texto}"
            self.historico.append(registro)

        except:
            QMessageBox.critical(self, "Erro", "Valor inválido!")

    def exportar_excel(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "Histórico"

        linhas = self.historico.toPlainText().split("\n")

        for i, linha in enumerate(linhas, start=1):
            ws[f"A{i}"] = linha

        wb.save("historico.xlsx")

        QMessageBox.information(self, "Sucesso", "Exportado para Excel!")

    def exportar_pdf(self):
        doc = SimpleDocTemplate("historico.pdf")
        styles = getSampleStyleSheet()

        conteudo = []

        linhas = self.historico.toPlainText().split("\n")

        for linha in linhas:
            conteudo.append(Paragraph(linha, styles["Normal"]))

        doc.build(conteudo)

        QMessageBox.information(self, "Sucesso", "Exportado para PDF!")


# === Executar app ===
app = QApplication(sys.argv)

# Ícone (opcional)
# app.setWindowIcon(QIcon("icone.png"))

janela = Conversor()
janela.show()

sys.exit(app.exec())