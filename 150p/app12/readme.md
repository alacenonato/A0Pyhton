Boa escolha — **Projeto 12: Sistema de Notas de Aluno** é PERFEITO pra começar a pensar como programador de verdade (regras, validação, lógica de negócio).

Vou te guiar como mentor 👇

---

# 🎯 PROJETO 12 — Sistema de Notas de Aluno (CLI)

## 🧠 Objetivo

Criar um sistema que:

* Recebe nome do aluno
* Recebe várias notas
* Calcula média
* Diz se foi **Aprovado / Recuperação / Reprovado**

---

# 🪜 ETAPA 1 — Versão SIMPLES (faça primeiro)

```python
nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")

if media >= 7:
    print("Status: Aprovado ✅")
elif media >= 5:
    print("Status: Recuperação ⚠️")
else:
    print("Status: Reprovado ❌")
```

---

# ⚙️ ETAPA 2 — Versão MELHORADA (nível profissional iniciante)

Agora vamos organizar como programador de verdade:

```python
def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_status(media):
    if media >= 7:
        return "Aprovado ✅"
    elif media >= 5:
        return "Recuperação ⚠️"
    else:
        return "Reprovado ❌"


def main():
    print("=== Sistema de Notas ===")

    nome = input("Nome do aluno: ")

    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    media = calcular_media(notas)
    status = verificar_status(media)

    print("\n--- Resultado ---")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")


if __name__ == "__main__":
    main()
```

---

# 🧱 ETAPA 3 — VALIDAÇÃO (isso te diferencia MUITO)

Agora vamos evitar erro de usuário:

```python
def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
```

👉 Use no lugar do `float(input())`

---

# 🚀 ETAPA 4 — MELHORIAS (faça depois)

Se quiser subir de nível:

### 🔹 1. Permitir qualquer quantidade de notas

```python
quantidade = int(input("Quantas notas deseja inserir? "))
```

---

### 🔹 2. Salvar resultado em arquivo

```python
with open("alunos.txt", "a") as f:
    f.write(f"{nome} - {media:.2f} - {status}\n")
```

---

### 🔹 3. Múltiplos alunos (loop)

```python
while True:
    # roda o sistema
    sair = input("Deseja continuar? (s/n): ")
    if sair.lower() == 'n':
        break
```

---

# 📁 Estrutura (comece a se acostumar)

```
projeto_notas/
├── main.py
└── alunos.txt
```

---

# 🧠 O que você aprende aqui

Esse projeto treina:

* Entrada de dados
* Listas
* Funções
* Condições
* Validação (ESSENCIAL no mercado)
* Organização de código

---

# 💣 Desafio (FAÇA ISSO)

Se quiser realmente evoluir:

👉 Transforme isso em um sistema com:

* Menu:

  * 1 - Adicionar aluno
  * 2 - Listar alunos
  * 3 - Sair

---

# 🔥 Próximo nível

Se você fizer esse projeto direito, o próximo passo natural é:

👉 **Projeto 31 (versão com arquivo JSON)**
ou
👉 transformar isso em **API com Flask (nível 2)**

---

Se quiser, posso fazer contigo a evolução completa:

👉 versão com menu
👉 versão com JSON
👉 versão com banco de dados
👉 versão web (Django/Flask)

Só fala:

**“quero evoluir esse projeto”** 🚀

---
# MAIS E MAIS 

Tá **muito bom mesmo** — aqui já dá pra ver claramente que você não tá mais no nível iniciante básico 👏

Mas vou ser direto como mentor:
👉 seu código **funciona**, mas ainda não está com “cara de profissional”

Vou te mostrar **os pontos de melhoria que realmente importam no mercado** 👇

---

# ⚠️ 1. BUG IMPORTANTE (você não percebeu)

```python
with open("aluno-{nome}.txt", "a") as f:
```

❌ Isso aqui está errado — não está usando f-string

### ✅ Correto:

```python
with open(f"aluno-{nome}.txt", "a") as f:
```

---

# ⚠️ 2. Falta validação na quantidade de notas

Hoje você faz:

```python
quantidade = int(input("Quantas notas deseja inserir? "))
```

👉 Se o usuário digitar:

* letra → quebra
* 0 → erro na média

### ✅ Versão profissional:

```python
def ler_quantidade():
    while True:
        try:
            q = int(input("Quantas notas deseja inserir? "))
            if q > 0:
                return q
            else:
                print("Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida.")
```

---

# ⚠️ 3. Nome de função pouco claro

```python
salvar_arquivo()
```

👉 Melhorar para algo mais explícito:

### ✅ Sugestão:

```python
salvar_resultado_aluno()
```

---

# ⚠️ 4. Organização (nível profissional começa aqui)

Seu `main()` está ficando grande.

👉 Separar responsabilidades melhora MUITO

---

# 🚀 VERSÃO MELHORADA (PADRÃO PROFISSIONAL INICIANTE)

Olha como seu código evolui 👇

```python
def salvar_resultado_aluno(nome, media, status):
    with open(f"aluno-{nome}.txt", "a") as f:
        f.write(f"{nome} - {media:.2f} - {status}\n")


def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def ler_quantidade():
    while True:
        try:
            q = int(input("Quantas notas deseja inserir? "))
            if q > 0:
                return q
            else:
                print("Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida.")


def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_status(media):
    if media >= 7:
        return "Aprovado ✅"
    elif media >= 5:
        return "Recuperação ⚠️"
    else:
        return "Reprovado ❌"


def coletar_notas():
    quantidade = ler_quantidade()
    notas = []

    for i in range(quantidade):
        nota = ler_nota(f"Digite a nota {i+1}: ")
        notas.append(nota)

    return notas


def exibir_resultado(nome, media, status):
    print("\n--- Resultado ---")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")


def main():
    print("=== Sistema de Notas ===")

    while True:
        nome = input("Nome do aluno: ")

        notas = coletar_notas()
        media = calcular_media(notas)
        status = verificar_status(media)

        exibir_resultado(nome, media, status)

        salvar = input("Deseja salvar em arquivo? [s/n]: ").lower()
        if salvar == 's':
            salvar_resultado_aluno(nome, media, status)

        sair = input("Deseja continuar? [s/n]: ").lower()
        if sair == 'n':
            break


if __name__ == "__main__":
    main()
```

---

# 🔥 Agora vem o que realmente te faz evoluir

## 🧠 Próximas melhorias (ESCOLHA 1 por vez)

### 🥇 1. Salvar tudo em UM arquivo (tipo banco simples)

Hoje você cria vários arquivos.

👉 Melhor:

```txt
alunos.txt
```

---

### 🥈 2. Listar alunos cadastrados

Criar opção:

```
1 - Adicionar aluno
2 - Listar alunos
3 - Sair
```

---

### 🥉 3. Usar JSON (isso muda seu nível)

```python
import json
```

Salvar assim:

```json
[
  {"nome": "João", "media": 7.5, "status": "Aprovado"}
]
```

---

### 🏆 4. Transformar em sistema real

* múltiplos alunos
* editar notas
* remover aluno
* histórico

---

# 💣 Feedback sincero

Você já está:

✅ usando funções
✅ validando entrada
✅ organizando lógica
✅ pensando em melhorias

👉 Isso já te coloca **na frente de MUITA gente**

---

# 🚀 Próximo passo (mentor mode)

Se quiser subir de nível de verdade agora:

👉 fala:

**“quero transformar isso em sistema com menu”**

ou

**“quero versão com JSON (nível profissional)”**

e eu te levo pro próximo nível real (onde começa a parecer sistema de verdade)

---
# MAIS E MAIS

Pronto — te entreguei um **sistema nível profissional inicial de verdade** no canvas 👆

Agora vou te explicar como usar e como evoluir (isso é o que vai te diferenciar de verdade):

---

# 🚀 O que você acabou de construir

Você já tem:

✅ Interface bonita com **Rich**
✅ Sistema com **turmas**
✅ **Múltiplos alunos**
✅ **Edição de notas**
✅ **Remoção de aluno**
✅ **Persistência em JSON**
✅ **Histórico de operações (log)**

👉 Isso já é MUITO acima de iniciante

---

# ▶️ Como rodar

Se ainda não tiver o Rich:

```bash
pip install rich
```

Rodar:

```bash
python main.py
```

---

# 📁 Arquivos gerados

* `dados_alunos.json` → banco de dados
* `historico.txt` → log de tudo que acontece

---

# 🧠 Agora vem a parte mais importante

## 🔥 Melhorias que vão te levar pro próximo nível

### 1. Validação de notas (profissional MESMO)

Hoje aceita qualquer número.

👉 Ideal:

* só aceitar 0 a 10
* tratar erro

---

### 2. Buscar aluno (UX melhor)

Hoje você precisa saber nome exato.

👉 Melhorar:

* listar antes de editar/remover
* escolher por número (ID)

---

### 3. Adicionar ID único (nível backend real)

```json
{
  "id": 1,
  "nome": "João"
}
```

---

### 4. Relatórios (🔥 MUITO VALOR)

Criar opção:

* média da turma
* quantidade de aprovados/reprovados

---

### 5. Interface mais avançada (Rich)

* cores por status:

  * verde = aprovado
  * amarelo = recuperação
  * vermelho = reprovado

---

### 6. Transformar em API (PRÓXIMO GRANDE SALTO)

👉 Flask + esse JSON

Aí você vira:

💻 desenvolvedor backend de verdade

---

# 💣 Feedback direto (nível mercado)

Se você colocar isso no GitHub com:

* README bem feito
* prints do terminal
* explicação da arquitetura

👉 você já começa a parecer **candidato a estágio**

---

# 🚀 Se quiser ir pro próximo nível

Posso evoluir isso com você para:

👉 versão com **ID + busca inteligente**
👉 versão com **relatórios completos**
👉 versão com **banco de dados (SQLite/PostgreSQL)**
👉 versão **web (Flask/Django)**

Só fala:

**“vamos evoluir esse sistema”** 🔥

---
# MAIS E MAIS

Agora sim — esse é o momento em que seu projeto deixa de ser “iniciante organizado” e vira **quase um sistema profissional CLI de verdade**.

Eu peguei seu código e apliquei:

✅ Validação completa de entradas
✅ Normalização de dados (nome, respostas)
✅ Evitar erros silenciosos
✅ Melhor experiência de uso
✅ Código mais robusto e reutilizável

---

# 🚀 VERSÃO MELHORADA (COM VALIDAÇÕES PROFISSIONAIS)

```python
def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        else:
            print("Entrada não pode ser vazia.")


def ler_opcao_sn(mensagem):
    while True:
        op = input(mensagem).strip().lower()
        if op in ['s', 'n']:
            return op
        else:
            print("Digite apenas 's' ou 'n'.")


def ler_quantidade():
    while True:
        try:
            q = int(input("Quantas notas deseja inserir: "))
            if q > 0:
                return q
            else:
                print("Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def salvar_resultado_aluno(nome, media, status):
    try:
        with open("alunos.txt", "a") as f:
            f.write(f"{nome} - {media:.2f} - {status}\n")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")


def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def verificar_status(media):
    if media >= 7:
        return "Aprovado ✅"
    elif media >= 5:
        return "Recuperação ⚠️"
    else:
        return "Reprovado ❌"


def coletar_notas():
    quantidade = ler_quantidade()
    notas = []

    for i in range(quantidade):
        nota = ler_nota(f"Digite a nota {i+1}: ")
        notas.append(nota)

    return notas


def exibir_resultado(nome, media, status):
    print("\n--- Resultado ---")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")


def main():
    print("=== Sistema de Notas ===")

    while True:
        nome = ler_texto("Nome do aluno: ")

        notas = coletar_notas()
        media = calcular_media(notas)
        status = verificar_status(media)

        exibir_resultado(nome, media, status)

        salvar = ler_opcao_sn("Deseja salvar em arquivo? [s/n]: ")
        if salvar == 's':
            salvar_resultado_aluno(nome, media, status)

        continuar = ler_opcao_sn("Deseja continuar? [s/n]: ")
        if continuar == 'n':
            print("Encerrando sistema...")
            break


if __name__ == "__main__":
    main()
```

---

# 🔥 O que você evoluiu aqui (nível real)

### 🧠 1. Entrada de dados PROFISSIONAL

* Não aceita vazio
* Não aceita lixo
* Não quebra o sistema

---

### 🧱 2. Código modular (top)

Você separou:

* leitura de dados
* regra de negócio
* exibição
* persistência

👉 isso é exatamente o que o mercado espera

---

### 🛡️ 3. Tratamento de erro real

```python
try:
    with open(...)
```

👉 Isso evita crash em produção

---

### 🧼 4. Experiência do usuário (UX)

* mensagens claras
* validação amigável
* fluxo controlado

---

# 💣 Agora o próximo salto (OBRIGATÓRIO se quiser evoluir)

Você já dominou CLI básico.

👉 Agora você precisa escolher:

---

## 🥇 Caminho 1 — Sistema com MENU (nível intermediário)

Transformar isso em:

```
1 - Adicionar aluno
2 - Listar alunos
3 - Sair
```

---

## 🥈 Caminho 2 — JSON (🔥 MUITO IMPORTANTE)

Parar de usar `.txt` e usar:

```python
import json
```

👉 Isso te leva para:

* backend
* APIs
* banco de dados

---

## 🥉 Caminho 3 — Rich (interface bonita)

Deixar isso com cara de sistema real no terminal

---

# 🚀 Minha recomendação (como mentor)

👉 Próximo passo IDEAL:

**JSON + múltiplos alunos + menu**

Porque isso vira:

👉 base de sistema real
👉 base pra API
👉 base pra banco de dados

---

Se quiser, eu te levo exatamente nisso:

👉 fala:

**“vamos para versão com JSON e menu”**

e a gente transforma seu projeto em algo nível portfólio 🔥

# MAIS E MAIS 
Perfeito — agora você vai dar um **salto grande de nível** usando **SEU código como base**, mas evoluindo para um **sistema real** com:

* Rich (interface bonita)
* Turmas
* Múltiplos alunos
* JSON (persistência)
* Edição / Remoção
* Log de operações

Vou manter sua lógica (validações etc.) e evoluir em cima dela 👇

---

# 🚀 SISTEMA COMPLETO (PROFISSIONAL CLI)

## 📦 Instale antes:

```bash
pip install rich
```

---

## 💻 Código completo:

```python
import json
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()
ARQUIVO = "dados.json"
LOG = "historico.txt"

# ================= UTIL =================

def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"turmas": {}}
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)


# ================= VALIDAÇÕES =================

def ler_texto(msg):
    while True:
        texto = input(msg).strip()
        if texto:
            return texto
        console.print("[red]Entrada não pode ser vazia[/red]")


def ler_nota(msg):
    while True:
        try:
            n = float(input(msg))
            if 0 <= n <= 10:
                return n
            console.print("[red]Nota deve ser entre 0 e 10[/red]")
        except:
            console.print("[red]Entrada inválida[/red]")


def ler_opcao():
    return Prompt.ask("Escolha uma opção")


# ================= REGRAS =================

def calcular_media(notas):
    return sum(notas) / len(notas)


def status(media):
    if media >= 7:
        return "[green]Aprovado[/green]"
    elif media >= 5:
        return "[yellow]Recuperação[/yellow]"
    return "[red]Reprovado[/red]"


# ================= TURMAS =================

def criar_turma(dados):
    nome = ler_texto("Nome da turma: ")
    if nome in dados["turmas"]:
        console.print("[red]Turma já existe[/red]")
        return
    
    dados["turmas"][nome] = []
    salvar_dados(dados)
    log(f"Turma criada: {nome}")


# ================= ALUNOS =================

def adicionar_aluno(dados):
    turma = ler_texto("Turma: ")

    if turma not in dados["turmas"]:
        console.print("[red]Turma não encontrada[/red]")
        return

    nome = ler_texto("Nome do aluno: ")
    qtd = int(input("Quantidade de notas: "))

    notas = []
    for i in range(qtd):
        notas.append(ler_nota(f"Nota {i+1}: "))

    media = calcular_media(notas)

    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media,
        "status": status(media)
    }

    dados["turmas"][turma].append(aluno)
    salvar_dados(dados)
    log(f"Aluno adicionado: {nome}")


def listar_alunos(dados):
    turma = ler_texto("Turma: ")

    if turma not in dados["turmas"]:
        console.print("[red]Turma não encontrada[/red]")
        return

    tabela = Table(title=f"Turma: {turma}")
    tabela.add_column("Nome")
    tabela.add_column("Média")
    tabela.add_column("Status")

    for aluno in dados["turmas"][turma]:
        tabela.add_row(
            aluno["nome"],
            f"{aluno['media']:.2f}",
            aluno["status"]
        )

    console.print(tabela)


def editar_aluno(dados):
    turma = ler_texto("Turma: ")
    nome = ler_texto("Nome do aluno: ")

    for aluno in dados["turmas"].get(turma, []):
        if aluno["nome"] == nome:
            console.print(f"Notas atuais: {aluno['notas']}")

            novas_notas = []
            for i in range(len(aluno["notas"])):
                novas_notas.append(ler_nota(f"Nova nota {i+1}: "))

            aluno["notas"] = novas_notas
            aluno["media"] = calcular_media(novas_notas)
            aluno["status"] = status(aluno["media"])

            salvar_dados(dados)
            log(f"Aluno editado: {nome}")
            return

    console.print("[red]Aluno não encontrado[/red]")


def remover_aluno(dados):
    turma = ler_texto("Turma: ")
    nome = ler_texto("Nome do aluno: ")

    alunos = dados["turmas"].get(turma, [])

    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            salvar_dados(dados)
            log(f"Aluno removido: {nome}")
            return

    console.print("[red]Aluno não encontrado[/red]")


# ================= MENU =================

def menu():
    console.print("""
[bold cyan]
1 - Criar turma
2 - Adicionar aluno
3 - Listar alunos
4 - Editar aluno
5 - Remover aluno
6 - Sair
""")
    return ler_opcao()


# ================= MAIN =================

def main():
    dados = carregar_dados()

    while True:
        op = menu()

        if op == "1":
            criar_turma(dados)
        elif op == "2":
            adicionar_aluno(dados)
        elif op == "3":
            listar_alunos(dados)
        elif op == "4":
            editar_aluno(dados)
        elif op == "5":
            remover_aluno(dados)
        elif op == "6":
            console.print("[bold red]Saindo...[/bold red]")
            break
        else:
            console.print("[red]Opção inválida[/red]")


if __name__ == "__main__":
    main()
```

---

# 🧠 O que você acabou de atingir

Você saiu de:

👉 script simples

para:

👉 **sistema CRUD completo com persistência + UI**

Isso aqui já envolve:

* Estrutura de dados real (JSON)
* Separação de responsabilidades
* Interface de usuário
* Operações completas (Create, Read, Update, Delete)

---

# 🔥 Próximo upgrade (nível estágio mesmo)

Se quiser subir mais ainda:

👉 adicionar **ID automático para aluno**
👉 implementar **busca por ID (melhor que nome)**
👉 criar **relatórios (média da turma, ranking)**
👉 migrar para **SQLite (banco real)**

---

Se quiser, posso te levar pro próximo nível agora:

👉 **“quero versão com banco de dados (SQLite)”**
👉 **“quero transformar isso em API com Flask”**

Aí você entra de vez no nível profissional 🚀
