import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, 
    QHBoxLayout, QPushButton, QLineEdit,
    QListWidget, QLabel, QMessageBox
)

class OrganiadorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Organizador de Lista")
        self.setGeometry(200, 200, 500, 600)

        layout = QVBoxLayout()

        # Entrada
        self.input_item = QLineEdit()
        self.input_item.setPlaceholderText("Digite um ittem")
        layout.addWidget(self.input_item)

        # Lista
        self.lista = QListWidget()
        layout.addWidget(self.lista)

        # Resultado / status
        self.status = QLabel("Total: 0 itens")
        layout.addWidget(self.status)

        # Botões
        botoes1 = QHBoxLayout()
        botoes2 = QHBoxLayout()

        self.btn_add = QPushButton("Adicionar")
        self.btn_remover = QPushButton("Remover")
        self.btn_buscar =QPushButton("Buscar")

        self.btn_az = QPushButton("Ordenar A-Z")
        self.btn_za = QPushButton("Ordenar Z-A")
        self.btn_limpar = QPushButton("Limpar")

        botoes1.addWidget(self.btn_add)
        botoes1.addWidget(self.btn_remover)
        botoes1.addWidget(self.btn_buscar)

        botoes2.addWidget(self.btn_az)
        botoes2.addWidget(self.btn_za)
        botoes2.addWidget(self.btn_limpar)

        layout.addLayout(botoes1)
        layout.addLayout(botoes2)

        self.setLayout(layout)

        # Eventos
        self.btn_add.clicked.connect(self.adicionar)
        self.btn_remover.clicked.connect(self.remover)
        self.btn_buscar.clicked .connect(self.buscar)

        self.btn_az.clicked.connect(self.ordenar_az)
        self.btn_za.clicked.connect(self.ordenar_za)
        self.btn_limpar.clicked.connect(self.limpar)

    def atualizar_total(self):
        total = self.lista.count()
        self.status.setText(f"Total: {total} itens")

    def adicionar(self):
        item = self.input_item.text().strip()

        if not item:
            return
        
        self.lista.addItem(item)
        self.input_item.clear()

        self. atualizar_total()

    def remover(self):
        item = self.lista.currentItem()

        if not item:
            QMessageBox.warning(self, "Erro", "Selecione um item")
            return
        
        self.lista.takeItem(self.lista.row(item))

        self.atualizar_total()

    def buscar(self):
        texto = self.input_item.text().strip().lower()

        if not texto:
            return
        
        encontrados = self.lista.findItems(
            "",
            Qt.MatchContains
        )

        achou = False

        for item in encontrados:
            if texto in item.text().lower():
                item.setSelected(True)
                achou = True

        if not achou:
            QMessageBox.information(
                self,
                "Buscar",
                "Nenhum item encontrado"
            )

    def ordenar_az(self):
        self.lista.sortItems()

    def ordenar_za(self):
        itens = []

        for i in range(self.lista.count()):
            itens.append(self.lista.item(i).text())

        itens.sort(reverse=True)

        self.lista.clear()

        for item in itens:
            self.lista.addItem(item)

    def limpar(self):
        self.lista.clear()
        self.atualizar_total()

# IMPORTANTE
from PySide6.QtCore import Qt

if __name__ == "__main__":
    app = QApplication(sys.argv)

    janela = OrganiadorApp()
    janela.show()

    sys.exit(app.exec())

