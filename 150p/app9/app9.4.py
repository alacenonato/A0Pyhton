import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QMessageBox
)


class TabuadaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Tabuada")
        self.setGeometry(300, 200, 500, 400)

        self.layout = QVBoxLayout()

        # Inputs
        self.numero_input = QLineEdit()
        self.numero_input.setPlaceholderText("Número (opcional p/ tabuada completa)")

        self.inicio_input = QLineEdit()
        self.inicio_input.setPlaceholderText("Início")

        self.fim_input = QLineEdit()
        self.fim_input.setPlaceholderText("Fim")

        self.layout.addWidget(QLabel("Digite os valores:"))
        self.layout.addWidget(self.numero_input)
        self.layout.addWidget(self.inicio_input)
        self.layout.addWidget(self.fim_input)

        # Botões
        botoes_layout = QHBoxLayout()

        self.btn_gerar = QPushButton("Gerar Tabuada")
        self.btn_gerar.clicked.connect(self.gerar_tabuada)

        self.btn_completa = QPushButton("Tabuada Completa")
        self.btn_completa.clicked.connect(self.tabuada_completa)

        self.btn_limpar = QPushButton("Limpar")
        self.btn_limpar.clicked.connect(self.limpar_tabela)

        botoes_layout.addWidget(self.btn_gerar)
        botoes_layout.addWidget(self.btn_completa)
        botoes_layout.addWidget(self.btn_limpar)

        self.layout.addLayout(botoes_layout)

        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(2)
        self.tabela.setHorizontalHeaderLabels(["Operação", "Resultado"])

        self.layout.addWidget(self.tabela)

        self.setLayout(self.layout)

    def validar_inputs(self):
        try:
            inicio = int(self.inicio_input.text())
            fim = int(self.fim_input.text())

            if inicio > fim:
                raise ValueError

            return inicio, fim
        except:
            QMessageBox.warning(self, "Erro", "Digite valores válidos para início e fim.")
            return None, None

    def gerar_tabuada(self):
        inicio, fim = self.validar_inputs()
        if inicio is None:
            return

        try:
            numero = int(self.numero_input.text())
        except:
            QMessageBox.warning(self, "Erro", "Digite um número válido.")
            return

        self.tabela.setRowCount(0)

        for i in range(inicio, fim + 1):
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)

            self.tabela.setItem(row, 0, QTableWidgetItem(f"{numero} x {i}"))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(numero * i)))

    def tabuada_completa(self):
        inicio, fim = self.validar_inputs()
        if inicio is None:
            return

        self.tabela.setRowCount(0)

        for n in range(1, 11):
            for i in range(inicio, fim + 1):
                row = self.tabela.rowCount()
                self.tabela.insertRow(row)

                self.tabela.setItem(row, 0, QTableWidgetItem(f"{n} x {i}"))
                self.tabela.setItem(row, 1, QTableWidgetItem(str(n * i)))

    def limpar_tabela(self):
        self.tabela.setRowCount(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TabuadaApp()
    janela.show()
    sys.exit(app.exec())