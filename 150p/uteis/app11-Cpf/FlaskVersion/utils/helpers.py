def limpar_cpf(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf))