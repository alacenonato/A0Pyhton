Boa. Agora você começou a usar o plano do jeito certo 🚀

---

# 🎯 PROJETO 14 — Gerador de Números Aleatórios

## 🧠 Objetivo do projeto

Aqui você vai treinar:

* Biblioteca `random`
* Entrada de dados (`input`)
* Validação
* Estrutura de repetição
* Organização em funções

---

# 🧱 Nível 1 — Versão básica (obrigatória)

## 📌 Requisitos

O programa deve:

* Pedir um número mínimo
* Pedir um número máximo
* Gerar um número aleatório entre eles
* Mostrar o resultado

---

## 💻 Código

```python
import random

def gerar_numero(minimo, maximo):
    return random.randint(minimo, maximo)

def main():
    print("=== Gerador de Números Aleatórios ===")
    
    try:
        minimo = int(input("Digite o valor mínimo: "))
        maximo = int(input("Digite o valor máximo: "))
        
        if minimo > maximo:
            print("Erro: o valor mínimo não pode ser maior que o máximo.")
            return
        
        numero = gerar_numero(minimo, maximo)
        print(f"Número gerado: {numero}")
    
    except ValueError:
        print("Erro: digite apenas números inteiros.")

if __name__ == "__main__":
    main()
```

---

# ⚙️ Melhorias (faça obrigatoriamente)

Agora começa o que realmente te faz evoluir 👇

---

## 🔁 1. Permitir repetir várias vezes

Perguntar se o usuário quer gerar outro número.

---

## 🎯 2. Gerar múltiplos números

Exemplo:

> Quantos números você quer gerar?

---

## 🚫 3. Evitar números repetidos

(usa `random.sample`)

---

## 📊 4. Mostrar estatísticas

* Maior número
* Menor número
* Média

---

# 💻 Versão melhorada (nível intermediário)

```python
import random

def gerar_numeros(minimo, maximo, quantidade):
    return random.sample(range(minimo, maximo + 1), quantidade)

def mostrar_estatisticas(numeros):
    print("\n📊 Estatísticas:")
    print(f"Maior: {max(numeros)}")
    print(f"Menor: {min(numeros)}")
    print(f"Média: {sum(numeros)/len(numeros):.2f}")

def main():
    print("=== Gerador Avançado ===")
    
    while True:
        try:
            minimo = int(input("Mínimo: "))
            maximo = int(input("Máximo: "))
            quantidade = int(input("Quantidade de números: "))
            
            if minimo > maximo:
                print("Erro: mínimo maior que máximo.")
                continue
            
            if quantidade > (maximo - minimo + 1):
                print("Erro: quantidade maior que o intervalo disponível.")
                continue
            
            numeros = gerar_numeros(minimo, maximo, quantidade)
            
            print(f"\nNúmeros gerados: {numeros}")
            mostrar_estatisticas(numeros)
        
        except ValueError:
            print("Digite apenas números válidos.")
        
        continuar = input("\nGerar novamente? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
```

---

# 🧪 Desafios (FAÇA — isso que te evolui)

## 🥉 Fácil

* Permitir números decimais (`uniform`)
* Mostrar números ordenados

## 🥈 Médio

* Salvar resultados em arquivo `.txt`
* Criar histórico de execuções

## 🥇 Difícil

* Criar interface gráfica (Tkinter)
* Transformar em API com Flask

---

# 💡 Como isso vira projeto de portfólio

Se você quiser subir nível:

👉 Nome do projeto:
**random-number-generator-pro**

👉 README deve ter:

* Descrição
* Funcionalidades
* Como usar
* Exemplos

---

# 🚀 Próximo nível (se quiser evoluir de verdade)

Posso transformar esse projeto em algo MUITO mais forte:

👉 Gerador tipo **Mega-Sena / Loteria**
👉 Sistema com interface gráfica
👉 API que gera números via HTTP
👉 Versão com frontend (HTML/CSS/JS)

---

Se quiser continuar no ritmo:

👉 fala: **“Projeto 15”**
ou
👉 **“Quero versão GUI desse projeto”**

e a gente sobe o nível pesado 🔥

---
---
---

Perfeito. Agora você saiu do básico e entrou em **projeto que parece produto real** 🔥

---

# 🎯 PROJETO 14 (UPGRADE) — Gerador Mega-Sena

## 🧠 Regras reais da Mega-Sena

* Números de **1 a 60**
* Você escolhe de **6 a 15 números**
* **Não pode repetir número**
* Ordem não importa (mas vamos ordenar)

---

# 🧱 Versão 1 — Simples e funcional

```python id="mega1"
import random

def gerar_jogo(quantidade):
    return sorted(random.sample(range(1, 61), quantidade))

def main():
    print("=== Gerador de Mega-Sena ===")
    
    try:
        quantidade = int(input("Quantos números (6 a 15)? "))
        
        if quantidade < 6 or quantidade > 15:
            print("Erro: escolha entre 6 e 15 números.")
            return
        
        jogo = gerar_jogo(quantidade)
        print(f"Jogo gerado: {jogo}")
    
    except ValueError:
        print("Digite um número válido.")

if __name__ == "__main__":
    main()
```

---

# ⚙️ Versão 2 — Profissional (nível portfólio)

Agora sim começa a ficar forte 👇

## ✅ Funcionalidades

* Gerar **vários jogos**
* Mostrar números formatados (tipo volante)
* Estatísticas
* Repetição

---

```python id="mega2"
import random

def gerar_jogo(quantidade):
    return sorted(random.sample(range(1, 61), quantidade))

def gerar_varios_jogos(qtd_jogos, qtd_numeros):
    jogos = []
    for _ in range(qtd_jogos):
        jogos.append(gerar_jogo(qtd_numeros))
    return jogos

def formatar_jogo(jogo):
    return " | ".join(f"{num:02d}" for num in jogo)

def main():
    print("=== 🎰 GERADOR MEGA-SENA ===")
    
    while True:
        try:
            qtd_jogos = int(input("Quantos jogos deseja gerar? "))
            qtd_numeros = int(input("Quantos números por jogo (6 a 15)? "))
            
            if qtd_numeros < 6 or qtd_numeros > 15:
                print("Erro: escolha entre 6 e 15 números.")
                continue
            
            jogos = gerar_varios_jogos(qtd_jogos, qtd_numeros)
            
            print("\n🎯 Jogos Gerados:\n")
            for i, jogo in enumerate(jogos, 1):
                print(f"Jogo {i}: {formatar_jogo(jogo)}")
        
        except ValueError:
            print("Digite valores válidos.")
        
        continuar = input("\nGerar novamente? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
```

---

# 🔥 DIFERENCIAL (faça isso pra subir nível)

## 🧠 1. Simular resultado oficial

* Gerar 6 números “sorteados”
* Comparar com seus jogos

---

## 🏆 2. Verificar acertos

* 4 acertos → Quadra
* 5 acertos → Quina
* 6 acertos → Sena

---

## 💻 Exemplo de função

```python
def verificar_acertos(jogo, resultado):
    acertos = len(set(jogo) & set(resultado))
    return acertos
```

---

## 🎯 3. Mostrar resultado final

Exemplo:

```
Resultado oficial: 05 12 23 34 45 60

Jogo 1: 02 05 12 20 34 60 → 4 acertos (Quadra)
Jogo 2: 01 07 11 22 33 44 → 0 acertos
```

---

# 🥇 MISSÃO (isso aqui te evolui MUITO)

Implementa:

✔ Simulação completa de sorteio
✔ Comparação automática
✔ Ranking dos jogos
✔ Destaque do melhor jogo

---

# 🚀 Versão INSANA (nível freelancer)

Se quiser transformar isso em algo vendável:

👉 Interface gráfica (Tkinter ou PyQt)
👉 API com Flask (`/gerar-jogo`)
👉 Site com HTML/CSS + backend Python
👉 Salvar histórico de jogos
👉 Simular várias apostas (estratégias)

---

# 💡 Nome de projeto pra GitHub

👉 `mega-sena-generator-pro`

---

# 📌 Próximo passo (recomendado)

Agora você tem 3 caminhos:

1. 👉 **“Quero adicionar verificação de acertos”**
2. 👉 **“Quero versão com interface gráfica”**
3. 👉 **“Quero transformar em API com Flask”**

Se seguir nessa linha, em poucos projetos você já tá com nível de estágio forte 🚀

---
---
---

Você não é “ruim” — você só ainda não construiu repertório suficiente. Isso aqui que você pediu já é **nível intermediário de verdade**, então é normal travar.

Agora vamos resolver isso do jeito certo: **código pronto + explicação clara pra você aprender de verdade** 👇

---

# 🎯 Mega-Sena COMPLETO (com tudo que você pediu)

## ✅ O que esse sistema faz:

✔ Gera vários jogos
✔ Simula resultado oficial
✔ Compara automaticamente
✔ Classifica (Quadra, Quina, Sena)
✔ Faz ranking
✔ Destaca o melhor jogo

---

# 💻 CÓDIGO COMPLETO

```python
import random

# =========================
# GERAR JOGOS
# =========================
def gerar_jogo(qtd_numeros):
    return sorted(random.sample(range(1, 61), qtd_numeros))

def gerar_varios_jogos(qtd_jogos, qtd_numeros):
    return [gerar_jogo(qtd_numeros) for _ in range(qtd_jogos)]

# =========================
# RESULTADO OFICIAL
# =========================
def gerar_resultado():
    return sorted(random.sample(range(1, 61), 6))

# =========================
# VERIFICAR ACERTOS
# =========================
def verificar_acertos(jogo, resultado):
    acertos = len(set(jogo) & set(resultado))
    
    if acertos == 6:
        status = "SENA 🥇"
    elif acertos == 5:
        status = "QUINA 🥈"
    elif acertos == 4:
        status = "QUADRA 🥉"
    else:
        status = "-"
    
    return acertos, status

# =========================
# FORMATAR JOGO
# =========================
def formatar(jogo):
    return " ".join(f"{n:02d}" for n in jogo)

# =========================
# RANKING
# =========================
def ranking(jogos, resultado):
    resultado_final = []
    
    for i, jogo in enumerate(jogos, 1):
        acertos, status = verificar_acertos(jogo, resultado)
        
        resultado_final.append({
            "id": i,
            "jogo": jogo,
            "acertos": acertos,
            "status": status
        })
    
    # ordenar por número de acertos (maior primeiro)
    resultado_final.sort(key=lambda x: x["acertos"], reverse=True)
    
    return resultado_final

# =========================
# MAIN
# =========================
def main():
    print("=== 🎰 SIMULADOR MEGA-SENA ===\n")
    
    try:
        qtd_jogos = int(input("Quantos jogos deseja gerar? "))
        qtd_numeros = int(input("Quantos números por jogo (6 a 15)? "))
        
        if qtd_numeros < 6 or qtd_numeros > 15:
            print("Erro: escolha entre 6 e 15 números.")
            return
        
        # gerar jogos
        jogos = gerar_varios_jogos(qtd_jogos, qtd_numeros)
        
        print("\n🎯 Seus jogos:")
        for i, jogo in enumerate(jogos, 1):
            print(f"Jogo {i}: {formatar(jogo)}")
        
        # gerar resultado oficial
        resultado = gerar_resultado()
        print("\n🏆 Resultado oficial:")
        print(formatar(resultado))
        
        # ranking
        resultado_rank = ranking(jogos, resultado)
        
        print("\n📊 Resultado dos jogos:\n")
        for item in resultado_rank:
            print(
                f"Jogo {item['id']}: {formatar(item['jogo'])} "
                f"→ {item['acertos']} acertos {item['status']}"
            )
        
        # melhor jogo
        melhor = resultado_rank[0]
        print("\n🔥 Melhor jogo:")
        print(
            f"Jogo {melhor['id']} com {melhor['acertos']} acertos {melhor['status']}"
        )
    
    except ValueError:
        print("Digite valores válidos.")

if __name__ == "__main__":
    main()
```

---

# 🧠 EXPLICAÇÃO (SIMPLIFICADA)

## 🔹 1. `random.sample`

Gera números **sem repetir**

```python
random.sample(range(1, 61), 6)
```

---

## 🔹 2. Comparação de acertos (ESSENCIAL)

```python
set(jogo) & set(resultado)
```

👉 Isso pega os números iguais entre os dois

---

## 🔹 3. Ranking

```python
sort(key=lambda x: x["acertos"], reverse=True)
```

👉 Ordena do melhor pro pior

---

# 💣 O que você acabou de aprender (sem perceber)

Se você entendeu isso aqui, você já sabe:

* Estrutura de dados (`list`, `dict`)
* Funções organizadas
* Lógica de comparação
* Ordenação (nível importante)
* Simulação de sistema real

👉 Isso já é MUITO acima de iniciante

---

# 🔥 Próximo nível (RECOMENDO)

Se quiser evoluir de verdade agora:

👉 Adiciona isso:

* Salvar jogos em arquivo `.txt`
* Simular **1000 apostas automáticas**
* Mostrar estatística de vitórias
* Interface gráfica (Tkinter)

---

# 🚀 Agora presta atenção nisso

Você NÃO é ruim.

Você só fez o que 99% faz:
👉 tentou aprender sem estrutura

Agora você tá:

✔ fazendo projeto real
✔ entendendo lógica prática
✔ evoluindo do jeito certo

---

Se quiser continuar no ritmo:

👉 fala: **“Projeto 15”**
ou
👉 **“Quero transformar esse em sistema com interface gráfica”**

e a gente sobe mais um nível 🔥

---
---
---

Perfeito — agora você entrou num nível que **já chama atenção em portfólio** 🔥
Vamos transformar seu projeto em um **app com interface gráfica usando PySide6 (Qt)**.

---

# 🎯 O que vamos construir

Um app com:

✔ Inputs (quantidade de jogos e números)
✔ Botão para gerar
✔ Exibição dos jogos
✔ Resultado oficial
✔ Ranking automático
✔ Destaque do melhor jogo

---

# 📦 1. Instalação (obrigatório)

```bash
pip install PySide6
```

---

# 🧱 2. Código completo (GUI com PySide6)

```python
import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QSpinBox, QTextEdit
)

# =========================
# LÓGICA (mesma do projeto)
# =========================
def gerar_jogo(qtd):
    return sorted(random.sample(range(1, 61), qtd))

def gerar_varios(qtd_jogos, qtd_nums):
    return [gerar_jogo(qtd_nums) for _ in range(qtd_jogos)]

def gerar_resultado():
    return sorted(random.sample(range(1, 61), 6))

def verificar(jogo, resultado):
    acertos = len(set(jogo) & set(resultado))
    
    if acertos == 6:
        status = "SENA 🥇"
    elif acertos == 5:
        status = "QUINA 🥈"
    elif acertos == 4:
        status = "QUADRA 🥉"
    else:
        status = "-"
    
    return acertos, status

def formatar(jogo):
    return " ".join(f"{n:02d}" for n in jogo)

# =========================
# INTERFACE
# =========================
class MegaSenaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎰 Mega-Sena Pro")
        self.setGeometry(200, 200, 600, 500)

        layout = QVBoxLayout()

        # Inputs
        input_layout = QHBoxLayout()

        self.qtd_jogos = QSpinBox()
        self.qtd_jogos.setMinimum(1)
        self.qtd_jogos.setMaximum(100)
        self.qtd_jogos.setValue(5)

        self.qtd_numeros = QSpinBox()
        self.qtd_numeros.setMinimum(6)
        self.qtd_numeros.setMaximum(15)
        self.qtd_numeros.setValue(6)

        input_layout.addWidget(QLabel("Jogos:"))
        input_layout.addWidget(self.qtd_jogos)
        input_layout.addWidget(QLabel("Números:"))
        input_layout.addWidget(self.qtd_numeros)

        # Botão
        self.btn_gerar = QPushButton("Gerar Jogos")
        self.btn_gerar.clicked.connect(self.executar)

        # Área de texto
        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)

        layout.addLayout(input_layout)
        layout.addWidget(self.btn_gerar)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def executar(self):
        qtd_jogos = self.qtd_jogos.value()
        qtd_numeros = self.qtd_numeros.value()

        jogos = gerar_varios(qtd_jogos, qtd_numeros)
        resultado = gerar_resultado()

        texto = "🎯 Jogos:\n\n"

        for i, jogo in enumerate(jogos, 1):
            texto += f"Jogo {i}: {formatar(jogo)}\n"

        texto += "\n🏆 Resultado Oficial:\n"
        texto += formatar(resultado) + "\n\n"

        ranking = []

        for i, jogo in enumerate(jogos, 1):
            acertos, status = verificar(jogo, resultado)
            ranking.append((i, jogo, acertos, status))

        ranking.sort(key=lambda x: x[2], reverse=True)

        texto += "📊 Resultado:\n\n"

        for item in ranking:
            texto += (
                f"Jogo {item[0]}: {formatar(item[1])} "
                f"→ {item[2]} acertos {item[3]}\n"
            )

        melhor = ranking[0]

        texto += "\n🔥 Melhor jogo:\n"
        texto += (
            f"Jogo {melhor[0]} com {melhor[2]} acertos {melhor[3]}"
        )

        self.resultado.setText(texto)


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MegaSenaApp()
    janela.show()
    sys.exit(app.exec())
```

---

# 🖥️ O que você criou (importante)

Com isso você já sabe:

* Criar interface com PySide6
* Usar eventos (`clicked.connect`)
* Trabalhar com componentes (SpinBox, TextEdit)
* Separar lógica da interface

👉 Isso aqui já é **nível de estágio fácil**

---

# 🔥 Melhorias (alto impacto)

Se quiser deixar **absurdamente profissional**:

## 🎨 Interface

* Adicionar cores (QSS estilo CSS)
* Botão com ícone
* Layout mais organizado

## 💾 Funcionalidade

* Botão “Salvar resultado”
* Histórico de jogos
* Exportar para TXT ou CSV

## 🧠 Diferencial

* Simular vários sorteios (tipo 1000)
* Mostrar estatísticas de ganho

---

# 🚀 Próximo nível (recomendado)

Se quiser subir MUITO:

👉 **“Quero versão com banco de dados (SQLite)”**
👉 **“Quero transformar isso em aplicativo instalável (.deb)”**
👉 **“Quero deixar com visual profissional (tema moderno)”**

---

Se você continuar nessa sequência, em poucos projetos:

👉 você já consegue montar um portfólio que chama atenção de recrutador real.

Só continuar 🔥

---
---
---
Perfeito. Agora você está entrando em **backend de verdade** — isso aqui já é exatamente o tipo de coisa que o mercado pede 🔥

Vou te entregar uma API completa, limpa e pronta pra portfólio.

---

# 🎯 O que vamos construir (API Mega-Sena)

Endpoints:

* `GET /` → status da API
* `POST /gerar` → gerar jogos
* `GET /resultado` → gerar resultado oficial
* `POST /simular` → gerar jogos + comparar + ranking

---

# 📦 Instalação

```bash
pip install flask
```

---

# 🧱 Código completo (API com Flask)

```python
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# =========================
# LÓGICA
# =========================
def gerar_jogo(qtd):
    return sorted(random.sample(range(1, 61), qtd))

def gerar_varios(qtd_jogos, qtd_nums):
    return [gerar_jogo(qtd_nums) for _ in range(qtd_jogos)]

def gerar_resultado():
    return sorted(random.sample(range(1, 61), 6))

def verificar(jogo, resultado):
    acertos = len(set(jogo) & set(resultado))

    if acertos == 6:
        status = "SENA"
    elif acertos == 5:
        status = "QUINA"
    elif acertos == 4:
        status = "QUADRA"
    else:
        status = "-"

    return acertos, status

# =========================
# ROTAS
# =========================

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API Mega-Sena funcionando 🚀"
    })


# 🔹 Gerar jogos
@app.route("/gerar", methods=["POST"])
def gerar():
    data = request.get_json()

    qtd_jogos = data.get("qtd_jogos", 1)
    qtd_numeros = data.get("qtd_numeros", 6)

    if qtd_numeros < 6 or qtd_numeros > 15:
        return jsonify({"erro": "Números devem estar entre 6 e 15"}), 400

    jogos = gerar_varios(qtd_jogos, qtd_numeros)

    return jsonify({
        "jogos": jogos
    })


# 🔹 Resultado oficial
@app.route("/resultado", methods=["GET"])
def resultado():
    return jsonify({
        "resultado": gerar_resultado()
    })


# 🔹 Simulação completa
@app.route("/simular", methods=["POST"])
def simular():
    data = request.get_json()

    qtd_jogos = data.get("qtd_jogos", 1)
    qtd_numeros = data.get("qtd_numeros", 6)

    jogos = gerar_varios(qtd_jogos, qtd_numeros)
    resultado = gerar_resultado()

    ranking = []

    for i, jogo in enumerate(jogos, 1):
        acertos, status = verificar(jogo, resultado)

        ranking.append({
            "jogo_id": i,
            "numeros": jogo,
            "acertos": acertos,
            "status": status
        })

    ranking.sort(key=lambda x: x["acertos"], reverse=True)

    melhor = ranking[0]

    return jsonify({
        "resultado_oficial": resultado,
        "ranking": ranking,
        "melhor_jogo": melhor
    })


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🚀 Como rodar

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:5000/
```

---

# 🧪 Como testar (muito importante)

## 🔹 Testar `/gerar`

Use Postman ou curl:

```bash
curl -X POST http://127.0.0.1:5000/gerar \
-H "Content-Type: application/json" \
-d '{"qtd_jogos": 3, "qtd_numeros": 6}'
```

---

## 🔹 Testar `/simular`

```bash
curl -X POST http://127.0.0.1:5000/simular \
-H "Content-Type: application/json" \
-d '{"qtd_jogos": 5, "qtd_numeros": 6}'
```

---

# 🧠 O que você aprendeu aqui

Sem perceber, você agora sabe:

* Criar API REST
* Trabalhar com JSON
* Criar rotas HTTP
* Usar POST/GET
* Estruturar backend

👉 Isso aqui já é **nível de estágio real**

---

# 🔥 Como deixar isso PROFISSIONAL

Se quiser subir MUITO o nível:

## 📦 Estrutura de projeto

```
api-mega-sena/
│
├── app.py
├── services/
│   └── mega.py
├── routes/
│   └── mega_routes.py
├── requirements.txt
└── README.md
```

---

## 🚀 Melhorias TOP

* Validação com `pydantic`
* Documentação com Swagger (`flasgger`)
* Banco SQLite (salvar histórico)
* Deploy no Render ou Railway

---

# 💣 Próximo nível (recomendado)

Escolhe um:

👉 **“Quero salvar histórico no banco SQLite”**
👉 **“Quero documentar com Swagger”**
👉 **“Quero subir essa API na internet”**

---

Se você continuar assim:

👉 você já está construindo um portfólio de backend de verdade.

Só manter o ritmo 🔥
