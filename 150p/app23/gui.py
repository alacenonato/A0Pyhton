import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QLineEdit, QLabel,
    QListWidget, QMessageBox
)

class votacaoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Votação")
        self.setGeometry(200, 200, 500, 600)

        self.candidatos = {}

        layout = QVBoxLayout()

        # Campo candidato
        self.input_candidato = QLineEdit()
        self.input_candidato.setPlaceholderText("Nome do candidato)")
        layout.addWidget(self.input_candidato)

        # Botões
        self.btn_add = QPushButton("Adicionar candidato")
        self.btn_votar = QPushButton("Votar")
        self.btn_resultado = QPushButton("Mostrar resultado")
        self.btn_vencedor = QPushButton("Mostrar vencedor")

        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_votar)
        layout.addWidget(self.btn_resultado)
        layout.addWidget(self.btn_vencedor)

        # Lista
        self.lista = QListWidget()
        layout.addWidget(self.lista)

        # Resultado 
        self.resultado = QLabel("Resultado aparecerã aqui")
        layout.addWidget(self.resultado)

        self.setLayout(layout)

        # Eventos
        self.btn_add.clicked.connect(self.adicionar_candidato)
        self.btn_votar.clicked.connect(self.votar)
        self.btn_resultado.clicked.connect(self.mostrar_resultado)
        self.btn_vencedor.clicked.connect(self.mostrar_vencedor)

    ############

    def adicionar_candidato(self):
        nome = self.input_candidato.text().strip()

        if not nome:
            return
        
        if nome in self.candidatos:
            QMessageBox.warning(self, "Erro", "Candidato já exite")
            return

        self.candidatos[nome] = 0

        self.lista.addItem(nome)
        self.input_candidato.clear()

    def votar(self):
        item = self.lista.currentItem()

        if not item:
            QMessageBox.warning(self, "Erro", "Selecione um candidato")
            return

        nome = item.text()

        self.candidatos[nome] += 1

        self.resultado.setText(f"Voto computado para {nome}")

    def mostrar_resultado(self):
        if not self.candidatos:
            self.resultado.setText("Nenhum candidato")
            return
        
        texto = "Resultado:\n"

        for nome, votos in self.candidatos.items():
            texto += f"{nome}: {votos} voto(s)\n"

        self.resultado.setText(texto)

    def mostrar_vencedor(self):
        if not self.candidatos:
            return
        
        vencedor = max(self.candidatos, key=self.candidatos.get)
        votos = self.candidatos[vencedor]

        self.resultado.setText(
            f"Vencedor: {vencedor} ({votos} votos)"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)

    janela = votacaoApp()
    janela.show()
    sys.exit(app.exec())


