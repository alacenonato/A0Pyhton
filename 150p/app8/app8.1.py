import sys
import json
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QListWidget, QLineEdit, QMessageBox, QComboBox,
    QHBoxLayout, QLabel, QDateEdit
)
from PySide6.QtCore import QDate

ARQUIVO = "tarefas.json"


# -----------------------------
# SALVAR / CARREGAR
# -----------------------------
def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)


# -----------------------------
# APP
# -----------------------------
class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List PRO")
        self.setGeometry(200, 200, 600, 500)

        self.tarefas = carregar_tarefas()

        layout = QVBoxLayout()

        # Input tarefa
        self.input = QLineEdit()
        self.input.setPlaceholderText("Digite a tarefa...")
        layout.addWidget(self.input)

        # Prioridade
        self.prioridade = QComboBox()
        self.prioridade.addItems(["Alta 🔴", "Média 🟡", "Baixa 🟢"])
        layout.addWidget(self.prioridade)

        # Data
        self.data = QDateEdit()
        self.data.setDate(QDate.currentDate())
        layout.addWidget(self.data)

        # Botões
        botoes = QHBoxLayout()

        btn_add = QPushButton("Adicionar")
        btn_add.clicked.connect(self.adicionar)
        botoes.addWidget(btn_add)

        btn_concluir = QPushButton("Concluir")
        btn_concluir.clicked.connect(self.concluir)
        botoes.addWidget(btn_concluir)

        btn_remover = QPushButton("Remover")
        btn_remover.clicked.connect(self.remover)
        botoes.addWidget(btn_remover)

        layout.addLayout(botoes)

        # Filtro
        self.filtro = QComboBox()
        self.filtro.addItems(["Todas", "Concluídas", "Pendentes"])
        self.filtro.currentIndexChanged.connect(self.atualizar_lista)
        layout.addWidget(QLabel("Filtro:"))
        layout.addWidget(self.filtro)

        # Lista
        self.lista = QListWidget()
        layout.addWidget(self.lista)

        self.setLayout(layout)

        self.atualizar_lista()

    # -----------------------------
    def adicionar(self):
        try:
            texto = self.input.text().strip()

            if not texto:
                raise ValueError("Tarefa vazia!")

            tarefa = {
                "titulo": texto,
                "concluida": False,
                "prioridade": self.prioridade.currentText(),
                "data": self.data.date().toString("yyyy-MM-dd")
            }

            self.tarefas.append(tarefa)
            salvar_tarefas(self.tarefas)

            self.input.clear()
            self.atualizar_lista()

        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))

    # -----------------------------
    def atualizar_lista(self):
        self.lista.clear()
        filtro = self.filtro.currentText()

        for i, t in enumerate(self.tarefas):
            if filtro == "Concluídas" and not t["concluida"]:
                continue
            if filtro == "Pendentes" and t["concluida"]:
                continue

            status = "✅" if t["concluida"] else "❌"
            texto = f"{i} - {t['titulo']} [{t['prioridade']}] (Até {t['data']}) {status}"
            self.lista.addItem(texto)

    # -----------------------------
    def concluir(self):
        try:
            item = self.lista.currentRow()

            if item < 0:
                raise ValueError("Selecione uma tarefa!")

            self.tarefas[item]["concluida"] = True
            salvar_tarefas(self.tarefas)
            self.atualizar_lista()

        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))

    # -----------------------------
    def remover(self):
        try:
            item = self.lista.currentRow()

            if item < 0:
                raise ValueError("Selecione uma tarefa!")

            self.tarefas.pop(item)
            salvar_tarefas(self.tarefas)
            self.atualizar_lista()

        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))


# -----------------------------
# EXECUÇÃO
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = App()
    janela.show()
    sys.exit(app.exec())