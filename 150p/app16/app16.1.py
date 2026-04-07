import json
import os 
import hashlib
import getpass

ARQVUIVO = "usuarios.json"
MAX_TENTATIVAS = 3

# ================
# UTIL
# ================
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar_ususarios():
    if not os.path.exists(ARQVUIVO):
        return {
        }
    
    with open(ARQVUIVO, "r") as f:
        return json.load(f)
    
def salvar_usuarios(usuarios):
    with open(ARQVUIVO, "w") as f:
        json.dump(usuarios, f, indent = 4)

# ====================
# SISTEMA
# ====================
def cadastrar():
    usuarios = carregar_ususarios()

    print("\n=== CADASTRO ===")
    usuario = input("Usuário: ")

    if usuario in usuarios:
        print("Usuário já existe")
        return
    
    senha = getpass.getpass("Senha: ")
    confirmar = getpass.getpass("Confirmar senha: ")

    if senha != confirmar:
        print("Senhas não coincidem!")
        return

    usuarios[usuarios] = hash_senha(senha)
    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")

def login():
    usuarios = carregar_ususarios()

    print("\n ==== LOGIN =====")
    usuario = input("Usuario: ")

    tentativas = 0
 
    while tentativas < MAX_TENTATIVAS:
        senha = getpass.getpass("Senha: ")
        senha_hash = hash_senha(senha)

        if usuario in usuarios and usuarios[usuario] == senha_hash:
            print("Login bem-sucedido!")
            return usuario
        else:
            tentativas += 1
            print(f"Tentativa {tentativas}/{MAX_TENTATIVAS}")

    print("Acesso bloqueado!")
    return None

def editar_senha()
    usuarios = carregar_ususarios()
    
    print("\n==== ALTERAR SENHA ====")
    usuario= input("Usuário: ")

    if usuario not in usuarios:
        print("Usuário não encontrado!")
        return
    
    senha_atual = getpass.getpass("Senha atual: ")

    if usuarios[usuario] != hash_senha(senha_atual)
        print("Senha incorreta! ")

    nova = getpass.getpass("Nova senha: ")
    confirmar = getpass.getpass("Confirmar nova senha: ")

    if nova != confirmar:
        print("Senhas não concidem!")
        return
    
    usuarios[usuario] = hash_senha(nova)
    salvar_usuarios(usuarios)

    print("Senha alterada com sucesso!")