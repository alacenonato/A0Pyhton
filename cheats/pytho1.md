Com certeza! Com base no site que você enviou, criei um **Cheat Sheet completo e organizado** do Python, agrupando e complementando as informações para facilitar a consulta.

---

# 🐍 PYTHON 3 - CHEAT SHEET COMPLETO

## 1. CONCEITOS BÁSICOS

### Hello World
```python
print("Hello, World!")
```

### Variáveis
```python
idade = 18           # int
nome = "João"        # str
pi = 3.14            # float
complexo = 1 + 2j    # complex
```

### Tipos de Dados Primitivos
| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| `int` | Inteiro | `10` |
| `float` | Ponto flutuante | `3.14` |
| `str` | String (texto) | `"Python"` |
| `bool` | Booleano | `True` / `False` |
| `complex` | Número complexo | `1 + 2j` |

### Conversão de Tipos (Casting)
```python
int(3.14)      # 3
float(5)       # 5.0
str(100)       # "100"
bool(0)        # False
bool(1)        # True
```

---

## 2. COLEÇÕES DE DADOS

### Listas (`list`) - Mutável, ordenada, permite duplicatas
```python
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")          # Adiciona ao final
frutas.insert(1, "morango")   # Insere na posição 1
frutas.remove("banana")       # Remove por valor
item = frutas.pop()           # Remove e retorna último
frutas[0] = "abacaxi"         # Altera elemento
print(len(frutas))            # Tamanho da lista
```

### Tuplas (`tuple`) - Imutável, ordenada
```python
coordenadas = (10, 20, 30)
x, y, z = coordenadas         # Desempacotamento
print(coordenadas[0])         # Acesso por índice (10)
print(coordenadas.count(20))  # Conta ocorrências (1)
```

### Conjuntos (`set`) - Mutável, não ordenado, sem duplicatas
```python
cores = {"vermelho", "azul", "verde"}
cores.add("amarelo")
cores.remove("azul")
outro_set = {1, 2, 3}
uniao = cores | outro_set      # União
intersecao = cores & outro_set # Interseção
```

### Dicionários (`dict`) - Mapeamento chave-valor
```python
pessoa = {"nome": "Ana", "idade": 30}
pessoa["cidade"] = "São Paulo"        # Adiciona nova chave
print(pessoa["nome"])                 # Acessa valor
idade = pessoa.get("idade", 0)        # Get com valor padrão
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

---

## 3. STRINGS (Texto)

### Operações Básicas
```python
texto = "Python é incrível"
print(texto[0])          # 'P' (primeiro caractere)
print(texto[-1])         # 'l' (último caractere)
print(len(texto))        # Tamanho da string
print(texto.upper())     # Maiúsculas
print(texto.lower())     # Minúsculas
print(texto.replace("incrível", "poderoso"))
print(texto.split())     # Divide em lista
```

### Fatiamento (Slicing)
```python
s = "Hello, World!"
print(s[2:5])   # "llo" (do índice 2 ao 4)
print(s[:5])    # "Hello"
print(s[7:])    # "World!"
print(s[::-1])  # "!dlroW ,olleH" (inverte)
```

### Formatação (f-Strings - Python 3.6+)
```python
nome = "João"
idade = 25
print(f"Olá, {nome}! Você tem {idade} anos.")
print(f"{nome:>10}")     # Alinha à direita
print(f"{nome:*^10}")    # Centraliza com *
```

---

## 4. ESTRUTURAS DE CONTROLE

### Condicionais (if/elif/else)
```python
idade = 18
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")

# Operador ternário
status = "Maior" if idade >= 18 else "Menor"
```

### match/case (Python 3.10+)
```python
comando = "salvar"
match comando:
    case "salvar":
        print("Salvando...")
    case "carregar":
        print("Carregando...")
    case _:
        print("Comando inválido")
```

### Loops

#### for (iterável)
```python
for i in range(5):        # 0 a 4
    print(i)

for item in ["a", "b", "c"]:
    print(item)

for i, valor in enumerate(["a", "b", "c"]):
    print(f"Índice {i}: {valor}")
```

#### while
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

#### Controle de loops
```python
for i in range(10):
    if i == 3:
        continue      # Pula para próxima iteração
    if i == 7:
        break         # Sai do loop
    print(i)
else:
    print("Loop completo sem break")  # Executa se não houver break
```

---

## 5. FUNÇÕES

### Definição e Chamada
```python
def saudacao(nome):
    """Função simples de saudação."""
    return f"Olá, {nome}!"

print(saudacao("Maria"))
```

### Parâmetros
```python
def soma(a, b, c=0):               # Parâmetro opcional (padrão)
    return a + b + c

def varargs(*args, **kwargs):      # *args (tupla), **kwargs (dict)
    print(args)                     # (1, 2, 3)
    print(kwargs)                   # {"nome": "Ana", "idade": 25}

varargs(1, 2, 3, nome="Ana", idade=25)
```

### Funções Anônimas (lambda)
```python
quadrado = lambda x: x ** 2
print(quadrado(5))   # 25

# Útil com map, filter
numeros = [1, 2, 3, 4]
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2, 4]
dobro = list(map(lambda x: x * 2, numeros))          # [2, 4, 6, 8]
```

### Decoradores
```python
def meu_decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes da função")
        resultado = func(*args, **kwargs)
        print("Depois da função")
        return resultado
    return wrapper

@meu_decorator
def minha_funcao():
    print("Executando a função")

minha_funcao()
```

---

## 6. COMPREENSÕES (List, Dict, Set)

### List Comprehension
```python
# [expressão for item in iterável if condição]
quadrados = [x**2 for x in range(10)]                    # [0, 1, 4, 9, ...]
pares = [x for x in range(20) if x % 2 == 0]             # [0, 2, 4, ...]
matriz = [[x for x in range(3)] for y in range(3)]       # Matriz 3x3
```

### Dict Comprehension
```python
quadrados_dict = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
```

### Set Comprehension
```python
pares_set = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
```

---

## 7. PROGRAMAÇÃO ORIENTADA A OBJETOS

### Classes e Objetos
```python
class Pessoa:
    # Construtor
    def __init__(self, nome, idade):
        self.nome = nome          # Atributo público
        self._idade = idade       # Atributo "protegido" (convenção)
        self.__cpf = "123"        # Atributo privado (name mangling)
    
    # Método de instância
    def saudacao(self):
        return f"Olá, meu nome é {self.nome}"
    
    # Método de classe
    @classmethod
    def criar_anonimo(cls):
        return cls("Anônimo", 0)
    
    # Método estático
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
    # Propriedade (getter/setter)
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self._idade = valor
    
    # Representação oficial (repr)
    def __repr__(self):
        return f"Pessoa('{self.nome}', {self._idade})"
    
    # Representação amigável (str)
    def __str__(self):
        return f"{self.nome} - {self._idade} anos"

# Uso
p = Pessoa("João", 25)
print(p.saudacao())
p.idade = 26
print(p)                    # Chama __str__
print(repr(p))              # Chama __repr__
```

### Herança
```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        raise NotImplementedError

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"
    
    def buscar(self):
        return "Buscando bola"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Uso
rex = Cachorro("Rex")
print(rex.fazer_som())   # "Au au!"
print(rex.buscar())      # "Buscando bola"
```

### Herança Múltipla e super()
```python
class A:
    def metodo(self):
        print("Método de A")

class B(A):
    def metodo(self):
        print("Método de B")
        super().metodo()   # Chama método da classe pai

class C(A):
    def metodo(self):
        print("Método de C")
        super().metodo()

class D(B, C):
    def metodo(self):
        print("Método de D")
        super().metodo()   # Segue a ordem MRO (Method Resolution Order)

# MRO: D -> B -> C -> A
```

---

## 8. MANIPULAÇÃO DE ARQUIVOS

### Leitura e Escrita
```python
# Escrita
with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.write("Primeira linha\n")
    f.write("Segunda linha\n")
    f.writelines(["Terceira\n", "Quarta\n"])

# Leitura completa
with open("arquivo.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)

# Leitura linha por linha
with open("arquivo.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())  # strip() remove quebra de linha

# Modos comuns: 'r' (leitura), 'w' (escrita, sobrescreve), 'a' (append)
#               'r+' (leitura e escrita), 'x' (cria, falha se existir)
```

### Manipulação com `os` e `pathlib`
```python
import os
from pathlib import Path

# os
os.remove("arquivo.txt")           # Remove arquivo
os.path.exists("arquivo.txt")      # Verifica existência
os.mkdir("pasta")                  # Cria diretório
os.rmdir("pasta")                  # Remove diretório vazio

# pathlib (moderno, recomendado)
caminho = Path("arquivo.txt")
caminho.write_text("Conteúdo")     # Escrita
texto = caminho.read_text()        # Leitura
print(caminho.exists())            # Verifica existência
print(caminho.parent)              # Diretório pai
```

---

## 9. TRATAMENTO DE EXCEÇÕES

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Por favor, digite um número válido.")
except ZeroDivisionError as e:
    print(f"Erro: {e} - Não é possível dividir por zero.")
except Exception as e:              # Captura qualquer outra exceção
    print(f"Erro inesperado: {e}")
else:
    print("Nenhuma exceção ocorreu.")
finally:
    print("Este bloco sempre executa.")

# Criando exceções customizadas
class MeuErro(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem

# Lançando exceção
raise MeuErro("Um erro personalizado ocorreu")
```

---

## 10. MÓDULOS E PACOTES

### Importação
```python
# Importar módulo inteiro
import math
print(math.sqrt(16))   # 4.0

# Importar itens específicos
from math import pi, sin
print(pi)              # 3.14159...

# Importar com alias
import pandas as pd

# Importar tudo (não recomendado)
from os import *

# Módulo principal
if __name__ == "__main__":
    print("Executado diretamente")
```

### Estrutura de Pacote
```
meu_pacote/
    __init__.py        # Pode estar vazio
    modulo1.py
    modulo2.py
    subpacote/
        __init__.py
        modulo3.py
```

---

## 11. FUNÇÕES EMBUTIDAS ÚTEIS

| Função | Descrição | Exemplo |
|--------|-----------|---------|
| `len()` | Tamanho | `len([1,2,3])` → 3 |
| `type()` | Tipo do objeto | `type(10)` → `<class 'int'>` |
| `range()` | Sequência de números | `range(5)` → 0,1,2,3,4 |
| `enumerate()` | Índice + valor | `enumerate(['a','b'])` → (0,'a'), (1,'b') |
| `zip()` | Combina iteráveis | `zip([1,2], ['a','b'])` → (1,'a'), (2,'b') |
| `map()` | Aplica função | `map(str, [1,2])` → '1','2' |
| `filter()` | Filtra por condição | `filter(lambda x: x>0, [-1,2])` → 2 |
| `sorted()` | Ordena | `sorted([3,1,2])` → [1,2,3] |
| `sum()`, `min()`, `max()` | Soma, mínimo, máximo | `sum([1,2,3])` → 6 |
| `any()`, `all()` | Algum/Todos verdadeiros | `any([True, False])` → True |

---

## 12. DATA E HORA (`datetime`)

```python
from datetime import datetime, date, time, timedelta

# Agora
agora = datetime.now()
print(agora)                  # 2024-01-15 14:30:45.123456
print(agora.date())           # 2024-01-15
print(agora.time())           # 14:30:45.123456

# Criar datas específicas
d = date(2024, 12, 25)
t = time(10, 30, 0)
dt = datetime(2024, 12, 25, 10, 30)

# Formatação
data_str = dt.strftime("%d/%m/%Y %H:%M")  # "25/12/2024 10:30"
dt_obj = datetime.strptime("25/12/2024", "%d/%m/%Y")

# Operações com timedelta
amanha = date.today() + timedelta(days=1)
diferenca = date(2024, 12, 31) - date(2024, 1, 1)
print(diferenca.days)         # 365
```

---

## 13. TIPAGEM ESTÁTICA (Type Hints - Python 3.5+)

```python
from typing import List, Dict, Tuple, Optional, Union

# Variáveis
nome: str = "João"
idade: int = 30
altura: float = 1.75
ativo: bool = True

# Coleções
frutas: List[str] = ["maçã", "banana"]
pessoa: Dict[str, Union[str, int]] = {"nome": "Ana", "idade": 25}
coordenadas: Tuple[float, float] = (10.5, 20.3)

# Funções
def saudacao(nome: str, idade: int = 0) -> str:
    return f"Olá, {nome}!"

def dividir(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b

# Python 3.10+ permite usar | para Union
def processar(valor: int | str) -> int | str:
    return valor
```

---

## 14. GERADORES (yield)

```python
def contador(maximo):
    n = 0
    while n < maximo:
        yield n          # Pausa a função e retorna valor
        n += 1

# Uso
for i in contador(5):
    print(i)             # 0, 1, 2, 3, 4

# Gerador de uma vez
quadrados = (x**2 for x in range(10))  # Generator expression
print(next(quadrados))   # 0
print(list(quadrados))   # [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

## 15. BIBLIOTECAS IMPORTANTES (PADRÃO)

| Módulo | Utilidade |
|--------|-----------|
| `os`, `sys` | Sistema operacional, argumentos de linha de comando |
| `json` | Trabalhar com JSON |
| `re` | Expressões regulares |
| `math`, `random` | Matemática, números aleatórios |
| `collections` | `deque`, `Counter`, `defaultdict` |
| `itertools` | Iteradores eficientes |
| `functools` | Funções de alta ordem (`lru_cache`, `partial`) |
| `threading`, `asyncio` | Concorrência |
| `unittest`, `pytest` | Testes |
| `logging` | Logs estruturados |
| `argparse` | Parsing de argumentos de linha de comando |

---

## 16. EXPRESSÕES REGULARES (re)

```python
import re

texto = "Meu email é usuario@exemplo.com e também contato@teste.com"

# Buscar padrão
email = re.search(r'[\w\.-]+@[\w\.-]+', texto)
print(email.group())  # usuario@exemplo.com

# Encontrar todos
emails = re.findall(r'[\w\.-]+@[\w\.-]+', texto)
print(emails)         # ['usuario@exemplo.com', 'contato@teste.com']

# Substituir
novo = re.sub(r'@[\w\.-]+', '@dominio.com', texto)
print(novo)

# Validar
if re.match(r'^\d{5}-\d{3}$', '12345-678'):
    print("CEP válido")
```

---

## 17. OPERADORES ESPECIAIS

### Walrus Operator `:=` (Python 3.8+)
```python
# Atribui e compara em uma expressão
if (n := len([1, 2, 3])) > 2:
    print(f"Lista grande com {n} elementos")

# Em loops
while (bloco := arquivo.read(1024)):
    processar(bloco)
```

### Operadores de Identidade `is` / `is not`
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True (mesmo objeto)
print(a is c)   # False (objetos diferentes)
print(a == c)   # True (conteúdo igual)
```

---

## 18. BOAS PRÁTICAS

### Formatação de Código (PEP 8)
- **Indentação**: 4 espaços (nunca tabs)
- **Linhas**: Máximo 79 caracteres
- **Nomes**: `snake_case` para variáveis/funções, `CamelCase` para classes
- **Constantes**: `MAIUSCULAS`

### Docstrings
```python
def funcao(parametro: str) -> int:
    """
    Exemplo de docstring.

    Args:
        parametro: Descrição do parâmetro.

    Returns:
        Descrição do retorno.
    
    Raises:
        ValueError: Se algo der errado.
    """
    if not parametro:
        raise ValueError("Parâmetro inválido")
    return len(parametro)
```

### Gerenciamento de Contexto (`with`)
```python
# Para recursos que precisam ser fechados/liberados
with open("arquivo.txt") as f, open("saida.txt", "w") as out:
    for linha in f:
        out.write(linha.upper())

# Criando seu próprio context manager
from contextlib import contextmanager

@contextmanager
def abrir_recurso():
    print("Abrindo recurso")
    yield
    print("Fechando recurso")

with abrir_recurso():
    print("Usando recurso")
```

---

## 📝 RESUMO DOS COMANDOS MAIS USADOS

| Tarefa | Código |
|--------|--------|
| Criar lista | `[1, 2, 3]` |
| Adicionar à lista | `lista.append(4)` |
| Criar dict | `{"a": 1, "b": 2}` |
| Acessar valor dict | `dict["a"]` |
| If/else | `if x > 0: ... else: ...` |
| Loop for | `for i in range(10):` |
| Função | `def func():` |
| Ler arquivo | `with open("f.txt") as f: f.read()` |
| Tratar erro | `try: ... except: ...` |
| Classe | `class MinhaClasse:` |

---

Este cheat sheet cobre os tópicos principais do site que você mencionou e adiciona mais contexto e exemplos. Para uma referência ainda mais completa, consulte a [documentação oficial do Python](https://docs.python.org/pt-br/3/).

Precisa de um aprofundamento em algum tópico específico?