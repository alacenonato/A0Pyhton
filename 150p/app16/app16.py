import json
import os
import hashlib

ARQUIVO = "usuarios.json"

# ===========================
# UTIL
# ===========================
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        return {}
    
    with open(ARQUIVO, "r") as f:
        return json.load(f)
    
def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)

# =============================
# SISTEMA
# =============================
def cadastrar():
    usuarios = carregar_usuarios()
    
    print("\n=== CADASTRO ===")
    usuario = input("Usuário: ")

    if usuario in usuarios:
        print("Usuário já existe!")
        return
    
    senha = input("Senha: ")
    senha_hash = hash_senha(senha)

    usuarios[usuario] = senha_hash
    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")

def login():
    usuarios = carregar_usuarios()

    print("\n=== LOGIN ===")
    usuario = input('Usuario: ')
    senha = input("Senha: ")

    senha_hash = hash_senha(senha)

    if usuario in usuarios and usuarios[usuario] == senha_hash:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha inválidos!")

# =====================
# MENU
# =====================
def menu():
    while True:
        print("\n=========MENU============")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# ======================
# EXECUÇÃO
# ======================
if __name__ == "__main__":
    menu()