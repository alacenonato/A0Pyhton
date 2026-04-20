from database import *
import re


def nome_valido(nome):
    return len(nome.strip()) >= 2

def telefone_valido(telefone):
    return telefone.isdigit() and len(telefone) >= 8

def adicionar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    if not nome_valido(nome):
        print("Nome inválido.")
        return
    
    if not telefone_valido(telefone):
        print("Telefone inválido.")
        return
    
    inserir_contatos(nome, telefone)
    print("Contato adicionado!")

def listar():
    contatos = listar_contatos_db()

    if not contatos:
        print("Agenda vazia.")
        return
    
    print("\nContatos:")
    for c in contatos:
        print(f"{c[0]}. {c[1]} - {c[2]}")

def buscar():
    termo = input("Buscar: ")
    resultados = buscar_contatos_db(termo)

    if not resultados:
        print("Nenhuma encontrado.")
        return
    
    for c in resultados:
        print(f"{c[0]} . {c[1]} - {c[2]}")

def remover():
    listar()
    try:
        id = int(input("ID para remover: "))
        confirm = input("Tem certeza? (s/n): ")

        if confirm.lower() == "s":
            deletar_contato(id)
            print("Removido")
    
    except ValueError:
        print("Entrada inválida.")

def editar():
    listar()
    try:
        id = int(input("ID para editar: "))

        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")

        if not nome_valido(nome) or not telefone_valido(telefone):
            print("Dados inválidos.")
            return
    
        atualizar_contato(id, nome, telefone)
        print("Atualizado!")

    except ValueError:
        print("Entrada inválida.")
