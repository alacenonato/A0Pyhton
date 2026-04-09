Boa escolha. Projeto 15 parece simples… mas dá pra transformar ele em algo MUITO mais forte se fizer do jeito certo.

---

# 🎮 Projeto 15 — Pedra, Papel e Tesoura (Nível Profissional)

## 🎯 Objetivo real

Você não vai só fazer um joguinho.

Você vai aprender:

* lógica de decisão
* organização de código
* modularização
* entrada de dados segura
* evolução de projeto (básico → profissional)

---

# 🧱 ETAPA 1 — Versão básica (funcional)

## 📌 Regras:

* Jogador escolhe: pedra, papel ou tesoura
* Computador escolhe aleatório
* Mostra quem venceu

---

## 💻 Código (versão simples)

```python
import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").lower()

computador = random.choice(opcoes)

print(f"Computador escolheu: {computador}")

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você venceu!")
else:
    print("Você perdeu!")
```

---

# ⚠️ Problema dessa versão

Ela funciona… mas:

* não valida entrada ❌
* não tem repetição ❌
* não tem estrutura ❌
* não é “projeto” ainda ❌

---

# 🚀 ETAPA 2 — Versão intermediária (estrutura correta)

Agora vamos organizar como um dev de verdade.

---

## 💻 Código melhorado

```python
import random

def escolher_computador():
    return random.choice(["pedra", "papel", "tesoura"])

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    
    vitorias = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }

    if vitorias[jogador] == computador:
        return "jogador"
    else:
        return "computador"

def jogar():
    while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou sair): ").lower()

        if jogador == "sair":
            print("Encerrando jogo...")
            break

        if jogador not in ["pedra", "papel", "tesoura"]:
            print("Opção inválida!")
            continue

        computador = escolher_computador()
        resultado = determinar_vencedor(jogador, computador)

        print(f"Computador: {computador}")

        if resultado == "empate":
            print("Empate!")
        elif resultado == "jogador":
            print("Você venceu!")
        else:
            print("Você perdeu!")

jogar()
```

---

# 🧠 O que você aprendeu aqui

* Funções (`def`)
* Loop com `while`
* Validação de entrada
* Uso de dicionário (muito importante!)
* Separação de responsabilidades

---

# 🔥 ETAPA 3 — Evolução PROFISSIONAL

Agora vem o que realmente te destaca.

---

## 💡 Melhorias que você DEVE implementar

### 1. 🏆 Sistema de pontuação

* jogador vs computador
* melhor de 3 / melhor de 5

---

### 2. 📊 Histórico de partidas

Salvar em arquivo:

```json
{
  "vitorias": 3,
  "derrotas": 2,
  "empates": 1
}
```

---

### 3. 🎮 Menu inicial

```
1 - Jogar
2 - Ver histórico
3 - Resetar histórico
4 - Sair
```

---

### 4. 🧪 Tratamento de erro

Evitar qualquer quebra do programa

---

### 5. 🧱 Separar arquivos (nível avançado)

```
jogo/
├── main.py
├── jogo.py
├── utils.py
└── dados.json
```

---

# 💣 DESAFIO (FAZ ISSO QUE VOCÊ EVOLUI RÁPIDO)

Implementa:

👉 Modo difícil (computador “aprende” padrão do jogador)

Exemplo:

* se jogador usa muita “pedra”
* computador começa a usar “papel”

---

# 🚀 EXTRA (se quiser subir de nível MESMO)

* Interface gráfica com Tkinter
* Versão web com Flask
* Multiplayer simples (socket)

---

# 📌 Missão pra você agora

Faça nessa ordem:

1. Copie a versão intermediária
2. Rode e entenda TUDO
3. Adicione sistema de pontuação
4. Depois histórico em arquivo

---

Se quiser continuar comigo:

👉 **“Corrige meu código”** (você manda o que fez)
👉 **“Quero versão com interface gráfica”**
👉 **“Vamos pro projeto 16”**

Vamos transformar você em nível profissional de verdade 🚀

---
---
---
---
Perfeito — agora sim estamos falando de um projeto **nível portfólio** 👇

Vou te entregar uma versão com as 5 melhorias:

✅ Sistema de pontuação (melhor de 3)
✅ Histórico salvo em JSON
✅ Menu interativo
✅ Tratamento de erros
✅ Código modular (simulado em um arquivo, mas estruturado corretamente)

---

# 🎮 Pedra, Papel e Tesoura — Versão Profissional

```python
import random
import json
import os

ARQUIVO = "dados.json"

# =========================
# UTIL / DADOS
# =========================

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"vitorias": 0, "derrotas": 0, "empates": 0}
    
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return {"vitorias": 0, "derrotas": 0, "empates": 0}


def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)


def resetar_dados():
    dados = {"vitorias": 0, "derrotas": 0, "empates": 0}
    salvar_dados(dados)
    print("Histórico resetado!")


# =========================
# LÓGICA DO JOGO
# =========================

def escolher_computador():
    return random.choice(["pedra", "papel", "tesoura"])


def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"

    regras = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }

    if regras[jogador] == computador:
        return "jogador"
    return "computador"


# =========================
# JOGO PRINCIPAL
# =========================

def jogar():
    dados = carregar_dados()

    pontos_jogador = 0
    pontos_computador = 0

    print("\n🎮 Melhor de 3 - Começou!")

    while pontos_jogador < 2 and pontos_computador < 2:
        try:
            jogador = input("Escolha pedra, papel ou tesoura: ").lower()

            if jogador not in ["pedra", "papel", "tesoura"]:
                print("❌ Opção inválida!")
                continue

            computador = escolher_computador()
            print(f"💻 Computador escolheu: {computador}")

            resultado = determinar_vencedor(jogador, computador)

            if resultado == "empate":
                print("🤝 Empate!")
                dados["empates"] += 1
            elif resultado == "jogador":
                print("🏆 Você venceu a rodada!")
                pontos_jogador += 1
                dados["vitorias"] += 1
            else:
                print("💀 Computador venceu!")
                pontos_computador += 1
                dados["derrotas"] += 1

            print(f"📊 Placar: Você {pontos_jogador} x {pontos_computador} Computador\n")

        except Exception as e:
            print("Erro inesperado:", e)

    # Resultado final
    if pontos_jogador > pontos_computador:
        print("🎉 Você ganhou a partida!")
    else:
        print("😢 Você perdeu a partida!")

    salvar_dados(dados)


# =========================
# MENU
# =========================

def ver_historico():
    dados = carregar_dados()
    print("\n📊 HISTÓRICO")
    print(f"Vitórias: {dados['vitorias']}")
    print(f"Derrotas: {dados['derrotas']}")
    print(f"Empates: {dados['empates']}\n")


def menu():
    while True:
        print("\n====== MENU ======")
        print("1 - Jogar")
        print("2 - Ver histórico")
        print("3 - Resetar histórico")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogar()
        elif opcao == "2":
            ver_historico()
        elif opcao == "3":
            resetar_dados()
        elif opcao == "4":
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

# 🧠 O que esse projeto já prova sobre você

Se você colocar isso no GitHub, você já demonstra:

* ✔ Uso de arquivos (JSON)
* ✔ Estrutura de código organizada
* ✔ Separação de responsabilidades
* ✔ Tratamento de erros
* ✔ Lógica de jogo
* ✔ Interação com usuário

👉 Isso já é MUITO acima de iniciante comum.

---

# 🔥 Próximo upgrade (nível diferenciado)

Se quiser deixar esse projeto absurdo:

### 💡 1. IA simples (modo difícil)

Computador aprende seus padrões

### 💡 2. Interface gráfica (Tkinter)

Transforma em app real

### 💡 3. Estatísticas avançadas

* taxa de vitória (%)
* escolha mais usada

---

# 🚀 Próximo passo

Se quiser evoluir mesmo:

👉 **“Quero versão com interface gráfica”**
👉 **“Quero modo difícil com IA”**
👉 **“Vamos pro projeto 16”**

Qual você quer agora?

---
---
---
---
Boa — e aqui vou ser direto contigo:

👉 **“pySice” não existe (ou você digitou errado)**

Provavelmente você quis dizer:

* **PySide (PySide6)** ✅
  ou
* **PyQt**

👉 No Linux, o melhor caminho hoje é **PySide6** (oficial da Qt e mais tranquilo de usar).

---

# 🚀 Vamos fazer com PySide6 (Interface PROFISSIONAL)

## 📦 Primeiro: instalar

```bash
pip install PySide6
```

---

# 🎮 Pedra, Papel e Tesoura — GUI com PySide6

## 💻 Código completo

```python
import sys
import random
import json
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QMessageBox
)

ARQUIVO = "dados.json"

# =========================
# DADOS
# =========================

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"vitorias": 0, "derrotas": 0, "empates": 0}
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def resetar_dados():
    salvar_dados({"vitorias": 0, "derrotas": 0, "empates": 0})

# =========================
# LÓGICA
# =========================

def escolher_computador():
    return random.choice(["pedra", "papel", "tesoura"])

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"

    regras = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }

    if regras[jogador] == computador:
        return "jogador"
    return "computador"

# =========================
# APP
# =========================

class JogoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pedra, Papel e Tesoura")
        self.resize(300, 250)

        self.dados = carregar_dados()
        self.pontos_jogador = 0
        self.pontos_computador = 0

        layout = QVBoxLayout()

        self.label_info = QLabel("Escolha sua jogada:")
        layout.addWidget(self.label_info)

        btn_pedra = QPushButton("🪨 Pedra")
        btn_pedra.clicked.connect(lambda: self.jogar("pedra"))
        layout.addWidget(btn_pedra)

        btn_papel = QPushButton("📄 Papel")
        btn_papel.clicked.connect(lambda: self.jogar("papel"))
        layout.addWidget(btn_papel)

        btn_tesoura = QPushButton("✂️ Tesoura")
        btn_tesoura.clicked.connect(lambda: self.jogar("tesoura"))
        layout.addWidget(btn_tesoura)

        self.label_resultado = QLabel("")
        layout.addWidget(self.label_resultado)

        self.label_placar = QLabel("Você 0 x 0 Computador")
        layout.addWidget(self.label_placar)

        btn_hist = QPushButton("📊 Ver Histórico")
        btn_hist.clicked.connect(self.ver_historico)
        layout.addWidget(btn_hist)

        btn_reset = QPushButton("🔄 Resetar Histórico")
        btn_reset.clicked.connect(self.resetar)
        layout.addWidget(btn_reset)

        self.setLayout(layout)

    def jogar(self, jogador):
        computador = escolher_computador()
        resultado = determinar_vencedor(jogador, computador)

        if resultado == "empate":
            self.label_resultado.setText(f"Empate! ({computador})")
            self.dados["empates"] += 1

        elif resultado == "jogador":
            self.label_resultado.setText(f"Você venceu! ({computador})")
            self.pontos_jogador += 1
            self.dados["vitorias"] += 1

        else:
            self.label_resultado.setText(f"Você perdeu! ({computador})")
            self.pontos_computador += 1
            self.dados["derrotas"] += 1

        self.label_placar.setText(
            f"Você {self.pontos_jogador} x {self.pontos_computador} Computador"
        )

        if self.pontos_jogador == 2 or self.pontos_computador == 2:
            if self.pontos_jogador > self.pontos_computador:
                QMessageBox.information(self, "Fim", "🎉 Você ganhou!")
            else:
                QMessageBox.information(self, "Fim", "💀 Você perdeu!")

            salvar_dados(self.dados)
            self.resetar_partida()

    def resetar_partida(self):
        self.pontos_jogador = 0
        self.pontos_computador = 0
        self.label_placar.setText("Você 0 x 0 Computador")
        self.label_resultado.setText("")

    def ver_historico(self):
        d = self.dados
        QMessageBox.information(
            self,
            "Histórico",
            f"Vitórias: {d['vitorias']}\nDerrotas: {d['derrotas']}\nEmpates: {d['empates']}"
        )

    def resetar(self):
        resetar_dados()
        self.dados = carregar_dados()
        QMessageBox.information(self, "Reset", "Histórico resetado!")

# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JogoApp()
    janela.show()
    sys.exit(app.exec())
```

---

# 🧠 Por que isso é melhor que Tkinter

* Interface mais moderna
* Mais usado no mercado
* Permite apps grandes depois (ERP, sistemas reais)
* Mais fácil evoluir para algo profissional

---

# ⚠️ Se der erro no Linux

Roda isso:

```bash
sudo apt install python3-pyside6
```

ou:

```bash
pip install PySide6 --break-system-packages
```

---

# 🔥 Próximo nível (agora começa a ficar sério)

Se quiser transformar isso em projeto de portfólio forte:

👉 Posso te ajudar a:

* deixar com **design moderno (tipo app de verdade)**
* adicionar **tema escuro**
* colocar **ícones e animações**
* gerar **.deb instalável no Linux**
* ou transformar em **app estilo sistema profissional**

---

Só fala:

👉 **“quero deixar com cara de app profissional”**
ou
👉 **“quero transformar em programa instalável (.deb)”**

Agora você saiu do básico MESMO 🚀
