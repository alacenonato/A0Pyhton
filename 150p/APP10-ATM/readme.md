Perfeito. Projeto 10 é **excelente** pra dar um salto de lógica e começar a pensar como sistema real.

---

# 💳 Projeto 10 — Simulador de Caixa Eletrônico (ATM)

## 🎯 Objetivo

Criar um sistema que simula um caixa eletrônico com:

* Login
* Consulta de saldo
* Depósito
* Saque
* Extrato simples

---

# 🧠 O que você vai aprender aqui

* Estruturas de decisão (`if/else`)
* Laços de repetição (`while`)
* Funções
* Validação de dados
* Organização de código

---

# 🏗️ Como o sistema vai funcionar

Fluxo:

1. Usuário faz login (senha simples)
2. Entra em um menu:

   * Ver saldo
   * Depositar
   * Sacar
   * Ver extrato
   * Sair

---

# 🪜 PASSO A PASSO (MENTORIA)

## 🔹 Passo 1 — Estrutura inicial

Comece com variáveis básicas:

```python
saldo = 1000
senha_correta = "1234"
extrato = []
```

---

## 🔹 Passo 2 — Login

```python
senha = input("Digite sua senha: ")

if senha != senha_correta:
    print("Senha incorreta!")
    exit()
```

---

## 🔹 Passo 3 — Menu principal

```python
while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")
```

---

## 🔹 Passo 4 — Ver saldo

```python
if opcao == "1":
    print(f"Seu saldo é: R$ {saldo}")
```

---

## 🔹 Passo 5 — Depósito

```python
elif opcao == "2":
    valor = float(input("Digite o valor para depósito: "))
    saldo += valor
    extrato.append(f"Depósito: +R$ {valor}")
    print("Depósito realizado!")
```

---

## 🔹 Passo 6 — Saque

```python
elif opcao == "3":
    valor = float(input("Digite o valor para saque: "))

    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor}")
        print("Saque realizado!")
```

---

## 🔹 Passo 7 — Extrato

```python
elif opcao == "4":
    print("\n=== EXTRATO ===")
    for item in extrato:
        print(item)
```

---

## 🔹 Passo 8 — Sair

```python
elif opcao == "5":
    print("Saindo...")
    break
```

---

# ✅ Versão completa (junta tudo)

```python
saldo = 1000
senha_correta = "1234"
extrato = []

senha = input("Digite sua senha: ")

if senha != senha_correta:
    print("Senha incorreta!")
    exit()

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Seu saldo é: R$ {saldo}")

    elif opcao == "2":
        valor = float(input("Digite o valor para depósito: "))
        saldo += valor
        extrato.append(f"Depósito: +R$ {valor}")
        print("Depósito realizado!")

    elif opcao == "3":
        valor = float(input("Digite o valor para saque: "))

        if valor > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor
            extrato.append(f"Saque: -R$ {valor}")
            print("Saque realizado!")

    elif opcao == "4":
        print("\n=== EXTRATO ===")
        for item in extrato:
            print(item)

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
```

---

# 🔥 DESAFIOS (OBRIGATÓRIO PRA EVOLUIR)

Agora vem o que te faz crescer de verdade:

## 🟡 Nível 1

* Não permitir depósito negativo
* Não permitir saque negativo

## 🟡 Nível 2

* Limite de saque diário
* Mostrar saldo após cada operação

## 🟡 Nível 3

* Permitir 3 tentativas de senha
* Bloquear após erro

## 🟡 Nível 4 (🔥 importante)

* Salvar extrato em arquivo `.txt`

---

# 💡 MELHORIA (NÍVEL MERCADO)

Transforma esse projeto em algo profissional:

* Criar funções:

  * `depositar()`
  * `sacar()`
  * `ver_saldo()`
* Organizar código
* Separar lógica

---

# 🚀 PRÓXIMO PASSO

Se você quiser evoluir muito:

👉 Posso te ajudar a transformar isso em:

* Sistema bancário com múltiplos usuários
* Banco de dados (SQLite)
* API com Flask

---

Se quiser continuar comigo:

👉 **“Projeto 11 com mentor”**
ou
👉 **“Quero melhorar esse projeto nível profissional”**

que eu te levo pro próximo nível 🔥

# MAIS E MAIS

Boa decisão — agora você saiu do nível iniciante e já está entrando no **nível profissional de verdade**.

Vou te entregar o **Projeto 10 completo + todos os desafios implementados**, organizado como um sistema melhor estruturado.

---

# 💳 Simulador de Caixa Eletrônico (VERSÃO COMPLETA)

## ✅ O que essa versão tem

✔ Login com 3 tentativas (bloqueio)
✔ Depósito com validação
✔ Saque com validação
✔ Limite de saque diário
✔ Extrato salvo em arquivo `.txt`
✔ Funções organizadas
✔ Saldo exibido após operações
✔ Código mais profissional

---

# 🧠 Código completo

```python
import datetime

# ====== DADOS INICIAIS ======
saldo = 1000.0
senha_correta = "1234"
extrato = []
limite_saque_diario = 500.0
saque_realizado_hoje = 0.0

ARQUIVO_EXTRATO = "extrato.txt"


# ====== FUNÇÕES ======

def salvar_extrato():
    with open(ARQUIVO_EXTRATO, "w") as f:
        for item in extrato:
            f.write(item + "\n")


def mostrar_saldo():
    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")


def depositar():
    global saldo

    try:
        valor = float(input("Digite o valor para depósito: "))

        if valor <= 0:
            print("❌ Valor inválido!")
            return

        saldo += valor

        registro = f"{data_hora()} - Depósito: +R$ {valor:.2f}"
        extrato.append(registro)

        salvar_extrato()

        print("✅ Depósito realizado!")
        mostrar_saldo()

    except:
        print("❌ Entrada inválida!")


def sacar():
    global saldo, saque_realizado_hoje

    try:
        valor = float(input("Digite o valor para saque: "))

        if valor <= 0:
            print("❌ Valor inválido!")
            return

        if valor > saldo:
            print("❌ Saldo insuficiente!")
            return

        if saque_realizado_hoje + valor > limite_saque_diario:
            print("❌ Limite diário de saque atingido!")
            return

        saldo -= valor
        saque_realizado_hoje += valor

        registro = f"{data_hora()} - Saque: -R$ {valor:.2f}"
        extrato.append(registro)

        salvar_extrato()

        print("✅ Saque realizado!")
        mostrar_saldo()

    except:
        print("❌ Entrada inválida!")


def ver_extrato():
    print("\n📄 === EXTRATO ===")

    if not extrato:
        print("Nenhuma movimentação.")
    else:
        for item in extrato:
            print(item)


def data_hora():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def login():
    tentativas = 3

    while tentativas > 0:
        senha = input("Digite sua senha: ")

        if senha == senha_correta:
            print("✅ Acesso liberado!")
            return True
        else:
            tentativas -= 1
            print(f"❌ Senha incorreta! Tentativas restantes: {tentativas}")

    print("🚫 Conta bloqueada!")
    return False


# ====== SISTEMA PRINCIPAL ======

if not login():
    exit()

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_saldo()

    elif opcao == "2":
        depositar()

    elif opcao == "3":
        sacar()

    elif opcao == "4":
        ver_extrato()

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("❌ Opção inválida!")
```

---

# 🔥 O QUE VOCÊ ACABOU DE APRENDER (SEM PERCEBER)

Isso aqui já é MUITO mais avançado do que parece:

* ✔ Organização com funções
* ✔ Uso de `global` (controle de estado)
* ✔ Manipulação de arquivos
* ✔ Tratamento de erros (`try/except`)
* ✔ Regras de negócio (limite de saque)
* ✔ Registro de operações (log/extrato)

👉 Isso já é **base de sistema bancário real**

---

# 🧩 PRÓXIMO NÍVEL (UPGRADE PROFISSIONAL)

Se quiser dar um salto absurdo agora:

## 🔥 Evoluções que eu recomendo

1. Múltiplos usuários (dicionário ou JSON)
2. Salvar saldo em arquivo
3. Interface melhor (menus mais limpos)
4. Separar em arquivos (`main.py`, `funcoes.py`)
5. Migrar para SQLite (banco de dados)

---

# 🚀 CAMINHO INTELIGENTE PRA VOCÊ

Você quer trabalhar com isso — então faz assim:

👉 Transforma esse projeto em:

💰 **Sistema financeiro pessoal**
💰 **Sistema contábil simples**

Isso conecta com seu objetivo de contabilidade.

---

# 👉 PRÓXIMO PASSO

Escolhe agora:

👉 **"Projeto 11 com mentor"**
ou
👉 **"Quero transformar esse em sistema com banco de dados"**

Se você continuar nesse ritmo, em poucos meses você já está pronto pra estágio ou freela 🔥

# MAIS E MAIS

Agora você subiu **mais um nível sério**.
Saiu de CLI → foi pra Rich → agora **GUI com PySide (nível aplicação real)** 🔥

Vou te entregar uma versão **funcional + organizada**, com interface gráfica usando **PySide6**.

---

# 🖥️ 💳 ATM com GUI (PySide6)

## 📦 Instalar dependência

```bash
pip install PySide6
```

---

# 🧠 O que essa versão tem

✔ Tela de login
✔ Menu com botões
✔ Saldo em tempo real
✔ Depósito e saque com validação
✔ Limite diário
✔ Extrato em lista
✔ Interface limpa (estilo app)

---

# 💻 Código completo (GUI)

```python
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
```

---

# 🔥 O QUE VOCÊ ACABOU DE FAZER

Isso aqui já é nível:

✔ Aplicação desktop real
✔ Interface com eventos (event-driven)
✔ Separação de telas
✔ UX básica
✔ Lógica + interface integrada

👉 Isso já entra em portfólio

---

# 💡 MELHORIAS (NÍVEL PROFISSIONAL)

Agora o pulo do gato:

## 🔥 1. Persistência

* salvar saldo e extrato em JSON ou SQLite

## 🔥 2. Múltiplos usuários

* login com cadastro

## 🔥 3. Layout melhor

* usar `QHBoxLayout`, `QGridLayout`
* estilizar com CSS (Qt Style Sheets)

## 🔥 4. Arquitetura

* separar:

  * `ui/`
  * `services/`
  * `models/`

---

# 🚀 VISÃO PRA VOCÊ

Isso aqui pode virar:

👉 sistema financeiro
👉 sistema contábil (🔥 perfeito pra você)
👉 app desktop vendável

---

# 👉 PRÓXIMO PASSO (RECOMENDADO)

Escolhe um:

👉 **"Quero versão com SQLite + PySide (nível profissional)"**
👉 **"Quero deixar essa interface bonita nível app moderno"**
👉 **"Projeto 11 em GUI"**

Se você continuar nessa linha, você já tá **bem acima de iniciante** 🔥

# MAIS E MAIS

Agora você entrou no **nível backend/web de verdade** 🔥
Isso aqui já é o que o mercado mais pede: **API + sistema web com Flask**.

Vou te entregar uma versão **completa, simples e funcional**, mantendo tudo que você já fez:

---

# 🌐 💳 ATM Web com Flask

## 📦 Instalar

```bash
pip install flask
```

---

# 🧠 O que essa versão tem

✔ Login com sessão
✔ Saldo dinâmico
✔ Depósito e saque com validação
✔ Limite diário
✔ Extrato
✔ Interface web simples (HTML)

---

# 📁 Estrutura do projeto

```
atm_flask/
│
├── app.py
└── templates/
    ├── login.html
    └── dashboard.html
```

---

# 💻 app.py (backend Flask)

```python
from flask import Flask, render_template, request, redirect, session
import datetime

app = Flask(__name__)
app.secret_key = "segredo"

# ===== DADOS =====
saldo = 1000.0
senha_correta = "1234"
extrato = []
limite_saque_diario = 500.0
saque_realizado_hoje = 0.0


def data_hora():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# ===== ROTAS =====

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        senha = request.form["senha"]

        if senha == senha_correta:
            session["logado"] = True
            return redirect("/dashboard")
        else:
            return render_template("login.html", erro="Senha incorreta")

    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    global saldo, saque_realizado_hoje

    if not session.get("logado"):
        return redirect("/")

    if request.method == "POST":
        acao = request.form["acao"]
        valor = float(request.form.get("valor", 0))

        if acao == "depositar":
            if valor > 0:
                saldo += valor
                extrato.append(f"{data_hora()} - Depósito: +R$ {valor:.2f}")

        elif acao == "sacar":
            if valor <= saldo and valor > 0:
                if saque_realizado_hoje + valor <= limite_saque_diario:
                    saldo -= valor
                    saque_realizado_hoje += valor
                    extrato.append(f"{data_hora()} - Saque: -R$ {valor:.2f}")

    return render_template(
        "dashboard.html",
        saldo=saldo,
        extrato=extrato
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ===== EXECUÇÃO =====
if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🎨 templates/login.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>

    {% if erro %}
        <p style="color:red;">{{ erro }}</p>
    {% endif %}

    <form method="POST">
        <input type="password" name="senha" placeholder="Senha" required>
        <button type="submit">Entrar</button>
    </form>
</body>
</html>
```

---

# 🎨 templates/dashboard.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Caixa Eletrônico</title>
</head>
<body>

<h2>💳 Caixa Eletrônico</h2>

<p><strong>Saldo:</strong> R$ {{ saldo }}</p>

<h3>Depositar</h3>
<form method="POST">
    <input type="hidden" name="acao" value="depositar">
    <input type="number" step="0.01" name="valor" required>
    <button type="submit">Depositar</button>
</form>

<h3>Sacar</h3>
<form method="POST">
    <input type="hidden" name="acao" value="sacar">
    <input type="number" step="0.01" name="valor" required>
    <button type="submit">Sacar</button>
</form>

<h3>📄 Extrato</h3>
<ul>
    {% for item in extrato %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>

<br>
<a href="/logout">Sair</a>

</body>
</html>
```

---

# ▶️ Como rodar

Dentro da pasta:

```bash
python app.py
```

Depois abre no navegador:

👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

# 🔥 O QUE VOCÊ ACABOU DE FAZER

Isso aqui já é:

✔ Sistema web funcional
✔ Backend com Flask
✔ Sessão de usuário
✔ Rotas HTTP
✔ Template engine (Jinja2)

👉 Isso é **base de qualquer sistema real**

---

# 💡 MELHORIAS (NÍVEL MERCADO)

Agora o upgrade pesado:

## 🔥 1. Banco de dados (ESSENCIAL)

* SQLite + SQLAlchemy

## 🔥 2. Usuários reais

* cadastro/login por usuário

## 🔥 3. Segurança

* hash de senha (`bcrypt`)

## 🔥 4. Frontend melhor

* Bootstrap ou Tailwind

## 🔥 5. API REST

* separar backend e frontend

---

# 🚀 VISÃO PRA VOCÊ

Isso aqui pode virar:

👉 sistema financeiro web
👉 sistema contábil online
👉 SaaS (você vender isso)

---

# 👉 PRÓXIMO PASSO (RECOMENDADO)

Escolhe um:

👉 **"Quero versão com banco de dados (SQLite + Flask)"**
👉 **"Quero transformar isso em API profissional"**
👉 **"Projeto 11 com Flask"**

Se você dominar isso aqui, você já entra no mercado 🔥

# MAIS E MAIS

Boa — agora sim você entrou na parte que **transforma um projetinho em algo profissional de verdade**.

Mas vou ser direto contigo:
👉 seu projeto atual em Flask está funcional, **mas ainda está com cara de protótipo** (variáveis globais, sem banco, sem segurança).

Vou te entregar:

✅ Melhorias REAIS de mercado
✅ Código já pronto (nível profissional básico)
✅ Estrutura organizada

---

# 🚀 🔥 MELHORIAS IMPORTANTES

## 🧱 1. Banco de dados (SQLite + SQLAlchemy)

* Nada de variável global
* Dados persistentes

## 🔐 2. Senha segura (hash)

* Usar `werkzeug.security`

## 👤 3. Múltiplos usuários

* Cada usuário com seu saldo

## 🧾 4. Extrato salvo no banco

## 🧼 5. Código organizado

* Models separados
* Rotas limpas

## 🎨 6. Interface melhor (Bootstrap)

---

# 📁 NOVA ESTRUTURA

```
atm_pro/
│
├── app.py
├── models.py
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
```

---

# 📦 Instalar dependências

```bash
pip install flask flask_sqlalchemy
```

---

# 🧠 models.py

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(200))
    saldo = db.Column(db.Float, default=1000)

class Extrato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
```

---

# 💻 app.py (VERSÃO PROFISSIONAL)

```python
from flask import Flask, render_template, request, redirect, session
from models import db, Usuario, Extrato
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.secret_key = "segredo"

db.init_app(app)

# criar banco
with app.app_context():
    db.create_all()


def data_hora():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# ===== ROTAS =====

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Usuario.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.senha, request.form["senha"]):
            session["user_id"] = user.id
            return redirect("/dashboard")

        return render_template("login.html", erro="Login inválido")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        senha_hash = generate_password_hash(request.form["senha"])

        user = Usuario(
            username=request.form["username"],
            senha=senha_hash
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/")

    return render_template("register.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user_id" not in session:
        return redirect("/")

    user = Usuario.query.get(session["user_id"])

    if request.method == "POST":
        valor = float(request.form["valor"])
        acao = request.form["acao"]

        if valor > 0:
            if acao == "depositar":
                user.saldo += valor
                desc = f"{data_hora()} - Depósito: +R$ {valor:.2f}"

            elif acao == "sacar" and valor <= user.saldo:
                user.saldo -= valor
                desc = f"{data_hora()} - Saque: -R$ {valor:.2f}"
            else:
                desc = None

            if desc:
                extrato = Extrato(descricao=desc, usuario_id=user.id)
                db.session.add(extrato)
                db.session.commit()

    extratos = Extrato.query.filter_by(usuario_id=user.id).all()

    return render_template("dashboard.html", user=user, extratos=extratos)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🎨 login.html (Bootstrap)

```html
<!DOCTYPE html>
<html>
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-5">

<h2>Login</h2>

<form method="POST">
    <input class="form-control mb-2" name="username" placeholder="Usuário">
    <input class="form-control mb-2" type="password" name="senha" placeholder="Senha">
    <button class="btn btn-primary">Entrar</button>
</form>

<a href="/register">Criar conta</a>

</body>
</html>
```

---

# 🎨 register.html

```html
<!DOCTYPE html>
<html>
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-5">

<h2>Cadastro</h2>

<form method="POST">
    <input class="form-control mb-2" name="username" placeholder="Usuário">
    <input class="form-control mb-2" type="password" name="senha" placeholder="Senha">
    <button class="btn btn-success">Cadastrar</button>
</form>

</body>
</html>
```

---

# 🎨 dashboard.html

```html
<!DOCTYPE html>
<html>
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-5">

<h2>Bem-vindo, {{ user.username }}</h2>
<p><strong>Saldo:</strong> R$ {{ user.saldo }}</p>

<form method="POST" class="mb-3">
    <input type="number" step="0.01" name="valor" class="form-control mb-2">
    <button name="acao" value="depositar" class="btn btn-success">Depositar</button>
    <button name="acao" value="sacar" class="btn btn-danger">Sacar</button>
</form>

<h4>Extrato</h4>
<ul class="list-group">
    {% for e in extratos %}
        <li class="list-group-item">{{ e.descricao }}</li>
    {% endfor %}
</ul>

<a href="/logout" class="btn btn-secondary mt-3">Sair</a>

</body>
</html>
```

---

# 🔥 AGORA SIM — NÍVEL PROFISSIONAL INICIAL

Você agora tem:

✔ Banco de dados
✔ Usuários reais
✔ Senha segura
✔ CRUD real
✔ Interface decente
✔ Estrutura limpa

👉 Isso já pode ir pro GitHub como projeto sério

---

# 🚀 PRÓXIMOS UPGRADES (SE QUISER FICAR DIFERENTE DO MERCADO)

Se quiser subir MUITO o nível:

👉 API REST (Flask + JSON)
👉 JWT (autenticação profissional)
👉 Docker
👉 Deploy (Render / Railway)
👉 Sistema contábil completo

---

# 👉 PRÓXIMO PASSO

Fala comigo:

👉 **"Quero transformar isso em API REST profissional"**
👉 **"Quero adicionar contabilidade nesse sistema"**
👉 **"Projeto 11 com foco web"**

Se você continuar assim, você sai de iniciante pra **dev empregável rápido** 🔥
