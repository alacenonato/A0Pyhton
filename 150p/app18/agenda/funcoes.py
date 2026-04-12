import json
import os
from utils import telefone_valido, nome_valido

ARQUIVO = 'dados.json'

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []
    
    with open(ARQUIVO, "r") as f:
        return json.load(f)
    
def salvar_dados(agenda):
    with open(ARQUIVO, "w") as f:
        json.dump(agenda, f, indent=4)

def contato_existe(agenda, nome):
    return any(c["nome"].lower() == nome.lower() for c in agenda)

def adicionar_contato(agenda):
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    if not nome_valido(nome):
        print("Nome inválido.")
        return

    if not telefone_valido(telefone):
        print("Telefone inválido.")
        return
    
    if contato_existe(agenda, nome):
        print("Contato já existe.")
        return
    
    agenda.append({"nome": nome, "telefone": telefone})
    salvar_dados(agenda)

    print("Contato adicionado!")

def listar_contatos(agenda):
    if not agenda:
        print("Agenda vazia")
        return
    
    agenda_ordenada = sorted(agenda, key=lambda x: x["nome"])

    print("\n Contatos:")
    for i, contato in enumerate(agenda_ordenada):
        print(f"{i+1}. {contato['nome']} - {contato['telefone']}")

    print(f"\nTotal: {len(agenda)} contatos")

def buscar_contato(agenda):
    termo = input("Buscar por nome ou telefone: ").lower()

    encontrados = [
        c for c in agenda
        if termo in c["nome"].lower() or termo in c["telefone"]
    ]

    if not encontrados:
        print("Nenhum contato encontrado.")
        return
              
    for c in encontrados:
        print(f"{c['nome']} - {c['telefone']}")

def remover_contato(agenda):
    listar_contatos(agenda)

    try:
        indice = int(input("Número do contato para remover: ")) -1

        if 0 <= indice < len(agenda):
            confirm = input("Tem certeza? (s/n): ").lower()
            if confirm == "s":
                removido = agenda.pop(indice)
                salvar_dados(agenda)
                print(f"Removido: {removido['nome']}")
            else:
                print("Cancelado.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def editar_contato(agenda):
    listar_contatos(agenda)

    try:
        indice = int(input("Número do contato para editar: ")) - 1
        if 0 <= indice < len(agenda):
            contato = agenda[indice]

            novo_nome = input(f"Novo nome ({contato['nome']}): ")
            novo_tel = input(f"Novo telefone ({contato['telefone']}): ")

            if not nome_valido(novo_nome) or not telefone_valido(novo_tel):
                print("Dados inválidos.")
                return

            contato["nome"] = novo_nome
            contato["telefone"] = novo_tel

            salvar_dados(agenda)
            print("Contato atualizado!")
        else:
            print("Índice inválido.")
    
    except ValueError:
        print("Entrada inválida.")
