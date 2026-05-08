import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLineEdit,
    QListWidget, QLabel, QMessageBox
)

class EstoqueApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simulador de Estoque")
        self.setGeometry(200, 200, 600, 600)

        self.produtos = {}

        layout = QVBoxLayout()

        # Entradas 
        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Nome do produto")

        self.input_qtd = QLineEdit()
        self.input_qtd.setPlaceholderText("Quantidade")

        layout.addWidget(self.input_nome)
        layout.addWidget(self.input_qtd)

        # Lista 
        self.lista = QListWidget()
        layout.addWidget(self.lista)

        # Status
        self.status = QLabel("Total de produtos: 0")
        layout.addWidget(self.status)

        # Botões
        botoes1 = QHBoxLayout()
        botoes2 = QHBoxLayout()

        self.btn_add = QPushButton("Adicionar Produto")
        self.btn_entrada = QPushButton("Entrada")
        self.btn_saida = QPushButton("Saida")

        self.btn_remover = QPushButton("Remover")
        self.btn_atualizar =QPushButton("Atualizar Lista")

        botoes1.addWidget(self.btn_add)
        botoes1.addWidget(self.btn_entrada)
        botoes1.addWidget(self.btn_saida)

        botoes2.addWidget(self.btn_remover)
        botoes2.addWidget(self.btn_atualizar)

        layout.addLayout(botoes1)
        layout.addLayout(botoes2)

        self.setLayout(layout)

        # Eventos
        self.btn_add.clicked.connect(self.adicionar_produto)
        self.btn_entrada.clicked.connect(self.entrada_estoque)
        self.btn_saida.clicked.connect(self.saida_estoque)

        self.btn_remover.clicked.connect(self.remover_produto)
        self.btn_atualizar.clicked.connect(self.atualizar_lista)

    # --------------------------
    def atualizar_status(self):
        total = len(self.produtos)
        self.status.setText(f"Total de produtos: {total}")

    def atualizar_lista(self):
        self.lista.clear()

        for nome, qtd in self.produtos.items():
            self.lista.addItem(f"{nome} - Estoque: {qtd}")

        self.atualizar_status()

    def adicionar_produto(self):
        nome = self.input_nome.text().strip()

        try:
            qtd = int(self.input_qtd.text())
        except:
            QMessageBox.warning(self, "Erro","Quantidade inválida")
            return
        
        if not nome:
            return
        
        if nome in self.produtos:
            QMessageBox.warning(
                self, 
                "Erro",
                "Produto já existe"
            )
            return
        
        self.produtos[nome] = qtd

        self.atualizar_lista()

        self.input_nome.clear()
        self.input_qtd.clear()

    def entrada_estoque(self):
        nome = self.input_nome.text().strip()

        try:
            qtd = int(self.input_qtd.text())
        except:
            QMessageBox.warning(self,"Erro", "Quantidade inválida")
            return
        
        if nome not in self.produtos:
            QMessageBox.warning(
                self, 
                "Erro",
                "Produto não encontrado"

            )
            return
        
        self.produtos[nome] += qtd

        self.atualizar_lista()

    def saida_estoque(self):
        nome = self.input_nome.text().strip()

        try:
            qtd = int(self.input_qtd.text())
        except:
            QMessageBox.warning(self,"Erro", "Quantidade inválida")
            return
        
        if nome not in self.produtos:
            QMessageBox.warning(
                self,
                "Erro",
                "Produto não encontrado"

            )
            return

        if self.produtos[nome] < qtd:
            QMessageBox.warning(
                self, "Erro",
                "Estoque insuficiente"
            )
            return
        
        self.produtos[nome] -= qtd

        self.atualizar_lista()

    def remover_produto(self):
        nome = self.input_nome.text().strip()

        if nome not in self.produtos:
            QMessageBox.warning(
                self,
                "Erro",
                "Produto não encontrado"
            )
            return
        
        del self.produtos[nome]

        self.atualizar_lista()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    janela = EstoqueApp()
    janela.show()

    sys.exit(app.exec())


