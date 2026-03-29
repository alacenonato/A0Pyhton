import random

# === Limpeza ===
def limpar_cpf(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf))

# === Validações Básicas ===
def validar_formato(cpf: str) -> tuple[bool, str]:
    if len(cpf) != 11:
        return False, "CPF deve ter 11 dígitos"
    
    if not cpf.isdigit():
        return False, "CPF deve conter apenas números"
    
    if cpf == cpf[0] * 11:
        return False, "CPF inválido (sequência repetida)"
    
    return True, "Ok"

# === Cálculo dos Dígitos ===
def calcular_digito(cpf_parcial: str, peso_incial: int) -> int:
    soma = sum(int(num) * peso for num, peso in zip(cpf_parcial, range(peso_incial, 1, -1)))
    resto = (soma * 10) % 11
    return 0 if resto >= 10 else resto

# === Validação Completa ===
def validar_cpf(cpf: str) -> tuple[bool, str]:
    cpf = limpar_cpf(cpf)

    valido, msg = validar_formato(cpf)
    if not valido:
        return False, msg
    
    d1 = calcular_digito(cpf[:9], 10)
    d2 = calcular_digito(cpf[:9] + str(d1), 11)

    if cpf[-2:] == f"{d1}{d2}":
        return True, "CPF Válido"
    else:
        return False, "Dígitos verificadores inválidos"
    
# === Formatar Cpf ===
def formatar_cpf(cpf: str) -> str:
    cpf = limpar_cpf(cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# === Gerar Cpf váliddo ===
def gerar_cpf() -> str:
    base = [random.randint(0, 9) for _ in range(9)]
    base_str = ''.join(map(str, base))

    d1 = calcular_digito(base_str, 10)
    d2 = calcular_digito(base_str + str(d1), 11)

    cpf = base_str + str(d1) + str(d2)
    return formatar_cpf(cpf)

# === Cli (Interface) ===
if __name__ == "__main__":
    print("=== Validador de Cpf ===")

    while True:
        print("\n1 - Validar Cpf")
        print("2 - Gerar Cpf")
        print("3 - Sair")

        opcao = input("Escolha :")

        if opcao == "1":
            cpf = input("Digite o Cpf: ")
            valido, msg = validar_cpf(cpf)

            if valido:
                print(f"{msg}: {formatar_cpf(cpf)}")
            else:
                print(f"{msg}")
        
        elif opcao == "2":
            print(f"Cpf gerado: {gerar_cpf()}")

        elif opcao == "3":
            break
        
        else:
            print("Opção Inválida")