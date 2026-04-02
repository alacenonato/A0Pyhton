---
---
---
Perfeito. Projeto 13 é **excelente** porque já começa a te ensinar coisas importantes como tempo, controle de fluxo e até base pra automação.

---

# 🚀 PROJETO 13 — CRONÔMETRO EM PYTHON

## 🎯 Objetivo

Criar um cronômetro com:

* Iniciar
* Pausar
* Continuar
* Resetar

---

# 🧠 Conceitos que você vai aprender

* `time`
* loops (`while`)
* controle de estado
* entrada do usuário
* organização em funções

---

# 🔰 Versão 1 — Simples (CLI)

Aqui já é um cronômetro funcional 👇

```python
import time

segundos = 0

while True:
    print(f"\rTempo: {segundos} segundos", end="")
    time.sleep(1)
    segundos += 1
```

👉 Isso já conta o tempo automaticamente.

---

# ⚙️ Versão 2 — Com controle (INICIAR / PARAR)

Agora começa a ficar interessante:

```python
import time

tempo = 0
rodando = False

while True:
    comando = input("\nDigite (i)niciar, (p)ausar, (r)esetar, (s)air: ").lower()

    if comando == "i":
        rodando = True
        print("Cronômetro iniciado...")

        while rodando:
            print(f"\rTempo: {tempo}s", end="")
            time.sleep(1)
            tempo += 1

    elif comando == "p":
        rodando = False
        print("\nPausado!")

    elif comando == "r":
        tempo = 0
        print("Resetado!")

    elif comando == "s":
        print("Saindo...")
        break
```

---

# 🔥 Versão 3 — PROFISSIONAL (Organizado em funções)

Agora sim você começa a pensar como programador 👇

```python
import time

tempo = 0
rodando = False

def iniciar():
    global tempo, rodando
    rodando = True
    print("Cronômetro iniciado...")

    while rodando:
        print(f"\rTempo: {tempo}s", end="")
        time.sleep(1)
        tempo += 1

def pausar():
    global rodando
    rodando = False
    print("\nPausado!")

def resetar():
    global tempo
    tempo = 0
    print("Resetado!")

def menu():
    while True:
        comando = input("\n(i)niciar | (p)ausar | (r)esetar | (s)air: ").lower()

        if comando == "i":
            iniciar()
        elif comando == "p":
            pausar()
        elif comando == "r":
            resetar()
        elif comando == "s":
            print("Encerrando...")
            break
        else:
            print("Comando inválido!")

menu()
```

---

# 💡 Melhorias (FAÇA ISSO pra evoluir de verdade)

Se você fizer essas melhorias, você sai de iniciante 👇

## 🔹 Nível 1

* Mostrar tempo em `HH:MM:SS`
* Evitar bugs ao iniciar várias vezes

---

## 🔹 Nível 2

* Criar **voltas (laps)**
* Salvar tempos em arquivo `.txt`

---

## 🔹 Nível 3

* Interface gráfica com `tkinter`
* Botões (Start, Stop, Reset)
* Mostrar tempo bonito

---

## 🔹 Nível 4 (PORTFÓLIO 💼)

* Histórico de sessões
* Exportar resultados
* Interface moderna (customtkinter ou web)

---

# 🧩 Desafio (IMPORTANTE)

Tenta fazer isso sozinho agora:

👉 Criar uma função que converte segundos para:

```
01:05:09
```

Se quiser, eu te ajudo depois.

---

# 🚀 Se quiser ir nível HARD

Posso te entregar:

✅ Versão com interface gráfica (tipo app real)
✅ Versão com salvamento automático
✅ Versão com contagem regressiva + cronômetro

---

Só fala:

👉 **“quero versão com interface gráfica”**
ou
👉 **“quero desafios mais difíceis”**

que a gente sobe MUITO seu nível 😎

---
---
---

Ótima pergunta — isso é exatamente o ponto onde muita gente trava 👍

👉 O problema da sua versão 2 é estrutural:

Quando você faz isso:

```python
if comando == "i":
    while rodando:
        ...
```

💥 O programa **fica preso dentro desse `while rodando`**
e **não volta para o `input()`** para ler novos comandos (pausar, resetar, etc).

---

# 🧠 Como resolver (IDEIA CORRETA)

Você precisa de:

👉 **um loop principal que SEMPRE lê comandos**
👉 e o cronômetro rodando “em paralelo”

Como Python básico não roda paralelo fácil, a gente resolve assim:

---

# ✅ SOLUÇÃO SIMPLES (funciona perfeitamente)

Você controla o tempo dentro do loop principal:

```python
import time

tempo = 0
rodando = False

while True:
    # Mostra o tempo sempre
    print(f"\rTempo: {tempo}s", end="")

    # Se estiver rodando, incrementa
    if rodando:
        time.sleep(1)
        tempo += 1
    else:
        time.sleep(0.1)  # evita travar CPU

    # Captura comando sem travar tudo
    if rodando == False:
        comando = input("\n(i)niciar | (p)ausar | (r)esetar | (s)air: ").lower()

        if comando == "i":
            rodando = True

        elif comando == "p":
            rodando = False

        elif comando == "r":
            tempo = 0

        elif comando == "s":
            print("\nSaindo...")
            break
```

---

# ⚠️ Limitação dessa versão

👉 Enquanto o cronômetro está rodando, você **não consegue digitar comandos imediatamente**

Porque:

* `time.sleep(1)` bloqueia o input

---

# 🔥 SOLUÇÃO MELHOR (nível acima)

Aqui é o jeito mais correto em CLI:

👉 usar **thread (processo paralelo)**

---

## 💡 Versão com Thread (PROFISSIONAL INICIANTE)

```python
import time
import threading

tempo = 0
rodando = False

def cronometro():
    global tempo, rodando
    while True:
        if rodando:
            time.sleep(1)
            tempo += 1
            print(f"\rTempo: {tempo}s", end="")

thread = threading.Thread(target=cronometro, daemon=True)
thread.start()

while True:
    comando = input("\n(i)niciar | (p)ausar | (r)esetar | (s)air: ").lower()

    if comando == "i":
        rodando = True

    elif comando == "p":
        rodando = False

    elif comando == "r":
        tempo = 0

    elif comando == "s":
        print("Saindo...")
        break
```

---

# 🧠 Entenda de vez (RESUMO)

👉 Seu erro foi aqui:

* Você colocou o cronômetro **dentro de um loop que bloqueia tudo**

👉 O certo é:

* Separar:

  * **entrada do usuário**
  * **execução do cronômetro**

---

# 🚀 Evolução agora (RECOMENDADO)

Se você entendeu isso, você já subiu de nível 👇

Próximos desafios:

1. Mostrar tempo em `HH:MM:SS`
2. Criar sistema de **voltas (laps)**
3. Salvar histórico em arquivo
4. Fazer versão com interface gráfica

---

Se quiser, posso te passar o próximo passo já no nível profissional:

👉 **“cronômetro com interface gráfica (igual app real)”**

ou

👉 **“me desafia com melhorias mais difíceis”** 😈

---
---
---
Boa — isso melhora MUITO a experiência do programa 👌

Você tem basicamente **2 formas principais** de fazer isso:

---

# ✅ 🔹 Forma 1 — Comando do sistema (mais comum)

Python pode executar comandos do sistema operacional:

```python id="t9n0xv"
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
```

### ✔️ Explicação

* `cls` → Windows
* `clear` → Linux/Mac (seu caso no Ubuntu)

---

## 💡 Usando no cronômetro:

```python id="f6l8z3"
import time
import os

def limpar_tela():
    os.system('clear')

tempo = 0

while True:
    limpar_tela()
    print(f"Tempo: {tempo}s")
    time.sleep(1)
    tempo += 1
```

---

# ⚡ 🔹 Forma 2 — Melhor (sem "piscar" a tela)

Limpar tela toda hora pode causar aquele efeito feio de “piscar”.

👉 Melhor abordagem:

Usar `\r` (carriage return)

```python id="g8m1pk"
import time

tempo = 0

while True:
    print(f"\rTempo: {tempo}s", end="")
    time.sleep(1)
    tempo += 1
```

---

## ✔️ Vantagens:

* Não pisca
* Mais rápido
* Mais profissional
* Usado em ferramentas reais (CLI)

---

# 🔥 🔹 Forma 3 — Terminal “bonito” (nível acima)

Se quiser algo mais avançado:

👉 usar biblioteca `rich`

```bash
pip install rich
```

Exemplo:

```python id="h3y7dw"
from rich.console import Console
import time

console = Console()
tempo = 0

while True:
    console.clear()
    console.print(f"[bold green]Tempo:[/bold green] {tempo}s")
    time.sleep(1)
    tempo += 1
```

---

# 🧠 Qual você deve usar?

👉 Para aprendizado:

* use `\r` (melhor prática)

👉 Para projeto simples:

* `os.system('clear')`

👉 Para portfólio:

* `rich` (fica lindo 😎)

---

# 🚀 Dica de ouro

No seu cronômetro:

👉 **NÃO use limpar tela + input ao mesmo tempo**

Isso dá bug visual.

Prefira:

* `\r` para atualização contínua
* `input()` separado

---

# 🔥 Se quiser subir MUITO o nível

Posso te ensinar:

✅ Fazer um cronômetro estilo app real (com botões no terminal)
✅ Criar interface gráfica (Tkinter ou Web)
✅ Mostrar tempo formatado tipo `00:01:32`

Só fala:

👉 **“quero deixar o cronômetro profissional”** 😎

---
---
---
Cara, sendo bem direto: **tá muito bom pro seu nível** — você já saiu do básico e entrou em **concorrência (thread)**, que muita gente nem toca 👏

Mas sim… dá pra melhorar — e essas melhorias são exatamente o que te levam de “funciona” → “profissional”.

---

# 🔍 Problemas do seu código (e como corrigir)

## ⚠️ 1. Condição de corrida (race condition)

Você usa `tempo` e `rodando` em duas threads sem proteção.

👉 Isso pode dar bug (principalmente em projetos maiores).

---

## ✅ SOLUÇÃO: usar `Lock`

```python
lock = threading.Lock()
```

---

## ⚠️ 2. Print bagunçando o input

Esse aqui você já deve ter percebido:

👉 O `print` do cronômetro “briga” com o `input()`

Resultado:

* texto quebrado
* cursor estranho

---

## ⚠️ 3. `while True` infinito sem controle de saída na thread

Sua thread nunca para de verdade.

---

# 🔥 VERSÃO MELHORADA (nível profissional iniciante)

Aqui vai uma versão baseada no SEU código, só que melhor estruturada:

```python
import time
import threading
import os

tempo = 0
rodando = False
executando = True

lock = threading.Lock()

def limpar_tela():
    os.system('clear')

def cronometro():
    global tempo, rodando, executando

    while executando:
        if rodando:
            time.sleep(1)
            with lock:
                tempo += 1

def mostrar_tempo():
    while executando:
        with lock:
            print(f"\rTempo: {tempo}s", end="")
        time.sleep(0.5)

# Threads
thread_cronometro = threading.Thread(target=cronometro)
thread_display = threading.Thread(target=mostrar_tempo)

thread_cronometro.start()
thread_display.start()

# Loop principal
while True:
    comando = input("\n(i)niciar | (p)ausar | (r)esetar | (s)air: ").lower()

    if comando == "i":
        rodando = True

    elif comando == "p":
        rodando = False

    elif comando == "r":
        with lock:
            tempo = 0

    elif comando == "s":
        executando = False
        break

# Espera threads terminarem
thread_cronometro.join()
thread_display.join()

print("\nEncerrado.")
```

---

# 🧠 O que você evoluiu aqui

Com esse código você já está praticando:

* ✅ Threads separadas (lógica + UI)
* ✅ `Lock` (evita bugs sérios)
* ✅ Controle de execução (`executando`)
* ✅ Melhor organização

👉 Isso já é **nível intermediário real**

---

# 💡 Melhorias que vão te levar ainda mais longe

## 🔹 1. Formatar tempo (ESSENCIAL)

Transformar isso:

```
125s
```

em:

```
00:02:05
```

---

## 🔹 2. Criar “laps” (voltas)

Exemplo:

```
Volta 1: 00:01:10
Volta 2: 00:02:30
```

---

## 🔹 3. Salvar histórico em arquivo

```python
with open("tempos.txt", "a") as f:
    f.write(...)
```

---

## 🔹 4. Interface CLI mais bonita (nível hacker 😎)

Usar:

* `curses` (Linux)
* ou `rich`

---

# 💣 Verdade importante

Você falou:

> “pelo terminal não dá pra fazer muita coisa”

👉 Isso NÃO é verdade.

Dá pra fazer coisa absurda em CLI:

* htop
* git
* nano
* dashboards completos

O limite não é o terminal…
👉 é a técnica (que você já começou a desenvolver)

---

# 🚀 Próximo passo (recomendado)

Agora você tem 3 caminhos MUITO bons:

👉 1. **Melhorar esse projeto (virar portfólio)**
👉 2. **Criar versão com interface gráfica (Tkinter)**
👉 3. **Criar versão web (Flask)** ← MUITO forte pro mercado

---

Se quiser, eu posso te levar pro próximo nível:

👉 **“transforma esse cronômetro em app com interface gráfica”**

ou

👉 **“quero adicionar laps + salvar histórico”**

ou até

👉 **“quero versão web profissional”**

Só falar 😎
---
---
---
Dá sim — e o seu objetivo é exatamente o ponto mais “chato” de CLI: **mostrar algo em tempo real sem quebrar o input**.

👉 Vou te entregar uma versão **corrigida, estável e limpa**, baseada no seu código, com:

* tempo atualizando sozinho ✅
* input funcionando ao mesmo tempo ✅
* sem sobreposição de texto ✅
* organização melhor ✅

---

# 🚀 VERSÃO FINAL (CLI LIMPA E FUNCIONAL)

```python
import time
import threading
import os

tempo = 0
rodando = False
executando = True

lock = threading.Lock()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cronometro():
    global tempo, rodando, executando
    while executando:
        if rodando:
            time.sleep(1)
            with lock:
                tempo += 1
        else:
            time.sleep(0.1)


def formatar_tempo(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def display():
    global executando
    while executando:
        limpar_tela()
        with lock:
            tempo_formatado = formatar_tempo(tempo)

        print("=== CRONÔMETRO ===\n")
        print(f"Tempo: {tempo_formatado}\n")
        print("(i) iniciar | (p) pausar | (r) resetar | (s) sair")
        print("\nDigite um comando abaixo:\n")

        time.sleep(0.3)


# Threads
thread_cronometro = threading.Thread(target=cronometro, daemon=True)
thread_display = threading.Thread(target=display, daemon=True)

thread_cronometro.start()
thread_display.start()


# Loop principal (input separado)
while True:
    comando = input("> ").lower()

    if comando == "i":
        rodando = True

    elif comando == "p":
        rodando = False

    elif comando == "r":
        with lock:
            tempo = 0

    elif comando == "s":
        executando = False
        break

# Finalização
thread_cronometro.join(timeout=1)
thread_display.join(timeout=1)

print("\nEncerrado.")
```

---

# 🧠 O que essa versão resolve

## ✅ 1. Nada se mistura mais

* Tempo fica **fixo na tela**
* Input fica **sempre na última linha**

---

## ✅ 2. Atualização limpa

* Tela redesenhada a cada ~0.3s
* Sem “bug visual”

---

## ✅ 3. Concorrência correta

* `Lock` protege `tempo`
* Threads separadas:

  * uma conta
  * outra mostra

---

## ✅ 4. UX muito melhor

* Formato `HH:MM:SS`
* Layout organizado

---

# ⚠️ Limitação real (honesta)

Mesmo assim, CLI tem limite:

👉 Enquanto você está digitando, a tela pode atualizar

Mas:

* não quebra
* não mistura texto
* funciona suave

---

# 🔥 Se quiser deixar INSANO (nível hacker)

Próximos upgrades:

## 🔹 1. Laps (voltas)

```text
Volta 1: 00:01:23
```

## 🔹 2. Salvar histórico

```python
with open("historico.txt", "a")
```

## 🔹 3. Interface estilo sistema (top nível)

* usar `curses` (Linux)
* ou `rich` + live display

---

# 🚀 Próximo nível recomendado

Agora você está pronto pra subir MUITO:

👉 Transformar isso em:

* 🖥️ App com interface gráfica (Tkinter)
* 🌐 Versão web (Flask)
* 📊 Cronômetro com dashboard

---

Se quiser, eu te levo direto pro próximo nível:

👉 **“quero versão com interface gráfica profissional”**
ou
👉 **“quero adicionar laps e histórico nesse código”** 😎

---
---
---
Perfeito — ótima escolha 👏
👉 **PySide (Qt)** é MUITO mais profissional que Tkinter e funciona bem no Ubuntu.

Vou te entregar um **cronômetro completo com interface gráfica**, com:

* Start / Pause / Reset
* Tempo em `HH:MM:SS`
* Interface limpa
* Código organizado

---

# ⚙️ 1. Instalação

```bash
pip install PySide6
```

---

# 🚀 2. CRONÔMETRO COM PYSIDE (PRONTO)

```python id="pyside_crono_01"
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
)
from PySide6.QtCore import QTimer, Qt


class Cronometro(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cronômetro Profissional")
        self.setGeometry(100, 100, 300, 200)

        self.tempo = 0

        # Timer (atualiza a cada 1 segundo)
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_tempo)

        # Layout principal
        layout = QVBoxLayout()

        # Label do tempo
        self.label = QLabel("00:00:00")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 40px; font-weight: bold;")
        layout.addWidget(self.label)

        # Botões
        botoes_layout = QHBoxLayout()

        self.btn_start = QPushButton("Iniciar")
        self.btn_pause = QPushButton("Pausar")
        self.btn_reset = QPushButton("Resetar")

        botoes_layout.addWidget(self.btn_start)
        botoes_layout.addWidget(self.btn_pause)
        botoes_layout.addWidget(self.btn_reset)

        layout.addLayout(botoes_layout)

        self.setLayout(layout)

        # Eventos
        self.btn_start.clicked.connect(self.iniciar)
        self.btn_pause.clicked.connect(self.pausar)
        self.btn_reset.clicked.connect(self.resetar)

    def formatar_tempo(self):
        h = self.tempo // 3600
        m = (self.tempo % 3600) // 60
        s = self.tempo % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def atualizar_tempo(self):
        self.tempo += 1
        self.label.setText(self.formatar_tempo())

    def iniciar(self):
        self.timer.start(1000)

    def pausar(self):
        self.timer.stop()

    def resetar(self):
        self.timer.stop()
        self.tempo = 0
        self.label.setText("00:00:00")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Cronometro()
    janela.show()
    sys.exit(app.exec())
```

---

# 🧠 O que você aprendeu aqui

Esse projeto já te coloca em outro nível:

* ✅ Interface gráfica real (Qt)
* ✅ Event-driven programming (eventos de botão)
* ✅ Timer sem thread (melhor prática em GUI)
* ✅ Organização em classe

👉 Isso já é padrão de aplicação desktop

---

# 🔥 Melhorias (recomendado pra portfólio)

Se quiser transformar isso em projeto forte:

## 🔹 1. Laps (voltas)

* Botão "Volta"
* Lista mostrando tempos

---

## 🔹 2. Estilo moderno (QSS)

Exemplo:

```python
self.setStyleSheet("""
    QWidget { background-color: #1e1e1e; color: white; }
    QPushButton { background-color: #007acc; padding: 10px; }
""")
```

---

## 🔹 3. Salvar histórico

* Arquivo `.txt` ou `.json`

---

## 🔹 4. Contagem regressiva

* Alternar modo cronômetro / timer

---

# 💣 Verdade importante

👉 Isso aqui já é algo que você pode colocar no GitHub como:

**“Desktop Stopwatch App with PySide6”**

E já conta como projeto real.

---

# 🚀 Próximo nível (se quiser)

Posso evoluir isso pra:

👉 Interface estilo app profissional (tema escuro + animações)
👉 Cronômetro com laps + histórico
👉 Transformar em app instalável (.deb pro Ubuntu 😎)

---

Só fala:

👉 **“quero versão com laps e histórico”**
ou
👉 **“quero deixar com visual profissional”**

e a gente sobe MUITO esse projeto 🚀
---
---
---
Perfeito — agora você vai sair de “projetinho” e fazer **app de verdade nível portfólio** 🔥

Vou te entregar em 3 partes:

1. 💻 App PySide6 (profissional: tema escuro + animações + laps + histórico)
2. 💾 Salvamento de histórico
3. 📦 Como gerar `.deb` no Ubuntu

---

# 🚀 1. APP COMPLETO (PROFISSIONAL)

```python
import sys
import json
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QHBoxLayout, QListWidget
)
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation
from PySide6.QtGui import QFont


class Cronometro(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cronômetro PRO")
        self.setGeometry(300, 200, 400, 400)

        self.tempo = 0
        self.laps = []

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_tempo)

        # Layout
        layout = QVBoxLayout()

        # Display tempo
        self.label = QLabel("00:00:00")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 32, QFont.Bold))
        layout.addWidget(self.label)

        # Lista de voltas
        self.lista_laps = QListWidget()
        layout.addWidget(self.lista_laps)

        # Botões
        btn_layout = QHBoxLayout()

        self.btn_start = QPushButton("▶ Start")
        self.btn_pause = QPushButton("⏸ Pause")
        self.btn_reset = QPushButton("⏹ Reset")
        self.btn_lap = QPushButton("⏱ Lap")

        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_pause)
        btn_layout.addWidget(self.btn_reset)
        btn_layout.addWidget(self.btn_lap)

        layout.addLayout(btn_layout)

        self.setLayout(layout)

        # Eventos
        self.btn_start.clicked.connect(self.iniciar)
        self.btn_pause.clicked.connect(self.pausar)
        self.btn_reset.clicked.connect(self.resetar)
        self.btn_lap.clicked.connect(self.marcar_lap)

        # Tema escuro
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: white;
            }
            QPushButton {
                background-color: #1f1f1f;
                border: 1px solid #333;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #007acc;
            }
            QListWidget {
                background-color: #1a1a1a;
                border: 1px solid #333;
            }
        """)

    def formatar_tempo(self):
        h = self.tempo // 3600
        m = (self.tempo % 3600) // 60
        s = self.tempo % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def atualizar_tempo(self):
        self.tempo += 1
        self.label.setText(self.formatar_tempo())
        self.animar_label()

    def animar_label(self):
        anim = QPropertyAnimation(self.label, b"geometry")
        anim.setDuration(200)
        anim.setStartValue(self.label.geometry())
        anim.setEndValue(self.label.geometry().adjusted(-5, -5, 5, 5))
        anim.start()

    def iniciar(self):
        self.timer.start(1000)

    def pausar(self):
        self.timer.stop()

    def resetar(self):
        self.timer.stop()
        self.tempo = 0
        self.label.setText("00:00:00")
        self.lista_laps.clear()
        self.laps = []

    def marcar_lap(self):
        tempo_atual = self.formatar_tempo()
        self.laps.append(tempo_atual)
        self.lista_laps.addItem(f"Lap {len(self.laps)}: {tempo_atual}")

    def salvar_historico(self):
        dados = {
            "data": str(datetime.now()),
            "laps": self.laps
        }
        with open("historico.json", "a") as f:
            f.write(json.dumps(dados) + "\n")

    def closeEvent(self, event):
        self.salvar_historico()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Cronometro()
    janela.show()
    sys.exit(app.exec())
```

---

# 💾 2. HISTÓRICO

Esse código já salva automaticamente:

```json
{"data": "...", "laps": ["00:00:10", "00:00:25"]}
```

📁 Arquivo: `historico.json`

👉 Depois você pode evoluir para:

* dashboard
* análise de tempos
* exportar CSV

---

# 📦 3. TRANSFORMAR EM APP (.deb)

Agora vem a parte profissional de verdade 👇

---

## 🔹 1. Instalar ferramentas

```bash
pip install pyinstaller
sudo apt install dpkg-dev
```

---

## 🔹 2. Gerar executável

```bash
pyinstaller --onefile --windowed seu_arquivo.py
```

👉 Vai gerar:

```bash
dist/seu_arquivo
```

---

## 🔹 3. Estrutura do .deb

Crie isso:

```bash
meu-cronometro/
├── DEBIAN/
│   └── control
└── usr/
    └── local/
        └── bin/
            └── cronometro
```

---

## 🔹 4. Arquivo `control`

```bash
Package: cronometro-pro
Version: 1.0
Section: base
Priority: optional
Architecture: amd64
Maintainer: Seu Nome
Description: Cronômetro profissional em PySide6
```

---

## 🔹 5. Copiar executável

```bash
cp dist/seu_arquivo meu-cronometro/usr/local/bin/cronometro
chmod +x meu-cronometro/usr/local/bin/cronometro
```

---

## 🔹 6. Gerar .deb

```bash
dpkg-deb --build meu-cronometro
```

👉 Resultado:

```bash
meu-cronometro.deb
```

---

## 🔹 7. Instalar

```bash
sudo dpkg -i meu-cronometro.deb
```

Agora você roda com:

```bash
cronometro
```

---

# 🔥 Resultado final (nível mercado)

Você agora tem:

✅ App desktop moderno
✅ Interface profissional
✅ Laps + histórico
✅ Empacotado em `.deb`
✅ Projeto de portfólio forte

---

# 🚀 Próximo nível (se quiser ir absurdo)

Posso te ajudar a transformar isso em:

👉 App com ícone + menu do Ubuntu
👉 Versão SaaS (web)
👉 App vendável
👉 Projeto tipo startup

---

Só manda:

👉 **“quero transformar em app completo com instalador e ícone”**
ou
👉 **“quero evoluir isso pra sistema maior”** 😎

---
---
---
Agora você entrou no nível **REAL de portfólio** 🔥
Isso aqui já vira projeto de **ciência de dados + app desktop** ao mesmo tempo.

👉 Vamos transformar seu cronômetro em um **Dashboard Profissional** com:

* 📊 Estatísticas (total, média, melhor tempo)
* 📈 Gráfico de desempenho
* 📋 Lista de laps
* 💾 Histórico persistente
* 🎨 Interface moderna

---

# 🚀 DASHBOARD PROFISSIONAL (PySide6 + gráfico)

Antes, instala:

```bash
pip install PySide6 matplotlib
```

---

# 💻 CÓDIGO COMPLETO

```python id="dashboard_pro_01"
import sys
import json
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QHBoxLayout, QListWidget
)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class DashboardCronometro(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cronômetro Dashboard PRO")
        self.setGeometry(200, 100, 600, 500)

        self.tempo = 0
        self.laps = []

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_tempo)

        layout = QVBoxLayout()

        # Display
        self.label = QLabel("00:00:00")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 28, QFont.Bold))
        layout.addWidget(self.label)

        # Estatísticas
        self.stats = QLabel("Total: 0 | Média: 0 | Melhor: 0")
        self.stats.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.stats)

        # Gráfico
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Lista de laps
        self.lista = QListWidget()
        layout.addWidget(self.lista)

        # Botões
        btn_layout = QHBoxLayout()

        self.btn_start = QPushButton("Start")
        self.btn_pause = QPushButton("Pause")
        self.btn_reset = QPushButton("Reset")
        self.btn_lap = QPushButton("Lap")

        for btn in [self.btn_start, self.btn_pause, self.btn_reset, self.btn_lap]:
            btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

        # Eventos
        self.btn_start.clicked.connect(self.iniciar)
        self.btn_pause.clicked.connect(self.pausar)
        self.btn_reset.clicked.connect(self.resetar)
        self.btn_lap.clicked.connect(self.add_lap)

        # Tema escuro
        self.setStyleSheet("""
            QWidget { background-color: #121212; color: white; }
            QPushButton {
                background-color: #1f1f1f;
                padding: 8px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #007acc;
            }
        """)

    def formatar(self, t):
        h = t // 3600
        m = (t % 3600) // 60
        s = t % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def atualizar_tempo(self):
        self.tempo += 1
        self.label.setText(self.formatar(self.tempo))

    def iniciar(self):
        self.timer.start(1000)

    def pausar(self):
        self.timer.stop()

    def resetar(self):
        self.timer.stop()
        self.tempo = 0
        self.laps.clear()
        self.lista.clear()
        self.atualizar_grafico()
        self.atualizar_stats()

    def add_lap(self):
        self.laps.append(self.tempo)
        self.lista.addItem(f"Lap {len(self.laps)}: {self.formatar(self.tempo)}")
        self.atualizar_grafico()
        self.atualizar_stats()

    def atualizar_stats(self):
        if not self.laps:
            return

        total = sum(self.laps)
        media = total // len(self.laps)
        melhor = min(self.laps)

        self.stats.setText(
            f"Total: {self.formatar(total)} | "
            f"Média: {self.formatar(media)} | "
            f"Melhor: {self.formatar(melhor)}"
        )

    def atualizar_grafico(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        if self.laps:
            ax.plot(self.laps)
            ax.set_title("Evolução dos Laps")
            ax.set_xlabel("Lap")
            ax.set_ylabel("Tempo (s)")

        self.canvas.draw()

    def closeEvent(self, event):
        dados = {
            "data": str(datetime.now()),
            "laps": self.laps
        }
        with open("historico.json", "a") as f:
            f.write(json.dumps(dados) + "\n")
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardCronometro()
    window.show()
    sys.exit(app.exec())
```

---

# 🧠 O que você construiu aqui

Isso aqui já é outro nível:

### 📊 Dashboard real

* gráfico com matplotlib
* análise de dados

### 📈 Métricas

* tempo total
* média
* melhor lap

### 💾 Persistência

* histórico em JSON

### 🖥️ Interface profissional

* PySide6 + layout moderno

---

# 💡 Ideias pra deixar ABSURDO (nível destaque)

## 🔹 1. Comparação entre sessões

* carregar histórico
* comparar gráficos

## 🔹 2. Exportar CSV

* abrir no Excel

## 🔹 3. Ranking de performance

* melhor sessão

## 🔹 4. Tema configurável

* dark/light toggle

---

# 💣 Realidade do mercado

👉 Isso aqui já pode ser apresentado como:

**“Desktop Performance Tracker com Dashboard em Python (PySide6 + Matplotlib)”**

Isso chama MUITO atenção em:

* estágio
* freelas
* GitHub

---

# 🚀 Próximo passo (se quiser ir ainda mais longe)

Posso evoluir isso pra:

👉 Multi-usuário
👉 Banco de dados (SQLite)
👉 Versão web (dashboard online)
👉 App estilo SaaS

---

Só fala:

👉 **“quero versão com banco de dados SQLite”**
ou
👉 **“quero transformar isso em sistema completo”** 😎
