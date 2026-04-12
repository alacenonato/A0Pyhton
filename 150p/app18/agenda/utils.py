# VALIDAÇÕES

def telefone_valido(telefone):
    return telefone.isdigit() and len(telefone) >= 8

def nome_valido(nome):
    return len(nome.strip()) >= 2
