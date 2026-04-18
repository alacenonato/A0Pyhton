import sqlite3

DB_NAME = "150p/app18/api/agenda.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS contatos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL, 
                   telefone TEXT NOT NULL )
                   """)
    
    conn.commit()
    conn.close()

def inserir_contatos(nome, telefone):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contatos (nome, telefone) VALUES (?, ?)", (nome, telefone)
    )

    conn.commit()
    conn.close()

def listar_contatos_db():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contatos ORDER BY nome")
    dados = cursor.fetchall()

    conn.close()
    return dados

def buscar_contatos_db(termo):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT * FROM contatos
                    WHERE nome LIKE ? OR telefone LIKE ? 
                    """, (f"%{termo}%", f"%{termo}%"))
    
    dados = cursor.fetchall()
    conn.close()
    return dados

def deletar_contato(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM contatos WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def atualizar_contato(id, nome, telefone):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
                   UPDATE contatos
                   SET nome = ? , telefone = ?
                   WHERE id = ? 
                   """, (nome, telefone, id))
    
    conn.commit()
    conn.close()


