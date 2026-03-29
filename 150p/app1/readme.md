
# 🚀 PROJETO 1 — Calculadora Profissional (CLI)

👉 Parece simples, mas aqui você vai aprender:

* Entrada de dados
* Estrutura condicional
* Funções
* Organização de código (muito importante!)
* Pensar como programador

---

## 🧠 ETAPA 1 — Entender o problema

Você precisa criar uma calculadora que:

* Recebe 2 números
* Recebe uma operação (+, -, *, /)
* Retorna o resultado

---

## 🧩 ETAPA 2 — Planejamento (faça isso sempre!)

Antes de codar, pense assim:

**Entradas:**

* número1
* número2
* operação

**Processamento:**

* verificar operação
* calcular

**Saída:**

* resultado

---

## 💻 ETAPA 3 — Versão inicial (faça você primeiro!)

Tente fazer sozinho antes de ver o código abaixo 👇

---

## ✅ SOLUÇÃO (versão simples)

```python
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


print("=== CALCULADORA ===")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    resultado = somar(num1, num2)
elif operacao == "-":
    resultado = subtrair(num1, num2)
elif operacao == "*":
    resultado = multiplicar(num1, num2)
elif operacao == "/":
    resultado = dividir(num1, num2)
else:
    resultado = "Operação inválida!"

print("Resultado:", resultado)
```

---

## 🔥 ETAPA 4 — Agora vem o que faz você evoluir

Você NÃO pode parar aqui.

Melhore o projeto:

### 🧪 DESAFIOS (faça todos)

1. Permitir repetir a operação (loop)
2. Validar entrada (evitar erro se digitar texto)
3. Criar menu bonito:

```
1 - Somar
2 - Subtrair
...
```

4. Permitir várias operações seguidas (tipo calculadora real)
5. Mostrar histórico de cálculos

---

## 🧠 ETAPA 5 — Pensamento profissional

Agora você começa a pensar como dev:

👉 Separe em funções:

* `menu()`
* `obter_numeros()`
* `executar_operacao()`

---

## 🎯 MISSÃO (IMPORTANTE)

Faça:

* Código funcionando
* Pelo menos 2 melhorias
* Salve como: `calculadora.py`

---

## 📈 Evolução real (não pule isso)

Depois de terminar, você pode:

* Subir no GitHub
* Criar versão 2 (mais avançada)
* Transformar em interface gráfica (futuro)

---

