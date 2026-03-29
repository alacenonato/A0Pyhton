Perfeito. Projeto 9 é **simples, mas MUITO importante** pra sua base.

---

# 🚀 Projeto 9 — Tabuada Automática

## 🎯 Objetivo

Criar um programa que gera a tabuada de um número escolhido pelo usuário.

---

## 🧠 O que você vai treinar

* Entrada de dados (`input`)
* Laços de repetição (`for`)
* Operações matemáticas
* Formatação de saída

---

## 📌 Regras do projeto (versão inicial)

O programa deve:

1. Pedir um número ao usuário
2. Mostrar a tabuada de 1 até 10
3. Exibir no formato:

```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

# 🛠️ Passo a passo (pense assim antes de codar)

### 1. Entrada

* Pedir número

### 2. Processamento

* Repetir de 1 até 10
* Multiplicar

### 3. Saída

* Mostrar cada linha

---

# 💻 Código base (faça junto)

```python
numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

---

# 🔥 AGORA VEM A PARTE IMPORTANTE (EVOLUIR)

Não para no básico. Faz essas melhorias:

---

## 🧩 Desafio 1 — Intervalo personalizado

Permitir que o usuário escolha até onde vai a tabuada:

```python
inicio = int(input("Início: "))
fim = int(input("Fim: "))
```

---

## 🧩 Desafio 2 — Várias tabuadas

Permitir que o usuário gere várias tabuadas:

```
Deseja continuar? (s/n)
```

---

## 🧩 Desafio 3 — Tabuada completa (1 a 10)

Mostrar todas as tabuadas automaticamente.

---

## 🧩 Desafio 4 — Formatação bonita

Exemplo:

```
==========
TABUADA DO 5
==========
```

---

## 🧩 Desafio 5 — Validação de entrada

Evitar erro se o usuário digitar texto:

```python
try:
    numero = int(input("Digite um número: "))
except:
    print("Digite um número válido!")
```

---

# 💡 Versão melhorada (nível iniciante forte)

```python
while True:
    try:
        numero = int(input("\nDigite um número: "))
        
        print("\n" + "="*20)
        print(f"TABUADA DO {numero}")
        print("="*20)

        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

        opcao = input("\nDeseja continuar? (s/n): ").lower()
        if opcao != 's':
            break

    except ValueError:
        print("❌ Digite um número válido!")
```

---

# 🧠 MISSÃO (FAÇA DE VERDADE)

Antes de ir pro próximo projeto:

✅ Digite o código sozinho
✅ Faça pelo menos 2 melhorias
✅ Rode várias vezes
✅ Teste erros

---

# 🚀 PRÓXIMO NÍVEL (SE QUISER IR ALÉM)

Posso te desafiar com uma versão mais forte:

👉 Tabuada com menu (tipo sistema)
👉 Tabuada em arquivo `.txt`
👉 Interface gráfica (Tkinter)

---

Se quiser continuar comigo no ritmo certo, fala:

👉 **"Projeto 10"**
ou
👉 **"Quero deixar esse mais avançado"** 🔥

# MAIS E MAIS

Perfeito — agora você saiu do básico e já está pensando como alguém que evolui rápido 🚀

Vou te entregar uma **versão completa da tabuada**, com **TODOS os desafios implementados** + organização de código (nível iniciante/intermediário forte).

---

# 💻 ✅ Tabuada Completa (Versão Profissional Inicial)

```python
def gerar_tabuada(numero, inicio, fim):
    print("\n" + "="*25)
    print(f"     TABUADA DO {numero}")
    print("="*25)

    for i in range(inicio, fim + 1):
        print(f"{numero} x {i} = {numero * i}")


def tabuada_completa(inicio, fim):
    print("\n" + "="*25)
    print("   TABUADA COMPLETA (1 a 10)")
    print("="*25)

    for n in range(1, 11):
        print("\n" + "-"*20)
        print(f"Tabuada do {n}")
        print("-"*20)
        for i in range(inicio, fim + 1):
            print(f"{n} x {i} = {n * i}")


while True:
    try:
        print("\n" + "="*30)
        print("      SISTEMA DE TABUADA")
        print("="*30)
        print("1 - Tabuada de um número")
        print("2 - Tabuada completa (1 a 10)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Encerrando...")
            break

        elif opcao in ['1', '2']:
            inicio = int(input("Início da tabuada: "))
            fim = int(input("Fim da tabuada: "))

            if inicio > fim:
                print("❌ O início não pode ser maior que o fim!")
                continue

            if opcao == '1':
                numero = int(input("Digite o número: "))
                gerar_tabuada(numero, inicio, fim)

            elif opcao == '2':
                tabuada_completa(inicio, fim)

        else:
            print("❌ Opção inválida!")

        continuar = input("\nDeseja continuar? (s/n): ").lower()
        if continuar != 's':
            print("Finalizando sistema...")
            break

    except ValueError:
        print("❌ Digite apenas números válidos!")
```

---

# 🔥 O que você aplicou aqui (isso é MUITO importante)

Você acabou de usar:

✅ Funções (`def`)
✅ Reutilização de código
✅ Laços (`for`, `while`)
✅ Tratamento de erro (`try/except`)
✅ Validação de entrada
✅ Menu interativo
✅ Organização de código (nível profissional inicial)

👉 Isso já te coloca **acima da maioria dos iniciantes**.

---

# 🧠 COMO MELHORAR AINDA MAIS (nível 2)

Se quiser subir de nível, tenta isso:

### 💾 1. Salvar em arquivo

Salvar a tabuada em `tabuada.txt`

---

### 🎨 2. Interface melhor

* Alinhar números
* Usar formatação tipo tabela

---

### 📊 3. Exportar como CSV

Pra abrir no Excel (olha seu interesse em contabilidade 👀)

---

### 🖥️ 4. Interface gráfica (Tkinter)

Transformar em app

---

# 🚀 DESAFIO EXTRA (MENTOR MODE)

👉 Adapte isso para:

💰 “Tabuada financeira”

* juros simples
* juros compostos
* parcelas

---

# 📌 PRÓXIMO PASSO

Agora você tem 2 caminhos:

👉 Continuar sequência:
**"Projeto 10"**

👉 Ou evoluir mais:
**"Quero transformar isso em app"**

👉 Ou focar no seu objetivo:
**"Quero versão contábil"**

Só fala que eu te levo pro próximo nível 🔥

# MAIS E MAIS

Boa decisão — isso aqui já é **nível acima da maioria dos iniciantes** 🔥
Usar `rich` deixa seu projeto com cara de **ferramenta profissional de terminal**.

---

# 🚀 Primeiro: instalar o Rich

No terminal:

```bash
pip install rich
```

---

# 💻 ✅ Tabuada com Interface Profissional (Rich)

```python
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich import box

console = Console()


def gerar_tabuada(numero, inicio, fim):
    table = Table(
        title=f"Tabuada do {numero}",
        box=box.DOUBLE,
        style="cyan"
    )

    table.add_column("Operação", justify="center")
    table.add_column("Resultado", justify="center", style="green")

    for i in range(inicio, fim + 1):
        table.add_row(f"{numero} x {i}", str(numero * i))

    console.print(table)


def tabuada_completa(inicio, fim):
    for n in range(1, 11):
        gerar_tabuada(n, inicio, fim)


def menu():
    console.print(Panel.fit(
        "[bold yellow]SISTEMA DE TABUADA[/bold yellow]\n"
        "[1] Tabuada de um número\n"
        "[2] Tabuada completa (1 a 10)\n"
        "[0] Sair",
        border_style="blue"
    ))


while True:
    menu()

    opcao = Prompt.ask("\nEscolha uma opção", choices=["1", "2", "0"])

    if opcao == "0":
        console.print("\n[bold red]Encerrando sistema...[/bold red]")
        break

    try:
        inicio = IntPrompt.ask("Início da tabuada")
        fim = IntPrompt.ask("Fim da tabuada")

        if inicio > fim:
            console.print("[bold red]Erro: início maior que fim![/bold red]")
            continue

        if opcao == "1":
            numero = IntPrompt.ask("Digite o número")
            gerar_tabuada(numero, inicio, fim)

        elif opcao == "2":
            tabuada_completa(inicio, fim)

        continuar = Prompt.ask(
            "\nDeseja continuar?",
            choices=["s", "n"],
            default="s"
        )

        if continuar == "n":
            console.print("[bold red]Finalizando...[/bold red]")
            break

    except Exception:
        console.print("[bold red]Erro: entrada inválida![/bold red]")
```

---

# 🔥 O que você ganhou com isso

Agora seu projeto tem:

✅ Interface bonita no terminal
✅ Menu profissional
✅ Tabelas organizadas
✅ Validação elegante (`Prompt`, `IntPrompt`)
✅ UX (experiência do usuário) melhor

👉 Isso aqui já parece **ferramenta real de portfólio**.

---

# 🧠 Se quiser subir MAIS um nível

Posso evoluir isso pra você com:

### 💾 Exportação

* Salvar tabela em `.txt` ou `.csv`

### 🎯 CLI profissional

* Usar `typer` ou `argparse`

### 🖥️ Interface gráfica

* Tkinter ou PyQt

### 📦 Empacotar como programa

* `.exe` com PyInstaller

---

# 🚀 Próximo passo

Me fala o que você quer agora:

👉 **"Projeto 10"** (continuar sequência)
👉 **"Quero salvar em CSV"**
👉 **"Quero transformar em app"**
👉 **"Quero versão contábil"**

Tô te guiando como mentor — só seguir que você chega forte no mercado 🔥

# MAIS E MAIS

Boa — agora você subiu de nível de verdade 🔥
Vamos transformar sua tabuada em um **app desktop com PySide6 (Qt)**.

---

# 🚀 1. Instalar PySide6

No terminal:

```bash
pip install PySide6
```

---

# 💻 ✅ App Tabuada com Interface Gráfica (PySide6)

Esse app tem:

✅ Campo para número
✅ Intervalo (início/fim)
✅ Botões (gerar / limpar)
✅ Tabela organizada
✅ Tabuada completa
✅ Interface bonita (estilo Qt)

---

```python
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QMessageBox
)


class TabuadaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Tabuada")
        self.setGeometry(300, 200, 500, 400)

        self.layout = QVBoxLayout()

        # Inputs
        self.numero_input = QLineEdit()
        self.numero_input.setPlaceholderText("Número (opcional p/ tabuada completa)")

        self.inicio_input = QLineEdit()
        self.inicio_input.setPlaceholderText("Início")

        self.fim_input = QLineEdit()
        self.fim_input.setPlaceholderText("Fim")

        self.layout.addWidget(QLabel("Digite os valores:"))
        self.layout.addWidget(self.numero_input)
        self.layout.addWidget(self.inicio_input)
        self.layout.addWidget(self.fim_input)

        # Botões
        botoes_layout = QHBoxLayout()

        self.btn_gerar = QPushButton("Gerar Tabuada")
        self.btn_gerar.clicked.connect(self.gerar_tabuada)

        self.btn_completa = QPushButton("Tabuada Completa")
        self.btn_completa.clicked.connect(self.tabuada_completa)

        self.btn_limpar = QPushButton("Limpar")
        self.btn_limpar.clicked.connect(self.limpar_tabela)

        botoes_layout.addWidget(self.btn_gerar)
        botoes_layout.addWidget(self.btn_completa)
        botoes_layout.addWidget(self.btn_limpar)

        self.layout.addLayout(botoes_layout)

        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(2)
        self.tabela.setHorizontalHeaderLabels(["Operação", "Resultado"])

        self.layout.addWidget(self.tabela)

        self.setLayout(self.layout)

    def validar_inputs(self):
        try:
            inicio = int(self.inicio_input.text())
            fim = int(self.fim_input.text())

            if inicio > fim:
                raise ValueError

            return inicio, fim
        except:
            QMessageBox.warning(self, "Erro", "Digite valores válidos para início e fim.")
            return None, None

    def gerar_tabuada(self):
        inicio, fim = self.validar_inputs()
        if inicio is None:
            return

        try:
            numero = int(self.numero_input.text())
        except:
            QMessageBox.warning(self, "Erro", "Digite um número válido.")
            return

        self.tabela.setRowCount(0)

        for i in range(inicio, fim + 1):
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)

            self.tabela.setItem(row, 0, QTableWidgetItem(f"{numero} x {i}"))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(numero * i)))

    def tabuada_completa(self):
        inicio, fim = self.validar_inputs()
        if inicio is None:
            return

        self.tabela.setRowCount(0)

        for n in range(1, 11):
            for i in range(inicio, fim + 1):
                row = self.tabela.rowCount()
                self.tabela.insertRow(row)

                self.tabela.setItem(row, 0, QTableWidgetItem(f"{n} x {i}"))
                self.tabela.setItem(row, 1, QTableWidgetItem(str(n * i)))

    def limpar_tabela(self):
        self.tabela.setRowCount(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TabuadaApp()
    janela.show()
    sys.exit(app.exec())
```

---

# 🎯 Como executar

Salva como:

```bash
tabuada_gui.py
```

Depois roda:

```bash
python tabuada_gui.py
```

---

# 🔥 O que você acabou de aprender

Isso aqui já é MUITO relevante:

✅ Interface gráfica real (Qt)
✅ Eventos (botões clicáveis)
✅ Validação de entrada
✅ Tabela dinâmica
✅ Estrutura orientada a objetos

👉 Isso já entra no seu portfólio fácil.

---

# 🧠 Como deixar MUITO mais profissional

Se quiser evoluir esse projeto:

### 🎨 Visual melhor

* Tema escuro (QSS)
* Ícones

### 💾 Exportação

* Botão "Exportar CSV"

### 📊 Organização

* Separar lógica em outro arquivo (arquitetura)

### 📦 Executável

* Gerar `.exe` com PyInstaller

---

# 🚀 Próximo nível (recomendado)

Posso te levar pra:

👉 **Projeto 10 (com GUI também)**
👉 Evoluir esse app para **calculadora completa**
👉 Criar um **sistema financeiro (nível contábil)**
👉 Transformar isso em **software vendável**

---

Só fala:

👉 **"quero evoluir esse app"**
ou
👉 **"projeto 10"**

que eu continuo te guiando 🔥
