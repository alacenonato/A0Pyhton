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