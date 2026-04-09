Bora — Projeto 16 é onde começa a ficar **mais próximo de sistema real** 👇

---

# 🔐 Projeto 16 — Simulador de Login (Nível Profissional)

## 🎯 Objetivo real

Você não vai só validar usuário/senha.

Você vai aprender:

* autenticação básica
* hash de senha (segurança)
* persistência (JSON)
* estrutura de sistema de usuários

👉 Isso aqui já é base de:

* sistemas web
* APIs
* apps reais

---

# 🚀 Versão PROFISSIONAL (com segurança básica)

## ✅ O que tem:

* Cadastro de usuário
* Login
* Senha criptografada (hash)
* Salvamento em JSON
* Tratamento de erros
* Estrutura organizada

---

# 💻 Código completo

```python
import json
import os
import hashlib

ARQUIVO = "usuarios.json"

# =========================
# UTIL
# =========================

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        return {}

    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)


# =========================
# SISTEMA
# =========================

def cadastrar():
    usuarios = carregar_usuarios()

    print("\n=== CADASTRO ===")
    usuario = input("Usuário: ")

    if usuario in usuarios:
        print("❌ Usuário já existe!")
        return

    senha = input("Senha: ")
    senha_hash = hash_senha(senha)

    usuarios[usuario] = senha_hash
    salvar_usuarios(usuarios)

    print("✅ Usuário cadastrado com sucesso!")


def login():
    usuarios = carregar_usuarios()

    print("\n=== LOGIN ===")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    senha_hash = hash_senha(senha)

    if usuario in usuarios and usuarios[usuario] == senha_hash:
        print("✅ Login bem-sucedido!")
    else:
        print("❌ Usuário ou senha inválidos!")


# =========================
# MENU
# =========================

def menu():
    while True:
        print("\n====== MENU ======")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida!")


# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    menu()
```

---

# 🧠 O que você aprendeu aqui

* ✔ Hash de senha (`sha256`)
* ✔ Persistência com JSON
* ✔ Estrutura de autenticação
* ✔ Validação de usuário

👉 Isso já é base de backend.

---

# ⚠️ Verdade importante (nível profissional)

Esse sistema ainda NÃO é seguro de verdade, porque:

* não tem salt
* não usa bcrypt
* não tem proteção contra ataque

👉 Mas está PERFEITO para seu nível atual.

---

# 🔥 Evolução (FAZ ISSO PRA SUBIR DE NÍVEL)

## 💡 1. Melhorar segurança

Use:

```bash
pip install bcrypt
```

---

## 💡 2. Adicionar:

* confirmação de senha
* ocultar senha (getpass)
* limite de tentativas

---

## 💡 3. Sistema mais completo:

* editar senha
* deletar usuário
* listar usuários (admin)

---

## 💣 DESAFIO (IMPORTANTE)

Transforma isso em:

👉 Interface gráfica com PySide6 (igual você fez no projeto anterior)

---

# 🚀 Próximo passo

Me fala:

👉 “Quero versão com PySide6”
👉 “Quero versão com bcrypt (segurança real)”
👉 “Vamos pro projeto 17”

Se você fizer esse projeto bem feito, já começa a pensar como backend dev 🔥

---
---
---
---
Perfeito — agora sim você está entrando no **nível profissional de verdade** 🔥
Esse aqui já parece **sistema real de autenticação (CLI)**.

Vou te entregar uma versão com:

✅ Confirmação de senha
✅ Senha oculta (`getpass`)
✅ Limite de tentativas
✅ Editar senha
✅ Deletar usuário
✅ Listar usuários (modo admin)
✅ Código organizado

---

# 🔐 Sistema de Login PROFISSIONAL (CLI)

```python
import json
import os
import hashlib
import getpass

ARQUIVO = "usuarios.json"
MAX_TENTATIVAS = 3

# =========================
# UTIL
# =========================

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        return {}

    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)


# =========================
# SISTEMA
# =========================

def cadastrar():
    usuarios = carregar_usuarios()

    print("\n=== CADASTRO ===")
    usuario = input("Usuário: ")

    if usuario in usuarios:
        print("❌ Usuário já existe!")
        return

    senha = getpass.getpass("Senha: ")
    confirmar = getpass.getpass("Confirmar senha: ")

    if senha != confirmar:
        print("❌ Senhas não coincidem!")
        return

    usuarios[usuario] = hash_senha(senha)
    salvar_usuarios(usuarios)

    print("✅ Usuário cadastrado com sucesso!")


def login():
    usuarios = carregar_usuarios()

    print("\n=== LOGIN ===")
    usuario = input("Usuário: ")

    tentativas = 0

    while tentativas < MAX_TENTATIVAS:
        senha = getpass.getpass("Senha: ")
        senha_hash = hash_senha(senha)

        if usuario in usuarios and usuarios[usuario] == senha_hash:
            print("✅ Login bem-sucedido!")
            return usuario
        else:
            tentativas += 1
            print(f"❌ Tentativa {tentativas}/{MAX_TENTATIVAS}")

    print("🚫 Acesso bloqueado!")
    return None


def editar_senha():
    usuarios = carregar_usuarios()

    print("\n=== ALTERAR SENHA ===")
    usuario = input("Usuário: ")

    if usuario not in usuarios:
        print("❌ Usuário não encontrado!")
        return

    senha_atual = getpass.getpass("Senha atual: ")

    if usuarios[usuario] != hash_senha(senha_atual):
        print("❌ Senha incorreta!")
        return

    nova = getpass.getpass("Nova senha: ")
    confirmar = getpass.getpass("Confirmar nova senha: ")

    if nova != confirmar:
        print("❌ Senhas não coincidem!")
        return

    usuarios[usuario] = hash_senha(nova)
    salvar_usuarios(usuarios)

    print("✅ Senha alterada com sucesso!")


def deletar_usuario():
    usuarios = carregar_usuarios()

    print("\n=== DELETAR USUÁRIO ===")
    usuario = input("Usuário: ")

    if usuario not in usuarios:
        print("❌ Usuário não encontrado!")
        return

    confirmacao = input("Tem certeza? (s/n): ").lower()

    if confirmacao == "s":
        del usuarios[usuario]
        salvar_usuarios(usuarios)
        print("🗑️ Usuário deletado!")
    else:
        print("Cancelado.")


def listar_usuarios():
    usuarios = carregar_usuarios()

    print("\n=== LISTA DE USUÁRIOS ===")

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for user in usuarios.keys():
        print(f"- {user}")


# =========================
# MENU
# =========================

def menu():
    while True:
        print("\n====== MENU ======")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Alterar senha")
        print("4 - Deletar usuário")
        print("5 - Listar usuários (admin)")
        print("6 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            editar_senha()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "5":
            listar_usuarios()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida!")


# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    menu()
```

---

# 🧠 O que você acabou de construir

Isso aqui já é **muito acima da média**:

* ✔ Sistema de autenticação completo (CLI)
* ✔ Segurança básica com hash
* ✔ Controle de tentativas
* ✔ CRUD de usuários
* ✔ Boas práticas de validação

👉 Isso já é base de:

* sistemas web (Django/Flask)
* APIs REST
* sistemas corporativos

---

# ⚠️ Crítica importante (pra você evoluir mais)

Isso ainda pode melhorar:

❌ Senha sem salt
❌ Não usa bcrypt
❌ Qualquer um pode listar usuários (sem admin real)

👉 Próximo nível = corrigir isso

---

# 🔥 Próximo upgrade (RECOMENDADO)

Se quiser ficar MUITO forte:

👉 Posso te ajudar a fazer:

* 🔐 versão com **bcrypt (segurança real)**
* 🖥️ versão com **PySide6 (interface gráfica)**
* 🌐 versão com **Flask (login web real)**

---

# 🚀 Próximo passo

Me fala:

👉 **“Quero versão com PySide6”**
👉 **“Quero segurança com bcrypt”**
👉 **“Vamos pro projeto 17”**

Você já tá começando a pensar como backend de verdade 🔥
---
---
---
---
Perfeito. Agora você entrou no **nível realmente profissional** 🔥
Vamos corrigir **tudo que faltava**:

---

# 🚀 O que vou implementar pra você

## 🔐 Segurança REAL

✅ Senha com **bcrypt (hash + salt automático)**
✅ Proteção contra ataques simples
✅ Comparação segura

## 👤 Controle de acesso

✅ Usuário **admin real**
✅ Só admin pode listar usuários

## 🖥️ Interface gráfica

✅ PySide6
✅ Login + Cadastro
✅ Painel diferente para admin

---

# 📦 Instalação

```bash
pip install PySide6 bcrypt
```

---

# 🔐 + 🖥️ Sistema completo (PROFISSIONAL)

```python
import sys
import json
import os
import bcrypt

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QLineEdit, QMessageBox
)

ARQUIVO = "usuarios.json"

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


# =========================
# SEGURANÇA (bcrypt)
# =========================

def hash_senha(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode(), salt).decode()


def verificar_senha(senha, hash_salvo):
    return bcrypt.checkpw(senha.encode(), hash_salvo.encode())


# =========================
# APP
# =========================

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
            QMessageBox.warning(self, "Erro", "Usuário já existe!")
            return

        usuarios[usuario] = {
            "senha": hash_senha(senha),
            "admin": False
        }

        salvar_usuarios(usuarios)
        QMessageBox.information(self, "OK", "Usuário cadastrado!")

    def login(self):
        usuario = self.input_user.text()
        senha = self.input_pass.text()

        usuarios = carregar_usuarios()

        if usuario not in usuarios:
            QMessageBox.warning(self, "Erro", "Usuário não existe!")
            return

        if verificar_senha(senha, usuarios[usuario]["senha"]):
            QMessageBox.information(self, "Sucesso", "Login OK!")

            if usuarios[usuario]["admin"]:
                self.abrir_admin()
        else:
            QMessageBox.warning(self, "Erro", "Senha incorreta!")

    def abrir_admin(self):
        self.admin = AdminPanel()
        self.admin.show()


class AdminPanel(QWidget):
    def __init__(self):
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

    def listar(self):
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


# =========================
# CRIAR ADMIN PADRÃO
# =========================

def criar_admin():
    usuarios = carregar_usuarios()

    if "admin" not in usuarios:
        usuarios["admin"] = {
            "senha": hash_senha("admin123"),
            "admin": True
        }
        salvar_usuarios(usuarios)


# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    criar_admin()

    app = QApplication(sys.argv)
    janela = LoginApp()
    janela.show()
    sys.exit(app.exec())
```

---

# 🔥 O que você acabou de construir

Isso aqui já é **nível sistema real**:

* 🔐 Segurança com bcrypt (igual backend real)
* 👤 Controle de acesso (admin vs usuário)
* 🖥️ Interface gráfica moderna
* 📁 Persistência em JSON
* 🧠 Estrutura orientada a objetos

👉 Isso já parece projeto de portfólio sério.

---

# 🔑 Login padrão

Quando rodar:

```
Usuário: admin
Senha: admin123
```

---

# 🚀 Próximo nível (se quiser virar absurdo)

Posso te ajudar a evoluir isso pra:

### 💣 nível MUITO alto:

* editar senha na GUI
* deletar usuário na GUI
* sistema de sessão (logout)
* tela separada (login → dashboard)
* salvar logs de acesso
* transformar em **.deb instalável no Linux**

---

# 🎯 Próximo passo

Me fala:

👉 **“quero melhorar a interface (design profissional)”**
👉 **“quero transformar em .deb instalável”**
👉 **“vamos pro projeto 17”**

Agora você já tá construindo coisa de DEV de verdade 🔥
