Bora! 🔥 Agora você entrou na parte divertida: **jogos**

---

# 🎮 PROJETO 5 — Jogo da Adivinhação

## 🎯 Objetivo

O computador escolhe um número aleatório, e o jogador tenta adivinhar.

---

## 🧠 O que você vai aprender

* `random`
* `while`
* `if/else`
* Loop infinito controlado
* Lógica de jogo

---

# 🪜 PASSO 1 — Versão simples

```python id="p5b1"
import random

numero_secreto = random.randint(1, 100)

tentativa = int(input("Adivinhe o número (1 a 100): "))

if tentativa == numero_secreto:
    print("Acertou! 🎉")
else:
    print(f"Errou! O número era {numero_secreto}")
```

---

# 🪜 PASSO 2 — Versão com loop (jogo de verdade)

```python id="p5b2"
import random

numero_secreto = random.randint(1, 100)

while True:
    tentativa = int(input("Adivinhe o número (1 a 100): "))

    if tentativa == numero_secreto:
        print("Parabéns! Você acertou 🎉")
        break
    elif tentativa < numero_secreto:
        print("Tente um número MAIOR 🔼")
    else:
        print("Tente um número MENOR 🔽")
```

---

# 🪜 PASSO 3 — Contador de tentativas

```python id="p5b3"
import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe o número: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Acertou em {tentativas} tentativas! 🎉")
        break
    elif tentativa < numero_secreto:
        print("Maior 🔼")
    else:
        print("Menor 🔽")
```

---

# 🔥 DESAFIOS (FAZ ISSO!)

## 🧩 Desafio 1

Limitar número de tentativas (ex: 5 chances)

---

## 🧩 Desafio 2

Escolher dificuldade:

* Fácil (1–50)
* Médio (1–100)
* Difícil (1–200)

---

## 🧩 Desafio 3

Mostrar histórico de tentativas

---

## 🧩 Desafio 4

Sistema de pontuação:

* Menos tentativas = mais pontos

---

## 🧩 Desafio 5 (TOP 🔥)

Perguntar:
👉 "Quer jogar novamente?"

---

# 🚀 Evolução desse projeto

Depois você pode transformar isso em:

* 🖥️ Interface gráfica (PySide6)
* 🌐 Versão web (Flask)
* 🎮 Jogo estilo app (com ranking)

---

# 📌 MISSÃO

👉 Faça o PASSO 3
👉 Depois tente pelo menos 1 desafio

---

Se quiser aprender MUITO mais rápido:

👉 fala: **“quero versão avançada do jogo”**

ou

👉 **“quero transformar em app”**

e eu te levo pro próximo nível 🔥



# Mais e mais 

Perfeito 🔥 — agora você vai transformar esse jogo simples em um **jogo completo de verdade** (nível intermediário já!).

Vou te entregar **TODOS os desafios resolvidos em um único código profissional**, bem organizado e com boas práticas.

---

# 🎮 JOGO DA ADIVINHAÇÃO — VERSÃO COMPLETA

```python
import random

def escolher_dificuldade():
    print("\nEscolha a dificuldade:")
    print("1 - Fácil (1 a 50)")
    print("2 - Médio (1 a 100)")
    print("3 - Difícil (1 a 200)")

    opcao = input("Opção: ")

    if opcao == "1":
        return 50
    elif opcao == "2":
        return 100
    elif opcao == "3":
        return 200
    else:
        print("Opção inválida! Usando padrão (1 a 100).")
        return 100


def calcular_pontos(tentativas, max_tentativas):
    # Quanto menos tentativas, maior a pontuação
    return max(0, (max_tentativas - tentativas + 1) * 10)


def jogar():
    limite = escolher_dificuldade()
    numero_secreto = random.randint(1, limite)

    max_tentativas = 5  # 🔥 Desafio 1
    tentativas = 0
    historico = []  # 🔥 Desafio 3

    print(f"\nAdivinhe o número entre 1 e {limite}")
    print(f"Você tem {max_tentativas} tentativas!\n")

    while tentativas < max_tentativas:
        try:
            tentativa = int(input("Digite seu palpite: "))
        except:
            print("Digite um número válido!")
            continue

        tentativas += 1
        historico.append(tentativa)

        if tentativa == numero_secreto:
            pontos = calcular_pontos(tentativas, max_tentativas)
            print(f"\n🎉 Acertou em {tentativas} tentativas!")
            print(f"⭐ Pontuação: {pontos}")
            break
        elif tentativa < numero_secreto:
            print("🔼 Tente um número MAIOR")
        else:
            print("🔽 Tente um número MENOR")

        print(f"Tentativas restantes: {max_tentativas - tentativas}")

    else:
        print(f"\n💀 Você perdeu! O número era {numero_secreto}")

    # 🔥 Mostrar histórico
    print("\n📜 Histórico de tentativas:", historico)


def main():
    while True:
        jogar()

        # 🔥 Desafio 5
        continuar = input("\nQuer jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por jogar! 👋")
            break


# Executar jogo
main()
```

---

# 🧠 O QUE VOCÊ ACABOU DE DOMINAR

### ✅ Desafio 1 — Limite de tentativas

```python
while tentativas < max_tentativas:
```

---

### ✅ Desafio 2 — Dificuldade

```python
def escolher_dificuldade()
```

---

### ✅ Desafio 3 — Histórico

```python
historico.append(tentativa)
```

---

### ✅ Desafio 4 — Pontuação

```python
def calcular_pontos()
```

---

### ✅ Desafio 5 — Jogar novamente

```python
while True:
    jogar()
```

---

# 🔥 NÍVEL PROFISSIONAL (AGORA SIM!)

Você já está fazendo coisas que iniciantes normalmente não fazem:

* Separação em funções ✔️
* Controle de fluxo ✔️
* Tratamento de erro ✔️
* Lógica de jogo ✔️

---

# 🚀 PRÓXIMO PASSO (ESCOLHE UM)

Agora você pode evoluir esse projeto para:

### 🎮 1. Interface gráfica (PySide6)

Jogo com botões e tela

### 🌐 2. Versão web (Flask)

Jogar pelo navegador

### 🏆 3. Ranking (salvar pontuação em arquivo)

### 🧠 4. IA que tenta adivinhar seu número (inverso)

---

Se quiser continuar no ritmo forte:

👉 fala: **“Projeto 6”**
ou
👉 **“quero versão com interface desse jogo”**

e eu te levo pro próximo nível 🔥


# Mais e mais

Perfeito 🔥 agora você vai transformar esse jogo em um **app de verdade com interface gráfica (PySide6)** — isso já é nível intermediário/avançado no portfólio.

Vou te entregar um **jogo completo com interface**, incluindo:

* Escolha de dificuldade
* Campo de input
* Botão de jogar
* Histórico
* Tentativas restantes
* Pontuação
* Botão "Novo jogo"

---

# 🎮 Jogo da Adivinhação — PySide6 (GUI)

## 🚀 Código completo

```python
import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QLineEdit, QTextEdit, QComboBox
)

class Jogo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jogo da Adivinhação 🎮")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        # Título
        self.titulo = QLabel("Adivinhe o número!")
        self.layout.addWidget(self.titulo)

        # Dificuldade
        self.dificuldade = QComboBox()
        self.dificuldade.addItems(["Fácil (1-50)", "Médio (1-100)", "Difícil (1-200)"])
        self.layout.addWidget(self.dificuldade)

        # Input
        self.input_numero = QLineEdit()
        self.input_numero.setPlaceholderText("Digite seu palpite")
        self.layout.addWidget(self.input_numero)

        # Botão jogar
        self.botao = QPushButton("Tentar")
        self.botao.clicked.connect(self.tentar)
        self.layout.addWidget(self.botao)

        # Resultado
        self.resultado = QLabel("")
        self.layout.addWidget(self.resultado)

        # Histórico
        self.historico = QTextEdit()
        self.historico.setReadOnly(True)
        self.layout.addWidget(self.historico)

        # Tentativas
        self.tentativas_label = QLabel("")
        self.layout.addWidget(self.tentativas_label)

        # Pontuação
        self.pontuacao_label = QLabel("")
        self.layout.addWidget(self.pontuacao_label)

        # Novo jogo
        self.novo_jogo_btn = QPushButton("Novo Jogo 🔄")
        self.novo_jogo_btn.clicked.connect(self.novo_jogo)
        self.layout.addWidget(self.novo_jogo_btn)

        self.setLayout(self.layout)

        self.novo_jogo()

    def configurar_jogo(self):
        dificuldade = self.dificuldade.currentIndex()

        if dificuldade == 0:
            self.limite = 50
        elif dificuldade == 1:
            self.limite = 100
        else:
            self.limite = 200

        self.numero_secreto = random.randint(1, self.limite)
        self.max_tentativas = 5
        self.tentativas = 0
        self.historico_lista = []

        self.historico.clear()
        self.resultado.setText("")
        self.pontuacao_label.setText("")

        self.atualizar_tentativas()

    def novo_jogo(self):
        self.configurar_jogo()

    def atualizar_tentativas(self):
        restantes = self.max_tentativas - self.tentativas
        self.tentativas_label.setText(f"Tentativas restantes: {restantes}")

    def calcular_pontos(self):
        return max(0, (self.max_tentativas - self.tentativas + 1) * 10)

    def tentar(self):
        try:
            tentativa = int(self.input_numero.text())
        except:
            self.resultado.setText("Digite um número válido!")
            return

        self.tentativas += 1
        self.historico_lista.append(tentativa)
        self.historico.append(str(tentativa))

        if tentativa == self.numero_secreto:
            pontos = self.calcular_pontos()
            self.resultado.setText("🎉 Você acertou!")
            self.pontuacao_label.setText(f"Pontuação: {pontos}")
            return

        elif tentativa < self.numero_secreto:
            self.resultado.setText("🔼 Tente um número maior")
        else:
            self.resultado.setText("🔽 Tente um número menor")

        self.atualizar_tentativas()

        if self.tentativas >= self.max_tentativas:
            self.resultado.setText(f"💀 Fim de jogo! Número era {self.numero_secreto}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Jogo()
    janela.show()
    sys.exit(app.exec())
```

---

# 🎯 O QUE VOCÊ ACABOU DE CONSTRUIR

Você criou um sistema com:

✅ Interface gráfica completa
✅ Eventos (botões funcionando)
✅ Estado do jogo (variáveis internas)
✅ Lógica separada
✅ Feedback visual pro usuário

👉 Isso já é nível de **projeto de portfólio**

---

# 🔥 MELHORIAS (SE QUISER VIRAR PRO)

Agora vem o upgrade real:

### 🧩 1. Cores dinâmicas

* Verde = acertou
* Vermelho = errou

---

### 🧩 2. Bloquear input após perder/ganhar

---

### 🧩 3. Sons (acerto/erro)

---

### 🧩 4. Ranking (salvar pontuação em arquivo)

---

### 🧩 5. Interface bonita (estilo app)

---

# 🚀 PRÓXIMO NÍVEL

Agora você tem 3 caminhos fortes:

👉 Criar versão WEB (Flask)
👉 Criar jogo mais complexo (forca)
👉 Criar sistema com banco de dados

---

Se quiser continuar no fluxo ideal:

👉 fala: **“Projeto 6”**
ou
👉 **“quero deixar esse jogo profissional nível app”**

e eu te levo pro próximo nível 🔥
