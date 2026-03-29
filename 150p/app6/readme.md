Perfeito. Projeto 6 é **um divisor de águas na sua lógica** — aqui você começa a pensar como programador de verdade.

---

# 🧩 PROJETO 6 — Verificador de Número Primo

## 🎯 Objetivo

Criar um programa que verifica se um número é **primo ou não**.

---

## 🧠 Conceito (simples e direto)

Um número primo:
👉 Só pode ser dividido por **1 e por ele mesmo**

Exemplos:

* 2 → primo ✅
* 3 → primo ✅
* 4 → não primo ❌ (divisível por 2)
* 7 → primo ✅

---

## 🔥 LÓGICA DO PROGRAMA

1. Receber um número
2. Testar divisões
3. Se tiver mais de 2 divisores → NÃO é primo

---

## 💻 VERSÃO 1 (BÁSICA — FAÇA ESSA PRIMEIRO)

```python
numero = int(input("Digite um número: "))

if numero <= 1:
    print("Não é primo")
else:
    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("É primo")
    else:
        print("Não é primo")
```

---

## 🧠 EXPLICAÇÃO RÁPIDA

* `range(2, numero)` → testa divisores
* `%` → verifica se sobra resto
* `break` → para o loop quando acha divisor

---

# 🚀 DESAFIOS (FAZ ISSO!)

## 🧩 Desafio 1 — Mostrar divisores

Exemplo:

```
Número: 12  
Divisores: 1, 2, 3, 4, 6, 12
```

---

## 🧩 Desafio 2 — Melhorar performance

👉 Testar até a raiz do número (mais avançado)

```python
import math

for i in range(2, int(math.sqrt(numero)) + 1):
```

---

## 🧩 Desafio 3 — Verificar vários números

Exemplo:

```
Digite vários números separados por vírgula:
```

---

## 🧩 Desafio 4 — Contar quantos primos existem até N

Exemplo:

```
Até 100 → existem 25 números primos
```

---

# 🔥 VERSÃO MELHORADA (NÍVEL INTERMEDIÁRIO)

```python
import math

numero = int(input("Digite um número: "))

if numero <= 1:
    print("Não é primo")
else:
    primo = True

    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("É primo")
    else:
        print("Não é primo")
```

---

# 🧠 MISSÃO DE VERDADE (IMPORTANTE)

Depois de fazer:

✅ Suba no GitHub
✅ Crie um README com:

* O que o projeto faz
* Como usar
* Exemplo de entrada/saída

---

# 🚀 SE QUISER EVOLUIR MAIS

Posso te levar pro próximo nível desse projeto:

👉 Interface gráfica (PySide6)
👉 API com Flask
👉 Versão web
👉 Ou integrar com um sistema maior

---

Se quiser continuar no ritmo forte:

👉 fala: **“Projeto 7”**

ou

👉 **“Quero versão avançada desse projeto”** 😎


# MAIS E MAIS


Perfeito — agora você está pensando como desenvolvedor de verdade 😎
Vou te entregar uma **versão única, completa e profissional**, juntando TODOS os desafios (1 a 4) em um só programa.

---

# 🚀 PROJETO 6 — VERSÃO COMPLETA (PRO)

## ✅ O que esse programa faz:

✔ Verifica se um número é primo
✔ Mostra todos os divisores
✔ Aceita múltiplos números
✔ Conta quantos números primos existem até N
✔ Usa lógica otimizada (raiz quadrada)

---

# 💻 CÓDIGO COMPLETO

```python
import math

# -----------------------------
# Função: verificar se é primo
# -----------------------------
def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False

    return True


# -----------------------------
# Função: listar divisores
# -----------------------------
def listar_divisores(numero):
    divisores = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)

    return divisores


# -----------------------------
# Função: contar primos até N
# -----------------------------
def contar_primos(limite):
    contador = 0

    for i in range(2, limite + 1):
        if eh_primo(i):
            contador += 1

    return contador


# -----------------------------
# MENU PRINCIPAL
# -----------------------------
def menu():
    while True:
        print("\n===== VERIFICADOR DE NÚMEROS PRIMOS =====")
        print("1 - Verificar um número")
        print("2 - Verificar vários números")
        print("3 - Contar primos até N")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        # -----------------------------
        # OPÇÃO 1
        # -----------------------------
        if opcao == "1":
            numero = int(input("Digite um número: "))

            if eh_primo(numero):
                print(f"{numero} é PRIMO ✅")
            else:
                print(f"{numero} NÃO é primo ❌")

            divisores = listar_divisores(numero)
            print(f"Divisores: {divisores}")

        # -----------------------------
        # OPÇÃO 2
        # -----------------------------
        elif opcao == "2":
            entrada = input("Digite números separados por vírgula: ")
            numeros = [int(n.strip()) for n in entrada.split(",")]

            for numero in numeros:
                if eh_primo(numero):
                    resultado = "PRIMO ✅"
                else:
                    resultado = "NÃO primo ❌"

                divisores = listar_divisores(numero)
                print(f"\nNúmero: {numero}")
                print(f"Resultado: {resultado}")
                print(f"Divisores: {divisores}")

        # -----------------------------
        # OPÇÃO 3
        # -----------------------------
        elif opcao == "3":
            limite = int(input("Contar primos até: "))
            total = contar_primos(limite)

            print(f"Existem {total} números primos até {limite}")

        # -----------------------------
        # SAIR
        # -----------------------------
        elif opcao == "0":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida!")


# -----------------------------
# EXECUÇÃO
# -----------------------------
menu()
```

---

# 🧠 O QUE VOCÊ APRENDEU AQUI (NÍVEL SUBIU 🔥)

Com esse projeto você já praticou:

* ✔ Funções (`def`)
* ✔ Modularização
* ✔ Loop (`for`, `while`)
* ✔ Condicionais
* ✔ Listas
* ✔ Entrada de dados
* ✔ Lógica otimizada (`sqrt`)
* ✔ Estrutura de menu (muito usado em sistemas reais)

👉 Isso já é **nível intermediário inicial**

---

# 🔥 DESAFIO EXTRA (NÍVEL HARD)

Se quiser ficar MUITO à frente:

👉 Adicione:

* Tratamento de erro (`try/except`)
* Interface mais bonita (cores no terminal)
* Salvar resultados em arquivo `.txt`
* Tempo de execução do algoritmo

---

# 🚀 MISSÃO AGORA

1. Copia esse código
2. Testa tudo
3. Modifica algo (IMPORTANTE!)
4. Sobe no GitHub

---

Se quiser subir o nível ainda mais:

👉 fala: **“Projeto 7”**
ou
👉 **“Quero transformar isso em API”**


# MAIS E MAIS

Perfeito — agora você está entrando no **nível profissional de verdade** 🔥
Vamos transformar esse projeto em uma **aplicação com interface gráfica (PySide6)** + **tratamento de erros completo**.

---

# 🚀 PROJETO 6 — VERSÃO GUI (PySide6 + Tratamento de Erros)

## ✅ O que essa versão tem:

✔ Interface gráfica (janela)
✔ Campo para entrada de dados
✔ Botões para ações
✔ Exibição organizada dos resultados
✔ Tratamento de erro (`try/except`)
✔ Todas as funcionalidades (1 a 4)

---

# 📦 PASSO 1 — INSTALAR O PySide6

No terminal:

```bash
pip install PySide6
```

---

# 💻 CÓDIGO COMPLETO (GUI)

```python
import sys
import math
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QTextEdit, QMessageBox
)


# -----------------------------
# LÓGICA
# -----------------------------
def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False

    return True


def listar_divisores(numero):
    return [i for i in range(1, numero + 1) if numero % i == 0]


def contar_primos(limite):
    return sum(1 for i in range(2, limite + 1) if eh_primo(i))


# -----------------------------
# INTERFACE
# -----------------------------
class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Verificador de Números Primos")
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Digite um número ou vários (separados por vírgula):")
        layout.addWidget(self.label)

        self.input = QLineEdit()
        layout.addWidget(self.input)

        # Botões
        self.btn_verificar = QPushButton("Verificar Número(s)")
        self.btn_verificar.clicked.connect(self.verificar)
        layout.addWidget(self.btn_verificar)

        self.btn_contar = QPushButton("Contar Primos até N")
        self.btn_contar.clicked.connect(self.contar)
        layout.addWidget(self.btn_contar)

        # Área de saída
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    # -----------------------------
    # FUNÇÃO: VERIFICAR
    # -----------------------------
    def verificar(self):
        entrada = self.input.text()

        try:
            numeros = [int(n.strip()) for n in entrada.split(",")]

            self.output.clear()

            for numero in numeros:
                resultado = "PRIMO ✅" if eh_primo(numero) else "NÃO primo ❌"
                divisores = listar_divisores(numero)

                self.output.append(f"Número: {numero}")
                self.output.append(f"Resultado: {resultado}")
                self.output.append(f"Divisores: {divisores}")
                self.output.append("-" * 30)

        except ValueError:
            QMessageBox.critical(self, "Erro", "Digite apenas números válidos!")

    # -----------------------------
    # FUNÇÃO: CONTAR PRIMOS
    # -----------------------------
    def contar(self):
        entrada = self.input.text()

        try:
            limite = int(entrada)

            if limite < 0:
                raise ValueError

            total = contar_primos(limite)

            self.output.clear()
            self.output.append(f"Existem {total} números primos até {limite}")

        except ValueError:
            QMessageBox.critical(self, "Erro", "Digite um número inteiro positivo!")


# -----------------------------
# EXECUÇÃO
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = App()
    janela.show()
    sys.exit(app.exec())
```

---

# 🧠 O QUE VOCÊ APRENDEU AQUI (NÍVEL SUBIU MUITO)

Agora você já sabe:

✔ Criar interface gráfica
✔ Trabalhar com eventos (botões)
✔ Usar `try/except` corretamente
✔ Separar lógica da interface
✔ Criar apps reais (não só terminal)

👉 Isso já é **nível intermediário/avançado inicial**

---

# 🔥 MELHORIAS (SE QUISER FICAR DIFERENCIADO)

Se quiser deixar isso MUITO forte pro portfólio:

## 💡 Ideias:

* Adicionar tema escuro 🌙
* Botão para limpar tela
* Exportar resultado para `.txt`
* Mostrar tempo de execução
* Mostrar quantidade de divisores
* Interface mais bonita (QGridLayout)

---

# 🚀 PRÓXIMO NÍVEL

Se quiser evoluir ainda mais esse projeto:

👉 Transformar em **aplicação web (Flask)**
👉 Criar **API de números primos**
👉 Ou integrar em um **sistema maior**

---

Se quiser continuar:

👉 fala: **“Projeto 7”**
ou
👉 **“Quero deixar esse com cara de sistema profissional”** 😎
