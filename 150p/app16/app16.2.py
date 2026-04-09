import sys
import json
import os
import bcrypt
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QLineEdit, QMessageBox
)

ARQUIVO = "usuarios.json"
MAX_TENTATIVAS = 3

# =========================
# DADOS
# =========================

def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        return {}

    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)

# ========================
# SEGURANÇA (bcrypt)
# ========================
def hash_senha(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode(), salt).decode()

def verificar_senha(senha, hash_salvo):
    return bcrypt.checkpw(senha.encode(),hash_salvo.encode())

# ========================
# APP
# ========================
class LoginApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Login")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Usuário:")
        layout.addWidget(self.label)

        self.input_user = QLineEdit()
        layout.addWidget(self.input_user)

        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_pass.setPlaceholderText("Senha")
        layout.addWidget(self.input_pass)

        btn_login = QPushButton("Login")
        btn_login.clicked.connect(self.login)
        layout.addWidget(btn_login)

        btn_cadastrar = QPushButton("Cadastrar")
        btn_cadastrar.clicked.connect(self.cadastrar)
        layout.addWidget(btn_cadastrar)

        self.setLayout(layout)

    def cadastrar(self):
        usuario = self.input_user.text()
        senha = self.input_pass.text()

        if not usuario or not senha:
            QMessageBox.warning(self, "Erro", "Preencha tudo!")
            return

        usuarios = carregar_usuarios()

        if usuario in usuarios:
            QMessageBox.warning(self, "Erro", "Usuário já existe!!")
            return
        
        usuarios[usuario] = {
            "senha": hash_senha(senha),
            "admin": False
        }

        salvar_usuarios(usuarios)
        QMessageBox.information(self, "Ok", "Usuário cadastrado!")

    def login(self):
        usuario = self.input_user.text()
        senha = self.input_pass.text()

        usuarios = carregar_usuarios()

        if usuario not in usuarios:
            QMessageBox.warning(self, "Erro", "Usuário não existe!")
            return

        if verificar_senha(senha, usuarios[usuario]["senha"]):
            QMessageBox.information(self, "Sucesso", "Login Ok!")

            if usuarios[usuario]["admin"]:
                self.abrir_admin()
            
        else:
            QMessageBox.warning(self, "Erro", "Senha incorreta!")

    def abrir_admin(self):
        self.admin = AdminPanel()
        self.admin.show()

class AdminPanel(QWidget):
    def __int__(self):
        super().__init__()

        self.setWindowTitle("Painel Admin")
        self.resize(300, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Usuários cadastrados:")
        layout.addWidget(self.label)

        self.lista = QLabel("")
        layout.addWidget(self.lista)

        btn_listar = QPushButton("Listar usuários")
        btn_listar.clicked.connect(self.listar)
        layout.addWidget(btn_listar)

        btn_reset = QPushButton("Resetar usuários")
        btn_reset.clicked.connect(self.resetar)
        layout.addWidget(btn_reset)

        self.setLayout(layout)

    def listr(self):
        usuarios = carregar_usuarios()

        if not usuarios:
            self.lista.setText("Nenhum usuário.")
            return

        texto = "\n".join(usuarios.keys())
        self.lista.setText(texto)

    def resetar(self):
        salvar_usuarios({})
        self.lista.setText("")
        QMessageBox.information(self, "OK", "Usuários removidos!")


# ==============================
# CRIAR ADMIN PADRÃO
# ==============================
def criar_admin():
    usuarios = carregar_usuarios()

    if "admin" not in usuarios:
        usuarios["admin"] = {
            "senha": hash_senha("admin123"),
            "admin": True
        }

        salvar_usuarios(usuarios)

# =============================
# EXECUÇÃO
# =============================
if __name__ == "__main__":
    criar_admin()

    app = QApplication(sys.argv)
    janela = LoginApp()
    janela.show()

    sys.exit(app.exec())
