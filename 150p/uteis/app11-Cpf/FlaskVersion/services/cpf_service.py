import random
from utils.helpers import limpar_cpf

def validar_formato(cpf: str):
    if len(cpf) != 11:
        return False, "Cpf dever ter 11 dígitos"
    
    if not cpf.isdigit():
        return False, "Cpf dever conter apenas números"
    
    if cpf == cpf[0]*11:
        return False, "Cpf inválido (sequência repetida)"
    
    return True, "OK"

def calcular_digito(cpf_parcial:str, peso_inicial: int) -> int:
    soma = sum(int(num) * peso for num, peso in zip(cpf_parcial, range(peso_inicial, 1, -1)))
    resto = (soma * 10) % 11
    return 0 if resto >= 10 else resto

def validar_cpf(cpf: str):
    cpf = limpar_cpf

    valido, msg = validar_formato(cpf)
    if not valido:
        return False, msg
    
    d1 = calcular_digito(cpf[:9], 10)
    d2 = calcular_digito(cpf[:9] + str(d1), 11)

    if cpf[-2:] == f"{d1}{d2}":
        return True, "Cpf Válido"
    else:
        return False, "Cpf Inválido"
    
def gerar_cpf():
    base = [random.randint(0, 9) for _ in range(9)]
    base_str = ''.join(map(str, base))

    d1 = calcular_digito(base_str, 10)
    d2 = calcular_digito(base_str + str(d1), 11)

    return base_str + str(d1) + str(d2)
