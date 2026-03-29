import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QLineEdit, QMessageBox, QListWidget
)

# ===== DADOS =====
saldo = 1000.0
senha_correta = "1234"
extrato = []
limite_saque_diario = 500.0
saque_realizado_hoje = 0.0


# ===== TELA PRINCIPAL =====
class CaixaEletronico(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caixa Eletrônico")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()

        self.label_saldo = QLabel(f"Saldo: R$ {saldo:.2f}")
        self.layout.addWidget(self.label_saldo)

        self.btn_depositar = QPushButton("Depositar")
        self.btn_sacar = QPushButton("Sacar")
        self.btn_extrato = QPushButton("Ver Extrato")

        self.layout.addWidget(self.btn_depositar)
        self.layout.addWidget(self.btn_sacar)
        self.layout.addWidget(self.btn_extrato)

        self.extrato_lista = QListWidget()
        self.layout.addWidget(self.extrato_lista)

        self.setLayout(self.layout)

        # Eventos
        self.btn_depositar.clicked.connect(self.depositar)
        self.btn_sacar.clicked.connect(self.sacar)
        self.btn_extrato.clicked.connect(self.mostrar_extrato)

    def atualizar_saldo(self):
        self.label_saldo.setText(f"Saldo: R$ {saldo:.2f}")

    def depositar(self):
        global saldo

        valor, ok = self.get_valor("Depósito")
        if not ok:
            return

        if valor <= 0:
            self.alerta("Valor inválido!")
            return

        saldo += valor
        extrato.append(f"Depósito: +R$ {valor:.2f}")

        self.atualizar_saldo()
        self.alerta("Depósito realizado!")

    def sacar(self):
        global saldo, saque_realizado_hoje

        valor, ok = self.get_valor("Saque")
        if not ok:
            return

        if valor <= 0:
            self.alerta("Valor inválido!")
            return

        if valor > saldo:
            self.alerta("Saldo insuficiente!")
            return

        if saque_realizado_hoje + valor > limite_saque_diario:
            self.alerta("Limite diário atingido!")
            return

        saldo -= valor
        saque_realizado_hoje += valor

        extrato.append(f"Saque: -R$ {valor:.2f}")

        self.atualizar_saldo()
        self.alerta("Saque realizado!")

    def mostrar_extrato(self):
        self.extrato_lista.clear()
        for item in extrato:
            self.extrato_lista.addItem(item)

    def get_valor(self, titulo):
        from PySide6.QtWidgets import QInputDialog
        valor, ok = QInputDialog.getDouble(self, titulo, "Digite o valor:")
        return valor, ok

    def alerta(self, msg):
        QMessageBox.information(self, "Info", msg)


# ===== TELA DE LOGIN =====
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Digite a senha:")
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Entrar")

        layout.addWidget(self.label)
        layout.addWidget(self.input_senha)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

        self.tentativas = 3

        self.btn_login.clicked.connect(self.verificar_login)

    def verificar_login(self):
        senha = self.input_senha.text()

        if senha == senha_correta:
            self.caixa = CaixaEletronico()
            self.caixa.show()
            self.close()
        else:
            self.tentativas -= 1
            QMessageBox.warning(self, "Erro", f"Senha incorreta! Restam {self.tentativas}")

            if self.tentativas == 0:
                QMessageBox.critical(self, "Bloqueado", "Conta bloqueada!")
                self.close()


# ===== EXECUÇÃO =====
app = QApplication(sys.argv)

login = Login()
login.show()

sys.exit(app.exec())