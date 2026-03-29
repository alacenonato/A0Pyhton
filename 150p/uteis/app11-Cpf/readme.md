Perfeito — agora você entrou numa parte **muito importante da sua evolução**.

👉 Projeto 11 é onde você começa a trabalhar com **validação real de dados brasileiros + lógica mais avançada**.

---

# 🇧🇷 📄 Projeto 11 — Validador de CPF (Nível Profissional)

## 🎯 Objetivo

Criar um sistema que:

✔ Valida CPF corretamente (algoritmo real)
✔ Remove caracteres (`.` e `-`)
✔ Detecta CPFs inválidos comuns
✔ Interface amigável (CLI ou evoluir depois pra Flask/GUI)

---

# 🧠 O que você vai aprender

* Manipulação de strings
* Listas
* Laços (`for`)
* Algoritmo matemático (dígitos verificadores)
* Validação real (nível mercado)

---

# ⚙️ REGRA DO CPF (SIMPLIFICADA)

CPF tem 11 dígitos:

```
XXX.XXX.XXX-YY
```

Os 2 últimos (`YY`) são calculados.

---

# 🔢 CÁLCULO (IDEIA)

1. Multiplica os 9 primeiros dígitos por pesos (10 → 2)
2. Soma tudo
3. Faz: `(soma * 10) % 11`
4. Se der 10 → vira 0

👉 Repete o processo para o segundo dígito

---

# 💻 CÓDIGO COMPLETO (PROFISSIONAL CLI)

```python
def limpar_cpf(cpf):
    return cpf.replace(".", "").replace("-", "").strip()


def cpf_invalido(cpf):
    # evita CPF tipo 11111111111
    return cpf == cpf[0] * len(cpf)


def calcular_digito(cpf, peso_inicial):
    soma = 0

    for i in range(len(cpf)):
        soma += int(cpf[i]) * (peso_inicial - i)

    resto = (soma * 10) % 11
    return 0 if resto == 10 else resto


def validar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11 or not cpf.isdigit():
        return False

    if cpf_invalido(cpf):
        return False

    primeiro_digito = calcular_digito(cpf[:9], 10)
    segundo_digito = calcular_digito(cpf[:10], 11)

    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"


# ===== EXECUÇÃO =====

cpf = input("Digite o CPF: ")

if validar_cpf(cpf):
    print("✅ CPF válido")
else:
    print("❌ CPF inválido")
```

---

# 🔥 MELHORIAS (OBRIGATÓRIO PRA EVOLUIR)

## 🟡 Nível 1

* Loop para validar vários CPFs
* Mensagem mais detalhada

## 🟡 Nível 2

* Formatar CPF automaticamente:

  ```
  12345678909 → 123.456.789-09
  ```

## 🟡 Nível 3

* Gerar CPFs válidos (🔥 muito bom pra prática)

## 🟡 Nível 4 (PRO)

* Criar função que retorna motivo do erro:

  * tamanho inválido
  * dígito errado
  * sequência inválida

---

# 💡 MELHORIA INTELIGENTE (SEU CASO)

👉 Conecta com contabilidade:

* validar CPF em cadastro de cliente
* integrar com sistema financeiro

---

# 🚀 EVOLUÇÃO DIRETA DESSE PROJETO

Você pode transformar isso em:

👉 API Flask (`/validar-cpf`)
👉 Sistema com cadastro de clientes
👉 Formulário web com validação automática
👉 App desktop com PySide

---

# 🧠 DIFERENCIAL DE DEV

Se você fizer isso:

* código limpo
* funções bem separadas
* README explicando

👉 Já vira projeto de portfólio

---

# 👉 PRÓXIMO PASSO

Escolhe:

👉 **"Quero versão com Flask (API de CPF)"**
👉 **"Quero versão com interface gráfica"**
👉 **"Projeto 12 com mentor"**

Se você seguir nessa sequência, você vai ficar **muito acima da média** 🔥

# MAIS E MAIS
