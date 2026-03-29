# Perfeito — vamos começar do jeito certo, como um programador profissional 👍

Você escolheu o **Projeto 2: Conversor de Temperatura** 🌡️
Esse projeto parece simples, mas dá pra extrinar MUITA base importante.

---

# 🧠 O que você vai aprender nesse projeto

* Entrada de dados (`input`)
* Conversão de tipos (`float`)
* Condições (`if`)
* Funções
* Organização de código

---

# 📐 Fórmulas que vamos usar

Aqui estão as principais conversões:

---

# 🏗️ Etapa 1 — Versão simples (CLI)

👉 Crie um arquivo chamado: `conversor_temperatura.py`

```python
print("=== Conversor de Temperatura ===")

temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Converter para (C/F/K): ").upper()

resultado = None

if origem == "C" and destino == "F":
    resultado = (temp * 9/5) + 32

elif origem == "F" and destino == "C":
    resultado = (temp - 32) * 5/9

elif origem == "C" and destino == "K":
    resultado = temp + 273.15

elif origem == "K" and destino == "C":
    resultado = temp - 273.15

elif origem == "F" and destino == "K":
    resultado = (temp - 32) * 5/9 + 273.15

elif origem == "K" and destino == "F":
    resultado = (temp - 273.15) * 9/5 + 32

else:
    print("Conversão inválida!")

if resultado is not None:
    print(f"Resultado: {resultado:.2f} {destino}")
```

---

# ▶️ Como executar

No terminal:

```bash
python conversor_temperatura.py
```

---

# 🔥 Etapa 2 — Melhorando o código (nível profissional iniciante)

Agora vamos fazer como dev de verdade: usar funções 👇

```python
def c_para_f(c):
    return (c * 9/5) + 32

def f_para_c(f):
    return (f - 32) * 5/9

def c_para_k(c):
    return c + 273.15

def k_para_c(k):
    return k - 273.15

def converter(temp, origem, destino):
    if origem == "C" and destino == "F":
        return c_para_f(temp)
    elif origem == "F" and destino == "C":
        return f_para_c(temp)
    elif origem == "C" and destino == "K":
        return c_para_k(temp)
    elif origem == "K" and destino == "C":
        return k_para_c(temp)
    elif origem == "F" and destino == "K":
        return c_para_k(f_para_c(temp))
    elif origem == "K" and destino == "F":
        return c_para_f(k_para_c(temp))
    else:
        return None


print("=== Conversor de Temperatura ===")

temp = float(input("Digite a temperatura: "))
origem = input("Origem (C/F/K): ").upper()
destino = input("Destino (C/F/K): ").upper()

resultado = converter(temp, origem, destino)

if resultado is not None:
    print(f"Resultado: {resultado:.2f} {destino}")
else:
    print("Conversão inválida!")
```

---

# 🧪 Desafios (FAÇA ISSO PRA EVOLUIR)

👉 Agora vem a parte importante (onde você realmente aprende):

1. Não permitir letras inválidas
2. Permitir repetir o programa (loop)
3. Criar menu (1 - Converter, 2 - Sair)
4. Mostrar histórico das conversões
5. Criar interface bonita no terminal

---

# 🚀 Próximo nível (se quiser subir rápido)

Depois disso, você pode transformar esse projeto em:

* 🖥️ Interface gráfica (Tkinter)
* 🌐 API com Flask
* 📱 App web simples

---

# 👉 Me chama assim:

Se quiser continuar comigo:

👉 “vamos para versão com menu”
ou
👉 “quero interface gráfica”

Eu te guio passo a passo como um mentor até nível profissional.
