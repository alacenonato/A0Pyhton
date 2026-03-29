# Projeto pra começar — simples, mas já te ensina entrada de dados, lógica e organização.

---

# 💱 Projeto 3 — Conversor de Moeda (CLI)

## 🎯 Objetivo

Criar um programa que:

* Recebe um valor em reais (R$)
* Converte para outras moedas (ex: dólar, euro)
* Mostra o resultado

---

# 🧠 PASSO 1 — Entender a lógica

Exemplo:

* Usuário digita: `100`
* Cotação:

  * Dólar: 5.00
  * Euro: 5.50

Resultado:

* 100 / 5 = 20 dólares
* 100 / 5.5 = 18.18 euros

---

# 🧩 PASSO 2 — Código inicial (simples)

```python
# Conversor de Moeda

# Entrada
valor_reais = float(input("Digite o valor em reais: R$ "))

# Cotações fixas
dolar = 5.00
euro = 5.50

# Conversão
valor_dolar = valor_reais / dolar
valor_euro = valor_reais / euro

# Saída
print("\n=== Conversão ===")
print(f"Dólar: ${valor_dolar:.2f}")
print(f"Euro: €{valor_euro:.2f}")
```

---

# ▶️ PASSO 3 — Teste

Teste com:

```
100
```

Saída esperada:

```
Dólar: $20.00
Euro: €18.18
```

---

# 🔥 PASSO 4 — Melhorar (nível iniciante+)

Agora vamos deixar mais profissional:

```python
print("=== Conversor de Moeda ===")

valor_reais = float(input("Digite o valor em reais (R$): "))

dolar = 5.00
euro = 5.50

valor_dolar = valor_reais / dolar
valor_euro = valor_reais / euro

print("\nResultado da conversão:")
print("-" * 30)
print(f"Real: R$ {valor_reais:.2f}")
print(f"Dólar: $ {valor_dolar:.2f}")
print(f"Euro: € {valor_euro:.2f}")
print("-" * 30)
```

---

# 🚀 PASSO 5 — Desafio (IMPORTANTE)

Agora é onde você realmente aprende.

Tente fazer sozinho:

### 🔹 Desafio 1

Adicionar:

* Libra (£)

---

### 🔹 Desafio 2

Permitir escolher moeda:

Exemplo:

```
1 - Dólar
2 - Euro
3 - Libra
```

---

### 🔹 Desafio 3 (top 🔥)

Validar erro:

* Se o usuário digitar letra → evitar crash

---

# 🧠 Dica de programador

Nunca pare no código básico.
Sempre pergunte:

👉 “Como deixo isso mais real?”

Exemplo:

* Atualizar cotação automaticamente (futuro)
* Interface gráfica
* API de moedas

---

# 💡 Se quiser evoluir mais

Posso te guiar agora para:

✅ Versão com menu interativo
✅ Versão com API (cotação real 🔥)
✅ Versão com interface gráfica (Tkinter)
✅ Transformar isso em projeto de portfólio

---

Se quiser continuar comigo, fala:

👉 **“próximo passo”**
ou
👉 **“quero versão com API real”**

e a gente evolui esse projeto pra nível profissional 🚀

### Continuando ....

Agora com resultado final

Agora tenho:
✅ Conversor com dados reais
✅ Interface gráfica
✅ Tratamento de erro
✅ Projeto de portfólio

Melhorias que posso fazer:
Atualizar cotação automaticamente a cada X segundos

Escolher moeda (dropdown)

Histórico de conversões

Tema escuro

Exportar resultado (PDF/Excel)
