Boa — agora vamos pegar o **Projeto 11 (Validador de CPF)** e transformar em algo **nível profissional de verdade** (código limpo, reutilizável, pronto pra API/sistema).

Sem gambiarra. Sem código “de exercício”.

---

# 🇧🇷 📄 Projeto 11 — Validador de CPF (VERSÃO PROFISSIONAL)

## 🎯 Objetivo dessa versão

✔ Código organizado (funções pequenas)
✔ Reutilizável (serve pra API, Flask, etc)
✔ Retorna erro detalhado (não só True/False)
✔ Formata CPF
✔ Gera CPF válido (🔥 diferencial)

---

# 🧠 Estrutura profissional

Você vai ter:

* Funções puras (sem input direto)
* Separação de responsabilidades
* Retornos claros

---

# 💻 Código completo (PRO)

```python
import random

# ===== LIMPEZA =====
def limpar_cpf(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf))


# ===== VALIDAÇÕES BÁSICAS =====
def validar_formato(cpf: str) -> tuple[bool, str]:
    if len(cpf) != 11:
        return False, "CPF deve ter 11 dígitos"

    if not cpf.isdigit():
        return False, "CPF deve conter apenas números"

    if cpf == cpf[0] * 11:
        return False, "CPF inválido (sequência repetida)"

    return True, "OK"


# ===== CÁLCULO DOS DÍGITOS =====
def calcular_digito(cpf_parcial: str, peso_inicial: int) -> int:
    soma = sum(int(num) * peso for num, peso in zip(cpf_parcial, range(peso_inicial, 1, -1)))
    resto = (soma * 10) % 11
    return 0 if resto >= 10 else resto


# ===== VALIDAÇÃO COMPLETA =====
def validar_cpf(cpf: str) -> tuple[bool, str]:
    cpf = limpar_cpf(cpf)

    valido, msg = validar_formato(cpf)
    if not valido:
        return False, msg

    d1 = calcular_digito(cpf[:9], 10)
    d2 = calcular_digito(cpf[:9] + str(d1), 11)

    if cpf[-2:] == f"{d1}{d2}":
        return True, "CPF válido"
    else:
        return False, "Dígitos verificadores inválidos"


# ===== FORMATAR CPF =====
def formatar_cpf(cpf: str) -> str:
    cpf = limpar_cpf(cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


# ===== GERAR CPF VÁLIDO =====
def gerar_cpf() -> str:
    base = [random.randint(0, 9) for _ in range(9)]
    base_str = ''.join(map(str, base))

    d1 = calcular_digito(base_str, 10)
    d2 = calcular_digito(base_str + str(d1), 11)

    cpf = base_str + str(d1) + str(d2)
    return formatar_cpf(cpf)


# ===== CLI (INTERFACE) =====
if __name__ == "__main__":
    print("=== VALIDADOR DE CPF ===")

    while True:
        print("\n1 - Validar CPF")
        print("2 - Gerar CPF")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cpf = input("Digite o CPF: ")
            valido, msg = validar_cpf(cpf)

            if valido:
                print(f"✅ {msg}: {formatar_cpf(cpf)}")
            else:
                print(f"❌ {msg}")

        elif opcao == "2":
            print(f"🎲 CPF gerado: {gerar_cpf()}")

        elif opcao == "3":
            break

        else:
            print("❌ Opção inválida")
```

---

# 🔥 O QUE ISSO TEM DE PROFISSIONAL

Agora você tem:

### 🧠 Arquitetura correta

* Funções separadas
* Fácil reutilização

### 🔍 Validação real

* Retorna motivo do erro

### 🎲 Geração de CPF

* Isso é nível avançado

### 🎯 Pronto pra evoluir

* Flask
* API
* Banco de dados

---

# 💡 COMO ISSO VIRA PROJETO DE PORTFÓLIO

Cria um README assim:

* O que o projeto faz
* Como rodar
* Exemplos
* Explicação do algoritmo

👉 Isso chama MUITA atenção

---

# 🚀 PRÓXIMO NÍVEL (RECOMENDADO)

Agora você pode transformar isso em:

## 🔥 1. API Flask

```
POST /validar-cpf
```

## 🔥 2. Sistema web

* formulário com validação

## 🔥 3. Sistema contábil

* cadastro de cliente com CPF válido

---

# 👉 PRÓXIMO PASSO

Fala comigo:

👉 **"Quero transformar isso em API Flask"**
👉 **"Quero interface web bonita"**
👉 **"Projeto 12 com mentor"**

Agora sim você está programando **como dev de verdade** 🔥
