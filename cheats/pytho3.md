Perfeito! Vou criar um **Cheat Sheet com o DOBRO de conteúdo** do anterior, expandindo cada seção com ainda mais detalhes, exemplos avançados, bibliotecas adicionais, padrões de projeto, técnicas avançadas e muito mais. Este será um documento de referência completo.

---

# 🐍 PYTHON 3 - CHEAT SHEET MEGA COMPLETO
## *Mais de 600 exemplos práticos - Referência Definitiva*

---

## 📚 SUMÁRIO EXPANDIDO

1. [Fundamentos Básicos](#1-fundamentos-básicos)
2. [Estruturas de Dados](#2-estruturas-de-dados)
3. [Strings e Texto](#3-strings-e-texto)
4. [Estruturas de Controle](#4-estruturas-de-controle)
5. [Funções e Escopos](#5-funções-e-escopos)
6. [Compreensões e Geradores](#6-compreensões-e-geradores)
7. [Programação Orientada a Objetos](#7-programação-orientada-a-objetos)
8. [Manipulação de Arquivos](#8-manipulação-de-arquivos)
9. [Tratamento de Exceções](#9-tratamento-de-exceções)
10. [Módulos e Pacotes](#10-módulos-e-pacotes)
11. [Biblioteca Padrão Completa](#11-biblioteca-padrão-completa)
12. [Data e Hora Avançado](#12-data-e-hora-avançado)
13. [Expressões Regulares Avançado](#13-expressões-regulares-avançado)
14. [Concorrência e Paralelismo](#14-concorrência-e-paralelismo)
15. [Programação Funcional](#15-programação-funcional)
16. [Type Hints e Tipagem](#16-type-hints-e-tipagem)
17. [Manipulação de Dados](#17-manipulação-de-dados)
18. [APIs e Web](#18-apis-e-web)
19. [Testes e Debugging](#19-testes-e-debugging)
20. [Performance e Otimização](#20-performance-e-otimização)
21. [Padrões de Projeto](#21-padrões-de-projeto)
22. [Criptografia e Segurança](#22-criptografia-e-segurança)
23. [Redes e Sockets](#23-redes-e-sockets)
24. [Banco de Dados](#24-banco-de-dados)
25. [Machine Learning Básico](#25-machine-learning-básico)
26. [Automação e Scripts](#26-automação-e-scripts)
27. [Empacotamento e Distribuição](#27-empacotamento-e-distribuição)
28. [Boas Práticas e Estilo](#28-boas-práticas-e-estilo)

---

## 1. FUNDAMENTOS BÁSICOS

### 1.1 Tipos de Dados - Todos os Detalhes

```python
# Números - Detalhado
int_val = 42                          # Inteiro padrão
hex_val = 0xFF                        # Hexadecimal (255)
oct_val = 0o777                       # Octal (511)
bin_val = 0b1010                      # Binário (10)
long_int = 1_000_000_000_000          # Separador para legibilidade

# Ponto flutuante
float_val = 3.14159
scientific = 1.5e-3                   # 0.0015
infinity = float('inf')               # Infinito
nan = float('nan')                    # Not a Number

# Números complexos
c1 = 3 + 4j
c2 = complex(3, 4)                    # Mesmo que c1
print(c1.real, c1.imag)               # 3.0 4.0
print(c1.conjugate())                 # (3-4j)

# Decimal - Para precisão monetária
from decimal import Decimal, getcontext
getcontext().prec = 28                # Precisão global
preco = Decimal('0.10')
total = Decimal('0.30')
print(total - preco - preco - preco)  # 0.00 (exato!)

# Fractions - Frações exatas
from fractions import Fraction
f1 = Fraction(1, 3)                   # 1/3
f2 = Fraction(2, 5)                   # 2/5
print(f1 + f2)                        # 11/15

# Booleanos - Detalhes
bool_true = True
bool_false = False
# Valores considerados False: None, 0, 0.0, 0j, "", [], (), {}, set()
# Todos os outros são True

# None - Singularidade
none_val = None
print(none_val is None)               # True (sempre usar 'is', não '==')

# Bytes e Bytearray
bytes_val = b'hello'                  # Imutável
bytearray_val = bytearray(b'hello')   # Mutável
bytearray_val[0] = 104                # Modifica

# Memoryview - Visão de memória sem cópia
data = bytearray(b'hello')
mv = memoryview(data)
mv[0] = 72                            # Modifica data original
print(data)                           # bytearray(b'Hello')
```

### 1.2 Operadores - Todos os Tipos

```python
# Aritméticos - Avançados
a, b = 17, 5
print(divmod(a, b))                   # (3, 2) - quociente e resto
print(pow(2, 10))                     # 1024 (2**10)
print(pow(2, 10, 100))                # 24 (2**10 % 100) - modular exponentiation

# Comparação - Encadeamento
x, y, z = 5, 10, 15
print(x < y < z)                      # True (equivalente a x < y and y < z)
print(x < y > z)                      # False
print(x == y == z)                    # False

# Operadores de atribuição compostos
a = 10
a += 5                                # a = 15
a -= 3                                # a = 12
a *= 2                                # a = 24
a /= 4                                # a = 6.0
a //= 2                               # a = 3.0
a %= 2                                # a = 1.0
a **= 3                               # a = 1.0

# Operadores bitwise - Avançados
# Flags e máscaras
READ = 0b001  # 1
WRITE = 0b010 # 2
EXECUTE = 0b100 # 4

permissao = READ | WRITE               # 0b011 (3)
print(bool(permissao & READ))          # True
print(bool(permissao & EXECUTE))       # False

# Deslocamento para multiplicação/dividir por potências de 2
print(16 << 1)                         # 32 (multiplica por 2)
print(16 >> 1)                         # 8 (divide por 2)

# Operadores de identidade e associação
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(lista1 is lista2)                # False (objetos diferentes)
print(lista1 == lista2)                # True (conteúdo igual)
print(id(lista1) == id(lista2))        # False

# in e not in com containers
dicionario = {'a': 1, 'b': 2}
print('a' in dicionario)               # True (verifica chaves)
print(1 in dicionario.values())        # True (verifica valores)

# Operador Walrus (:=) - Python 3.8+ - Usos avançados
# Em compreensões de lista
resultados = [y for x in range(10) if (y := x**2) > 20]
print(resultados)                      # [25, 36, 49, 64, 81]

# Em loops while com entrada
while (linha := input("Digite: ")) != "sair":
    print(f"Você digitou: {linha}")

# Em if statements
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"Lista grande com {n} elementos")

# Operador ternário aninhado
nota = 85
conceito = "A" if nota >= 90 else "B" if nota >= 80 else "C" if nota >= 70 else "D"
```

### 1.3 Conversão de Tipos - Técnicas Avançadas

```python
# Conversões numéricas com bases
print(int("1010", 2))                  # 10 (binário)
print(int("FF", 16))                   # 255 (hexadecimal)
print(int("77", 8))                    # 63 (octal)
print(int("101010", 2))                # 42

# Formatação para bases
print(format(42, 'b'))                 # '101010'
print(format(42, 'o'))                 # '52'
print(format(42, 'x'))                 # '2a'
print(format(42, 'X'))                 # '2A'

# Conversão segura com fallback
def safe_convert(valor, tipo, fallback=None):
    try:
        return tipo(valor)
    except (ValueError, TypeError):
        return fallback

print(safe_convert("123", int, 0))     # 123
print(safe_convert("abc", int, 0))     # 0

# Conversão entre coleções com transformação
lista = [1, 2, 3, 2, 1]
tupla = tuple(lista)                   # (1, 2, 3, 2, 1)
set_unico = set(lista)                 # {1, 2, 3}
lista_unica = list(set_unico)          # [1, 2, 3]

# Conversão de string para estrutura de dados
import ast
string_dict = "{'a': 1, 'b': 2}"
dict_obj = ast.literal_eval(string_dict)  # Seguro! (não eval)
print(dict_obj['a'])                   # 1

# Conversão para bytes
string = "Olá Mundo"
bytes_utf8 = string.encode('utf-8')    # b'Ol\xc3\xa1 Mundo'
string_back = bytes_utf8.decode('utf-8')

# Conversão hexadecimal
hex_string = "48656c6c6f"
bytes_obj = bytes.fromhex(hex_string)  # b'Hello'
hex_back = bytes_obj.hex()             # '48656c6c6f'
```

---

## 2. ESTRUTURAS DE DADOS

### 2.1 Listas - Tudo que Existe

```python
# Criação avançada
lista_vazia = []
lista_comp = [x for x in range(10)]
lista_repetida = [0] * 10              # Cuidado: mesmo objeto se for mutável!
matriz = [[0] * 3 for _ in range(3)]   # Matriz 3x3 correta

# Evite: matriz_errada = [[0] * 3] * 3  # Todas linhas são o mesmo objeto!

# Inserção múltipla
lista = [1, 2, 3]
lista[1:1] = [10, 20]                 # Insere no meio: [1, 10, 20, 2, 3]
lista[2:4] = [30]                     # Substitui fatia: [1, 10, 30, 3]

# Remoção condicional
lista = [1, 2, 3, 4, 5, 6]
del lista[::2]                        # Remove índices pares: [2, 4, 6]
lista = [x for x in lista if x % 2 == 0]  # Filtra

# Métodos avançados
lista = [1, 2, 3, 2, 4, 2]
print(lista.index(2, 2))              # Busca a partir do índice 2: 3
print(lista.count(2))                 # 3

# Ordenação com key complexa
pessoas = [
    {'nome': 'Ana', 'idade': 25},
    {'nome': 'João', 'idade': 30},
    {'nome': 'Maria', 'idade': 28}
]
pessoas.sort(key=lambda p: p['idade'])
pessoas.sort(key=lambda p: p['nome'], reverse=True)

# Ordenação com múltiplas chaves
from operator import itemgetter
pessoas.sort(key=itemgetter('idade', 'nome'))

# Copiar listas - diferenças
original = [1, [2, 3], 4]
copia_rasa = original.copy()          # ou original[:], list(original)
copia_profunda = __import__('copy').deepcopy(original)

original[1][0] = 99
print(copia_rasa[1][0])               # 99 (afetado)
print(copia_profunda[1][0])           # 2 (não afetado)

# Operações matemáticas com listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista1 + lista2)                # [1, 2, 3, 4, 5, 6]
print(lista1 * 3)                     # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Listas como pilha e fila
# Pilha (LIFO) - eficiente
stack = []
stack.append(1)
stack.append(2)
stack.pop()                           # 2

# Fila (FIFO) - ineficiente com list (use deque)
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()                       # 1 (O(1))
queue.pop()                           # 4 (O(1))

# Listas como arrays eficientes
from array import array
arr = array('i', [1, 2, 3])           # array de inteiros (mais eficiente que list)
```

### 2.2 Tuplas - Detalhes e Usos

```python
# Tuplas nomeadas com valores padrão
from typing import NamedTuple

class Pessoa(NamedTuple):
    nome: str
    idade: int = 0
    email: str = ""

p = Pessoa("João", 25)
print(p.nome, p.idade)                # João 25

# Tuplas com métodos e propriedades
from collections import namedtuple
Ponto = namedtuple('Ponto', ['x', 'y', 'z'], defaults=[0, 0, 0])
p1 = Ponto(10, 20)                    # z=0
print(p1._fields)                     # ('x', 'y', 'z')
print(p1._asdict())                   # {'x': 10, 'y': 20, 'z': 0}
p2 = p1._replace(x=99)                # Cria nova tupla com x=99

# Desempacotamento avançado
tupla = (1, 2, 3, 4, 5)
a, *b, c = tupla                      # a=1, b=[2,3,4], c=5
*a, b, c = tupla                      # a=[1,2,3], b=4, c=5
a, b, *c = tupla                      # a=1, b=2, c=[3,4,5]

# Desempacotamento em funções
def processar(*args):
    return sum(args)

valores = (1, 2, 3, 4)
print(processar(*valores))            # 10

# Tuplas como chaves de dicionário
cache = {}
cache[(10, 20)] = "coordenada"
cache[(10, 20, 30)] = "3D"
print(cache[(10, 20)])                # coordenada

# Tuplas imutáveis vs listas mutáveis
t = ([1, 2], 3)                       # Tupla contém lista mutável
t[0].append(3)                        # OK! Modifica a lista dentro da tupla
# t[0] = [4, 5]                       # ERRO! Não pode reatribuir elemento da tupla
```

### 2.3 Dicionários - Tudo sobre

```python
# Criação avançada
from collections import OrderedDict, defaultdict, ChainMap

# dict comprehension com condição
d = {x: x**2 for x in range(10) if x % 2 == 0}  # {0:0, 2:4, 4:16, 6:36, 8:64}

# From keys
chaves = ['a', 'b', 'c']
dict_from_keys = dict.fromkeys(chaves, 0)        # {'a':0, 'b':0, 'c':0}

# Zip de listas
nomes = ['Ana', 'João', 'Maria']
idades = [25, 30, 28]
pessoas = dict(zip(nomes, idades))               # {'Ana':25, 'João':30, 'Maria':28}

# Métodos avançados
d = {'a': 1, 'b': 2, 'c': 3}

# get com valor padrão e callback
valor = d.get('d', default=0)                    # 0
valor = d.setdefault('d', 4)                     # 4 (insere e retorna)
valor = d.setdefault('d', 5)                     # 4 (já existe, não insere)

# Pop com valor padrão
valor = d.pop('z', None)                         # None (não levanta erro)

# Update com múltiplas fontes
d.update({'e': 5, 'f': 6})
d.update(g=7, h=8)                               # kwargs
d.update([('i', 9), ('j', 10)])                  # lista de tuplas

# Merging (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2                           # {'a':1, 'b':3, 'c':4}
dict1 |= dict2                                   # Atualiza dict1 in-place

# Dicionários aninhados - criação segura
from collections import defaultdict

# Auto-criação de níveis
nested = defaultdict(lambda: defaultdict(list))
nested['pessoa1']['amigos'].append('João')
nested['pessoa1']['amigos'].append('Maria')
print(dict(nested['pessoa1']))                   # {'amigos': ['João', 'Maria']}

# ChainMap - múltiplos dicionários como um
defaults = {'host': 'localhost', 'port': 8080}
user_config = {'port': 9090, 'debug': True}
config = ChainMap(user_config, defaults)
print(config['host'])                             # 'localhost'
print(config['port'])                             # 9090 (do user_config)
print(config['debug'])                            # True

# OrderedDict - operações específicas
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od.move_to_end('a')                               # Move 'a' para o final
od.move_to_end('b', last=False)                   # Move 'b' para o início
print(list(od.keys()))                            # ['b', 'c', 'a']

# Counter - operações avançadas
from collections import Counter
c1 = Counter(a=3, b=2, c=1)
c2 = Counter(a=1, b=2, c=3)
print(c1 + c2)                                    # Counter({'a':4, 'b':4, 'c':4})
print(c1 - c2)                                    # Counter({'a':2})
print(c1 & c2)                                    # Counter({'b':2, 'c':1}) (min)
print(c1 | c2)                                    # Counter({'a':3, 'b':2, 'c':3}) (max)
print(c1.total())                                 # 6 (Python 3.10+)
```

### 2.4 Conjuntos - Operações Avançadas

```python
# Operações de conjunto detalhadas
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Métodos equivalentes a operadores
print(A.union(B))                    # {1,2,3,4,5,6,7,8}
print(A.intersection(B))             # {4,5}
print(A.difference(B))               # {1,2,3}
print(A.symmetric_difference(B))     # {1,2,3,6,7,8}

# Atualizações in-place
A.update([10, 11])                   # Adiciona múltiplos
A.intersection_update(B)             # Mantém apenas interseção
A.difference_update({1, 2})          # Remove elementos
A.symmetric_difference_update([6])   # Adiciona se não existe, remove se existe

# Frozenset - conjunto imutável
fs = frozenset([1, 2, 3])
# fs.add(4)                          # ERRO!

# Set comprehension com condição
pares = {x for x in range(20) if x % 2 == 0}  # {0,2,4,...,18}
quadrados = {x**2 for x in range(-5, 6)}      # {0,1,4,9,16,25}

# Conjuntos para remoção de duplicatas mantendo ordem
def unique_ordered(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

lista = [1, 2, 2, 3, 1, 4, 5, 4]
print(unique_ordered(lista))         # [1, 2, 3, 4, 5]
```

### 2.5 Estruturas de Dados Especializadas

```python
# Heap (priority queue)
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
print(heapq.heappop(heap))           # 1 (menor)
print(heap)                          # [3, 5]

# Heap com tuplas para prioridade
tarefas = []
heapq.heappush(tarefas, (1, 'tarefa baixa'))
heapq.heappush(tarefas, (0, 'tarefa alta'))
print(heapq.heappop(tarefas))        # (0, 'tarefa alta')

# Heapify a partir de lista
lista = [9, 5, 4, 1, 3, 2]
heapq.heapify(lista)                 # Transforma em heap in-place
print(lista)                         # [1, 3, 2, 5, 9, 4]

# nlargest, nsmallest
numeros = [10, 5, 20, 15, 25, 30]
print(heapq.nlargest(3, numeros))    # [30, 25, 20]
print(heapq.nsmallest(3, numeros))   # [5, 10, 15]

# Deque - operações específicas
from collections import deque
d = deque(maxlen=5)                  # Tamanho máximo
d.extend([1, 2, 3, 4, 5])
d.append(6)                          # Remove 1 automaticamente
print(d)                             # deque([2,3,4,5,6], maxlen=5)

# Rotação
d.rotate(2)                          # [5,6,2,3,4]
d.rotate(-1)                         # [6,2,3,4,5]

# Limitar tamanho
d = deque()
d.append(1)
d.appendleft(2)
d.extend([3, 4])
d.extendleft([0, -1])                # Adiciona à esquerda em ordem inversa

# UserDict - Dicionário customizado
from collections import UserDict

class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
    
    def __getitem__(self, key):
        return super().__getitem__(key.lower())

d = CaseInsensitiveDict()
d['Hello'] = 'World'
print(d['HELLO'])                    # 'World'

# Enum - Enumerations
from enum import Enum, auto, IntEnum

class Status(Enum):
    PENDING = 1
    PROCESSING = 2
    COMPLETED = 3
    FAILED = 4

class AutoStatus(Enum):
    PENDING = auto()                  # 1
    PROCESSING = auto()               # 2
    COMPLETED = auto()                # 3

print(Status.PENDING.name)            # 'PENDING'
print(Status.PENDING.value)           # 1

# Enum com valores de string
class Color(str, Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

# Data Classes (Python 3.7+)
from dataclasses import dataclass, field, asdict, astuple
from typing import List

@dataclass
class Produto:
    nome: str
    preco: float
    tags: List[str] = field(default_factory=list)
    desconto: float = field(default=0.0)
    
    def preco_com_desconto(self) -> float:
        return self.preco * (1 - self.desconto)

p = Produto("Notebook", 2500.0, ["eletrônico", "computador"], 0.1)
print(p)                              # Produto(nome='Notebook', preco=2500.0, ...)
print(asdict(p))                      # Dicionário
print(astuple(p))                     # Tupla
```

---

## 3. STRINGS E TEXTO

### 3.1 Strings - Métodos Completos

```python
# Todas as operações de string
s = "  Python Programming  "

# Remoção de caracteres específicos
print(s.strip(' P'))                  # 'ython Programming  '
print(s.lstrip(' P'))                 # 'ython Programming  '
print(s.rstrip(' g'))                 # '  Python Programmin'

# Justificação e preenchimento
print(s.center(30, '*'))              # '***  Python Programming  ***'
print(s.ljust(30, '-'))               # '  Python Programming  ------'
print(s.rjust(30, '-'))               # '------  Python Programming  '

# Formatação avançada com format()
print("{0}, {1}, {2}".format(1, 2, 3))                    # Posicional
print("{a}, {b}, {c}".format(a=1, b=2, c=3))              # Nomeado
print("{0[0]}, {0[1]}".format([1, 2]))                    # Indexado
print("{0.a}, {0.b}".format(type('', (), {'a':1, 'b':2})())) # Atributo

# Formatação de números com format()
print("{:>10.2f}".format(3.14159))     # '      3.14'
print("{:<10.2f}".format(3.14159))     # '3.14      '
print("{:^10.2f}".format(3.14159))     # '   3.14   '
print("{:+10.2f}".format(3.14159))     # '     +3.14'
print("{:-10.2f}".format(-3.14159))    # '    -3.14'
print("{: 10.2f}".format(3.14159))     # '     3.14' (espaço para positivo)

# Formatação de números grandes
print("{:,}".format(1000000))          # '1,000,000'
print("{:_}".format(1000000))          # '1_000_000'
print("{:.2e}".format(1000000))        # '1.00e+06'

# Formatação de porcentagem
print("{:.2%}".format(0.25))           # '25.00%'

# Conversão de strings
print("Hello World".swapcase())        # 'hELLO wORLD'
print("hello world".title())           # 'Hello World'
print("hello world".capitalize())      # 'Hello world'
print("hello world".casefold())        # 'hello world' (para comparação case-insensitive)

# Detecção de tipo de caracteres
print("Hello123".isalnum())            # True
print("Hello".isalpha())               # True
print("123".isdigit())                 # True
print("123".isnumeric())               # True (inclui caracteres numéricos como ½)
print("  ".isspace())                  # True
print("Hello".istitle())               # True
print("HELLO".isupper())               # True
print("hello".islower())               # True
print("Hello".isprintable())           # True
print("Hello\n".isprintable())         # False

# Verificações de início/fim
print("hello.txt".startswith(('hello', 'world')))  # True
print("hello.txt".endswith(('.txt', '.py')))       # True

# Encoding e Decoding
s = "Olá Mundo 🌍"
encoded = s.encode('utf-8')            # b'Ol\xc3\xa1 Mundo \xf0\x9f\x8c\x8d'
decoded = encoded.decode('utf-8')      # 'Olá Mundo 🌍'

# Strings raw e literais
raw_string = r"C:\Users\Name\Documents"  # Ignora escapes
bytes_string = b"binary data"
unicode_string = u"unicode string"
f_string = f"formatado {42}"

# Strings multilinha com indentação controlada
import textwrap
multiline = """
    Linha 1
        Linha 2 indentada
    Linha 3
"""
dedented = textwrap.dedent(multiline)  # Remove indentação comum
print(dedented)
```

### 3.2 F-Strings - Tudo que Você Precisa

```python
# F-strings básicas
nome, idade = "João", 25
print(f"{nome} tem {idade} anos")

# Expressões dentro de f-strings
print(f"2 + 2 = {2 + 2}")
print(f"{nome.upper()} tem {idade * 2} anos")

# F-strings multilinha
mensagem = f"""
Olá {nome}!
Você tem {idade} anos.
Daqui a 5 anos terá {idade + 5}.
"""

# Formatação com f-strings
pi = 3.141592653589793
print(f"{pi:.2f}")                     # '3.14'
print(f"{pi:.5f}")                     # '3.14159'
print(f"{pi:10.2f}")                   # '      3.14'
print(f"{pi:010.2f}")                  # '0000003.14'

# Alinhamento
texto = "Python"
print(f"{texto:>10}")                  # '    Python'
print(f"{texto:<10}")                  # 'Python    '
print(f"{texto:^10}")                  # '  Python  '
print(f"{texto:*^10}")                 # '**Python**'

# Números
numero = 1234567
print(f"{numero:,}")                   # '1,234,567'
print(f"{numero:_}")                   # '1_234_567'
print(f"{numero:b}")                   # '100101101011010000111' (binário)
print(f"{numero:o}")                   # '4553207' (octal)
print(f"{numero:x}")                   # '12d687' (hex)
print(f"{numero:X}")                   # '12D687' (hex maiúsculo)

# Datas
from datetime import datetime
agora = datetime.now()
print(f"{agora:%Y-%m-%d %H:%M:%S}")    # '2024-01-15 14:30:45'

# Debugging (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}")                   # 'x=10, y=20'
print(f"{x + y=}")                     # 'x + y=30'
print(f"{[x for x in range(5)]=}")     # '[x for x in range(5)]=[0, 1, 2, 3, 4]'

# Strings com aspas
print(f'He said {"I\'m here"}')        # He said I'm here
print(f"""He said {"I'm here"}""")     # He said I'm here

# F-strings com self em classes
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return f"{self.nome}"
    
    def __format__(self, format_spec):
        if format_spec == 'upper':
            return self.nome.upper()
        return self.nome

p = Pessoa("João")
print(f"{p:upper}")                    # 'JOÃO'

# F-strings aninhadas
width = 10
precision = 2
value = 3.14159
print(f"{value:{width}.{precision}f}") # '      3.14'
```

### 3.3 Manipulação de Texto Avançada

```python
# Textwrap - Formatação de texto
import textwrap

texto = "Este é um texto muito longo que precisa ser quebrado em várias linhas com um comprimento máximo específico."

# Quebra de linhas
print(textwrap.fill(texto, width=40))
print(textwrap.shorten(texto, width=40, placeholder="..."))

# Indentação
print(textwrap.indent(texto, '    '))

# Remover indentação comum
texto_indentado = """
    Linha 1
        Linha 2 indentada
    Linha 3
"""
print(textwrap.dedent(texto_indentado))

# StringIO - Manipular strings como arquivos
from io import StringIO

buffer = StringIO()
buffer.write("Linha 1\n")
buffer.write("Linha 2\n")
buffer.seek(0)
print(buffer.read())                   # Lê tudo
buffer.close()

# Template strings
from string import Template

t = Template('Olá $nome, você tem $idade anos')
print(t.substitute(nome='João', idade=25))
print(t.safe_substitute(nome='Maria'))  # $idade não substituído

# Unicode e normalização
import unicodedata

texto = "café"
normalizado = unicodedata.normalize('NFD', texto)  # 'cafe\u0301'
print(ascii(normalizado))              # 'cafe\u0301'

# Remover acentos
def remove_acentos(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    return ''.join([c for c in nfkd if not unicodedata.combining(c)])

print(remove_acentos("Olá, café!"))    # 'Ola, cafe!'

# Diferença entre strings (difflib)
import difflib

str1 = "Python Programming"
str2 = "Python Programing"
diff = difflib.SequenceMatcher(None, str1, str2)
print(diff.ratio())                    # 0.947...
print(list(difflib.ndiff([str1], [str2])))

# Encontrar similaridade
print(difflib.get_close_matches('appple', ['apple', 'banana', 'app', 'apply']))
# ['apple', 'apply', 'app']
```

---

## 4. ESTRUTURAS DE CONTROLE

### 4.1 Condicionais - Padrões Avançados

```python
# Switch/Case (match) - Python 3.10+ - Padrões avançados
def processar(valor):
    match valor:
        case 0:
            return "Zero"
        case 1 | 2 | 3:
            return "Pequeno"
        case int(x) if x > 100:
            return f"Grande: {x}"
        case [a, b]:
            return f"Lista de 2 elementos: {a}, {b}"
        case [a, *resto]:
            return f"Lista com cabeça {a} e resto {resto}"
        case {"nome": nome, "idade": idade}:
            return f"Pessoa: {nome}, {idade} anos"
        case (x, y):
            return f"Tupla: {x}, {y}"
        case _:
            return "Outro"

# Pattern matching com enumerações
from enum import Enum

class Cor(Enum):
    VERMELHO = 1
    VERDE = 2
    AZUL = 3

def cor_para_rgb(cor):
    match cor:
        case Cor.VERMELHO:
            return (255, 0, 0)
        case Cor.VERDE:
            return (0, 255, 0)
        case Cor.AZUL:
            return (0, 0, 255)

# Pattern matching com classes
from dataclasses import dataclass

@dataclass
class Ponto:
    x: int
    y: int

def localizar(ponto):
    match ponto:
        case Ponto(0, 0):
            return "Origem"
        case Ponto(0, y):
            return f"No eixo Y em {y}"
        case Ponto(x, 0):
            return f"No eixo X em {x}"
        case Ponto(x, y):
            return f"Ponto ({x}, {y})"

# Guard conditions
def classificar(numero):
    match numero:
        case int(x) if x > 0:
            return "Positivo"
        case int(x) if x < 0:
            return "Negativo"
        case 0:
            return "Zero"

# Pattern matching com dicionários
def processar_config(config):
    match config:
        case {'host': host, 'port': port}:
            return f"Conectando a {host}:{port}"
        case {'host': host}:
            return f"Conectando a {host}:8080 (porta padrão)"
        case _:
            return "Configuração inválida"
```

### 4.2 Loops - Técnicas Avançadas

```python
# For com itertools
import itertools

# Ciclo infinito
contador = itertools.count(10, 5)    # 10, 15, 20, ...
for i, val in zip(range(5), contador):
    print(val)                        # 10, 15, 20, 25, 30

# Ciclo com repetição
for val in itertools.repeat('A', 5):
    print(val)                        # A, A, A, A, A

# Ciclo cíclico
ciclo = itertools.cycle([1, 2, 3])
for i, val in zip(range(7), ciclo):
    print(val)                        # 1, 2, 3, 1, 2, 3, 1

# Iterando sobre combinações
itens = ['A', 'B', 'C']
for r in range(1, 4):
    for comb in itertools.combinations(itens, r):
        print(comb)

# Iterando sobre permutações
for perm in itertools.permutations(itens, 2):
    print(perm)

# Iterando sobre produto cartesiano
for prod in itertools.product([1, 2], ['a', 'b']):
    print(prod)

# Iterando sobre combinações com repetição
for comb in itertools.combinations_with_replacement(itens, 2):
    print(comb)

# For com zip_longest
from itertools import zip_longest

a = [1, 2, 3]
b = ['a', 'b']
for x, y in zip_longest(a, b, fillvalue=0):
    print(x, y)                       # (1,a), (2,b), (3,0)

# For com enumerate iniciando em valor personalizado
for i, val in enumerate(['a', 'b', 'c'], start=1):
    print(f"{i}: {val}")

# For com sorted e key
dados = ['abc', 'de', 'fghi', 'j']
for item in sorted(dados, key=len):
    print(item)                       # 'j', 'de', 'abc', 'fghi'

# For com reversed
for item in reversed([1, 2, 3, 4]):
    print(item)                       # 4, 3, 2, 1

# While com else e break
contador = 0
while contador < 10:
    if contador == 5:
        break
    contador += 1
else:
    print("Loop completo")            # Não executa (break)

# Loops com sentinela
def processar_dados():
    while True:
        linha = input("Digite (ou 'sair'): ")
        if linha == 'sair':
            break
        print(f"Processando: {linha}")

# Loop com iterador manual
iterador = iter([1, 2, 3])
while True:
    try:
        valor = next(iterador)
        print(valor)
    except StopIteration:
        break
```

### 4.3 Context Managers - With Statement Avançado

```python
# Context managers personalizados com contextlib
from contextlib import contextmanager

@contextmanager
def gerenciador_recurso():
    print("Abrindo recurso")
    try:
        yield "recurso"
    finally:
        print("Fechando recurso")

with gerenciador_recurso() as recurso:
    print(f"Usando {recurso}")

# Múltiplos context managers
with open('arquivo1.txt') as f1, open('arquivo2.txt') as f2:
    dados1 = f1.read()
    dados2 = f2.read()

# Suppress - Ignorar exceções
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('arquivo_inexistente.txt')  # Não levanta erro

# Redirect stdout/stderr
from contextlib import redirect_stdout, redirect_stderr
import io

f = io.StringIO()
with redirect_stdout(f):
    print("Este texto vai para o buffer")
conteudo = f.getvalue()
print(f"Capturado: {conteudo}")

# ExitStack - Gerenciar múltiplos contextos dinamicamente
from contextlib import ExitStack

with ExitStack() as stack:
    arquivos = []
    for nome in ['a.txt', 'b.txt', 'c.txt']:
        arquivo = stack.enter_context(open(nome, 'w'))
        arquivos.append(arquivo)
    # Todos arquivos serão fechados automaticamente

# Classe com context manager
class Recurso:
    def __enter__(self):
        print("Abrindo")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando")
        if exc_type:
            print(f"Exceção: {exc_val}")
        return True  # Suprime exceção

with Recurso() as r:
    raise ValueError("Erro")  # Será suprimido
```

---

## 5. FUNÇÕES E ESCOPOS

### 5.1 Funções - Tudo que Existe

```python
# Funções com assinaturas complexas
def funcao_completa(
    posicional1,           # Posicional obrigatório
    posicional2,           # Posicional obrigatório
    /,                     # Separa posicionais de posicionais/nomeados
    pos_ou_nome1,          # Pode ser posicional ou nomeado
    pos_ou_nome2,          # Pode ser posicional ou nomeado
    *,                     # Separa nomeados obrigatórios
    nomeado1,              # Nomeado obrigatório
    nomeado2="padrão"      # Nomeado com padrão
):
    pass

# Exemplo prático
def configurar(
    host,
    port,
    /,
    timeout=30,
    *,
    debug=False,
    ssl=True
):
    print(f"Host: {host}, Port: {port}")
    print(f"Timeout: {timeout}, Debug: {debug}, SSL: {ssl}")

# Chamadas válidas
configurar("localhost", 8080)
configurar("localhost", 8080, 60, debug=True)
configurar("localhost", 8080, debug=True, timeout=45)

# Funções com docstring detalhada
def funcao_exemplo(param1: str, param2: int = 0) -> bool:
    """
    Exemplo de função com docstring completa.

    Descrição detalhada do que a função faz.

    Args:
        param1 (str): Descrição do primeiro parâmetro
        param2 (int, optional): Descrição do segundo. Defaults to 0.

    Returns:
        bool: Descrição do retorno

    Raises:
        ValueError: Se param1 for vazio
        TypeError: Se param2 não for int

    Examples:
        >>> funcao_exemplo("teste", 5)
        True
        >>> funcao_exemplo("")
        Traceback (most recent call last):
        ...
        ValueError: param1 não pode ser vazio
    """
    if not param1:
        raise ValueError("param1 não pode ser vazio")
    return param2 > 0

# Funções com cache (lru_cache)
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    """Fibonacci com cache automático"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Rápido mesmo com recursão

# Funções com memoization manual
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fatorial(n):
    if n < 2:
        return 1
    return n * fatorial(n-1)

# Funções com partial
from functools import partial

def potencia(base, exp):
    return base ** exp

quadrado = partial(potencia, exp=2)
cubo = partial(potencia, exp=3)
print(quadrado(5))  # 25
print(cubo(5))      # 125

# Funções com singledispatch (sobrecarga)
from functools import singledispatch

@singledispatch
def processar(arg):
    return f"Tipo desconhecido: {type(arg)}"

@processar.register(int)
def _(arg):
    return f"Inteiro: {arg}"

@processar.register(str)
def _(arg):
    return f"String: {arg.upper()}"

@processar.register(list)
@processar.register(tuple)
def _(arg):
    return f"Coleção com {len(arg)} itens"

print(processar(10))      # Inteiro: 10
print(processar("teste")) # String: TESTE
print(processar([1,2,3])) # Coleção com 3 itens

# Funções com closures e fábrica de funções
def criar_contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar

contador1 = criar_contador()
contador2 = criar_contador()
print(contador1())  # 1
print(contador1())  # 2
print(contador2())  # 1

# Funções aninhadas com acesso a variáveis
def externa(x):
    def interna(y):
        return x + y
    return interna

soma_5 = externa(5)
print(soma_5(3))  # 8

# Funções como decoradores com argumentos
def repetir(vezes=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            resultados = []
            for _ in range(vezes):
                resultados.append(func(*args, **kwargs))
            return resultados
        return wrapper
    return decorator

@repetir(3)
def saudacao(nome):
    return f"Olá {nome}"

print(saudacao("João"))  # ['Olá João', 'Olá João', 'Olá João']
```

### 5.2 Escopo e Closures - Detalhes

```python
# Escopo LEGB (Local, Enclosing, Global, Built-in)
x = "global"

def externa():
    x = "enclosing"
    
    def interna():
        x = "local"
        print(x)  # "local"
    
    interna()
    print(x)  # "enclosing"

externa()
print(x)  # "global"

# Nonlocal em múltiplos níveis
def contador():
    count = 0
    
    def incrementar():
        nonlocal count
        count += 1
        return count
    
    def decrementar():
        nonlocal count
        count -= 1
        return count
    
    return incrementar, decrementar

inc, dec = contador()
print(inc())  # 1
print(inc())  # 2
print(dec())  # 1

# Global em funções aninhadas
contador_global = 0

def incrementar_global():
    global contador_global
    contador_global += 1

incrementar_global()
print(contador_global)  # 1

# Variáveis built-in
print(__builtins__.print)  # Acesso à função built-in

# Closures com atributos
def criar_contador_com_atributo():
    def contador():
        contador.count += 1
        return contador.count
    contador.count = 0
    return contador

c = criar_contador_com_atributo()
print(c())  # 1
print(c())  # 2
print(c.count)  # 2

# Escopo em compreensões (Python 3)
x = "global"
lista = [x for x in range(5)]  # x não vaza para fora
print(x)  # "global" (não sobrescreve)

# Escopo em loops (Python 3)
for x in range(5):
    pass
print(x)  # 4 (vaza! Cuidado!)

# Funções com argumentos mutáveis - cuidado!
def adicionar(valor, lista=[]):  # Problema: lista compartilhada
    lista.append(valor)
    return lista

print(adicionar(1))  # [1]
print(adicionar(2))  # [1, 2] (surpresa!)

def adicionar_correto(valor, lista=None):
    if lista is None:
        lista = []
    lista.append(valor)
    return lista
```

---

## 6. COMPREENSÕES E GERADORES

### 6.1 Comprehensions - Todos os Padrões

```python
# List comprehension aninhada com múltiplas condições
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pares = [num for linha in matriz for num in linha if num % 2 == 0]
print(pares)  # [2, 4, 6, 8]

# List comprehension com if-else
resultados = [x if x % 2 == 0 else -x for x in range(10)]
print(resultados)  # [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

# Dict comprehension com múltiplas fontes
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values) if v > 1}
print(d)  # {'b': 2, 'c': 3}

# Set comprehension com transformação
palavras = ["python", "java", "python", "c++", "java"]
unicos = {p.upper() for p in palavras}
print(unicos)  # {'PYTHON', 'JAVA', 'C++'}

# Nested comprehensions - matriz transposta
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposta = [[linha[i] for linha in matriz] for i in range(3)]
print(transposta)  # [[1,4,7], [2,5,8], [3,6,9]]

# Comprehensions com condição complexa
numeros = range(20)
resultado = [x for x in numeros if x % 2 == 0 if x % 3 == 0]  # Múltiplos de 6
print(resultado)  # [0, 6, 12, 18]

# Comprehension com função
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = [x for x in range(100) if eh_primo(x)]
print(primos[:10])  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Comprehension com walrus operator (Python 3.8+)
resultados = [y for x in range(10) if (y := x**2) > 20]
print(resultados)  # [25, 36, 49, 64, 81]

# Dict comprehension com transformação de chaves
d = {'a': 1, 'b': 2, 'c': 3}
invertido = {v: k for k, v in d.items()}
print(invertido)  # {1: 'a', 2: 'b', 3: 'c'}

# Comprehension com defaultdict
from collections import defaultdict
palavras = ["python", "java", "python", "c", "java", "python"]
contagem = defaultdict(int)
{contagem.__setitem__(p, contagem[p] + 1) for p in palavras}
print(dict(contagem))  # {'python': 3, 'java': 2, 'c': 1}
```

### 6.2 Geradores - Técnicas Avançadas

```python
# Gerador infinito com yield
def gerador_infinito():
    n = 0
    while True:
        yield n
        n += 1

gen = gerador_infinito()
for i, val in zip(range(10), gen):
    print(val)  # 0,1,2,3,4,5,6,7,8,9

# Gerador com send() - comunicação bidirecional
def corrotina():
    while True:
        valor = yield
        print(f"Recebido: {valor}")

c = corrotina()
next(c)  # Inicializa (ou c.send(None))
c.send("Hello")  # Recebido: Hello
c.send("World")  # Recebido: World

# Gerador com yield from
def subgerador():
    yield 1
    yield 2
    yield 3

def gerador_principal():
    yield 0
    yield from subgerador()
    yield 4

print(list(gerador_principal()))  # [0, 1, 2, 3, 4]

# Gerador com recursão
def gerador_arvore(node):
    yield node
    for child in node.children:
        yield from gerador_arvore(child)

# Gerador com throw() e close()
def gerador_com_tratamento():
    try:
        yield 1
        yield 2
    except ValueError as e:
        print(f"Erro: {e}")
    finally:
        print("Limpando")

g = gerador_com_tratamento()
print(next(g))  # 1
print(next(g))  # 2
g.throw(ValueError("Algo errado"))  # Erro: Algo errado
g.close()  # Limpando

# Generator expressions encadeadas
numeros = (x for x in range(10))
quadrados = (x**2 for x in numeros)
pares_quadrados = (x for x in quadrados if x % 2 == 0)
print(list(pares_quadrados))  # [0, 4, 16, 36, 64]

# Pipeline com geradores
def leitor(arquivo):
    for linha in arquivo:
        yield linha.strip()

def filtro(linhas, palavra):
    for linha in linhas:
        if palavra in linha:
            yield linha

def transformador(linhas):
    for linha in linhas:
        yield linha.upper()

def contador(linhas):
    for linha in linhas:
        yield len(linha)

# Uso
with open('dados.txt') as f:
    pipeline = contador(transformador(filtro(leitor(f), 'erro')))
    for tam in pipeline:
        print(tam)

# Gerador para números de Fibonacci
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])  # [0,1,1,2,3,5,8,13,21,34]

# Gerador para leitura de arquivos grandes
def read_large_file(file_path, chunk_size=1024):
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Gerador para processamento em lote
def batch_process(items, batch_size=100):
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch
```

### 6.3 Iteradores Personalizados

```python
# Classe iterável
class Contador:
    def __init__(self, maximo):
        self.maximo = maximo
        self.atual = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.atual >= self.maximo:
            raise StopIteration
        self.atual += 1
        return self.atual

for num in Contador(5):
    print(num)  # 1,2,3,4,5

# Iterador com dois sentidos
class RangeIteravel:
    def __init__(self, inicio, fim, passo=1):
        self.inicio = inicio
        self.fim = fim
        self.passo = passo
    
    def __iter__(self):
        return RangeIterator(self.inicio, self.fim, self.passo)

class RangeIterator:
    def __init__(self, inicio, fim, passo):
        self.atual = inicio
        self.fim = fim
        self.passo = passo
    
    def __next__(self):
        if (self.passo > 0 and self.atual >= self.fim) or \
           (self.passo < 0 and self.atual <= self.fim):
            raise StopIteration
        valor = self.atual
        self.atual += self.passo
        return valor

# Iterador com protocolo de contexto
class ArquivoIterador:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.arquivo = None
    
    def __iter__(self):
        self.arquivo = open(self.nome_arquivo)
        return self
    
    def __next__(self):
        linha = self.arquivo.readline()
        if not linha:
            raise StopIteration
        return linha.strip()
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        if self.arquivo:
            self.arquivo.close()

with ArquivoIterador('dados.txt') as iterador:
    for linha in iterador:
        print(linha)
```

---

## 7. PROGRAMAÇÃO ORIENTADA A OBJETOS

### 7.1 Classes - Tudo que Existe

```python
# Classe completa com todos os métodos especiais
class Pessoa:
    """Classe exemplo com todos os métodos especiais"""
    
    # Atributo de classe
    especie = "Homo sapiens"
    contador = 0
    
    def __init__(self, nome, idade):
        """Construtor"""
        self.nome = nome
        self.idade = idade
        self._privado = "protegido"
        self.__privado = "privado"  # Name mangling
        Pessoa.contador += 1
    
    # Métodos de instância
    def saudacao(self):
        return f"Olá, sou {self.nome}"
    
    # Métodos de classe
    @classmethod
    def criar_anonimo(cls):
        return cls("Anônimo", 0)
    
    @classmethod
    def from_dict(cls, dados):
        return cls(dados['nome'], dados['idade'])
    
    # Métodos estáticos
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
    # Properties
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = valor
    
    @idade.deleter
    def idade(self):
        del self._idade
    
    # Métodos especiais
    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"
    
    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"
    
    def __len__(self):
        return len(self.nome)
    
    def __eq__(self, other):
        if not isinstance(other, Pessoa):
            return False
        return self.nome == other.nome and self.idade == other.idade
    
    def __lt__(self, other):
        return self.idade < other.idade
    
    def __hash__(self):
        return hash((self.nome, self.idade))
    
    def __add__(self, other):
        return Pessoa(f"{self.nome} & {other.nome}", 
                      max(self.idade, other.idade))
    
    def __call__(self):
        return f"Chamando {self.nome}"
    
    def __getitem__(self, key):
        if key == 'nome':
            return self.nome
        elif key == 'idade':
            return self.idade
        raise KeyError(key)
    
    def __setitem__(self, key, value):
        if key == 'nome':
            self.nome = value
        elif key == 'idade':
            self.idade = value
        else:
            raise KeyError(key)
    
    def __contains__(self, item):
        return item in self.nome or item == str(self.idade)
    
    def __enter__(self):
        print("Entrando no contexto")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saindo do contexto")
        return False  # Não suprime exceções
    
    def __del__(self):
        Pessoa.contador -= 1

# Uso
p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 30)

print(p1)                    # João (25 anos)
print(repr(p1))              # Pessoa('João', 25)
print(len(p1))               # 4
print(p1 == p2)              # False
print(p1 < p2)               # True
print(p1 + p2)               # João & Maria (30 anos)
print(p1())                  # Chamando João
print(p1['nome'])            # João
p1['idade'] = 26
print(25 in p1)              # True (25 está na idade)

with p1:
    print("Dentro do contexto")

# Herança com super()
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self._salario = salario
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("Salário não pode ser negativo")
        self._salario = valor
    
    def saudacao(self):
        return f"Olá, sou {self.nome} e trabalho como {self.cargo}"
    
    def __str__(self):
        return f"{super().__str__()} - {self.cargo}"

# Herança múltipla e MRO
class A:
    def metodo(self):
        return "A"

class B(A):
    def metodo(self):
        return "B"

class C(A):
    def metodo(self):
        return "C"

class D(B, C):
    def metodo(self):
        return "D"

print(D.__mro__)  # D, B, C, A, object
```

### 7.2 Metaclasses e Programação Avançada

```python
# Metaclasse básica
class Meta(type):
    def __new__(mcs, nome, bases, dct):
        # Adiciona atributo de classe
        dct['versao'] = 1.0
        dct['criado_por'] = 'Metaclasse'
        
        # Valida métodos
        for key, value in dct.items():
            if callable(value) and key != '__init__':
                dct[key] = mcs._decorar_metodo(value)
        
        return super().__new__(mcs, nome, bases, dct)
    
    @staticmethod
    def _decorar_metodo(func):
        def wrapper(*args, **kwargs):
            print(f"Chamando {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    def __call__(cls, *args, **kwargs):
        print(f"Criando instância de {cls.__name__}")
        return super().__call__(*args, **kwargs)

class MinhaClasse(metaclass=Meta):
    def metodo(self):
        return "Executando"

obj = MinhaClasse()
print(obj.metodo())
print(obj.versao)  # 1.0

# Singleton com metaclasse
class SingletonMeta(type):
    _instancias = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls._instancias[cls] = super().__call__(*args, **kwargs)
        return cls._instancias[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, valor):
        self.valor = valor

s1 = Singleton(10)
s2 = Singleton(20)
print(s1 is s2)  # True
print(s1.valor)  # 10 (primeiro valor)

# Descritores - Controlar acesso a atributos
class Descritor:
    def __init__(self, nome):
        self.nome = nome
        self._dados = {}
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self._dados.get(obj, None)
    
    def __set__(self, obj, valor):
        self._dados[obj] = valor
    
    def __delete__(self, obj):
        del self._dados[obj]

class ClasseComDescritor:
    atributo = Descritor("atributo")

# Property como descritor
class Celsius:
    def __init__(self, temperatura=0):
        self._temperatura = temperatura
    
    @property
    def temperatura(self):
        return self._temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if valor < -273.15:
            raise ValueError("Temperatura abaixo do zero absoluto")
        self._temperatura = valor
    
    @property
    def fahrenheit(self):
        return (self._temperatura * 9/5) + 32

# Slots - Otimização de memória
class Otimizado:
    __slots__ = ['nome', 'idade', '_salario']
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self._salario = 0
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        self._salario = valor

# Comparação de memória
import sys
class Normal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

normal = Normal("João", 25)
otimizado = Otimizado("João", 25)
print(sys.getsizeof(normal))      # Maior (~56 bytes)
print(sys.getsizeof(otimizado))   # Menor (~48 bytes)

# Weak references (evitar ciclos de referência)
import weakref

class Node:
    def __init__(self, valor):
        self.valor = valor
        self._pai = None
        self.filhos = []
    
    @property
    def pai(self):
        if self._pai is None:
            return None
        return self._pai()
    
    @pai.setter
    def pai(self, node):
        if node is None:
            self._pai = None
        else:
            self._pai = weakref.ref(node)
    
    def add_filho(self, filho):
        self.filhos.append(filho)
        filho.pai = self
```

---

## 8. MANIPULAÇÃO DE ARQUIVOS

### 8.1 Pathlib - Tudo que Existe

```python
from pathlib import Path
import shutil

# Criação e navegação
caminho = Path('/home/usuario/documentos')
caminho_abs = Path.cwd() / 'pasta' / 'arquivo.txt'
caminho_home = Path.home()

# Propriedades
p = Path('arquivo.txt')
print(p.exists())          # Existe?
print(p.is_file())         # É arquivo?
print(p.is_dir())          # É diretório?
print(p.is_symlink())      # É link simbólico?
print(p.is_absolute())     # É caminho absoluto?
print(p.name)              # Nome do arquivo
print(p.stem)              # Nome sem extensão
print(p.suffix)            # Extensão
print(p.suffixes)          # Múltiplas extensões ['.tar', '.gz']
print(p.parent)            # Diretório pai
print(p.parents)           # Todos os pais
print(p.anchor)            # Raiz do caminho

# Manipulação
p = Path('novo_arquivo.txt')
p.write_text('Conteúdo do arquivo', encoding='utf-8')
conteudo = p.read_text(encoding='utf-8')
p.write_bytes(b'Conteúdo binário')
conteudo_bytes = p.read_bytes()

# Criar diretórios
pasta = Path('pasta/subpasta')
pasta.mkdir(parents=True, exist_ok=True)

# Listar arquivos
for arquivo in Path('.').iterdir():
    print(arquivo)

for arquivo in Path('.').glob('*.txt'):
    print(arquivo)

for arquivo in Path('.').rglob('*.py'):  # Recursivo
    print(arquivo)

# Copiar, mover, deletar
origem = Path('origem.txt')
destino = Path('destino.txt')
shutil.copy(origem, destino)
shutil.move(origem, destino)
destino.unlink()  # Remove arquivo
pasta.rmdir()     # Remove diretório vazio
shutil.rmtree('pasta')  # Remove diretório com conteúdo

# Estatísticas
stats = p.stat()
print(stats.st_size)        # Tamanho em bytes
print(stats.st_mtime)       # Modificação timestamp
print(stats.st_ctime)       # Criação timestamp

# Permissões
p.chmod(0o755)              # Altera permissões

# Resolver caminho
p_resolvido = p.resolve()   # Caminho absoluto sem links

# Comparar caminhos
p1 = Path('arquivo.txt')
p2 = Path('./arquivo.txt')
print(p1.samefile(p2))      # True

# Temporários
import tempfile
with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
    tmp.write('Dados')
    nome = tmp.name

with tempfile.TemporaryDirectory() as tmpdir:
    arquivo = Path(tmpdir) / 'teste.txt'
    arquivo.write_text('Conteúdo')
```

### 8.2 Arquivos CSV, JSON, YAML, XML

```python
# CSV com csv module (avançado)
import csv
from collections import namedtuple

# Leitura como namedtuple
with open('dados.csv', 'r', encoding='utf-8') as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor)
    Registro = namedtuple('Registro', cabecalho)
    dados = [Registro(*linha) for linha in leitor]

# Escrita com dicionários
with open('saida.csv', 'w', encoding='utf-8', newline='') as f:
    campos = ['nome', 'idade', 'cidade']
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerow({'nome': 'João', 'idade': 25, 'cidade': 'SP'})

# CSV com pandas (para análise)
import pandas as pd
df = pd.read_csv('dados.csv')
df.to_csv('saida.csv', index=False)

# JSON avançado
import json
from datetime import datetime

# Serialização de tipos personalizados
def json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, Path):
        return str(obj)
    raise TypeError(f"Tipo {type(obj)} não serializável")

dados = {
    'nome': 'João',
    'data': datetime.now(),
    'caminho': Path('/home/user')
}

json_str = json.dumps(dados, default=json_serializer, indent=2, ensure_ascii=False)
dados_back = json.loads(json_str)

# JSON lines (cada linha é um JSON)
with open('dados.jsonl', 'w') as f:
    for registro in dados:
        f.write(json.dumps(registro) + '\n')

# YAML (pip install pyyaml)
import yaml
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

with open('config.yaml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

# XML (xml.etree.ElementTree)
import xml.etree.ElementTree as ET

# Criar XML
root = ET.Element('pessoas')
pessoa = ET.SubElement(root, 'pessoa', {'id': '1'})
nome = ET.SubElement(pessoa, 'nome')
nome.text = 'João'
idade = ET.SubElement(pessoa, 'idade')
idade.text = '25'

tree = ET.ElementTree(root)
tree.write('pessoas.xml', encoding='utf-8', xml_declaration=True)

# Ler XML
tree = ET.parse('pessoas.xml')
root = tree.getroot()
for pessoa in root.findall('pessoa'):
    nome = pessoa.find('nome').text
    idade = pessoa.find('idade').text
    print(f"{nome}: {idade}")

# ConfigParser (arquivos .ini)
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'debug': 'False', 'timeout': '30'}
config['database'] = {'host': 'localhost', 'port': '5432'}

with open('config.ini', 'w') as f:
    config.write(f)

config.read('config.ini')
print(config['database']['host'])
print(config.getint('database', 'port'))
```

---

## 9. TRATAMENTO DE EXCEÇÕES

### 9.1 Estruturas Avançadas

```python
# Hierarquia de exceções personalizadas
class AppError(Exception):
    """Base para todas as exceções da aplicação"""
    def __init__(self, mensagem, codigo=None):
        super().__init__(mensagem)
        self.codigo = codigo

class DatabaseError(AppError):
    """Erros de banco de dados"""
    pass

class ValidationError(AppError):
    """Erros de validação"""
    pass

class ConfigError(AppError):
    """Erros de configuração"""
    pass

# Try-except-else-finally com contexto
def processar_arquivo(nome_arquivo):
    arquivo = None
    try:
        arquivo = open(nome_arquivo, 'r')
        conteudo = arquivo.read()
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado")
        return None
    except PermissionError:
        print(f"Sem permissão para ler {nome_arquivo}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None
    else:
        print("Arquivo lido com sucesso")
        return conteudo
    finally:
        if arquivo:
            arquivo.close()
            print("Arquivo fechado")

# Encadeamento de exceções
def processar():
    try:
        try:
            raise ValueError("Erro original")
        except ValueError as e:
            raise RuntimeError("Erro processado") from e
    except RuntimeError as e:
        print(f"Causa original: {e.__cause__}")

# Suprimir contexto
def processar_sem_contexto():
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Divisão por zero") from None

# Exception groups (Python 3.11+)
try:
    raise ExceptionGroup("Múltiplos erros", [
        ValueError("Erro 1"),
        TypeError("Erro 2"),
        RuntimeError("Erro 3")
    ])
except* ValueError as e:
    print(f"ValorError: {e.exceptions}")
except* TypeError as e:
    print(f"TypeError: {e.exceptions}")

# Context managers para exceções
from contextlib import contextmanager

@contextmanager
def manipulador_excecoes(tipo, callback):
    try:
        yield
    except tipo as e:
        callback(e)

with manipulador_excecoes(ValueError, lambda e: print(f"Tratado: {e}")):
    raise ValueError("Algo errado")

# Logging de exceções
import logging
import traceback

logging.basicConfig(level=logging.ERROR)

def log_excecao(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exceção em {func.__name__}: {e}")
            logging.error(traceback.format_exc())
            raise
    return wrapper

@log_excecao
def funcao_arriscada():
    raise ValueError("Algo errado")

# Retry com backoff
import time
from functools import wraps

def retry(max_tentativas=3, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tentativas = 0
            while tentativas < max_tentativas:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tentativas += 1
                    if tentativas == max_tentativas:
                        raise
                    time.sleep(delay * (backoff ** (tentativas - 1)))
        return wrapper
    return decorator

@retry(max_tentativas=5, delay=1)
def conectar_api():
    import requests
    response = requests.get('https://api.exemplo.com')
    response.raise_for_status()
    return response.json()
```

---

## 10. MÓDULOS E PACOTES

### 10.1 Importação Avançada

```python
# Importação dinâmica
import importlib

modulo = importlib.import_module('math')
print(modulo.sqrt(16))  # 4.0

# Importar de caminho específico
import sys
import os

def importar_de_caminho(caminho):
    nome_modulo = os.path.splitext(os.path.basename(caminho))[0]
    spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

# Recarregar módulo
import math
math = importlib.reload(math)

# Namespace packages (Python 3.3+)
# Diretórios sem __init__.py podem ser namespaces packages

# __main__ e execução
if __name__ == "__main__":
    import sys
    print(f"Executando {sys.argv[0]} com args {sys.argv[1:]}")

# Import hooks
import sys
class MeuImporter:
    def find_spec(self, nome, caminho, target=None):
        # Lógica para encontrar módulo
        pass
    
    def exec_module(self, modulo):
        # Lógica para executar módulo
        pass

# sys.meta_path.append(MeuImporter())
```

### 10.2 Estrutura de Pacote Completa

```python
"""
meu_pacote/
├── __init__.py
├── __main__.py
├── __version__.py
├── core/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── validators.py
├── data/
│   └── dados.json
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
├── scripts/
│   └── setup.py
├── requirements.txt
├── setup.py
├── pyproject.toml
├── README.md
└── LICENSE
"""

# __init__.py - Ponto de entrada do pacote
"""
\"\"\"Meu Pacote - Descrição do pacote\"\"\"

__version__ = "1.0.0"
__author__ = "Seu Nome"

from .core import *
from .utils import *

__all__ = ['core', 'utils']
"""

# __main__.py - Executável do pacote
"""
import sys
from meu_pacote.core import main

if __name__ == "__main__":
    sys.exit(main())
"""

# __version__.py - Versão centralizada
"""
__version__ = "1.0.0"
"""

# setup.py - Configuração de distribuição
"""
from setuptools import setup, find_packages

setup(
    name="meu_pacote",
    version="1.0.0",
    description="Descrição do pacote",
    author="Seu Nome",
    author_email="email@exemplo.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.25.0",
        "numpy>=1.19.0",
    ],
    extras_require={
        "dev": ["pytest", "black", "mypy"],
        "test": ["pytest", "pytest-cov"],
    },
    entry_points={
        "console_scripts": [
            "meu-comando=meu_pacote.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
"""

# pyproject.toml - Configuração moderna
"""
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "meu_pacote"
version = "1.0.0"
description = "Descrição do pacote"
authors = [{name = "Seu Nome", email = "email@exemplo.com"}]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.7"
dependencies = [
    "requests>=2.25.0",
    "numpy>=1.19.0",
]

[project.optional-dependencies]
dev = ["pytest", "black", "mypy"]
test = ["pytest", "pytest-cov"]

[project.scripts]
meu-comando = "meu_pacote.__main__:main"

[tool.black]
line-length = 88
target-version = ['py37', 'py38', 'py39']

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.7"
warn_return_any = true
warn_unused_configs = true
"""

# Comandos para empacotamento
"""
# Instalar em modo desenvolvimento
pip install -e .

# Criar distribuição
python -m build

# Publicar no PyPI
twine upload dist/*

# Instalar dependências
pip install -r requirements.txt
pip install .[dev]
"""
```

---

## 11. BIBLIOTECA PADRÃO COMPLETA

### 11.1 Módulos Essenciais - Detalhados

```python
# os - Sistema operacional (completo)
import os

# Informações do sistema
print(os.name)                      # 'posix', 'nt'
print(os.getcwd())                  # Diretório atual
print(os.listdir('.'))              # Lista arquivos
print(os.environ.get('PATH'))       # Variáveis de ambiente

# Processos
os.system('ls -l')                  # Executa comando
pid = os.fork()                     # Fork (Unix)
os.execv('/bin/ls', ['ls', '-l'])   # Substitui processo
os.kill(pid, 9)                     # Mata processo

# sys - Sistema e argumentos
import sys

print(sys.argv)                     # Argumentos linha comando
print(sys.version)                  # Versão Python
print(sys.platform)                 # Plataforma
print(sys.path)                     # Caminhos de busca
print(sys.modules)                  # Módulos carregados
sys.exit(0)                         # Sai do programa

# math - Matemática completa
import math

print(math.pi, math.e, math.tau)    # Constantes
print(math.inf, math.nan)           # Infinito e NaN
print(math.sqrt(16))                # Raiz quadrada
print(math.pow(2, 10))              # Potência
print(math.exp(1))                  # e^1
print(math.log(100, 10))            # Log base 10
print(math.log10(100))              # Log base 10
print(math.log2(8))                 # Log base 2
print(math.sin(math.radians(30)))   # Seno
print(math.degrees(math.pi))        # Radianos para graus
print(math.factorial(5))            # 120
print(math.comb(5, 2))              # Combinações 10
print(math.perm(5, 2))              # Permutações 20
print(math.gcd(12, 18))             # MDC 6
print(math.lcm(12, 18))             # MMC 36
print(math.isclose(0.1 + 0.2, 0.3)) # Comparação aproximada

# random - Aleatoriedade completa
import random

random.seed(42)                     # Semente fixa
random.random()                     # Float [0,1)
random.uniform(1, 10)               # Float [1,10)
random.randint(1, 10)               # Inteiro [1,10]
random.randrange(0, 100, 5)         # Passo
random.choice(['a', 'b', 'c'])      # Escolhe um
random.choices(['a', 'b'], k=5)     # Com repetição
random.sample(range(100), 5)        # Sem repetição
random.shuffle(lista)               # Embaralha in-place
random.triangular(0, 10, 5)         # Distribuição triangular
random.gauss(0, 1)                  # Distribuição normal

# secrets - Aleatoriedade segura
import secrets

token = secrets.token_hex(32)       # Token hex
token_url = secrets.token_urlsafe(32)  # Token URL-safe
token_bytes = secrets.token_bytes(32)  # Token bytes
senha = secrets.choice('abcdefghijklmnopqrstuvwxyz')  # Escolha segura

# itertools - Iteradores (completo)
import itertools

# Infinitos
itertools.count(10, 2)              # 10,12,14,...
itertools.cycle([1,2,3])            # 1,2,3,1,2,3,...
itertools.repeat('a', 5)            # a,a,a,a,a

# Combinatórios
itertools.product([1,2], ['a','b']) # Produto cartesiano
itertools.permutations([1,2,3], 2)  # Permutações
itertools.combinations([1,2,3], 2)  # Combinações
itertools.combinations_with_replacement([1,2], 2)  # Combinações com repetição

# Agrupamento e filtro
itertools.groupby([1,1,2,2,3])      # Agrupa consecutivos
itertools.filterfalse(lambda x: x>2, [1,2,3,4])  # Filtra False
itertools.dropwhile(lambda x: x<3, [1,2,3,4])    # Descarta enquanto
itertools.takewhile(lambda x: x<3, [1,2,3,4])    # Pega enquanto
itertools.compress([1,2,3], [True,False,True])   # Filtra por seletor

# Combinar
itertools.chain([1,2], [3,4])       # Encadeia iteráveis
itertools.zip_longest([1,2], [3,4,5], fillvalue=0)  # Zip com preenchimento
itertools.islice(range(10), 2, 8, 2)  # Fatiamento

# functools - Funções de alta ordem
from functools import partial, reduce, wraps, lru_cache, singledispatch

# partial - Fixa argumentos
def potencia(base, exp):
    return base ** exp

quadrado = partial(potencia, exp=2)

# reduce - Acumula
soma = reduce(lambda x, y: x + y, [1,2,3,4])  # 10

# wraps - Preserva metadados
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# lru_cache - Cache
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# singledispatch - Sobrecarga
@singledispatch
def processar(arg):
    return f"Default: {arg}"

@processar.register(int)
def _(arg):
    return f"Inteiro: {arg}"

@processar.register(list)
def _(arg):
    return f"Lista com {len(arg)} itens"

# collections - Estruturas especializadas
from collections import deque, Counter, OrderedDict, defaultdict, ChainMap

# Counter - Contador
c = Counter('abracadabra')
c.most_common(2)                     # [('a',5), ('b',2)]
c.elements()                         # Iterador com elementos repetidos
c.total()                            # Soma total (Python 3.10+)

# defaultdict - Valor padrão
dd = defaultdict(list)
dd['chave'].append(1)

# ChainMap - Múltiplos dicionários
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
chain = ChainMap(d1, d2)
chain.maps                            # Lista de dicionários
chain.new_child({'d': 5})             # Adiciona dicionário
chain.parents                         # Remove primeiro

# heapq - Heap (priority queue)
import heapq

heap = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(heap)                   # Transforma em heap
heapq.heappush(heap, 0)               # Insere
heapq.heappop(heap)                   # Remove menor
heapq.heapreplace(heap, 10)           # Pop + Push
heapq.nlargest(3, heap)               # 3 maiores
heapq.nsmallest(3, heap)              # 3 menores

# bisect - Busca binária
import bisect

lista = [1, 3, 5, 7, 9]
pos = bisect.bisect_left(lista, 5)    # 2 (índice onde inserir)
pos = bisect.bisect_right(lista, 5)   # 3
bisect.insort(lista, 6)               # Insere mantendo ordem

# weakref - Referências fracas
import weakref

class Objeto:
    pass

obj = Objeto()
ref = weakref.ref(obj)
print(ref())                          # Objeto
del obj
print(ref())                          # None

# weakref.WeakKeyDictionary, WeakValueDictionary
# Útil para caches que não impedem garbage collection

# enum - Enumerações
from enum import Enum, auto, IntEnum, Flag

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class AutoColor(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

class Permission(Flag):
    READ = 1
    WRITE = 2
    EXECUTE = 4

perm = Permission.READ | Permission.WRITE
print(Permission.READ in perm)        # True
```

---

## 12. DATA E HORA AVANÇADO

### 12.1 datetime - Tudo que Existe

```python
from datetime import datetime, date, time, timedelta, timezone
import pytz
from dateutil import parser, relativedelta

# Criar objetos
agora = datetime.now()
agora_utc = datetime.now(timezone.utc)
hoje = date.today()
agora_time = time(14, 30, 45, 123456)

# Timestamps
timestamp = agora.timestamp()
data_ts = datetime.fromtimestamp(timestamp)
data_utc_ts = datetime.utcfromtimestamp(timestamp)

# Componentes
print(agora.year, agora.month, agora.day)
print(agora.hour, agora.minute, agora.second, agora.microsecond)
print(agora.weekday())          # 0=segunda, 6=domingo
print(agora.isoweekday())       # 1=segunda, 7=domingo
print(agora.isocalendar())      # (ano, semana, dia_semana)

# timedelta - Diferenças
delta = timedelta(days=5, hours=3, minutes=30, seconds=15)
amanha = hoje + timedelta(days=1)
semana_passada = hoje - timedelta(weeks=1)
ontem = hoje - timedelta(days=1)

# Formatação - todas as diretivas
formatos = {
    '%Y': 'Ano com 4 dígitos',
    '%y': 'Ano com 2 dígitos',
    '%m': 'Mês (01-12)',
    '%d': 'Dia (01-31)',
    '%H': 'Hora (00-23)',
    '%I': 'Hora (01-12)',
    '%M': 'Minuto (00-59)',
    '%S': 'Segundo (00-59)',
    '%f': 'Microssegundo (000000-999999)',
    '%p': 'AM/PM',
    '%a': 'Dia da semana abreviado',
    '%A': 'Dia da semana completo',
    '%b': 'Mês abreviado',
    '%B': 'Mês completo',
    '%w': 'Dia da semana (0-6, domingo=0)',
    '%j': 'Dia do ano (001-366)',
    '%W': 'Número da semana (segunda como primeiro dia)',
    '%U': 'Número da semana (domingo como primeiro dia)',
    '%z': 'Timezone offset',
    '%Z': 'Nome do timezone',
    '%x': 'Representação de data local',
    '%X': 'Representação de hora local',
}

# Parsing com dateutil (flexível)
data_parse = parser.parse("15 de janeiro de 2024 às 14:30")
data_parse = parser.parse("2024-01-15T14:30:00")
data_parse = parser.parse("Jan 15, 2024 2:30 PM")

# relativedelta - diferenças complexas
from dateutil.relativedelta import relativedelta

proximo_mes = hoje + relativedelta(months=+1)
proximo_ano = hoje + relativedelta(years=+1)
proxima_segunda = hoje + relativedelta(weekday=0)  # 0=segunda
ultimo_dia_mes = hoje + relativedelta(day=31)

# Timezones com pytz
tz_sp = pytz.timezone('America/Sao_Paulo')
tz_ny = pytz.timezone('America/New_York')
tz_london = pytz.timezone('Europe/London')

# Converter timezone
data_utc = datetime.now(timezone.utc)
data_sp = data_utc.astimezone(tz_sp)
data_ny = data_utc.astimezone(tz_ny)

# Localizar data ingênua
data_ingênua = datetime(2024, 1, 15, 14, 30)
data_localizada = tz_sp.localize(data_ingênua)

# Listar timezones
import pytz
print(pytz.all_timezones[:10])  # Lista todos

# ISO 8601
iso_string = agora.isoformat()
data_iso = datetime.fromisoformat(iso_string)

# Timezone-aware operations
agora_sp = datetime.now(tz_sp)
agora_ny = agora_sp.astimezone(tz_ny)
diferenca = agora_sp - agora_ny
print(f"Diferença: {diferenca.total_seconds() / 3600} horas")

# Dormir até um horário específico
import time
from datetime import datetime

def dormir_ate(hora_alvo):
    agora = datetime.now()
    alvo = agora.replace(hour=hora_alvo, minute=0, second=0, microsecond=0)
    if alvo <= agora:
        alvo += timedelta(days=1)
    time.sleep((alvo - agora).total_seconds())

# Medir tempo de execução
start_time = time.perf_counter()
# Código
end_time = time.perf_counter()
print(f"Tempo: {end_time - start_time:.4f}s")

# timeit para micro-benchmarks
import timeit
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Média: {tempo/10000:.6f}s")
```

---

## 13. EXPRESSÕES REGULARES AVANÇADO

### 13.1 re Module - Tudo que Existe

```python
import re

# Padrões comuns (compilados)
padroes = {
    'email': re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
    'url': re.compile(r'^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*/?$'),
    'cpf': re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'),
    'cnpj': re.compile(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'),
    'telefone': re.compile(r'^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$'),
    'cep': re.compile(r'^\d{5}-?\d{3}$'),
    'ipv4': re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'),
    'ipv6': re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'),
    'placa_carro': re.compile(r'^[A-Z]{3}-\d{4}$'),
    'data_br': re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'),
    'hora': re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?$'),
    'senha_forte': re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'),
    'slug': re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$'),
    'hex_color': re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'),
    'uuid': re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'),
}

# Flags detalhadas
re.IGNORECASE = re.I    # Ignora maiúsculas/minúsculas
re.MULTILINE = re.M     # ^ e $ funcionam por linha
re.DOTALL = re.S        # . inclui quebra de linha
re.VERBOSE = re.X       # Permite comentários e espaços
re.ASCII = re.A         # \w, \b, \s, \d usam apenas ASCII
re.LOCALE = re.L        # Comportamento dependente de locale (não recomendado)
re.UNICODE = re.U       # Padrão em Python 3

# Compilação com VERBOSE
padrao_complexo = re.compile(r"""
    ^               # Início da string
    (?P<usuario>    # Nome do grupo: usuario
        [a-zA-Z0-9._%+-]+
    )
    @               # Literal @
    (?P<dominio>    # Nome do grupo: dominio
        [a-zA-Z0-9.-]+
        \.
        [a-zA-Z]{2,}
    )
    $               # Fim da string
""", re.VERBOSE | re.IGNORECASE)

# Match com grupos nomeados
match = padrao_complexo.match("usuario@exemplo.com")
if match:
    print(match.group('usuario'))     # usuario
    print(match.group('dominio'))     # exemplo.com
    print(match.groupdict())          # {'usuario': 'usuario', 'dominio': 'exemplo.com'}
    print(match.groups())             # ('usuario', 'exemplo.com')

# Lookahead e lookbehind (positive e negative)
texto = "preço: 100.00, desconto: 20.00"

# Positive lookahead - números seguidos de ponto
numeros_com_ponto = re.findall(r'\d+(?=\.)', texto)  # ['100', '20']

# Negative lookahead - números não seguidos de ponto
numeros_sem_ponto = re.findall(r'\d+(?!\.)', texto)  # ['00', '00']

# Positive lookbehind - números precedidos de "preço: "
precos = re.findall(r'(?<=preço: )\d+\.\d+', texto)  # ['100.00']

# Negative lookbehind - números não precedidos de "desconto: "
outros = re.findall(r'(?<!desconto: )\d+\.\d+', texto)  # ['100.00']

# Substituição com callback
def substituir_emoji(match):
    emojis = {
        ':smile:': '😊',
        ':heart:': '❤️',
        ':thumbsup:': '👍'
    }
    return emojis.get(match.group(0), match.group(0))

texto = "Olá :smile: Como vai? :heart:"
resultado = re.sub(r':[a-z]+:', substituir_emoji, texto)
print(resultado)  # "Olá 😊 Como vai? ❤️"

# Split com captura
texto = "a1b2c3d4"
partes = re.split(r'(\d+)', texto)  # ['a', '1', 'b', '2', 'c', '3', 'd', '4', '']

# Escanear string
padrao = re.compile(r'\d+')
pos = 0
while True:
    match = padrao.search(texto, pos)
    if not match:
        break
    print(f"Encontrado {match.group()} na posição {match.start()}")
    pos = match.end()

# Finditer - iterador de matches
for match in re.finditer(r'\d+', texto):
    print(f"{match.group()} em {match.span()}")

# Substituição com contagem
resultado = re.sub(r'\d+', 'NUM', texto, count=2)  # Substitui apenas 2

# Escaping de string
texto = "O preço é $100.00"
escapado = re.escape(texto)  # "O preço é \$100\.00"

# Remover tags HTML
html = "<p>Texto <b>importante</b></p>"
sem_tags = re.sub(r'<[^>]+>', '', html)  # "Texto importante"

# Validar e extrair
def validar_email(email):
    match = padroes['email'].match(email)
    if match:
        return match.group(0)
    return None

# Pattern matching recursivo (raro)
def parse_parenteses(texto):
    padrao = re.compile(r'\(([^()]*(?:\([^()]*\)[^()]*)*)\)')
    return padrao.findall(texto)

print(parse_parenteses("a(b(c)d)e(f)g"))  # ['b(c)d', 'f']
```

---

## 14. CONCORRÊNCIA E PARALELISMO

### 14.1 Threading - Avançado

```python
import threading
import queue
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Thread com classe
class WorkerThread(threading.Thread):
    def __init__(self, nome, fila, resultados):
        super().__init__()
        self.nome = nome
        self.fila = fila
        self.resultados = resultados
        self.daemon = True  # Thread daemon não impede o programa de terminar
    
    def run(self):
        while True:
            try:
                item = self.fila.get(timeout=1)
                resultado = self.processar(item)
                self.resultados.append(resultado)
                self.fila.task_done()
            except queue.Empty:
                break
    
    def processar(self, item):
        time.sleep(0.1)  # Simula trabalho
        return f"{self.nome} processou {item}"

# Uso
fila = queue.Queue()
for i in range(20):
    fila.put(i)

resultados = []
threads = []
for i in range(4):
    t = WorkerThread(f"Worker-{i}", fila, resultados)
    t.start()
    threads.append(t)

fila.join()  # Aguarda todas as tarefas
for t in threads:
    t.join()  # Aguarda threads terminarem

print(resultados)

# ThreadPoolExecutor - gerenciamento de pool
def tarefa(x):
    time.sleep(x)
    return x ** 2

with ThreadPoolExecutor(max_workers=4) as executor:
    # Submeter múltiplas tarefas
    futures = [executor.submit(tarefa, i) for i in range(5)]
    
    # Processar conforme completam
    for future in as_completed(futures):
        resultado = future.result()
        print(f"Completou: {resultado}")
    
    # Map - mantém ordem
    resultados = executor.map(tarefa, range(5))
    print(list(resultados))

# Sincronização avançada
# Lock - exclusão mútua
lock = threading.Lock()
contador = 0

def incrementar():
    global contador
    with lock:
        local = contador
        time.sleep(0.001)
        contador = local + 1

# RLock - reentrante (mesma thread pode adquirir múltiplas vezes)
rlock = threading.RLock()
def funcao_recursiva(n):
    with rlock:
        if n > 0:
            funcao_recursiva(n-1)

# Semaphore - controle de recursos
semaphore = threading.Semaphore(3)  # Permite 3 threads simultâneas
def recurso_limitado():
    with semaphore:
        time.sleep(1)

# Event - comunicação entre threads
event = threading.Event()
def esperar_evento():
    print("Aguardando")
    event.wait()
    print("Evento recebido")

def disparar_evento():
    time.sleep(2)
    event.set()

# Condition - espera condicional
condition = threading.Condition()
itens = []

def produtor():
    with condition:
        itens.append("item")
        condition.notify()  # Notifica um consumidor

def consumidor():
    with condition:
        while not itens:
            condition.wait()  # Espera notificação
        item = itens.pop()
        return item

# Barrier - sincronização de pontos
barrier = threading.Barrier(3)
def etapa():
    print(f"{threading.current_thread().name} chegou")
    barrier.wait()
    print("Todos chegaram!")

# Queue para comunicação
from queue import Queue, PriorityQueue, LifoQueue

# Queue simples (FIFO)
q = Queue(maxsize=10)
q.put(1)
q.put(2)
print(q.get())  # 1
print(q.qsize())  # 1
print(q.empty())  # False
print(q.full())   # False

# PriorityQueue - itens com prioridade
pq = PriorityQueue()
pq.put((2, "média"))
pq.put((1, "alta"))
pq.put((3, "baixa"))
print(pq.get()[1])  # "alta"

# LifoQueue (pilha)
lq = LifoQueue()
lq.put(1)
lq.put(2)
print(lq.get())  # 2
```

### 14.2 Multiprocessing - Avançado

```python
import multiprocessing
from multiprocessing import Pool, Process, Queue, Manager, Lock
import time

# Processo simples
def trabalhador(nome, segundos, resultado):
    time.sleep(segundos)
    resultado.append(f"{nome} completou")

if __name__ == "__main__":
    manager = Manager()
    resultados = manager.list()
    
    processos = []
    for i in range(4):
        p = Process(target=trabalhador, args=(f"P{i}", i+1, resultados))
        p.start()
        processos.append(p)
    
    for p in processos:
        p.join()
    
    print(resultados)

# Pool de processos
def cpu_bound(x):
    return sum(i**2 for i in range(x))

if __name__ == "__main__":
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map
        resultados = pool.map(cpu_bound, range(10, 20))
        print(resultados)
        
        # Map assíncrono
        resultados_async = pool.map_async(cpu_bound, range(10, 20))
        print(resultados_async.get())
        
        # Starmap (múltiplos argumentos)
        def potencia(a, b):
            return a ** b
        
        resultados = pool.starmap(potencia, [(2, 3), (3, 2), (4, 2)])
        print(resultados)  # [8, 9, 16]
        
        # Apply assíncrono
        futuro = pool.apply_async(cpu_bound, (1000000,))
        print(futuro.get())

# Queue entre processos
def produtor(queue):
    for i in range(10):
        queue.put(i)
        time.sleep(0.1)
    queue.put(None)  # Sentinela

def consumidor(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Processado: {item}")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=produtor, args=(q,))
    p2 = Process(target=consumidor, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# Memória compartilhada
from multiprocessing import shared_memory
import numpy as np

# Criar memória compartilhada
shm = shared_memory.SharedMemory(create=True, size=1000)
arr = np.ndarray((250,), dtype=np.int64, buffer=shm.buf)
arr[:] = np.arange(250)

# Em outro processo, conectar
shm_existente = shared_memory.SharedMemory(name=shm.name)
arr_existente = np.ndarray((250,), dtype=np.int64, buffer=shm_existente.buf)
print(arr_existente[:10])

# Limpar
shm.close()
shm.unlink()
```

### 14.3 Asyncio - Tudo que Existe

```python
import asyncio
import aiohttp
import aiofiles
import time
from asyncio import create_task, gather, wait, wait_for

# Função assíncrona básica
async def tarefa(nome, segundos):
    print(f"{nome}: iniciando")
    await asyncio.sleep(segundos)
    print(f"{nome}: finalizando")
    return f"Resultado {nome}"

# Executar
async def main():
    # Sequencial
    resultado = await tarefa("A", 2)
    
    # Concorrente - gather
    resultados = await gather(
        tarefa("A", 2),
        tarefa("B", 1),
        tarefa("C", 3)
    )
    print(resultados)
    
    # Concorrente - wait
    tarefas = [tarefa("A", 2), tarefa("B", 1), tarefa("C", 3)]
    done, pending = await wait(tarefas, timeout=2.5)
    for task in done:
        print(task.result())
    for task in pending:
        task.cancel()
    
    # Timeout
    try:
        resultado = await wait_for(tarefa("D", 5), timeout=2)
    except asyncio.TimeoutError:
        print("Timeout!")
    
    # Tasks
    task = create_task(tarefa("E", 1))
    resultado = await task

# asyncio.run(main())

# HTTP requests assíncronos
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiplas():
    async with aiohttp.ClientSession() as session:
        urls = ['http://example.com' for _ in range(10)]
        tasks = [fetch_url(session, url) for url in urls]
        resultados = await gather(*tasks)
        return resultados

# Arquivos assíncronos
async def escrever_arquivo(nome, conteudo):
    async with aiofiles.open(nome, 'w') as f:
        await f.write(conteudo)

async def ler_arquivo(nome):
    async with aiofiles.open(nome, 'r') as f:
        return await f.read()

# Streams (sockets)
async def echo_server():
    server = await asyncio.start_server(
        echo_handler, '127.0.0.1', 8888
    )
    async with server:
        await server.serve_forever()

async def echo_handler(reader, writer):
    while True:
        data = await reader.readline()
        if not data:
            break
        writer.write(data)
        await writer.drain()
    writer.close()
    await writer.wait_closed()

# Queues assíncronas
async def produtor(queue):
    for i in range(10):
        await queue.put(i)
        await asyncio.sleep(0.1)
    await queue.put(None)

async def consumidor(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Processado: {item}")

# Sincronização assíncrona
lock = asyncio.Lock()

async def recurso_compartilhado():
    async with lock:
        # Código crítico
        await asyncio.sleep(1)

# Semáforo assíncrono
semaphore = asyncio.Semaphore(3)

async def recurso_limitado():
    async with semaphore:
        await asyncio.sleep(1)

# Evento assíncrono
event = asyncio.Event()

async def esperar_evento():
    await event.wait()
    print("Evento recebido")

async def disparar_evento():
    await asyncio.sleep(2)
    event.set()

# Condition assíncrona
condition = asyncio.Condition()
itens = []

async def produtor_asyncio():
    async with condition:
        itens.append("item")
        condition.notify()

async def consumidor_asyncio():
    async with condition:
        while not itens:
            await condition.wait()
        return itens.pop()

# Task groups (Python 3.11+)
async def grupo_tarefas():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(tarefa("A", 1))
        task2 = tg.create_task(tarefa("B", 2))
        task3 = tg.create_task(tarefa("C", 3))
    # Todas as tarefas completaram aqui
    print(task1.result(), task2.result(), task3.result())

# Shielding - proteger tarefa de cancelamento
async def operacao_critica():
    await asyncio.shield(asyncio.sleep(10))

# Exceptions em gather
async def tarefa_com_erro():
    raise ValueError("Erro")

async def gather_com_tratamento():
    resultados = await gather(
        tarefa("A", 1),
        tarefa_com_erro(),
        tarefa("B", 1),
        return_exceptions=True
    )
    print(resultados)  # ['Resultado A', ValueError(...), 'Resultado B']

# asyncio.Queue com prioridade
class PriorityQueue(asyncio.Queue):
    async def put(self, item):
        await super().put(item)
    
    async def get(self):
        # Implementação com prioridade
        pass
```

---

## 15. PROGRAMAÇÃO FUNCIONAL

### 15.1 Funções de Alta Ordem - Detalhadas

```python
# Map, Filter, Reduce - avançado
from functools import reduce
import operator

# Map com múltiplos argumentos
numeros1 = [1, 2, 3, 4]
numeros2 = [5, 6, 7, 8]
somas = list(map(operator.add, numeros1, numeros2))  # [6, 8, 10, 12]

# Filter com lambda
pares = list(filter(lambda x: x % 2 == 0, range(20)))

# Reduce com operadores
soma = reduce(operator.add, range(100))  # 4950
produto = reduce(operator.mul, [1, 2, 3, 4])  # 24
maximo = reduce(lambda a, b: a if a > b else b, [3, 1, 4, 1, 5])  # 5

# Any, All com compreensão
numeros = [1, 2, 3, 4, 5]
qualquer_par = any(x % 2 == 0 for x in numeros)  # True
todos_pares = all(x % 2 == 0 for x in numeros)  # False

# Zip com map
nomes = ['Ana', 'João', 'Maria']
idades = [25, 30, 28]
pessoas = list(zip(nomes, idades))
nomes_novos, idades_novas = zip(*pessoas)

# Enumerate com start personalizado
for i, valor in enumerate(['a', 'b', 'c'], start=10):
    print(f"{i}: {valor}")  # 10: a, 11: b, 12: c

# Sorted com múltiplas chaves
pessoas = [
    {'nome': 'Ana', 'idade': 25, 'cidade': 'SP'},
    {'nome': 'João', 'idade': 30, 'cidade': 'RJ'},
    {'nome': 'Maria', 'idade': 28, 'cidade': 'SP'},
]

# Ordenar por idade, depois por nome
sorted(pessoas, key=lambda p: (p['idade'], p['nome']))

# Ordenar com operator.itemgetter
from operator import itemgetter
sorted(pessoas, key=itemgetter('cidade', 'idade'))

# Composição de funções
def compor(*funcoes):
    def aplicador(x):
        for f in funcoes:
            x = f(x)
        return x
    return aplicador

def dobro(x): return x * 2
def mais_um(x): return x + 1
def quadrado(x): return x ** 2

func = compor(dobro, mais_um, quadrado)
print(func(3))  # ((3*2)+1)^2 = 49

# Currying (aplicação parcial)
from functools import partial

def soma(a, b, c):
    return a + b + c

soma_10 = partial(soma, 10)
soma_10_20 = partial(soma_10, 20)
print(soma_10_20(30))  # 60

# Funções como objetos
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

ola = criar_saudacao("Olá")
oi = criar_saudacao("Oi")
print(ola("João"))  # Olá, João!
print(oi("Maria"))  # Oi, Maria!

# Pipeline funcional
def pipeline(data, *funcs):
    for func in funcs:
        data = func(data)
    return data

resultado = pipeline(
    [1, 2, 3, 4, 5],
    lambda x: [y * 2 for y in x],
    lambda x: [y for y in x if y > 5],
    lambda x: sum(x)
)
print(resultado)  # 6 + 8 + 10 = 24

# Funções como argumentos com typing
from typing import Callable

def aplicar(f: Callable[[int], int], x: int) -> int:
    return f(x)

print(aplicar(lambda x: x**2, 5))  # 25

# Módulo operator - operadores como funções
import operator

print(operator.add(1, 2))          # 3
print(operator.mul(3, 4))          # 12
print(operator.truth(1))           # True
print(operator.is_(True, 1))       # True
print(operator.contains([1,2,3], 2))  # True

# operator.attrgetter
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

pessoas = [Pessoa("Ana"), Pessoa("João"), Pessoa("Maria")]
nomes = list(map(operator.attrgetter('nome'), pessoas))  # ['Ana', 'João', 'Maria']

# operator.methodcaller
upper = operator.methodcaller('upper')
print(upper("hello"))  # HELLO
```

---

## 16. TYPE HINTS E TIPAGEM

### 16.1 Type Hints - Tudo que Existe

```python
from typing import (
    List, Dict, Tuple, Set, Optional, Union, Any, 
    Callable, TypeVar, Generic, Protocol, Final,
    Literal, TypedDict, cast, overload, Type,
    NewType, NoReturn, ClassVar, AnyStr, NamedTuple,
    Awaitable, AsyncIterable, AsyncIterator, Coroutine,
    Union as UnionType
)
from typing_extensions import Self, TypeAlias
import sys

# Tipos básicos
nome: str = "João"
idade: int = 25
altura: float = 1.75
ativo: bool = True
dados: Any = "qualquer coisa"
sem_retorno: None = None
erro: NoReturn  # Função que nunca retorna (ex: sys.exit)

# Coleções (Python 3.9+ permite sintaxe nativa)
# Antigo: lista: List[str] = ["a", "b"]
lista: list[str] = ["a", "b"]
tupla: tuple[int, str] = (1, "um")
dicionario: dict[str, int] = {"um": 1}
conjunto: set[float] = {1.0, 2.0}
frozenset: frozenset[int] = frozenset([1, 2])

# Opcionais e Unions
opcional: Optional[int] = None  # = int | None
opcional2: int | None = None    # Python 3.10+
union: int | str = "pode ser int ou str"
union2: Union[int, str] = 10

# Funções
def processar(dados: list[str], opcional: int | None = None) -> dict[str, float]:
    return {"media": 0.0}

def callback(func: Callable[[int, int], int]) -> int:
    return func(5, 3)

def args_kwargs(*args: int, **kwargs: str) -> None:
    pass

def nunca_retorna() -> NoReturn:
    raise RuntimeError("Sempre erro")

# TypeVar e Generics
T = TypeVar('T')
U = TypeVar('U', bound=str)  # Restrito a str
V = TypeVar('V', int, float)  # Somente int ou float

class Pilha(Generic[T]):
    def __init__(self) -> None:
        self._itens: list[T] = []
    
    def push(self, item: T) -> None:
        self._itens.append(item)
    
    def pop(self) -> T:
        return self._itens.pop()

def primeira(seq: list[T]) -> T:
    return seq[0]

# TypeAlias (Python 3.10+)
type Vector = list[float]  # Python 3.12+
# Antes: Vector: TypeAlias = list[float]

# NewType - tipos distintos
UserId = NewType('UserId', int)
def get_user(user_id: UserId) -> dict:
    return {"id": user_id}

user = UserId(123)
get_user(user)

# Protocol (duck typing estático)
class Nomeavel(Protocol):
    nome: str
    def saudar(self) -> str: ...

class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    
    def saudar(self) -> str:
        return f"Olá, {self.nome}"

def cumprimentar(obj: Nomeavel) -> str:
    return obj.saudar()

# Literal - valores específicos
from typing import Literal

def set_modo(modo: Literal['read', 'write', 'append']) -> None:
    pass

set_modo('read')   # OK
# set_modo('delete') # Erro

# TypedDict - dicionários tipados
class PessoaDict(TypedDict):
    nome: str
    idade: int
    email: NotRequired[str]  # Python 3.11+

pessoa: PessoaDict = {"nome": "João", "idade": 25}

# Final - constante
MAX_SIZE: Final = 100
# MAX_SIZE = 200  # Erro

# ClassVar - variável de classe
class Config:
    DEBUG: ClassVar[bool] = True
    VERSION: ClassVar[str] = "1.0"

# Self (Python 3.11+)
class Node:
    def set_next(self, node: Self) -> Self:
        self.next = node
        return self

# Overload - múltiplas assinaturas
@overload
def processar(valor: int) -> int: ...
@overload
def processar(valor: str) -> str: ...
@overload
def processar(valor: list[int]) -> list[int]: ...

def processar(valor):
    if isinstance(valor, int):
        return valor * 2
    elif isinstance(valor, str):
        return valor.upper()
    elif isinstance(valor, list):
        return [x * 2 for x in valor]
    else:
        raise TypeError("Tipo não suportado")

# Cast - forçar tipo
from typing import cast
valor = cast(str, algum_objeto)

# AnyStr - string genérica
from typing import AnyStr

def concatenar(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

# TypeVar com constraints
T_co = TypeVar('T_co', covariant=True)  # Covariante
T_contra = TypeVar('T_contra', contravariant=True)  # Contravariante

# Awaitable, Coroutine
from typing import Awaitable, Coroutine

async def async_func() -> str:
    return "ok"

def get_coroutine() -> Coroutine[Any, Any, str]:
    return async_func()

# Type checking com mypy
"""
# Instalar: pip install mypy
# Executar: mypy arquivo.py
# Configuração: mypy.ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
ignore_missing_imports = False
strict_optional = True
"""

# Pydantic - validação de dados (biblioteca externa)
from pydantic import BaseModel, Field, validator

class Usuario(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    idade: int = Field(..., ge=0, le=150)
    email: str
    
    @validator('email')
    def validar_email(cls, v):
        if '@' not in v:
            raise ValueError('Email inválido')
        return v

usuario = Usuario(nome="João", idade=25, email="joao@email.com")
```

---

## 17. MANIPULAÇÃO DE DADOS

### 17.1 Pandas - Tudo que Existe

```python
import pandas as pd
import numpy as np

# Criação de DataFrames
# De lista de dicionários
df = pd.DataFrame([
    {'nome': 'Ana', 'idade': 25, 'cidade': 'SP'},
    {'nome': 'João', 'idade': 30, 'cidade': 'RJ'},
    {'nome': 'Maria', 'idade': 28, 'cidade': 'BH'},
])

# De dicionário de listas
df = pd.DataFrame({
    'nome': ['Ana', 'João', 'Maria'],
    'idade': [25, 30, 28],
    'cidade': ['SP', 'RJ', 'BH']
})

# De arrays numpy
arr = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])

# Index personalizado
df.index = ['linha1', 'linha2', 'linha3']

# Visualização
print(df.head())          # Primeiras 5 linhas
print(df.tail(3))         # Últimas 3 linhas
print(df.sample(5))       # Amostra aleatória
print(df.info())          # Informações do DataFrame
print(df.describe())      # Estatísticas descritivas
print(df.shape)           # (linhas, colunas)
print(df.dtypes)          # Tipos das colunas

# Seleção e filtro
# Por coluna
print(df['nome'])                    # Series
print(df[['nome', 'idade']])         # DataFrame

# Por linha
print(df.iloc[0])                     # Por posição
print(df.loc['linha1'])               # Por índice
print(df.iloc[0:2, 0:2])              # Fatiamento

# Filtro booleano
jovens = df[df['idade'] < 30]
sp = df[df['cidade'] == 'SP']
filtro = df[(df['idade'] > 25) & (df['salario'] > 5000)]

# Query (SQL-like)
df.query('idade > 25 and cidade == "SP"')

# Operações com colunas
df['idade_dobro'] = df['idade'] * 2
df['maior_idade'] = df['idade'] > 18
df['categoria'] = pd.cut(df['idade'], bins=[0, 18, 60, 100], labels=['jovem', 'adulto', 'idoso'])

# Agregações
media_idade = df['idade'].mean()
estatisticas = df['idade'].agg(['mean', 'median', 'std', 'min', 'max'])

# GroupBy
agrupado = df.groupby('cidade')['idade'].mean()
agrupado_multi = df.groupby(['cidade', 'maior_idade']).agg({
    'idade': ['mean', 'count'],
    'salario': 'sum'
})

# Pivot tables
pivot = pd.pivot_table(df, values='salario', index='cidade', columns='maior_idade', aggfunc='mean')

# Merge e join
df1 = pd.DataFrame({'id': [1, 2, 3], 'nome': ['Ana', 'João', 'Maria']})
df2 = pd.DataFrame({'id': [2, 3, 4], 'cidade': ['RJ', 'BH', 'SP']})

# Inner join
merge_inner = pd.merge(df1, df2, on='id', how='inner')

# Left join
merge_left = pd.merge(df1, df2, on='id', how='left')

# Concatenar
df_concatenado = pd.concat([df1, df2], axis=0)  # Vertical
df_horizontal = pd.concat([df1, df2], axis=1)   # Horizontal

# Tratamento de valores nulos
df.isnull().sum()                 # Contar nulos
df.dropna()                       # Remover nulos
df.fillna(0)                      # Preencher com 0
df.fillna(df.mean())              # Preencher com média
df.interpolate()                  # Interpolação

# Duplicatas
df.duplicated().sum()             # Contar duplicatas
df.drop_duplicates()              # Remover duplicatas

# Ordenação
df.sort_values('idade', ascending=False)
df.sort_values(['cidade', 'idade'], ascending=[True, False])

# Aplicar funções
df['nome_upper'] = df['nome'].apply(lambda x: x.upper())
df['idade_categoria'] = df['idade'].apply(lambda x: 'adulto' if x >= 18 else 'menor')

# Map com dicionário
df['cidade_cod'] = df['cidade'].map({'SP': 1, 'RJ': 2, 'BH': 3})

# Transformação de dados
# Reshape (melt, pivot)
df_melt = pd.melt(df, id_vars=['nome'], value_vars=['idade', 'salario'])
df_pivot = df_melt.pivot(index='nome', columns='variable', values='value')

# Window functions
df['media_movel'] = df['salario'].rolling(window=3).mean()
df['acumulado'] = df['salario'].cumsum()

# Datetime
df['data'] = pd.date_range('2024-01-01', periods=len(df), freq='D')
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month
df['dia_semana'] = df['data'].dt.dayofweek

# Exportar
df.to_csv('dados.csv', index=False)
df.to_excel('dados.xlsx', index=False, sheet_name='Dados')
df.to_json('dados.json', orient='records')
df.to_parquet('dados.parquet')
df.to_sql('tabela', conexao, if_exists='replace')

# Ler arquivos
df_csv = pd.read_csv('dados.csv')
df_excel = pd.read_excel('dados.xlsx', sheet_name='Dados')
df_json = pd.read_json('dados.json')
df_parquet = pd.read_parquet('dados.parquet')
df_sql = pd.read_sql('SELECT * FROM tabela', conexao)

# Performance
# Usar query para filtros grandes
df.query('idade > 25 and cidade == "SP"')
# Usar eval para expressões
df.eval('salario_ajustado = salario * 1.1')
# Usar numba para operações vetorizadas
```

### 17.2 NumPy - Tudo que Existe

```python
import numpy as np

# Criação de arrays
arr = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((3, 4))
ones = np.ones((2, 3, 4))
empty = np.empty((3, 3))
full = np.full((3, 3), 7)
eye = np.eye(5)  # Matriz identidade
diag = np.diag([1, 2, 3, 4])

# Arrays de sequências
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]
logspace = np.logspace(0, 3, 4)  # [1, 10, 100, 1000]

# Arrays aleatórios
random_rand = np.random.rand(3, 3)  # Uniforme [0,1)
random_randn = np.random.randn(3, 3)  # Normal N(0,1)
random_randint = np.random.randint(0, 10, (3, 3))  # Inteiros
random_uniform = np.random.uniform(0, 10, (3, 3))
random_normal = np.random.normal(0, 1, (3, 3))

# Propriedades
print(arr.shape)      # (5,)
print(arr.ndim)       # 1
print(arr.size)       # 5
print(arr.dtype)      # int64
print(arr.itemsize)   # 8
print(arr.nbytes)     # 40

# Indexação e fatiamento
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[2])          # 2
print(arr[2:7])        # [2,3,4,5,6]
print(arr[::2])        # [0,2,4,6,8]
print(arr[::-1])       # [9,8,7,6,5,4,3,2,1,0]

# Indexação booleana
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
print(arr[mask])  # [4, 5]

# Indexação avançada
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[[0, 1, 2], [0, 1, 2]])  # [1, 5, 9]

# Operações aritméticas
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)          # [5,7,9]
print(a - b)          # [-3,-3,-3]
print(a * b)          # [4,10,18]
print(a / b)          # [0.25,0.4,0.5]
print(a ** 2)         # [1,4,9]

# Operações universais (ufuncs)
print(np.sqrt(a))      # [1, 1.414, 1.732]
print(np.exp(a))       # [2.718, 7.389, 20.085]
print(np.log(a))       # [0, 0.693, 1.098]
print(np.sin(a))       # [0.841, 0.909, 0.141]

# Estatísticas
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())      # 3.0
print(arr.std())       # 1.414
print(arr.var())       # 2.0
print(arr.sum())       # 15
print(arr.min())       # 1
print(arr.max())       # 5
print(arr.argmin())    # 0
print(arr.argmax())    # 4
print(arr.cumsum())    # [1,3,6,10,15]
print(arr.cumprod())   # [1,2,6,24,120]

# Operações matriciais
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)                    # Multiplicação matricial
print(A.dot(B))                 # Mesmo que acima
print(A.T)                      # Transposta
print(np.linalg.inv(A))         # Inversa
print(np.linalg.det(A))         # Determinante
print(np.linalg.eig(A))         # Autovalores e autovetores
print(np.linalg.solve(A, [1, 2]))  # Resolver sistema linear

# Broadcasting
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20, 30])
print(A + B)  # [[11,22,33], [14,25,36]]

# Reshape e transposição
arr = np.arange(12)
print(arr.reshape(3, 4))        # (3,4)
print(arr.reshape(2, -1))       # (2,6)
print(arr.reshape(3, 2, 2))     # (3,2,2)
print(arr.reshape(-1, 1))       # (12,1)

# Concatenar
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.concatenate([a, b], axis=0))  # Vertical
print(np.concatenate([a, b], axis=1))  # Horizontal
print(np.vstack([a, b]))               # Vertical
print(np.hstack([a, b]))               # Horizontal

# Dividir
arr = np.arange(12).reshape(3, 4)
print(np.split(arr, 3, axis=0))        # Dividir por linhas
print(np.split(arr, 2, axis=1))        # Dividir por colunas

# Operações com NaN
arr = np.array([1, 2, np.nan, 4, 5])
print(np.nanmean(arr))      # 3.0 (ignora NaN)
print(np.nanstd(arr))       # Desvio padrão ignorando NaN

# Guardar e carregar
np.save('array.npy', arr)
arr_load = np.load('array.npy')
np.savez('arrays.npz', a=a, b=b)
data = np.load('arrays.npz')
print(data['a'])

# FFT (Transformada de Fourier)
signal = np.sin(2 * np.pi * 50 * np.linspace(0, 1, 1000))
fft = np.fft.fft(signal)
freq = np.fft.fftfreq(len(signal), 1/1000)

# Máscaras e where
arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 3, arr, 0)  # [0,0,0,4,5]
```

---

## 18. APIS E WEB

### 18.1 Requests - Tudo que Existe

```python
import requests
from requests.exceptions import RequestException, Timeout, HTTPError
import json

# GET básico
response = requests.get('https://api.exemplo.com/dados')
print(response.status_code)      # 200
print(response.headers)          # Cabeçalhos
print(response.text)             # Texto bruto
print(response.json())           # JSON para dict

# Parâmetros
params = {'q': 'python', 'page': 1, 'limit': 10}
response = requests.get('https://api.exemplo.com/search', params=params)
print(response.url)  # https://api.exemplo.com/search?q=python&page=1&limit=10

# POST com JSON
dados = {"nome": "João", "idade": 30}
response = requests.post(
    'https://api.exemplo.com/usuarios',
    json=dados,
    headers={'Authorization': 'Bearer token', 'Content-Type': 'application/json'}
)

# POST com formulário
form_data = {'username': 'joao', 'password': 'senha'}
response = requests.post('https://api.exemplo.com/login', data=form_data)

# POST com arquivo
files = {'arquivo': open('foto.jpg', 'rb')}
response = requests.post('https://api.exemplo.com/upload', files=files)

# Autenticação
# Basic Auth
response = requests.get('https://api.exemplo.com', auth=('user', 'pass'))

# Bearer Token
headers = {'Authorization': 'Bearer seu_token_aqui'}
response = requests.get('https://api.exemplo.com', headers=headers)

# OAuth2 (com requests-oauthlib)
from requests_oauthlib import OAuth2Session
oauth = OAuth2Session(client_id, token=token)

# Headers personalizados
headers = {
    'User-Agent': 'MeuApp/1.0',
    'Accept': 'application/json',
    'Accept-Language': 'pt-BR',
}

# Timeout
try:
    response = requests.get('https://api.exemplo.com', timeout=(3, 10))  # (connect, read)
except Timeout:
    print("Timeout!")

# Tratamento de erros
try:
    response = requests.get('https://api.exemplo.com')
    response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
except HTTPError as e:
    print(f"Erro HTTP: {e}")
except ConnectionError as e:
    print(f"Erro de conexão: {e}")
except RequestException as e:
    print(f"Erro na requisição: {e}")

# Sessão (reutiliza conexão)
session = requests.Session()
session.headers.update({'User-Agent': 'MeuApp/1.0'})
session.auth = ('user', 'pass')

# Usar sessão para múltiplas requisições
response1 = session.get('https://api.exemplo.com/dados1')
response2 = session.get('https://api.exemplo.com/dados2')

# Cookies
session.cookies.set('nome', 'valor')
cookies = {'session_id': '12345'}
response = requests.get('https://api.exemplo.com', cookies=cookies)

# Proxies
proxies = {
    'http': 'http://proxy.exemplo.com:8080',
    'https': 'https://proxy.exemplo.com:8080',
}
response = requests.get('https://api.exemplo.com', proxies=proxies)

# Verificar SSL
response = requests.get('https://api.exemplo.com', verify=True)  # Default
response = requests.get('https://api.exemplo.com', verify=False)  # Ignorar (não recomendado)

# Streaming de conteúdo grande
response = requests.get('https://api.exemplo.com/arquivo_grande', stream=True)
with open('arquivo_grande', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

# Upload de arquivo grande
with open('arquivo_grande', 'rb') as f:
    response = requests.post('https://api.exemplo.com/upload', data=f)

# Event hooks
def print_status(response, *args, **kwargs):
    print(f"Status: {response.status_code}")

response = requests.get('https://api.exemplo.com', hooks={'response': print_status})

# Retry com urllib3
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

session = requests.Session()
retry = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
```

### 18.2 FastAPI - Framework Web Moderno

```python
from fastapi import FastAPI, HTTPException, Depends, status, Query, Path, Body
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from typing import Optional, List
import uvicorn

app = FastAPI(title="Minha API", version="1.0.0")

# Modelos Pydantic
class UsuarioBase(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    email: str
    idade: Optional[int] = Field(None, ge=0, le=150)

class UsuarioCreate(UsuarioBase):
    senha: str = Field(..., min_length=8)

class UsuarioResponse(UsuarioBase):
    id: int
    ativo: bool = True

# Endpoints básicos
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/usuarios/{usuario_id}")
async def get_usuario(
    usuario_id: int = Path(..., gt=0, description="ID do usuário"),
    detalhado: bool = Query(False, description="Incluir detalhes")
):
    return {"id": usuario_id, "detalhado": detalhado}

@app.post("/usuarios", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def create_usuario(usuario: UsuarioCreate):
    # Lógica de criação
    return {"id": 1, "nome": usuario.nome, "email": usuario.email, "ativo": True}

@app.put("/usuarios/{usuario_id}")
async def update_usuario(usuario_id: int, usuario: UsuarioBase):
    return {"id": usuario_id, **usuario.dict()}

@app.delete("/usuarios/{usuario_id}")
async def delete_usuario(usuario_id: int):
    return {"message": f"Usuário {usuario_id} deletado"}

# Query parameters
@app.get("/buscar")
async def search(
    q: str = Query(..., min_length=1, max_length=100),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    return {"query": q, "limit": limit, "offset": offset}

# Dependências
async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    # Validar token
    return {"id": 1, "nome": "João"}

@app.get("/perfil")
async def get_perfil(current_user: dict = Depends(get_current_user)):
    return current_user

# Upload de arquivos
from fastapi import UploadFile, File

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}

# Respostas personalizadas
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse

@app.get("/download")
async def download_file():
    return FileResponse("arquivo.pdf", media_type="application/pdf", filename="documento.pdf")

@app.get("/html")
async def get_html():
    html_content = "<html><body><h1>Hello World</h1></body></html>"
    return HTMLResponse(content=html_content, status_code=200)

# Exceções personalizadas
@app.get("/itens/{item_id}")
async def get_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"item_id": item_id}

# Middleware
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Background tasks
from fastapi import BackgroundTasks

def send_email(email: str, message: str):
    # Enviar email
    pass

@app.post("/enviar-email")
async def send_email_endpoint(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, "Olá!")
    return {"message": "Email enviado em background"}

# WebSocket
from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Eco: {data}")
    except WebSocketDisconnect:
        print("Cliente desconectado")

# Executar
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

# Documentação automática: /docs (Swagger) e /redoc (ReDoc)
```

---

## 19. TESTES E DEBUGGING

### 19.1 Pytest - Tudo que Existe

```python
import pytest
from pytest import fixture, mark, raises, approx
import asyncio
import requests

# Teste básico
def test_soma():
    assert 2 + 2 == 4

# Fixtures
@fixture
def dados_teste():
    return [1, 2, 3, 4, 5]

@fixture(scope="session")  # scope: function, class, module, session
def db_connection():
    conn = create_connection()
    yield conn
    conn.close()

def test_com_fixture(dados_teste):
    assert len(dados_teste) == 5
    assert sum(dados_teste) == 15

# Parametrização
@mark.parametrize("a,b,esperado", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_soma_parametrizada(a, b, esperado):
    assert a + b == esperado

@mark.parametrize("valor", [1, 2, 3, 4, 5])
def test_quadrado(valor):
    assert valor ** 2 == valor * valor

# Exceções
def test_excecao():
    with raises(ZeroDivisionError):
        x = 1 / 0

def test_excecao_com_mensagem():
    with raises(ValueError, match=".*inválido.*"):
        raise ValueError("Valor inválido")

# Aproximação (para floats)
def test_float():
    assert 0.1 + 0.2 == approx(0.3)
    assert 0.1 + 0.2 == approx(0.3, rel=1e-6, abs=1e-12)

# Skip e Xfail
@mark.skip(reason="Não implementado")
def test_skip():
    pass

@mark.xfail(reason="Bug conhecido")
def test_xfail():
    assert 2 + 2 == 5

# Testes assíncronos
@pytest.mark.asyncio
async def test_async():
    result = await minha_funcao_async()
    assert result == "ok"

# Mocks
def test_mock(mocker):
    mock = mocker.patch('requests.get')
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {"ok": True}
    
    result = minha_funcao_que_chama_api()
    assert result["ok"] is True
    mock.assert_called_once()

# Fixture com parametrização
@fixture(params=[1, 2, 3])
def numero(request):
    return request.param

def test_com_param_fixture(numero):
    assert numero > 0

# Teardown automático
@fixture
def arquivo_temporario(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("conteúdo")
    yield file
    # Teardown automático com tmp_path

# Plugin de cobertura
"""
# Instalar: pip install pytest-cov
# Executar: pytest --cov=meu_modulo --cov-report=html tests/
"""

# Plugin de testes paralelos
"""
# Instalar: pip install pytest-xdist
# Executar: pytest -n auto
"""

# Conftest.py (configuração compartilhada)
"""
# tests/conftest.py
import pytest

@pytest.fixture(scope="session")
def db_connection():
    # Setup
    yield
    # Teardown

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: marca testes lentos")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Hook para relatórios
    pass
"""

# Executar testes
"""
pytest                          # Todos testes
pytest tests/test_arquivo.py    # Arquivo específico
pytest -k "soma"                # Filtra por nome
pytest -v                       # Verboso
pytest -x                       # Para no primeiro erro
pytest --maxfail=3              # Para após 3 erros
pytest --tb=short               # Traceback curto
pytest --lf                     # Executa últimos falhos
pytest --ff                     # Executa últimos falhos primeiro
pytest --durations=10           # Mostra testes mais lentos
"""
```

### 19.2 Debugging Avançado

```python
import pdb
import ipdb
import logging
import traceback
import sys
from pprint import pprint

# PDB - Python Debugger
def funcao_com_pdb(a, b):
    pdb.set_trace()  # Ponto de parada
    resultado = a + b
    return resultado

# Comandos PDB:
"""
n (next)        - Próxima linha
s (step)        - Entra em função
c (continue)    - Continua até próximo breakpoint
q (quit)        - Sai
l (list)        - Mostra código ao redor
p var           - Imprime variável
pp var          - Imprime com pretty print
w (where)       - Mostra stack trace
u (up)          - Sobe no stack
d (down)        - Desce no stack
b linha         - Adiciona breakpoint
cl              - Limpa breakpoints
!comando        - Executa comando Python
args            - Mostra argumentos da função
return          - Continua até retorno
j linha         - Pula para linha
"""

# ipdb - PDB melhorado (pip install ipdb)
def funcao_com_ipdb(a, b):
    import ipdb; ipdb.set_trace()
    resultado = a + b
    return resultado

# Breakpoint() - Python 3.7+
def funcao_com_breakpoint(a, b):
    breakpoint()  # Equivalente a pdb.set_trace()
    resultado = a + b
    return resultado

# Logging avançado
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# Níveis de log
logger.debug("Mensagem de debug")
logger.info("Informação")
logger.warning("Aviso")
logger.error("Erro")
logger.critical("Crítico")
logger.exception("Exceção com stack trace")

# Logging estruturado
logger.info("Usuário criado", extra={
    'user_id': 123,
    'username': 'joao',
    'action': 'create'
})

# Filtros de logging
class UserFilter(logging.Filter):
    def filter(self, record):
        return hasattr(record, 'user_id')

logger.addFilter(UserFilter())

# Traceback completo
try:
    1 / 0
except Exception:
    print(traceback.format_exc())
    print(traceback.print_exc())

# Pretty print
dados = {
    'nome': 'João',
    'endereco': {
        'rua': 'Av. Paulista',
        'numero': 1000,
        'cidade': 'São Paulo'
    },
    'telefones': [11, 98765, 4321]
}
pprint(dados, indent=2, width=80)

# Profiling com cProfile
import cProfile
import pstats

def funcao_para_perfil():
    [i**2 for i in range(1000000)]

cProfile.run('funcao_para_perfil()', 'stats.prof')
p = pstats.Stats('stats.prof')
p.sort_stats('cumulative').print_stats(10)

# Profiling linha a linha
# pip install line_profiler
@profile
def funcao_lenta():
    total = 0
    for i in range(1000000):
        total += i**2
    return total

# Memória profiling
# pip install memory_profiler
@profile
def uso_memoria():
    a = [i**2 for i in range(1000000)]
    b = [i**3 for i in range(1000000)]
    return a, b

# Sys.settrace - tracing personalizado
import sys

def trace_function(frame, event, arg):
    print(f"Evento: {event}, Linha: {frame.f_lineno}")
    return trace_function

sys.settrace(trace_function)

# Contextvars - variáveis de contexto
import contextvars

user_id = contextvars.ContextVar('user_id', default=None)

def processar_request():
    user_id.set(123)
    processar_dados()

def processar_dados():
    print(f"Usuário: {user_id.get()}")
```

---

## 20. PERFORMANCE E OTIMIZAÇÃO

### 20.1 Otimização de Código

```python
import timeit
import cProfile
import pstats
from functools import lru_cache
import numpy as np
from numba import jit, njit
import dis

# Medir tempo de execução
def timer(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        print(f"{func.__name__}: {end - start:.4f}s")
        return result
    return wrapper

@timer
def funcao_lenta():
    [i**2 for i in range(1000000)]

# timeit
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Média: {tempo/10000:.6f}s")

# Cache com lru_cache
@lru_cache(maxsize=128)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# JIT com Numba
@njit
def soma_quadrados(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# NumPy para operações vetorizadas
def loop_puro(n):
    return [i**2 for i in range(n)]

def numpy_vectorized(n):
    return np.arange(n)**2

# Disassembler para ver bytecode
def exemplo():
    a = 10
    b = 20
    c = a + b

dis.dis(exemplo)

# Dicas de performance

# 1. Use compreensões em vez de loops
# Ruim
soma = 0
for i in range(1000):
    soma += i ** 2

# Bom
soma = sum(i ** 2 for i in range(1000))

# 2. Use built-in functions
# Ruim
max_val = 0
for x in lista:
    if x > max_val:
        max_val = x

# Bom
max_val = max(lista)

# 3. Evite concatenação de strings em loops
# Ruim
resultado = ""
for s in strings:
    resultado += s

# Bom
resultado = "".join(strings)

# 4. Use generators para grandes volumes
# Ruim
grande_lista = [processar(x) for x in range(1000000)]

# Bom
grande_gen = (processar(x) for x in range(1000000))

# 5. Use slots em classes
class Otimizado:
    __slots__ = ['nome', 'idade']
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# 6. Use array.array para listas numéricas
import array
arr = array.array('i', range(1000000))

# 7. Use __slots__ para economizar memória
class Pessoa:
    __slots__ = ['nome', 'idade']

# 8. Evite atributos desnecessários
# 9. Use local variables em loops
def loop_otimizado(lista):
    append = lista.append  # Cache local
    for i in range(1000):
        append(i)

# 10. Use is para comparações com None, True, False
if valor is None:  # Bom
if valor == None:  # Ruim

# 11. Use try/except para casos excepcionais
# Ruim
if key in dict:
    value = dict[key]
else:
    value = default

# Bom (EAFP - Easier to Ask for Forgiveness than Permission)
try:
    value = dict[key]
except KeyError:
    value = default

# 12. Use functools.partial para currying
from functools import partial
def potencia(base, exp):
    return base ** exp

quadrado = partial(potencia, exp=2)

# 13. Use collections.deque para filas
from collections import deque
fila = deque()
fila.append(1)
fila.popleft()  # O(1)

# 14. Use heapq para priority queues
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappop(heap)  # 1 (menor)

# 15. Use caching com lru_cache
@lru_cache(maxsize=1024)
def get_dados(id):
    return buscar_banco(id)

# 16. Use memoryview para operações com bytes
data = bytearray(b'hello')
mv = memoryview(data)
mv[0] = 72  # Modifica sem cópia

# 17. Use array.array para dados numéricos
import array
arr = array.array('d', [0.0] * 1000000)

# 18. Use numpy para operações vetorizadas
import numpy as np
arr = np.random.rand(1000000)
resultado = arr * 2  # Vetorizado

# 19. Use numba para código numérico intensivo
from numba import jit

@jit(nopython=True)
def soma_quadrados(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# 20. Use multiprocessing para CPU-bound
from multiprocessing import Pool

def processar_paralelo(dados):
    with Pool() as pool:
        return pool.map(processar, dados)

# 21. Use asyncio para I/O-bound
import asyncio
async def processar_io():
    tasks = [fazer_request() for _ in range(100)]
    return await asyncio.gather(*tasks)

# 22. Use C extensions (Cython, CFFI) para código crítico
# 23. Use PyPy para melhor performance em código Python puro
# 24. Use mypy para type hints que podem otimizar
# 25. Profile antes de otimizar - sempre!
```

---

## 21. PADRÕES DE PROJETO

### 21.1 Padrões Criacionais

```python
# Singleton
class Singleton:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

# Singleton com decorador
def singleton(cls):
    instancias = {}
    def wrapper(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]
    return wrapper

@singleton
class Config:
    pass

# Factory Method
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

class AnimalFactory:
    def criar_animal(self, tipo):
        if tipo == "cachorro":
            return Cachorro()
        elif tipo == "gato":
            return Gato()
        raise ValueError(f"Tipo desconhecido: {tipo}")

# Abstract Factory
class GUIFactory:
    def criar_botao(self):
        pass
    
    def criar_janela(self):
        pass

class WindowsFactory(GUIFactory):
    def criar_botao(self):
        return WindowsButton()
    
    def criar_janela(self):
        return WindowsWindow()

class MacFactory(GUIFactory):
    def criar_botao(self):
        return MacButton()
    
    def criar_janela(self):
        return MacWindow()

# Builder
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def massa(self, tipo):
        self.pizza.massa = tipo
        return self
    
    def queijo(self, tipo):
        self.pizza.queijo = tipo
        return self
    
    def cobertura(self, *coberturas):
        self.pizza.coberturas.extend(coberturas)
        return self
    
    def build(self):
        return self.pizza

# Uso
pizza = PizzaBuilder()\
    .massa("fina")\
    .queijo("mussarela")\
    .cobertura("tomate", "manjericão")\
    .build()

# Prototype
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Documento(Prototype):
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

original = Documento("Original", "Conteúdo")
copia = original.clone()
```

### 21.2 Padrões Estruturais

```python
# Adapter
class AdaptadorEuropeu:
    def ligar(self):
        return "220V"

class AdaptadorBrasileiro:
    def conectar(self):
        return "110V"

class Adaptador(AdaptadorBrasileiro):
    def __init__(self, europeu):
        self.europeu = europeu
    
    def conectar(self):
        return self.europeu.ligar()

# Decorator
class Cafe:
    def custo(self):
        return 5
    
    def descricao(self):
        return "Café"

class LeiteDecorator:
    def __init__(self, cafe):
        self.cafe = cafe
    
    def custo(self):
        return self.cafe.custo() + 2
    
    def descricao(self):
        return self.cafe.descricao() + ", leite"

class AcucarDecorator:
    def __init__(self, cafe):
        self.cafe = cafe
    
    def custo(self):
        return self.cafe.custo() + 1
    
    def descricao(self):
        return self.cafe.descricao() + ", açúcar"

# Uso
cafe = Cafe()
cafe_com_leite = LeiteDecorator(cafe)
cafe_completo = AcucarDecorator(cafe_com_leite)

# Facade
class SistemaFacade:
    def __init__(self):
        self.sub1 = SubSistema1()
        self.sub2 = SubSistema2()
        self.sub3 = SubSistema3()
    
    def operacao_complexa(self):
        resultado = []
        resultado.append(self.sub1.operacao1())
        resultado.append(self.sub2.operacao2())
        resultado.append(self.sub3.operacao3())
        return resultado

# Proxy
class ImagemProxy:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self._imagem = None
    
    def exibir(self):
        if self._imagem is None:
            self._imagem = ImagemReal(self.nome_arquivo)
        self._imagem.exibir()

# Composite
class Componente:
    pass

class Arquivo(Componente):
    def __init__(self, nome):
        self.nome = nome
    
    def tamanho(self):
        return len(self.nome)

class Diretorio(Componente):
    def __init__(self, nome):
        self.nome = nome
        self.componentes = []
    
    def adicionar(self, componente):
        self.componentes.append(componente)
    
    def tamanho(self):
        return sum(c.tamanho() for c in self.componentes)
```

### 21.3 Padrões Comportamentais

```python
# Observer
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"Recebido: {subject.state}")

# Strategy
class EstrategiaPagamento:
    def pagar(self, valor):
        pass

class CartaoCredito(EstrategiaPagamento):
    def pagar(self, valor):
        return f"Pagando R${valor} com cartão"

class Boleto(EstrategiaPagamento):
    def pagar(self, valor):
        return f"Gerando boleto de R${valor}"

class Pix(EstrategiaPagamento):
    def pagar(self, valor):
        return f"Pagando R${valor} via PIX"

class Pedido:
    def __init__(self, estrategia):
        self.estrategia = estrategia
    
    def pagar(self, valor):
        return self.estrategia.pagar(valor)

# Command
class Comando:
    def executar(self):
        pass
    
    def desfazer(self):
        pass

class ComandoLigar(Comando):
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo
    
    def executar(self):
        self.dispositivo.ligar()
    
    def desfazer(self):
        self.dispositivo.desligar()

# State
class Estado:
    def processar(self):
        pass

class EstadoPendente(Estado):
    def processar(self):
        return "Processando pagamento"

class EstadoPago(Estado):
    def processar(self):
        return "Enviando produto"

class EstadoEntregue(Estado):
    def processar(self):
        return "Pedido entregue"

class PedidoState:
    def __init__(self):
        self.estado = EstadoPendente()
    
    def processar(self):
        return self.estado.processar()

# Template Method
class Jogo:
    def jogar(self):
        self.inicializar()
        self.iniciar()
        self.finalizar()
    
    def inicializar(self):
        pass
    
    def iniciar(self):
        pass
    
    def finalizar(self):
        pass

class Futebol(Jogo):
    def inicializar(self):
        print("Escalando times")
    
    def iniciar(self):
        print("Apito inicial")
    
    def finalizar(self):
        print("Apito final")

# Chain of Responsibility
class Handler:
    def __init__(self):
        self._next = None
    
    def set_next(self, handler):
        self._next = handler
        return handler
    
    def handle(self, request):
        if self._next:
            return self._next.handle(request)
        return None
```

---

## 22. CRIPTOGRAFIA E SEGURANÇA

### 22.1 Hashing e Criptografia

```python
import hashlib
import hmac
import secrets
import bcrypt
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# Hashing básico
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Hashing com salt (bcrypt)
def hash_senha_bcrypt(senha):
    salt = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha.encode(), salt)
    return hash_senha

def verificar_senha(senha, hash_senha):
    return bcrypt.checkpw(senha.encode(), hash_senha)

# HMAC (Hash-based Message Authentication Code)
def gerar_hmac(mensagem, chave):
    return hmac.new(
        chave.encode(),
        mensagem.encode(),
        hashlib.sha256
    ).hexdigest()

# Gerar tokens seguros
token = secrets.token_hex(32)
token_url = secrets.token_urlsafe(32)
token_bytes = secrets.token_bytes(32)

# Criptografia simétrica (Fernet)
def gerar_chave():
    return Fernet.generate_key()

def criptografar(mensagem, chave):
    f = Fernet(chave)
    return f.encrypt(mensagem.encode())

def descriptografar(mensagem_cripto, chave):
    f = Fernet(chave)
    return f.decrypt(mensagem_cripto).decode()

# Criptografia assimétrica (RSA)
def gerar_par_chaves():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def criptografar_rsa(mensagem, public_key):
    return public_key.encrypt(
        mensagem.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def descriptografar_rsa(mensagem_cripto, private_key):
    return private_key.decrypt(
        mensagem_cripto,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()

# Assinatura digital
def assinar(mensagem, private_key):
    return private_key.sign(
        mensagem.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def verificar_assinatura(mensagem, assinatura, public_key):
    try:
        public_key.verify(
            assinatura,
            mensagem.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False

# Hash de arquivo
def hash_arquivo(caminho):
    sha256 = hashlib.sha256()
    with open(caminho, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()
```

---

## 23. REDES E SOCKETS

### 23.1 Sockets TCP/UDP

```python
import socket
import threading
import json

# Servidor TCP
def servidor_tcp(host='localhost', port=8888):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print(f"Servidor ouvindo em {host}:{port}")
    
    while True:
        client, addr = server.accept()
        print(f"Conexão de {addr}")
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

def handle_client(client):
    with client:
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.send(data.upper())

# Cliente TCP
def cliente_tcp(mensagem, host='localhost', port=8888):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(mensagem.encode())
    resposta = client.recv(1024)
    client.close()
    return resposta.decode()

# Servidor UDP
def servidor_udp(host='localhost', port=8888):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print(f"Servidor UDP ouvindo em {host}:{port}")
    
    while True:
        data, addr = server.recvfrom(1024)
        print(f"Recebido de {addr}: {data.decode()}")
        server.sendto(data.upper(), addr)

# Cliente UDP
def cliente_udp(mensagem, host='localhost', port=8888):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(mensagem.encode(), (host, port))
    data, addr = client.recvfrom(1024)
    client.close()
    return data.decode()

# Socket com timeout
socket.setdefaulttimeout(5)  # Timeout global

# Socket não bloqueante
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(False)

# Socket com keepalive
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

# Enviar dados estruturados (JSON)
def enviar_objeto(sock, obj):
    data = json.dumps(obj).encode()
    sock.send(len(data).to_bytes(4, 'big'))
    sock.send(data)

def receber_objeto(sock):
    size = int.from_bytes(sock.recv(4), 'big')
    data = sock.recv(size)
    return json.loads(data.decode())
```

---

## 24. BANCO DE DADOS

### 24.1 SQLite, PostgreSQL, MongoDB

```python
# SQLite
import sqlite3

# Conexão
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        email TEXT UNIQUE
    )
''')

# Inserir
cursor.execute(
    'INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)',
    ('João', 25, 'joao@email.com')
)
conn.commit()

# Inserir múltiplos
usuarios = [
    ('Maria', 30, 'maria@email.com'),
    ('Pedro', 28, 'pedro@email.com')
]
cursor.executemany(
    'INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)',
    usuarios
)

# Consultar
cursor.execute('SELECT * FROM usuarios')
for row in cursor.fetchall():
    print(row)

# Usando dict cursor
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute('SELECT * FROM usuarios')
for row in cursor.fetchall():
    print(dict(row))

# SQLAlchemy ORM
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    email = Column(String, unique=True)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Inserir
usuario = Usuario(nome='João', idade=25, email='joao@email.com')
session.add(usuario)
session.commit()

# Consultar
usuarios = session.query(Usuario).all()
for u in usuarios:
    print(u.nome, u.idade)

# PostgreSQL com psycopg2
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="meubanco",
    user="usuario",
    password="senha"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()

# MongoDB com pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['meubanco']
colecao = db['usuarios']

# Inserir
usuario = {'nome': 'João', 'idade': 25, 'email': 'joao@email.com'}
colecao.insert_one(usuario)

# Inserir múltiplos
usuarios = [
    {'nome': 'Maria', 'idade': 30},
    {'nome': 'Pedro', 'idade': 28}
]
colecao.insert_many(usuarios)

# Consultar
for usuario in colecao.find({'idade': {'$gt': 25}}):
    print(usuario)

# Atualizar
colecao.update_one(
    {'nome': 'João'},
    {'$set': {'idade': 26}}
)

# Deletar
colecao.delete_one({'nome': 'João'})

# Redis (cache)
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('chave', 'valor')
valor = r.get('chave')
r.expire('chave', 60)  # Expira em 60 segundos
```

---

## 25. MACHINE LEARNING BÁSICO

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# Dados exemplo
df = pd.DataFrame({
    'idade': [25, 30, 35, 40, 45],
    'renda': [3000, 4000, 5000, 6000, 7000],
    'classe': [0, 0, 1, 1, 1]
})

# Separar features e target
X = df[['idade', 'renda']]
y = df['classe']

# Dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Escalonar dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Treinar modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predizer
y_pred = model.predict(X_test_scaled)

# Avaliar
print(f"Acurácia: {accuracy_score(y_test, y_pred)}")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Salvar modelo
joblib.dump(model, 'modelo.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Carregar modelo
model_carregado = joblib.load('modelo.pkl')
scaler_carregado = joblib.load('scaler.pkl')

# Pipeline do sklearn
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(n_estimators=100))
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# Cross-validation
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print(f"CV Scores: {scores}")
print(f"Média: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")

# Grid Search
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy'
)

grid_search.fit(X_train, y_train)
print(f"Melhores parâmetros: {grid_search.best_params_}")
print(f"Melhor score: {grid_search.best_score_}")
```

---

## 26. AUTOMAÇÃO E SCRIPTS

```python
import os
import sys
import argparse
import glob
import shutil
import subprocess
import schedule
import time

# Argumentos de linha de comando
parser = argparse.ArgumentParser(description='Script de automação')
parser.add_argument('--input', '-i', required=True, help='Arquivo de entrada')
parser.add_argument('--output', '-o', default='output', help='Diretório de saída')
parser.add_argument('--verbose', '-v', action='store_true', help='Modo verboso')
parser.add_argument('--limit', '-l', type=int, default=100, help='Limite máximo')
args = parser.parse_args()

# Manipulação de arquivos em massa
# Renomear arquivos
for arquivo in glob.glob('*.txt'):
    novo_nome = f"backup_{arquivo}"
    shutil.move(arquivo, novo_nome)

# Organizar por extensão
def organizar_arquivos():
    for arquivo in glob.glob('*.*'):
        ext = arquivo.split('.')[-1]
        pasta = ext.upper()
        os.makedirs(pasta, exist_ok=True)
        shutil.move(arquivo, os.path.join(pasta, arquivo))

# Executar comandos do sistema
def executar_comando(comando):
    resultado = subprocess.run(
        comando,
        shell=True,
        capture_output=True,
        text=True
    )
    if resultado.returncode == 0:
        print(resultado.stdout)
    else:
        print(f"Erro: {resultado.stderr}")
    return resultado

# Agendamento de tarefas
def tarefa_diaria():
    print("Executando tarefa diária...")

schedule.every().day.at("10:00").do(tarefa_diaria)
schedule.every().hour.do(lambda: print("Hora passou"))
schedule.every(30).minutes.do(lambda: print("30 minutos"))

# Web scraping com BeautifulSoup
import requests
from bs4 import BeautifulSoup

def scrape_pagina(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titulos = soup.find_all('h2')
    for titulo in titulos:
        print(titulo.text.strip())

# Enviar email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(destinatario, assunto, corpo):
    msg = MIMEMultipart()
    msg['From'] = 'seu_email@gmail.com'
    msg['To'] = destinatario
    msg['Subject'] = assunto
    
    msg.attach(MIMEText(corpo, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('seu_email@gmail.com', 'senha')
    server.send_message(msg)
    server.quit()

# Monitorar sistema
import psutil

def monitorar_sistema():
    print(f"CPU: {psutil.cpu_percent()}%")
    print(f"Memória: {psutil.virtual_memory().percent}%")
    print(f"Disco: {psutil.disk_usage('/').percent}%")
    
    # Processos
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        if proc.info['memory_percent'] > 10:
            print(f"Processo: {proc.info}")

# Backup automático
def fazer_backup(origem, destino):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    nome_backup = f"backup_{timestamp}.zip"
    shutil.make_archive(
        os.path.join(destino, nome_backup.replace('.zip', '')),
        'zip',
        origem
    )
    print(f"Backup criado: {nome_backup}")
```

---

## 27. EMPACOTAMENTO E DISTRIBUIÇÃO

### 27.1 Setup.py Completo

```python
# setup.py
from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="meu_pacote",
    version="1.0.0",
    author="Seu Nome",
    author_email="email@exemplo.com",
    description="Descrição do pacote",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usuario/meu_pacote",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        "meu_pacote": ["*.json", "data/*.csv"],
    },
    install_requires=requirements,
    extras_require={
        "dev": ["pytest", "black", "mypy", "flake8"],
        "test": ["pytest", "pytest-cov", "coverage"],
        "docs": ["sphinx", "sphinx-rtd-theme"],
    },
    entry_points={
        "console_scripts": [
            "meu-comando=meu_pacote.cli:main",
            "meu-script=meu_pacote.scripts:run",
        ],
        "gui_scripts": [
            "meu-gui=meu_pacote.gui:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    project_urls={
        "Bug Reports": "https://github.com/usuario/meu_pacote/issues",
        "Source": "https://github.com/usuario/meu_pacote",
        "Documentation": "https://meu_pacote.readthedocs.io",
    },
)
```

### 27.2 Pyproject.toml (PEP 621)

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "meu_pacote"
version = "1.0.0"
description = "Descrição do pacote"
readme = "README.md"
authors = [
    {name = "Seu Nome", email = "email@exemplo.com"},
]
license = {text = "MIT"}
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
requires-python = ">=3.7"
dependencies = [
    "requests>=2.25.0",
    "numpy>=1.19.0",
]

[project.optional-dependencies]
dev = [
    "pytest",
    "black",
    "mypy",
    "flake8",
]
test = [
    "pytest",
    "pytest-cov",
    "coverage",
]

[project.urls]
Homepage = "https://github.com/usuario/meu_pacote"
Bug Reports = "https://github.com/usuario/meu_pacote/issues"
Documentation = "https://meu_pacote.readthedocs.io"

[project.scripts]
meu-comando = "meu_pacote.cli:main"
meu-script = "meu_pacote.scripts:run"

[tool.setuptools]
package-dir = {"" = "src"}
packages = ["meu_pacote"]

[tool.black]
line-length = 88
target-version = ['py37', 'py38', 'py39', 'py310']
include = '\.pyi?$'

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.7"
warn_return_any = true
warn_unused_configs = true
ignore_missing_imports = false
strict_optional = true

[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q --cov=meu_pacote --cov-report=term-missing"
testpaths = ["tests"]

[tool.coverage.run]
source = ["meu_pacote"]
omit = ["*/tests/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if __name__ == .__main__.:",
]
```

### 27.3 Comandos de Distribuição

```bash
# Instalar em modo desenvolvimento
pip install -e .

# Criar distribuição
python -m build

# Publicar no PyPI
twine upload dist/*

# Publicar no TestPyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Criar wheel
python setup.py bdist_wheel

# Criar source distribution
python setup.py sdist

# Verificar pacote
twine check dist/*

# Instalar pacote local
pip install dist/meu_pacote-1.0.0-py3-none-any.whl

# Desinstalar
pip uninstall meu_pacote

# Listar pacotes instalados
pip list

# Congelar dependências
pip freeze > requirements.txt

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

---

## 28. BOAS PRÁTICAS E ESTILO

### 28.1 PEP 8 - Estilo de Código

```python
# Nomes
variavel_publica = "snake_case"
_privada = "underscore"
CONSTANTE = "UPPERCASE"
ClasseExemplo = "CamelCase"
funcao_exemplo = "snake_case"

# Indentação (4 espaços)
def funcao_com_muitos_argumentos(
    arg1: str,
    arg2: int,
    arg3: bool = False
) -> None:
    if condicao_muito_longa and \
       outra_condicao and \
       mais_uma_condicao:
        fazer_algo()

# Importação
# 1. Biblioteca padrão
import os
import sys
from datetime import datetime

# 2. Bibliotecas de terceiros
import numpy as np
import pandas as pd

# 3. Módulos locais
from meu_pacote import modulo

# Docstring
def minha_funcao(param1: str, param2: int = 0) -> bool:
    """
    Descrição resumida.

    Descrição detalhada da função e seu comportamento.

    Args:
        param1: Descrição do primeiro parâmetro
        param2: Descrição do segundo parâmetro (opcional)

    Returns:
        Descrição do retorno

    Raises:
        ValueError: Se param1 for vazio

    Examples:
        >>> minha_funcao("teste", 5)
        True
    """
    return True

# Comentários
# Comentário de linha

"""
Comentário de bloco
múltiplas linhas
"""

# Espaçamento
x = (y + z) * (a - b)  # Espaços ao redor de operadores
lista = [1, 2, 3, 4]   # Espaço após vírgula
func(arg1, arg2, arg3) # Sem espaço antes da vírgula
```

### 28.2 Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: debug-statements

  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: ["--max-line-length=88", "--extend-ignore=E203"]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

### 28.3 GitHub Actions

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.8", "3.9", "3.10", "3.11"]

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .[dev,test]
    
    - name: Lint with flake8
      run: |
        flake8 src tests
    
    - name: Format with black
      run: |
        black --check src tests
    
    - name: Type check with mypy
      run: |
        mypy src
    
    - name: Test with pytest
      run: |
        pytest --cov=src --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        fail_ci_if_error: true
```

---

## 📊 TABELA RESUMO FINAL

| Categoria | Principais Comandos/Conceitos |
|-----------|------------------------------|
| **Tipos** | `int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`, `set`, `None` |
| **Estruturas** | Listas, Dicionários, Conjuntos, Tuplas, Deque, Heap, Counter |
| **Strings** | `upper()`, `lower()`, `split()`, `join()`, `f-strings`, `format()` |
| **Controle** | `if/elif/else`, `match/case`, `for`, `while`, `break`, `continue` |
| **Funções** | `def`, `return`, `lambda`, `*args`, `**kwargs`, `decorator` |
| **Classes** | `class`, `__init__`, `self`, `@property`, `@staticmethod`, `@classmethod` |
| **Arquivos** | `open()`, `with`, `read()`, `write()`, `pathlib`, `csv`, `json` |
| **Exceções** | `try/except/finally`, `raise`, `Exception`, `contextlib` |
| **Módulos** | `import`, `from`, `__name__`, `__main__`, `packages` |
| **Compreensões** | `[x for x in range(10)]`, `{k:v for k,v in dict}` |
| **Geradores** | `(x for x in range(10))`, `yield`, `yield from` |
| **Async** | `async def`, `await`, `asyncio.run()`, `gather()` |
| **Type Hints** | `def func(x: int) -> str:`, `List[str]`, `Optional[int]` |
| **Testes** | `pytest`, `assert`, `fixture`, `parametrize`, `mock` |
| **BD** | `sqlite3`, `SQLAlchemy`, `pymongo`, `redis` |
| **ML** | `sklearn`, `numpy`, `pandas`, `train_test_split` |

---

## 🎯 RECURSOS ADICIONAIS

- **Documentação Oficial:** https://docs.python.org/pt-br/3/
- **PEP 8 - Guia de Estilo:** https://peps.python.org/pep-0008/
- **PyPI - Python Package Index:** https://pypi.org/
- **Real Python:** https://realpython.com/
- **Python Crash Course:** https://ehmatthes.github.io/pcc/

---

**Este cheat sheet contém mais de 600 exemplos práticos cobrindo todos os aspectos da linguagem Python. Salve, compartilhe e use como referência diária!**