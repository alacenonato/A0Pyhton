import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLineEdit, QListWidget, QMessageBox
)

from database import *
from services import nome_valido, telefone_valido

class AgendaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agenda de Contatos")
        self.setGeometry(100, 100, 400, 500)
        
        self.layout = QVBoxLayout()

        # Campos de entrada
        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome")

        self.telefone_input = QLineEdit()
        self.telefone_input.setPlaceholderText("Telefone")

        self.layout.addWidget(self.nome_input)
        self.layout.addWidget(self.telefone_input)

        # Lista de contatos
        self.lista = QListWidget()
        self.layout.addWidget(self.lista)

        # Botões
        botoes_layout = QHBoxLayout()

        self.btn_add = QPushButton("Adicionar")
        self.btn_edit = QPushButton("Editar")
        self.btn_del = QPushButton("Remover")

        botoes_layout.addWidget(self.btn_add)
        botoes_layout.addWidget(self.btn_edit)
        botoes_layout.addWidget(self.btn_del)

        self.layout.addLayout(botoes_layout)

        self.setLayout(self.layout)

        # Eventos
        self.btn_add.clicked.connect(self.adicionar)
        self.btn_edit.clicked.connect(self.editar)
        self.btn_del.clicked.connect(self.remover)
        self.lista.itemClicked.connect(self.carregar_selecionado)

        # Inicializar banco
        criar_tabela()
        self.carregar_lista()

    def carregar_lista(self):
        self.lista.clear()
        contatos = listar_contatos_db()

        for c in contatos:
            self.lista.addItem(f"{c[0]} - {c[1]} - {c[2]}")

    def adicionar(self):
        nome = self.nome_input.text()
        telefone = self.telefone_input.text()

        if not nome_valido(nome) or not telefone_valido(telefone):
            QMessageBox.warning(self, "Erro", "Dados inválidos")
            return

        inserir_contatos(nome, telefone)
        self.carregar_lista()
        self.limpar_campos()

    def editar(self):
        item = self.lista.currentItem()
        if not item:
            return
        
        id = int(item.text().split(" - ")[0])
        nome = self.nome_input.text()
        telefone = self.telefone_input.text()

        if not nome_valido(nome) or not telefone_valido(telefone):
            QMessageBox.warning(self, "Erro", "Dados inválidos")
            return
        
        atualizar_contato(id, nome, telefone)
        self.carregar_lista()
        self.limpar_campos()

    def remover(self):
        item = self.lista.currentItem()
        if not item:
            return
        
        id = int(item.text().split(" - ")[0])

        confirmar = QMessageBox.question(
            self, "Confirm", "Deseja remover? "
        )

        if confirmar == QMessageBox.Yes:
            deletar_contato(id)
            self.carregar_lista()
            self.limpar_campos()
    
    def carregar_selecionado(self, item):
        dados = item.text().split(" - ")
        self.nome_input.setText(dados[1])
        self.telefone_input.setText(dados[2])

    def limpar_campos(self):
        self.nome_input.clear()
        self.telefone_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AgendaApp()
    janela.show()
    sys.exit(app.exec())