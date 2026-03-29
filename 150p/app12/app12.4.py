import json
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()
ARQUIVO = "dados.json"
LOG = "historico.txt"

# === UTIL ===
def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"turmas": {}}
    with open(ARQUIVO, "r") as f:
        return json.load(f)
    
def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

# === VALIDAÇÕES ===
def ler_texto(msg):
    