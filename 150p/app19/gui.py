import sys
import json
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QListView, QLabel, QMessageBox, QListWidget
)

ARQUIVO = "dados.json"

class SorteadoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFilePath("Sorteador de Nomes")
        self.setGeometry(200, 200, 400, 500)

        self.layout = QVBoxLayout()

        # Campo de entrada
        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Digite um nome: ")
        self.layout.addWidget(self.input_nome)

        # lista
        self.lista = QListWidget()
        self.layout.addWidget(self.lista)

        # Resultado
        self.resultado = QLabel("Resultado apareceŕa aqui")
        self.layout.addWidget(self.resultado)

        # Botões

        botoes = QHBoxLayout()
        self.btn_add = QPushButton("Adicionar")
        self.btn_sortear = QPushButton("Sortear 1")
        self.btn_sortear_varios = QPushButton("Sortear vários")
        self.btn_limpar = QPushButton("Limpar")

        botoes.addWidget(self.btn_add)
        botoes.addWidget(self.btn_sortear)
        botoes.addWidget(self.btn_sortear_varios)
        botoes.addWidget(self.btn_limpar)

        self.layout.addLayout(botoes)

        self.setLayout(self.layout)

        # Eventos
        self.btn_add.clicked.connect(self.adicionar)
        self.btn_sortear.clicked.connect(self.sortear_um)
        self.btn_sortear_varios.clicked.connect(self.sortear_varios)
        self.btn_limpar.clicked.connect(self.limpar_lista)

        # Dados
        self.nomes = []
        self.carregar()
        
    # --- Funções ----

    def adicionar(self):
        nome = self.input_nome.text().strip()

        if not nome:
            return
        
        if nome in self.nomes:
            QMessageBox.warning(self, "Erro", "Nome já existe!")
            return

        self.nomes.append(nome)
        self.lista.addItem(nome)
        self.input_nome.clear()
        self.salvar()

    def sortear_um(self):
        if not self.nomes:
            QMessageBox.warning(self, "Erro", "Lista vazia")
            return
        
        sorteado = random.choice(self.nomes)
        self.resultado.setText(f"{sorteado}")

    def sortear_varios(self):
        if not self.nomes:
            return
        
        try:
            qtd = int(self.input_nome.text())
        except:
            QMessageBox.warning(self, "Erro", "Digite um número no campo")
            return

        if qtd > len(self.nomes):
            QMessageBox.warning(self, "Erro","Quantidade maior que a lista")
            return
        
        sorteados = random.sample(self.nomes, qtd)
        self.resultado.setText("🎉 " + ", ".join(sorteados))

    def limpar_lista(self):
        self.nomes = []
        self.lista.clear()
        self.salvar()
        self.resultado.setText("Lista limpa")

    # --- JSON ---
    def salvar(self):
        with open(ARQUIVO, "w") as f:
            json.dump(self.nomes, f)

    def carregar(self):
        try:
            with open(ARQUIVO, "r") as f:
                self.nomes = json.load()
                for nome in self.nomes:
                    self.lista.addItem(nome)
        except:
            self.nomes = []
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = SorteadoApp()
    janela.show()
    sys.exit(app.exec())
