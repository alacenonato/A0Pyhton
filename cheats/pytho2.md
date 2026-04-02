Perfeito! Vou criar um **Cheat Sheet duplicado em conteúdo**, mantendo a organização mas adicionando muito mais exemplos, casos de uso, funções avançadas e tópicos importantes que não estavam no site original.

---

# 🐍 PYTHON 3 - CHEAT SHEET ULTRA COMPLETO
## *Mais de 300 exemplos práticos e referências*

---

## 📚 SUMÁRIO
1. [Fundamentos Básicos](#1-fundamentos-básicos)
2. [Estruturas de Dados](#2-estruturas-de-dados)
3. [Strings Avançado](#3-strings-avançado)
4. [Estruturas de Controle](#4-estruturas-de-controle)
5. [Funções e Escopos](#5-funções-e-escopos)
6. [Compreensões e Geradores](#6-compreensões-e-geradores)
7. [Programação Orientada a Objetos](#7-programação-orientada-a-objetos)
8. [Manipulação de Arquivos](#8-manipulação-de-arquivos)
9. [Tratamento de Exceções](#9-tratamento-de-exceções)
10. [Módulos e Pacotes](#10-módulos-e-pacotes)
11. [Biblioteca Padrão Essencial](#11-biblioteca-padrão-essencial)
12. [Data e Hora](#12-data-e-hora)
13. [Expressões Regulares](#13-expressões-regulares)
14. [Concorrência e Paralelismo](#14-concorrência-e-paralelismo)
15. [Programação Funcional](#15-programação-funcional)
16. [Type Hints Avançado](#16-type-hints-avançado)
17. [Manipulação de Dados](#17-manipulação-de-dados)
18. [JSON e APIs](#18-json-e-apis)
19. [Testes e Debugging](#19-testes-e-debugging)
20. [Boas Práticas e Performance](#20-boas-práticas-e-performance)

---

## 1. FUNDAMENTOS BÁSICOS

### 1.1 Tipos de Dados Completos

```python
# Numéricos
int_val = 42                    # Inteiro
float_val = 3.14159             # Ponto flutuante
complex_val = 3 + 4j            # Número complexo
from decimal import Decimal
decimal_val = Decimal('0.1')    # Decimal exato (para dinheiro)
from fractions import Fraction
frac_val = Fraction(1, 3)       # Fração exata

# Sequências
str_val = "Python"              # String
list_val = [1, 2, 3]            # Lista (mutável)
tuple_val = (1, 2, 3)           # Tupla (imutável)
range_val = range(10)           # Range

# Mapeamentos
dict_val = {"a": 1, "b": 2}     # Dicionário

# Conjuntos
set_val = {1, 2, 3}             # Set (mutável)
frozenset_val = frozenset([1, 2, 3])  # Frozenset (imutável)

# Booleanos
bool_true = True                # Verdadeiro
bool_false = False              # Falso

# Binários
bytes_val = b"hello"            # Bytes (imutável)
bytearray_val = bytearray(b"hello")  # Bytearray (mutável)
memoryview_val = memoryview(b"hello")  # Memoryview

# None
none_val = None                 # Representa ausência de valor
```

### 1.2 Operadores

```python
# Aritméticos
a, b = 10, 3
print(a + b)    # 13 - Soma
print(a - b)    # 7  - Subtração
print(a * b)    # 30 - Multiplicação
print(a / b)    # 3.33333 - Divisão float
print(a // b)   # 3  - Divisão inteira (floor)
print(a % b)    # 1  - Módulo (resto)
print(a ** b)   # 1000 - Potência

# Comparação
print(a == b)   # False - Igual
print(a != b)   # True  - Diferente
print(a > b)    # True  - Maior
print(a < b)    # False - Menor
print(a >= b)   # True  - Maior ou igual
print(a <= b)   # False - Menor ou igual

# Lógicos
x, y = True, False
print(x and y)  # False - AND
print(x or y)   # True  - OR
print(not x)    # False - NOT

# Identidade
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print(lista1 is lista2)   # False (objetos diferentes)
print(lista1 is lista3)   # True (mesmo objeto)
print(lista1 == lista2)   # True (conteúdo igual)

# Associação
frutas = ["maçã", "banana"]
print("maçã" in frutas)   # True
print("uva" not in frutas) # True

# Bitwise
p, q = 5, 3  # 0101, 0011
print(p & q)   # 1  - AND bitwise (0001)
print(p | q)   # 7  - OR bitwise (0111)
print(p ^ q)   # 6  - XOR bitwise (0110)
print(~p)      # -6 - NOT bitwise
print(p << 1)  # 10 - Deslocamento esquerda (1010)
print(p >> 1)  # 2  - Deslocamento direita (0010)

# Walrus Operator (Python 3.8+)
if (n := len([1, 2, 3])) > 2:
    print(f"Lista com {n} elementos")
```

### 1.3 Conversões Avançadas

```python
# Conversões numéricas
int("1010", 2)      # 10 (binário para int)
int("A", 16)        # 10 (hex para int)
int("12", 8)        # 10 (octal para int)
bin(10)             # '0b1010'
oct(10)             # '0o12'
hex(10)             # '0xa'

# Conversões com validação
def safe_int(valor, default=0):
    try:
        return int(valor)
    except (ValueError, TypeError):
        return default

# Conversão entre coleções
lista = [1, 2, 3]
tupla = tuple(lista)        # (1, 2, 3)
conjunto = set(lista)       # {1, 2, 3}
lista_nova = list(tupla)    # [1, 2, 3]
```

---

## 2. ESTRUTURAS DE DADOS

### 2.1 Listas - Todas as Operações

```python
# Criação
lista = [1, 2, 3]
lista_comp = [x for x in range(10)]
lista_repetida = [0] * 5          # [0, 0, 0, 0, 0]
lista_mista = [1, "dois", 3.0]

# Inserção
lista.append(4)                    # Adiciona no final
lista.insert(0, 0)                 # Insere na posição
lista.extend([5, 6])               # Estende com outra lista
lista += [7, 8]                    # Concatena

# Remoção
lista.pop()                        # Remove e retorna último
lista.pop(0)                       # Remove e retorna índice 0
lista.remove(3)                    # Remove primeira ocorrência
del lista[1:3]                     # Remove fatia
lista.clear()                      # Remove todos

# Acesso e busca
primeiro = lista[0]                # Primeiro elemento
ultimo = lista[-1]                 # Último elemento
indice = lista.index(3)            # Índice do valor 3
contagem = lista.count(2)          # Conta ocorrências

# Fatiamento (slicing) avançado
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[2:7])      # [2, 3, 4, 5, 6]
print(lista[:5])       # [0, 1, 2, 3, 4]
print(lista[5:])       # [5, 6, 7, 8, 9]
print(lista[::2])      # [0, 2, 4, 6, 8] - passo 2
print(lista[1::2])     # [1, 3, 5, 7, 9] - índices ímpares
print(lista[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reverso
print(lista[-3:-1])    # [7, 8] - índices negativos

# Ordenação
lista.sort()                       # Ordena in-place (crescente)
lista.sort(reverse=True)           # Ordena decrescente
lista.sort(key=lambda x: abs(x))   # Ordena por valor absoluto
nova_lista = sorted(lista)         # Retorna nova lista ordenada
nova_lista = sorted(lista, reverse=True)

# Outras operações
lista.reverse()                    # Inverte in-place
copia = lista.copy()               # Cópia rasa
copia_profunda = lista[:]          # Outra forma de cópia
len(lista)                         # Tamanho
max(lista), min(lista)             # Maior e menor
sum(lista)                         # Soma (para números)

# Empilhamento e desempilhamento (como pilha)
pilha = []
pilha.append(1)                    # Push
pilha.append(2)
topo = pilha.pop()                 # Pop -> 2

# Fila com lista (ineficiente, use deque)
fila = []
fila.append(1)                     # Enqueue
fila.append(2)
primeiro = fila.pop(0)             # Dequeue -> 1 (O(n))
```

### 2.2 Tuplas - Operações e Usos

```python
# Criação
tupla = (1, 2, 3)
tupla_sem_parenteses = 1, 2, 3
tupla_um_elemento = (1,)           # Vírgula necessária
tupla_vazia = ()

# Desempacotamento
a, b, c = (1, 2, 3)                # a=1, b=2, c=3
a, *resto = (1, 2, 3, 4)          # a=1, resto=[2,3,4]
*inicio, ultimo = (1, 2, 3, 4)    # inicio=[1,2,3], ultimo=4

# Métodos
tupla = (1, 2, 3, 2, 4)
print(tupla.count(2))              # 2
print(tupla.index(3))              # 2
print(tupla.index(2, 2))           # 3 (busca a partir do índice 2)

# Quando usar tuplas
# - Dados que não devem mudar (coordenadas, configurações)
# - Chaves de dicionário (listas não podem)
# - Retorno de múltiplos valores em funções
coordenadas = (10, 20)
dict_com_tupla = {(0,0): "origem", (1,2): "ponto"}

# Named Tuples
from collections import namedtuple
Ponto = namedtuple('Ponto', ['x', 'y'])
p = Ponto(10, 20)
print(p.x, p.y)                    # 10 20
print(p[0], p[1])                  # 10 20 (acesso por índice)
```

### 2.3 Dicionários - Tudo que Você Precisa

```python
# Criação
dict1 = {"a": 1, "b": 2}
dict2 = dict(a=1, b=2)
dict3 = dict([("a", 1), ("b", 2)])
dict4 = {k: v for k, v in zip(["a", "b"], [1, 2])}

# Acesso
valor = dict1["a"]                 # 1 (levanta KeyError se não existir)
valor = dict1.get("c", 0)          # 0 (valor padrão)
valor = dict1.setdefault("c", 3)   # Se não existe, insere e retorna 3

# Inserção e atualização
dict1["c"] = 3                     # Insere ou atualiza
dict1.update({"d": 4, "e": 5})     # Múltiplas atualizações
dict1.update(f=6)                  # Outra forma

# Remoção
valor = dict1.pop("a")             # Remove e retorna
valor = dict1.popitem()            # Remove e retorna último par
del dict1["b"]                     # Remove chave
dict1.clear()                      # Remove todos

# Visualizações (views)
chaves = dict1.keys()              # Vista de chaves
valores = dict1.values()           # Vista de valores
itens = dict1.items()              # Vista de pares (chave, valor)

# Iteração
for chave in dict1:                # Itera sobre chaves
    print(chave, dict1[chave])

for chave, valor in dict1.items(): # Itera sobre pares
    print(chave, valor)

# Dicionários aninhados
matriz = {
    "pessoa1": {"nome": "Ana", "idade": 30},
    "pessoa2": {"nome": "João", "idade": 25}
}
print(matriz["pessoa1"]["nome"])   # "Ana"

# DefaultDict (collections)
from collections import defaultdict
dd = defaultdict(int)              # Valor padrão 0
dd["a"] += 1                       # Funciona mesmo sem chave
dd = defaultdict(list)             # Valor padrão lista vazia
dd["chave"].append(1)

# OrderedDict (collections) - Mantém ordem de inserção
from collections import OrderedDict
od = OrderedDict([("a", 1), ("b", 2)])
od.move_to_end("a")                # Move chave para o final

# Counter (collections) - Contador
from collections import Counter
contador = Counter([1, 2, 2, 3, 3, 3])
print(contador)                    # Counter({3: 3, 2: 2, 1: 1})
print(contador.most_common(2))     # [(3, 3), (2, 2)]
```

### 2.4 Conjuntos (Sets) - Operações Completas

```python
# Criação
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])
set3 = set("hello")                # {'h', 'e', 'l', 'o'}

# Operações básicas
set1.add(5)                        # Adiciona elemento
set1.update([6, 7])                # Adiciona múltiplos
set1.remove(3)                     # Remove (KeyError se não existe)
set1.discard(10)                   # Remove sem erro
elemento = set1.pop()              # Remove e retorna elemento arbitrário
set1.clear()                       # Remove todos

# Operações de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)                       # União: {1,2,3,4,5,6}
print(A & B)                       # Interseção: {3,4}
print(A - B)                       # Diferença: {1,2}
print(B - A)                       # Diferença: {5,6}
print(A ^ B)                       # Diferença simétrica: {1,2,5,6}

# Métodos equivalentes
print(A.union(B))                  # União
print(A.intersection(B))           # Interseção
print(A.difference(B))             # Diferença
print(A.symmetric_difference(B))   # Diferença simétrica

# Verificações
print(A.issubset(B))               # A é subconjunto de B? False
print(A.issuperset(B))             # A é superconjunto de B? False
print(A.isdisjoint(B))             # Disjuntos? False

# Set comprehensions
quadrados = {x**2 for x in range(10)}  # {0,1,4,9,16,...}
pares = {x for x in range(10) if x % 2 == 0}  # {0,2,4,6,8}

# Frozenset (imutável)
fs = frozenset([1, 2, 3])
# fs.add(4)  # Erro! Frozenset não pode ser modificado
```

### 2.5 Deque (Fila Dupla) - Coleções Avançadas

```python
from collections import deque

# Criação
d = deque([1, 2, 3])
d = deque(maxlen=5)                # Limita tamanho máximo

# Operações
d.append(4)                        # Adiciona à direita
d.appendleft(0)                    # Adiciona à esquerda
d.extend([5, 6])                   # Estende à direita
d.extendleft([-2, -1])             # Estende à esquerda (ordem invertida)

direita = d.pop()                  # Remove e retorna da direita
esquerda = d.popleft()             # Remove e retorna da esquerda

# Rotações
d.rotate(2)                        # Rotaciona 2 passos para direita
d.rotate(-1)                       # Rotaciona 1 passo para esquerda

# Outros métodos
d.remove(3)                        # Remove primeira ocorrência
d.reverse()                        # Inverte a ordem
d.count(2)                         # Conta ocorrências
d.clear()                          # Limpa o deque

# Performance: O(1) para append/pop em ambos lados
# Útil para filas, pilhas, buffer circular
```

---

## 3. STRINGS AVANÇADO

### 3.1 Métodos de String - Completo

```python
s = "  Python Programming  "

# Case manipulation
print(s.upper())                   # "  PYTHON PROGRAMMING  "
print(s.lower())                   # "  python programming  "
print(s.title())                   # "  Python Programming  "
print(s.capitalize())              # "  python programming  "
print(s.swapcase())                # Inverte maiúsculas/minúsculas
print(s.casefold())                # Case folding (para comparações)

# Remoção de espaços
print(s.strip())                   # "Python Programming"
print(s.lstrip())                  # "Python Programming  "
print(s.rstrip())                  # "  Python Programming"
print(s.replace(" ", ""))          # "PythonProgramming"

# Busca e substituição
print(s.find("thon"))              # 6 (índice, -1 se não encontrado)
print(s.index("thon"))             # 6 (ValueError se não encontrado)
print(s.rfind("P"))                # 7 (busca da direita)
print(s.count("P"))                # 2
print(s.startswith("  "))          # True
print(s.endswith("  "))            # True

# Substituição
print(s.replace("Python", "Java")) # "  Java Programming  "
print(s.replace(" ", "_", 2))      # "__Python Programming  "

# Split e join
palavras = s.split()               # ['Python', 'Programming']
linhas = "a\nb\nc".splitlines()    # ['a', 'b', 'c']
print(" ".join(palavras))          # "Python Programming"

# Validação
print("abc123".isalnum())          # True (letras/números)
print("abc".isalpha())             # True (só letras)
print("123".isdigit())             # True (só dígitos)
print("123".isnumeric())           # True (inclui caracteres numéricos)
print("   ".isspace())             # True (só espaços)
print("Hello".istitle())           # True (formato título)
print("HELLO".isupper())           # True
print("hello".islower())           # True

# Formatação
print("Olá {:>10}".format("Mundo"))   # Alinha à direita
print("Olá {:<10}".format("Mundo"))   # Alinha à esquerda
print("Olá {:^10}".format("Mundo"))   # Centraliza
print("{:.2f}".format(3.14159))       # "3.14"
print("{:,}".format(1000000))         # "1,000,000"
print("{:_}".format(1000000))         # "1_000_000"
print("{:b}".format(10))              # "1010" (binário)
print("{:x}".format(255))             # "ff" (hexadecimal)

# F-strings (Python 3.6+)
nome, idade = "João", 25
print(f"{nome} tem {idade} anos")
print(f"{nome:>10}")                  # Alinhamento
print(f"{idade:05d}")                 # Preenchimento com zeros
print(f"{idade:b}")                   # Binário
print(f"{idade:o}")                   # Octal
print(f"{idade:x}")                   # Hexadecimal
print(f"{3.14159:.2f}")               # 3.14
print(f"{1000000:,}")                 # 1,000,000
print(f"{1000000:_}")                 # 1_000_000
print(f"{0.25:.0%}")                  # 25%

# Strings multilinha
multilinha = """Linha 1
Linha 2
Linha 3"""

# Raw strings (ignora escapes)
caminho = r"C:\Users\Nome\Documentos"

# Prefixos de string
b_string = b"bytes"                   # Bytes
f_string = f"formatado {nome}"        # Formatado
r_string = r"raw\string"              # Raw
u_string = u"unicode"                 # Unicode (padrão no Python 3)
```

### 3.2 Fatiamento Avançado de Strings

```python
s = "Python Programming"

# Fatiamento básico
print(s[0:6])        # "Python"
print(s[7:18])       # "Programming"
print(s[:6])         # "Python"
print(s[7:])         # "Programming"
print(s[:])          # Cópia completa

# Com passo
print(s[::2])        # "Pto rgamn" (índices pares)
print(s[1::2])       # "yhnPormig" (índices ímpares)
print(s[::-1])       # "gnimmargorP nohtyP" (inverso)

# Índices negativos
print(s[-11:-1])     # "Programmin"
print(s[-11:])       # "Programming"

# Combinando
print(s[7:18:2])     # "Pormg" (do índice 7 ao 18, passo 2)
print(s[18:7:-1])    # "gnimmargor" (reverso de 18 a 7)
```

### 3.3 Expressões Regulares (re) - Aprofundado

```python
import re

# Compilação de padrões
padrao = re.compile(r'\d+')
texto = "Idade: 25, CEP: 12345-678"

# Busca
print(padrao.search(texto))          # Match object
print(padrao.findall(texto))         # ['25', '12345', '678']
print(padrao.finditer(texto))        # Iterador de matches

# Substituição
novo = padrao.sub("NÚMERO", texto)   # "Idade: NÚMERO, CEP: NÚMERO-NÚMERO"
novo = padrao.subn("NÚMERO", texto)  # Retorna tupla (texto, qtde_subst)

# Splitting
print(re.split(r'\s+', "a b   c d")) # ['a', 'b', 'c', 'd']

# Flags
re.IGNORECASE     # Ignora maiúsculas/minúsculas
re.MULTILINE      # ^ e $ funcionam por linha
re.DOTALL         # . inclui quebra de linha
re.VERBOSE        # Permite espaços e comentários no padrão

# Exemplos práticos
# Email
email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# URL
url = r'^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*/?$'
# CPF
cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
# Telefone
telefone = r'^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$'
```

---

## 4. ESTRUTURAS DE CONTROLE

### 4.1 Condicionais Avançadas

```python
# if com múltiplas condições
idade = 25
renda = 3000
if idade >= 18 and renda >= 2000:
    print("Elegível para crédito")

# Operador ternário aninhado
status = "Maior" if idade >= 18 else "Menor"

# Verificação em uma linha
if x > 0: print("Positivo")

# Chaining comparisons (comparações encadeadas)
x = 5
if 1 < x < 10:      # Equivalente a: if 1 < x and x < 10
    print("Entre 1 e 10")

# Any e All
lista = [True, False, True]
if any(lista):      # True se algum é True
    print("Pelo menos um True")
if all(lista):      # True se todos são True
    print("Todos True")

# Match case (Python 3.10+) - pattern matching avançado
def processar(valor):
    match valor:
        case 0:
            return "Zero"
        case 1 | 2 | 3:          # Múltiplos valores
            return "Pequeno"
        case int(x) if x > 100:   # Com guard condition
            return f"Grande: {x}"
        case [a, b]:              # Desempacotamento de lista
            return f"Lista de 2: {a}, {b}"
        case {"nome": nome, "idade": idade}:  # Desempacotamento de dict
            return f"Nome: {nome}, Idade: {idade}"
        case _:                    # Caso padrão
            return "Outro"
```

### 4.2 Loops - Técnicas Avançadas

```python
# For com enumerate
for i, item in enumerate(["a", "b", "c"], start=1):
    print(f"{i}: {item}")

# For com zip (iterar múltiplas sequências)
nomes = ["Ana", "João", "Maria"]
idades = [25, 30, 28]
cidades = ["SP", "RJ", "BH"]
for nome, idade, cidade in zip(nomes, idades, cidades):
    print(f"{nome}, {idade} anos, {cidade}")

# For com zip_longest (collections)
from itertools import zip_longest
for a, b in zip_longest([1, 2], [3, 4, 5], fillvalue=0):
    print(a, b)  # (1,3), (2,4), (0,5)

# While com else
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Loop completo (sem break)")

# Loop com break e continue
for i in range(10):
    if i % 2 == 0:
        continue  # Pula números pares
    if i > 7:
        break     # Para no 9
    print(i)      # 1, 3, 5, 7

# Iterando sobre dicionários
d = {"a": 1, "b": 2, "c": 3}
for key, value in d.items():
    print(f"{key}: {value}")

# Iterando sobre múltiplos dicionários
from collections import ChainMap
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
for key, value in ChainMap(d1, d2).items():
    print(key, value)

# Loops com iteração reversa
for i in reversed(range(10)):
    print(i)  # 9,8,7,...

# List comprehension dentro de loops
resultados = []
for x in range(5):
    resultados.append([y**2 for y in range(x+1)])
```

### 4.3 Itertools - Ferramentas de Iteração

```python
import itertools

# Ciclos infinitos
contador = itertools.count(start=10, step=2)  # 10, 12, 14, ...
ciclo = itertools.cycle([1, 2, 3])            # 1, 2, 3, 1, 2, 3, ...
repetidor = itertools.repeat("A", times=3)    # "A", "A", "A"

# Combinações e permutações
itens = [1, 2, 3]
permutacoes = list(itertools.permutations(itens, 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

combinacoes = list(itertools.combinations(itens, 2))
# [(1,2), (1,3), (2,3)]

combinacoes_com_repeticao = list(itertools.combinations_with_replacement(itens, 2))
# [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]

produto_cartesiano = list(itertools.product([1,2], ['a','b']))
# [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

# Agrupamento
dados = [1, 1, 2, 2, 2, 3, 3]
for chave, grupo in itertools.groupby(dados):
    print(chave, list(grupo))
# 1 [1,1]
# 2 [2,2,2]
# 3 [3,3]

# Acumulação
import operator
soma_acumulada = list(itertools.accumulate([1,2,3,4], operator.add))  # [1,3,6,10]
multiplicacao = list(itertools.accumulate([1,2,3,4], operator.mul))    # [1,2,6,24]

# Filtragem
pares = list(itertools.filterfalse(lambda x: x%2, [1,2,3,4]))  # [2,4]
dropwhile = list(itertools.dropwhile(lambda x: x<3, [1,2,3,4]))  # [3,4]
takewhile = list(itertools.takewhile(lambda x: x<3, [1,2,3,4]))   # [1,2]

# Encadeamento
encadeado = list(itertools.chain([1,2], [3,4], [5,6]))  # [1,2,3,4,5,6]
```

---

## 5. FUNÇÕES E ESCOPOS

### 5.1 Definição e Parâmetros Avançados

```python
# Parâmetros posicionais e nomeados
def func(a, b, /, c, d, *, e, f):
    """/ → argumentos posicionais obrigatórios
       * → argumentos nomeados obrigatórios"""
    pass

# Exemplo prático
def configurar(host, port, /, *, debug=False, timeout=30):
    print(f"Host: {host}, Port: {port}, Debug: {debug}, Timeout: {timeout}")

configurar("localhost", 8080, debug=True)  # OK
# configurar(host="localhost", 8080)       # Erro! host deve ser posicional

# Parâmetros com valores padrão mutáveis (cuidado!)
def errado(lista=[]):      # Problema: lista é compartilhada entre chamadas
    lista.append(1)
    return lista

def certo(lista=None):     # Correto
    if lista is None:
        lista = []
    lista.append(1)
    return lista

# Funções aninhadas e closures
def multiplicador(fator):
    def multiplicar(x):
        return x * fator
    return multiplicar

dobro = multiplicador(2)
triplo = multiplicador(3)
print(dobro(5))   # 10
print(triplo(5))  # 15

# Funções com assinaturas dinâmicas
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes")
        resultado = func(*args, **kwargs)
        print("Depois")
        return resultado
    return wrapper

# Funções recursivas com memoization (cache)
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Funções com typing detalhado
from typing import Callable, Any

def aplicador(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# Funções com docstring detalhada
def minha_funcao(param1: str, param2: int = 0) -> bool:
    """
    Descrição da função.

    Args:
        param1: Descrição do primeiro parâmetro.
        param2: Descrição do segundo parâmetro (opcional).

    Returns:
        Descrição do retorno.

    Raises:
        ValueError: Se algo der errado.

    Examples:
        >>> minha_funcao("teste", 5)
        True
    """
    return True
```

### 5.2 Decoradores - Avançado

```python
import functools
import time

# Decorador básico
def cronometrar(func):
    @functools.wraps(func)  # Preserva metadados da função original
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} levou {fim - inicio:.2f}s")
        return resultado
    return wrapper

# Decorador com argumentos
def repetir(vezes=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            resultados = []
            for _ in range(vezes):
                resultados.append(func(*args, **kwargs))
            return resultados
        return wrapper
    return decorator

# Decorador de classe
def singleton(cls):
    instancias = {}
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]
    return wrapper

@singleton
class Config:
    pass

# Múltiplos decoradores
@cronometrar
@repetir(3)
def funcao_teste():
    time.sleep(0.1)
    return "OK"

# Decoradores em métodos
class MinhaClasse:
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()
    
    @staticmethod
    def metodo_estatico():
        pass
    
    @classmethod
    def metodo_classe(cls):
        pass
```

### 5.3 Escopo e Closures

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

# Nonlocal (modificar variáveis do escopo enclosing)
def contador():
    count = 0
    
    def incrementar():
        nonlocal count
        count += 1
        return count
    
    return incrementar

c = contador()
print(c())  # 1
print(c())  # 2

# Global
variavel_global = 10

def modificar_global():
    global variavel_global
    variavel_global = 20

# Funções como objetos de primeira classe
def saudacao(idioma):
    def pt():
        return "Olá!"
    
    def en():
        return "Hello!"
    
    if idioma == 'pt':
        return pt
    else:
        return en

saudar = saudacao('pt')
print(saudar())  # "Olá!"
```

---

## 6. COMPREENSÕES E GERADORES

### 6.1 Comprehensions - Todos os Tipos

```python
# List comprehensions - avançado
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Simples
quadrados = [x**2 for x in numeros]  # [1,4,9,16,25,36,49,64,81,100]

# Com condição
pares = [x for x in numeros if x % 2 == 0]  # [2,4,6,8,10]

# Com else (expressão ternária)
par_ou_impar = ["par" if x % 2 == 0 else "ímpar" for x in numeros]

# Com função
import math
raizes = [math.sqrt(x) for x in numeros if x > 0]

# Aninhada
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elementos = [elem for linha in matriz for elem in linha]  # [1,2,3,4,5,6,7,8,9]

# Com múltiplas condições
complexo = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]  # Múltiplos de 6

# Dict comprehensions
quadrados_dict = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# Filtrando dict
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
pares_dict = {k: v for k, v in d.items() if v % 2 == 0}  # {'b':2, 'd':4}

# Invertendo chave-valor
invertido = {v: k for k, v in d.items()}  # {1:'a', 2:'b', 3:'c', 4:'d'}

# Set comprehensions
quadrados_set = {x**2 for x in range(10)}  # {0,1,4,9,16,25,36,49,64,81}

# Tuple comprehensions? (na verdade é gerador)
tupla_compre = tuple(x**2 for x in range(5))  # (0,1,4,9,16)
```

### 6.2 Geradores e Yield

```python
# Gerador simples
def gerador_numeros(n):
    for i in range(n):
        yield i

gen = gerador_numeros(5)
print(next(gen))  # 0
print(next(gen))  # 1
print(list(gen))  # [2, 3, 4]

# Gerador infinito
def gerador_infinito():
    n = 0
    while True:
        yield n
        n += 1

# Gerador com send() e yield from
def corrotina():
    while True:
        valor = yield
        print(f"Recebido: {valor}")

def gerador_aninhado():
    yield from range(3)
    yield from "ABC"

print(list(gerador_aninhado()))  # [0,1,2,'A','B','C']

# Gerador com close() e throw()
def gen_com_erro():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("Gerador fechado")
    except ValueError:
        print("Erro tratado")

# Generator expressions (economia de memória)
soma_quadrados = sum(x**2 for x in range(1000000))  # Mais eficiente que lista

# Pipeline com geradores
def leitor(arquivo):
    for linha in arquivo:
        yield linha.strip()

def filtrador(linhas, palavra):
    for linha in linhas:
        if palavra in linha:
            yield linha

def contador(linhas):
    for linha in linhas:
        yield len(linha)

# Uso
with open('arquivo.txt') as f:
    linhas = leitor(f)
    filtradas = filtrador(linhas, 'erro')
    tamanhos = contador(filtradas)
    for tam in tamanhos:
        print(tam)

# Generators vs List Comprehension - Memória
import sys
lista = [x**2 for x in range(100000)]      # Ocupa memória
gerador = (x**2 for x in range(100000))    # Ocupa quase nada
print(sys.getsizeof(lista))    # ~800KB
print(sys.getsizeof(gerador))  # ~120 bytes
```

---

## 7. PROGRAMAÇÃO ORIENTADA A OBJETOS

### 7.1 Classes Avançadas

```python
class Pessoa:
    # Atributo de classe (compartilhado por todas instâncias)
    especie = "Homo sapiens"
    contador_instancias = 0
    
    def __init__(self, nome, idade):
        # Atributos de instância
        self.nome = nome
        self.idade = idade
        self._privado = "protegido"      # Convenção: privado
        self.__muito_privado = "privado" # Name mangling: _Pessoa__muito_privado
        Pessoa.contador_instancias += 1
    
    # Método de instância
    def saudacao(self):
        return f"Olá, sou {self.nome}"
    
    # Método de classe
    @classmethod
    def criar_anonimo(cls):
        return cls("Anônimo", 0)
    
    # Método estático
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
    # Property (getter)
    @property
    def idade(self):
        return self._idade
    
    # Setter
    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = valor
    
    # Deleter
    @idade.deleter
    def idade(self):
        del self._idade
    
    # Métodos especiais (dunder methods)
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
    
    def __add__(self, other):
        return Pessoa(f"{self.nome} & {other.nome}", 
                      max(self.idade, other.idade))
    
    def __call__(self):
        return f"Chamando {self.nome} como função"
    
    def __del__(self):
        Pessoa.contador_instancias -= 1

# Uso
p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 30)

print(p1)                     # João (25 anos)
print(repr(p1))               # Pessoa('João', 25)
print(len(p1))                # 4
print(p1 == p2)               # False
print(p1 < p2)                # True (25 < 30)
print(p1 + p2)                # João & Maria (30 anos)
print(p1())                   # Chamando João como função
```

### 7.2 Herança e Mixins

```python
# Herança simples
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        raise NotImplementedError("Subclasse deve implementar")
    
    def mover(self):
        return f"{self.nome} está se movendo"

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # Chama construtor da superclasse
        self.raca = raca
    
    def fazer_som(self):
        return "Au au!"
    
    def buscar(self):
        return f"{self.nome} está buscando a bola"

# Herança múltipla e Mixins
class NadadorMixin:
    def nadar(self):
        return f"{self.nome} está nadando"

class VoadorMixin:
    def voar(self):
        return f"{self.nome} está voando"

class Pato(Animal, NadadorMixin, VoadorMixin):
    def fazer_som(self):
        return "Quack!"

# MRO (Method Resolution Order)
print(Pato.__mro__)  # Mostra ordem de resolução

# Herança abstrata
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)

# Super() em herança múltipla
class Base:
    def __init__(self):
        print("Base.__init__")

class A(Base):
    def __init__(self):
        super().__init__()
        print("A.__init__")

class B(Base):
    def __init__(self):
        super().__init__()
        print("B.__init__")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C.__init__")

c = C()  # Base.__init__, B.__init__, A.__init__, C.__init__
```

### 7.3 Metaclasses e Programação Avançada

```python
# Metaclasse simples
class Meta(type):
    def __new__(mcs, nome, bases, dct):
        # Adiciona atributo automático
        dct['criado_por'] = 'Metaclasse'
        return super().__new__(mcs, nome, bases, dct)
    
    def __call__(cls, *args, **kwargs):
        print(f"Criando instância de {cls.__name__}")
        return super().__call__(*args, **kwargs)

class MinhaClasse(metaclass=Meta):
    pass

obj = MinhaClasse()  # "Criando instância de MinhaClasse"
print(obj.criado_por)  # "Metaclasse"

# Descritores (property, classmethod, staticmethod são descritores)
class Descritor:
    def __init__(self, nome):
        self.nome = nome
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.nome, None)
    
    def __set__(self, obj, valor):
        obj.__dict__[self.nome] = valor
    
    def __delete__(self, obj):
        del obj.__dict__[self.nome]

class Exemplo:
    atributo = Descritor("atributo")

# Slots (otimização de memória)
class Otimizado:
    __slots__ = ['nome', 'idade']  # Restringe atributos e economiza memória
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Comparação de memória
import sys
class Normal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

normal = Normal("João", 25)
otimizado = Otimizado("João", 25)
print(sys.getsizeof(normal))     # Maior
print(sys.getsizeof(otimizado))  # Menor
```

---

## 8. MANIPULAÇÃO DE ARQUIVOS

### 8.1 Operações Básicas e Avançadas

```python
import os
import shutil
from pathlib import Path
import tempfile

# Usando pathlib (recomendado)
p = Path('/caminho/para/arquivo.txt')
print(p.exists())          # Verifica existência
print(p.is_file())         # É arquivo?
print(p.is_dir())          # É diretório?
print(p.name)              # Nome do arquivo
print(p.stem)              # Nome sem extensão
print(p.suffix)            # Extensão
print(p.parent)            # Diretório pai
print(p.resolve())         # Caminho absoluto

# Criar diretórios
p = Path('pasta/subpasta')
p.mkdir(parents=True, exist_ok=True)  # Cria recursivamente

# Listar arquivos
for arquivo in Path('.').iterdir():
    print(arquivo)

for arquivo in Path('.').glob('*.txt'):
    print(arquivo)

for arquivo in Path('.').rglob('*.py'):  # Recursivo
    print(arquivo)

# Leitura e escrita avançada
# Modos: 'r' (leitura), 'w' (escrita, sobrescreve), 'a' (append)
#        'x' (cria, erro se existir), 'b' (binário), 't' (texto)
#        '+' (leitura e escrita)

# Escrita
with open('arquivo.txt', 'w', encoding='utf-8') as f:
    f.write('Linha 1\n')
    f.writelines(['Linha 2\n', 'Linha 3\n'])
    f.flush()  # Força escrita

# Leitura
with open('arquivo.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()                    # Tudo
    conteudo = f.read(100)                 # 100 caracteres
    linha = f.readline()                   # Uma linha
    linhas = f.readlines()                 # Todas linhas (lista)
    
    # Iterador eficiente
    for linha in f:
        processar(linha)

# Arquivos binários
with open('imagem.jpg', 'rb') as f:
    dados = f.read()

with open('copia.jpg', 'wb') as f:
    f.write(dados)

# Seek e tell
with open('arquivo.txt', 'r') as f:
    print(f.tell())  # Posição atual
    f.seek(10)       # Move para posição 10
    print(f.read(5))

# Arquivo temporário
with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
    tmp.write('Dados temporários')
    nome_tmp = tmp.name
    print(f"Arquivo temporário: {nome_tmp}")

# Diretório temporário
with tempfile.TemporaryDirectory() as tmpdir:
    arquivo = Path(tmpdir) / 'teste.txt'
    arquivo.write_text('Conteúdo')
    print(f"Arquivo em: {tmpdir}")

# Copiar, mover, deletar
import shutil

shutil.copy('origem.txt', 'destino.txt')      # Copia
shutil.move('origem.txt', 'pasta/destino.txt') # Move
shutil.rmtree('pasta')                         # Remove diretório com conteúdo
os.remove('arquivo.txt')                       # Remove arquivo
os.rmdir('pasta_vazia')                        # Remove diretório vazio

# Permissões
os.chmod('arquivo.txt', 0o755)                 # Altera permissões
```

### 8.2 Trabalhando com CSV e Excel

```python
import csv
import pandas as pd

# CSV com csv module
# Leitura
with open('dados.csv', 'r', encoding='utf-8') as f:
    leitor = csv.reader(f, delimiter=';')
    cabecalho = next(leitor)  # Primeira linha
    for linha in leitor:
        print(linha)

# Leitura como dicionário
with open('dados.csv', 'r', encoding='utf-8') as f:
    leitor = csv.DictReader(f, delimiter=';')
    for linha in leitor:
        print(linha['nome'], linha['idade'])

# Escrita
with open('saida.csv', 'w', encoding='utf-8', newline='') as f:
    escritor = csv.writer(f, delimiter=';')
    escritor.writerow(['nome', 'idade', 'cidade'])
    escritor.writerow(['João', 25, 'São Paulo'])
    escritor.writerows([
        ['Maria', 30, 'Rio'],
        ['Pedro', 28, 'Belo Horizonte']
    ])

# CSV com pandas (recomendado para análise)
df = pd.read_csv('dados.csv', sep=';')
print(df.head())  # Primeiras linhas
print(df.describe())  # Estatísticas

# Excel
# Instalar: pip install openpyxl xlrd
df.to_excel('saida.xlsx', index=False)
df_excel = pd.read_excel('dados.xlsx', sheet_name='Planilha1')
```

---

## 9. TRATAMENTO DE EXCEÇÕES

### 9.1 Estruturas Avançadas

```python
# Exceções aninhadas
try:
    try:
        arquivo = open('inexistente.txt')
    except FileNotFoundError:
        print("Arquivo não encontrado")
        raise  # Relança exceção
except Exception as e:
    print(f"Erro externo: {e}")
else:
    print("Arquivo aberto com sucesso")
finally:
    print("Sempre executa")

# Exceções customizadas
class MeuErro(Exception):
    """Exceção personalizada"""
    def __init__(self, mensagem, codigo=None):
        super().__init__(mensagem)
        self.codigo = codigo
    
    def __str__(self):
        return f"{self.args[0]} (Código: {self.codigo})" if self.codigo else self.args[0]

# Raise com from (encadeamento)
def funcao():
    try:
        raise ValueError("Erro original")
    except ValueError as e:
        raise RuntimeError("Erro processado") from e

# Contexto de exceção
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError("Divisão por zero") from None  # Suprime contexto

# Suppress (ignorar exceções específicas)
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('arquivo_inexistente.txt')  # Não levanta erro

# Finally com recursos
class Recurso:
    def __enter__(self):
        print("Abrindo recurso")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando recurso")
        if exc_type:
            print(f"Exceção tratada: {exc_val}")
        return True  # Suprime a exceção

with Recurso() as r:
    raise ValueError("Erro dentro do contexto")
print("Continua executando")  # Executa porque __exit__ retornou True

# Try-except-else-finally completo
def processar_arquivo(nome):
    try:
        f = open(nome)
    except OSError:
        print("Erro ao abrir arquivo")
        return
    else:
        print("Arquivo aberto")
        conteudo = f.read()
    finally:
        print("Fechando arquivo")
        f.close()
    return conteudo
```

---

## 10. MÓDULOS E PACOTES

### 10.1 Estrutura e Importação

```python
# Estrutura de pacote
"""
meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py
    subpacote/
        __init__.py
        modulo3.py
"""

# __init__.py pode conter código de inicialização
# __all__ = ['modulo1', 'modulo2']  # Controla from meu_pacote import *

# Importações relativas e absolutas
# No módulo: from . import subpacote      (relativa)
# from ..modulo1 import funcao            (relativa ao pai)
# from meu_pacote.modulo1 import funcao   (absoluta)

# Importação dinâmica
import importlib
modulo = importlib.import_module('math')
print(modulo.sqrt(16))  # 4.0

# Recarregar módulo
importlib.reload(modulo)

# Namespace packages (Python 3.3+)
# Diretórios sem __init__.py podem ser namespaces packages

# Módulos como scripts
if __name__ == "__main__":
    print("Executado diretamente")
    import sys
    print(sys.argv)  # Argumentos da linha de comando
```

### 10.2 Criando e Distribuindo Pacotes

```python
# setup.py (para distribuição)
"""
from setuptools import setup, find_packages

setup(
    name='meu_pacote',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.0',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'meu-comando=meu_pacote.cli:main',
        ],
    },
    author='Seu Nome',
    description='Descrição do pacote',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
"""

# pyproject.toml (moderno)
"""
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "meu_pacote"
version = "1.0.0"
dependencies = [
    "requests>=2.25.0",
    "numpy",
]
"""

# Instalar em modo desenvolvimento
# pip install -e .

# Publicar no PyPI
# python -m build
# twine upload dist/*
```

---

## 11. BIBLIOTECA PADRÃO ESSENCIAL

### 11.1 Módulos Fundamentais

```python
# os - Sistema operacional
import os
print(os.getcwd())           # Diretório atual
os.chdir('/tmp')             # Muda diretório
os.environ.get('PATH')       # Variáveis de ambiente
os.system('ls -l')           # Executa comando
print(os.cpu_count())        # Número de CPUs

# sys - Sistema e argumentos
import sys
print(sys.argv)              # Argumentos linha comando
print(sys.version)           # Versão Python
sys.exit(0)                  # Sai do programa
sys.path                     # Caminhos de busca de módulos

# math - Matemática
import math
math.pi, math.e              # Constantes
math.sqrt(16)                # Raiz quadrada
math.pow(2, 3)               # Potência
math.sin(math.radians(30))   # Seno
math.log(100, 10)            # Logaritmo base 10
math.factorial(5)            # Fatorial 120
math.gcd(12, 18)             # MDC 6
math.ceil(3.14)              # 4
math.floor(3.14)             # 3

# random - Números aleatórios
import random
random.random()              # Float entre 0 e 1
random.randint(1, 10)        # Inteiro entre 1 e 10
random.choice(['a','b','c']) # Escolhe um item
random.sample(range(100), 5) # Amostra sem repetição
random.shuffle(lista)        # Embaralha in-place

# datetime - Data e hora
from datetime import datetime, timedelta
datetime.now()               # Data/hora atual
datetime.today()             # Data/hora atual (sem timezone)
datetime.now().strftime('%Y-%m-%d')  # Formatação
datetime.strptime('2024-01-01', '%Y-%m-%d')  # Parsing

# time - Tempo
import time
time.time()                  # Timestamp atual
time.sleep(1)                # Pausa por 1 segundo
time.perf_counter()          # Timer de alta precisão

# json - JavaScript Object Notation
import json
data = {'nome': 'João', 'idade': 30}
json_str = json.dumps(data)   # Para string
json.dump(data, file)         # Para arquivo
data_back = json.loads(json_str)  # De string
data_back = json.load(file)       # De arquivo

# pickle - Serialização Python
import pickle
data = {'lista': [1,2,3], 'string': 'teste'}
pickle.dump(data, open('data.pkl', 'wb'))
data_back = pickle.load(open('data.pkl', 'rb'))
```

### 11.2 Collections - Estruturas Especializadas

```python
from collections import (
    namedtuple, deque, Counter, OrderedDict, 
    defaultdict, ChainMap, UserDict, UserList
)

# namedtuple - Tupla com campos nomeados
Ponto = namedtuple('Ponto', ['x', 'y', 'z'])
p = Ponto(1, 2, 3)
print(p.x, p.y, p.z)          # Acesso por nome
print(p[0], p[1], p[2])       # Acesso por índice

# deque - Fila dupla (já visto)

# Counter - Contador
c = Counter('abracadabra')
print(c)                      # Counter({'a':5, 'b':2, 'r':2, 'c':1, 'd':1})
c.update('aaa')               # Adiciona contagens
c.most_common(2)              # [('a', 8), ('b', 2)]

# OrderedDict - Dict com ordem (Python 3.7+ dict mantém ordem)
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od.move_to_end('a')           # Move 'a' para o final
od.popitem(last=False)        # Remove primeiro

# defaultdict - Dict com valor padrão
dd = defaultdict(list)
dd['chave'].append(1)         # Não precisa verificar existência

# ChainMap - Múltiplos dicionários como um
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print(chain['b'])             # 2 (primeiro encontrado)
print(chain['c'])             # 4

# UserDict, UserList - Para criar subclasses personalizadas
class MeuDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value.upper())
```

### 11.3 Functools - Funções de Alta Ordem

```python
import functools

# lru_cache - Cache de resultados
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# partial - Fixa argumentos
def potencia(base, exp):
    return base ** exp

quadrado = functools.partial(potencia, exp=2)
cubo = functools.partial(potencia, exp=3)
print(quadrado(5))  # 25

# reduce - Acumula valores
from functools import reduce
numeros = [1, 2, 3, 4]
soma = reduce(lambda x, y: x + y, numeros)  # 10
produto = reduce(lambda x, y: x * y, numeros)  # 24

# wraps - Preserva metadados em decoradores
def meu_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

# singledispatch - Sobrecarga de funções
from functools import singledispatch

@singledispatch
def processar(arg):
    return f"Default: {arg}"

@processar.register(int)
def _(arg):
    return f"Inteiro: {arg}"

@processar.register(list)
def _(arg):
    return f"Lista com {len(arg)} itens"

print(processar(10))      # Inteiro: 10
print(processar([1,2]))   # Lista com 2 itens
print(processar("texto")) # Default: texto

# total_ordering - Implementa operadores automaticamente
@functools.total_ordering
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __eq__(self, other):
        return self.idade == other.idade
    
    def __lt__(self, other):
        return self.idade < other.idade
    # >, >=, <=, != são automaticamente implementados

# cmp_to_key - Converte função de comparação para key
def comparar(a, b):
    return (a > b) - (a < b)

lista = [3, 1, 4, 1, 5, 9]
lista.sort(key=functools.cmp_to_key(comparar))
```

---

## 12. DATA E HORA

### 12.1 datetime Completo

```python
from datetime import datetime, date, time, timedelta, timezone
import pytz  # pip install pytz (para timezones)

# Criando objetos
hoje = date.today()                    # 2024-01-15
agora = datetime.now()                 # 2024-01-15 14:30:45.123456
utc_agora = datetime.now(timezone.utc) # Com timezone

# Componentes
print(agora.year, agora.month, agora.day)
print(agora.hour, agora.minute, agora.second, agora.microsecond)
print(agora.weekday())                 # 0=segunda, 6=domingo
print(agora.isoweekday())              # 1=segunda, 7=domingo

# Diferenças (timedelta)
delta = timedelta(days=5, hours=3, minutes=30)
amanha = hoje + timedelta(days=1)
semana_passada = hoje - timedelta(weeks=1)
diferenca = agora - utc_agora
print(diferenca.total_seconds())       # Diferença em segundos

# Formatação
formatado = agora.strftime("%d/%m/%Y %H:%M:%S")
print(formatado)  # 15/01/2024 14:30:45

# Parsing
data_str = "2024-12-25 15:30:00"
data_obj = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")

# Diretivas de formatação
"""
%d - Dia (01-31)
%m - Mês (01-12)
%Y - Ano com 4 dígitos
%y - Ano com 2 dígitos
%H - Hora (00-23)
%I - Hora (01-12)
%M - Minuto (00-59)
%S - Segundo (00-59)
%f - Microssegundo (000000-999999)
%p - AM/PM
%a - Dia da semana abreviado
%A - Dia da semana completo
%b - Mês abreviado
%B - Mês completo
%w - Dia da semana (0-6, domingo=0)
%W - Número da semana
"""

# Timezones com pytz
tz_sp = pytz.timezone('America/Sao_Paulo')
data_sp = datetime.now(tz_sp)
print(data_sp)

# Convertendo timezone
data_utc = datetime.now(timezone.utc)
data_sp = data_utc.astimezone(pytz.timezone('America/Sao_Paulo'))

# ISO 8601
iso_string = agora.isoformat()
data_iso = datetime.fromisoformat(iso_string)

# Timestamps
timestamp = agora.timestamp()
data_from_ts = datetime.fromtimestamp(timestamp)

# Dateutil (biblioteca mais flexível)
from dateutil import parser
data_parse = parser.parse("15 de janeiro de 2024 às 14:30")
from dateutil.relativedelta import relativedelta
proximo_mes = hoje + relativedelta(months=+1)
```

---

## 13. EXPRESSÕES REGULARES

### 13.1 re Module - Completo

```python
import re

# Padrões comuns
padroes = {
    'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    'url': r'^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*/?$',
    'cpf': r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    'cnpj': r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
    'telefone': r'^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$',
    'cep': r'^\d{5}-?\d{3}$',
    'placa_carro': r'^[A-Z]{3}-\d{4}$',
    'ipv4': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
}

# Flags
re.IGNORECASE    # Ignora maiúsculas/minúsculas
re.MULTILINE     # ^ e $ funcionam por linha
re.DOTALL        # . inclui quebra de linha
re.VERBOSE       # Permite comentários e espaços no padrão

# Exemplo com VERBOSE
padrao = re.compile(r"""
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

# Match com grupos
match = padrao.match("usuario@exemplo.com")
if match:
    print(match.group('usuario'))  # usuario
    print(match.group('dominio'))  # exemplo.com
    print(match.groups())          # ('usuario', 'exemplo.com')

# Substitution com função
def substituir(match):
    return match.group(0).upper()

texto = "abc123def456"
resultado = re.sub(r'\d+', substituir, texto)  # abcDEFdef

# Lookahead e lookbehind
# (?=...) - Lookahead positivo
# (?!...) - Lookahead negativo
# (?<=...) - Lookbehind positivo
# (?<!...) - Lookbehind negativo

# Exemplo: encontrar números seguidos de "px"
texto = "10px 20em 30px 40rem"
numeros_px = re.findall(r'\d+(?=px)', texto)  # ['10', '30']

# Exemplo: encontrar números não seguidos de "px"
numeros_sem_px = re.findall(r'\d+(?!px)', texto)  # ['20', '40']

# Exemplo: encontrar números precedidos de "width:"
texto = "width: 100px; height: 200px;"
larguras = re.findall(r'(?<=width: )\d+', texto)  # ['100']

# Exemplo: encontrar números não precedidos de "height:"
alturas = re.findall(r'(?<!height: )\d+', texto)  # ['100', '200']

# Escaping de caracteres especiais
texto = "O preço é $100.00"
re.escape(texto)  # Escapa caracteres especiais para usar em padrão

# Compilação de padrões (melhor performance para reuso)
padrao = re.compile(r'\d+')
padrao.findall(texto)
```

---

## 14. CONCORRÊNCIA E PARALELISMO

### 14.1 Threading (I/O-bound)

```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Thread simples
def trabalhador(nome, segundos):
    print(f"Thread {nome}: iniciando")
    time.sleep(segundos)
    print(f"Thread {nome}: finalizando")
    return f"Resultado {nome}"

thread = threading.Thread(target=trabalhador, args=("A", 2))
thread.start()
thread.join()  # Aguarda terminar

# Thread com classe
class MinhaThread(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
    
    def run(self):
        print(f"Executando {self.nome}")

# ThreadPoolExecutor (recomendado)
with ThreadPoolExecutor(max_workers=4) as executor:
    # Submeter única tarefa
    future = executor.submit(trabalhador, "A", 2)
    resultado = future.result()
    
    # Submeter múltiplas tarefas
    nomes = ["A", "B", "C"]
    resultados = executor.map(trabalhador, nomes, [2, 1, 3])
    for r in resultados:
        print(r)

# Sincronização
lock = threading.Lock()
contador = 0

def incrementar():
    global contador
    with lock:  # Bloqueio automático
        local = contador
        time.sleep(0.001)
        contador = local + 1

# Eventos
evento = threading.Event()

def esperar_evento():
    print("Aguardando evento")
    evento.wait()
    print("Evento recebido")

# Semáforo
semaphore = threading.Semaphore(3)  # Permite 3 threads simultâneas

# Queue para comunicação entre threads
from queue import Queue

fila = Queue()
def produtor():
    for i in range(10):
        fila.put(i)
        time.sleep(0.1)

def consumidor():
    while True:
        item = fila.get()
        if item is None:
            break
        print(f"Processando {item}")
        fila.task_done()
```

### 14.2 Multiprocessing (CPU-bound)

```python
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

# Processo simples
def processar_dados(dados):
    return sum(dados)

if __name__ == "__main__":
    # ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=4) as executor:
        dados = [range(1000000) for _ in range(4)]
        resultados = executor.map(processar_dados, dados)
        print(list(resultados))
    
    # Queue para processos
    queue = multiprocessing.Queue()
    
    def worker():
        queue.put("Resultado")
    
    p = multiprocessing.Process(target=worker)
    p.start()
    print(queue.get())
    p.join()

    # Pool de processos
    with multiprocessing.Pool(processes=4) as pool:
        resultado = pool.map(processar_dados, dados)
        resultado_assincrono = pool.apply_async(processar_dados, (range(1000),))
        print(resultado_assincrono.get())
```

### 14.3 Asyncio (I/O assíncrono)

```python
import asyncio
import aiohttp  # pip install aiohttp

# Função assíncrona básica
async def tarefa(nome, segundos):
    print(f"{nome}: iniciando")
    await asyncio.sleep(segundos)  # Operação não-bloqueante
    print(f"{nome}: finalizando")
    return f"Resultado {nome}"

# Executar múltiplas tarefas
async def main():
    # Executar sequencial
    resultado = await tarefa("A", 2)
    
    # Executar concorrentemente
    resultados = await asyncio.gather(
        tarefa("A", 2),
        tarefa("B", 1),
        tarefa("C", 3)
    )
    print(resultados)
    
    # Timeout
    try:
        resultado = await asyncio.wait_for(tarefa("D", 5), timeout=2)
    except asyncio.TimeoutError:
        print("Timeout!")
    
    # Tasks
    task = asyncio.create_task(tarefa("E", 1))
    resultado = await task

# Executar
asyncio.run(main())

# HTTP requests assíncronos
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiplas():
    async with aiohttp.ClientSession() as session:
        urls = ['http://exemplo.com' for _ in range(10)]
        tasks = [fetch_url(session, url) for url in urls]
        resultados = await asyncio.gather(*tasks)
        return resultados

# Streams assíncronos
async def processar_stream():
    reader, writer = await asyncio.open_connection('localhost', 8888)
    writer.write(b'Hello')
    await writer.drain()
    data = await reader.read(100)
    writer.close()
    await writer.wait_closed()

# Sincronização com asyncio
lock = asyncio.Lock()
async def tarefa_com_lock():
    async with lock:
        # Código crítico
        await asyncio.sleep(1)

# Queue assíncrona
fila = asyncio.Queue()
```

---

## 15. PROGRAMAÇÃO FUNCIONAL

```python
from functools import reduce
import operator

# Map - Aplica função a todos elementos
numeros = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, numeros))  # [2,4,6,8,10]

# Filter - Filtra elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2,4]

# Reduce - Reduz a um valor
soma = reduce(operator.add, numeros)  # 15
produto = reduce(operator.mul, numeros)  # 120

# Zip - Combina iteráveis
nomes = ["Ana", "João", "Maria"]
idades = [25, 30, 28]
pessoas = list(zip(nomes, idades))  # [('Ana',25), ('João',30), ('Maria',28)]

# Zip com desempacotamento
nomes, idades = zip(*pessoas)  # Volta para tuplas

# Enumerate - Índices
for i, valor in enumerate(numeros):
    print(f"{i}: {valor}")

# Sorted - Ordenação funcional
sorted(numeros, reverse=True)
sorted(pessoas, key=lambda x: x[1])  # Ordena por idade

# Any, All - Condições
qualquer_par = any(x % 2 == 0 for x in numeros)  # True
todos_pares = all(x % 2 == 0 for x in numeros)   # False

# Funções de ordem superior
def aplicar(func, valores):
    return [func(x) for x in valores]

print(aplicar(lambda x: x**2, [1,2,3]))  # [1,4,9]

# Composição de funções
def compor(*funcoes):
    def aplicador(x):
        for f in funcoes:
            x = f(x)
        return x
    return aplicador

dobro = lambda x: x * 2
mais_um = lambda x: x + 1
quadrado = lambda x: x ** 2

func_combinada = compor(dobro, mais_um, quadrado)
print(func_combinada(3))  # ((3*2)+1)^2 = 49

# Curry (parcial aplicação)
from functools import partial

def soma(a, b, c):
    return a + b + c

soma_10 = partial(soma, 10)  # Fixa primeiro argumento
soma_10_20 = partial(soma_10, 20)  # Fixa segundo
print(soma_10_20(30))  # 60
```

---

## 16. TYPE HINTS AVANÇADO

```python
from typing import (
    List, Dict, Tuple, Set, Optional, Union, Any, 
    Callable, TypeVar, Generic, Protocol, Final,
    Literal, TypedDict, cast, overload
)
from typing_extensions import TypedDict  # Python < 3.8

# Tipos básicos
nome: str = "João"
idade: int = 25
altura: float = 1.75
ativo: bool = True
dados: Any = "qualquer coisa"

# Coleções
lista_nomes: List[str] = ["Ana", "João"]
dict_idades: Dict[str, int] = {"Ana": 25, "João": 30}
tupla_coords: Tuple[float, float] = (10.5, 20.3)
conjunto: Set[int] = {1, 2, 3}
opcional: Optional[int] = None  # int ou None
union: Union[int, str] = "pode ser int ou str"

# Python 3.10+ permite sintaxe mais simples
lista: list[str] = ["a", "b", "c"]
dict: dict[str, int] = {"a": 1}
opcional: int | None = None
union: int | str = "teste"

# Funções
def processar(dados: List[int]) -> Dict[str, float]:
    return {"media": sum(dados) / len(dados)}

def callback(func: Callable[[int, int], int]) -> int:
    return func(5, 3)

def args_kwargs(*args: int, **kwargs: str) -> None:
    pass

# Generics
T = TypeVar('T')
U = TypeVar('U', int, float)  # Restrito

class Pilha(Generic[T]):
    def __init__(self) -> None:
        self._itens: List[T] = []
    
    def push(self, item: T) -> None:
        self._itens.append(item)
    
    def pop(self) -> T:
        return self._itens.pop()

def primeira(seq: List[T]) -> T:
    return seq[0]

# Protocol (duck typing estático)
class Nomeavel(Protocol):
    nome: str

class Pessoa:
    nome: str
    idade: int

def saudar(obj: Nomeavel) -> str:
    return f"Olá, {obj.nome}"

# Literal (valores específicos)
from typing import Literal

def set_modo(modo: Literal['read', 'write', 'append']) -> None:
    pass

set_modo('read')   # OK
# set_modo('delete') # Erro de tipo

# TypedDict (dicionário com formato específico)
class PessoaDict(TypedDict):
    nome: str
    idade: int
    email: Optional[str]

pessoa: PessoaDict = {"nome": "João", "idade": 25, "email": None}

# Final (constante)
from typing import Final

MAX_SIZE: Final = 100
# MAX_SIZE = 200  # Erro de tipo

# Overload (múltiplas assinaturas)
from typing import overload

@overload
def duplicar(valor: int) -> int: ...
@overload
def duplicar(valor: str) -> str: ...

def duplicar(valor):
    return valor * 2

# Cast (forçar tipo)
from typing import cast

valor = cast(str, algum_objeto)  # Força interpretação como str

# Type aliases
Coordenadas = Tuple[float, float, float]
Ponto3D = Tuple[float, float, float]

# Type checkers: mypy, pyright
# pip install mypy
# mypy arquivo.py
```

---

## 17. MANIPULAÇÃO DE DADOS

### 17.1 Pandas - DataFrames

```python
import pandas as pd
import numpy as np

# Criar DataFrame
df = pd.DataFrame({
    'nome': ['Ana', 'João', 'Maria', 'Pedro'],
    'idade': [25, 30, 28, 35],
    'cidade': ['SP', 'RJ', 'BH', 'SP'],
    'salario': [5000, 6000, 5500, 7000]
})

# Visualização
print(df.head())          # Primeiras 5 linhas
print(df.tail(3))         # Últimas 3 linhas
print(df.info())          # Informações do DataFrame
print(df.describe())      # Estatísticas descritivas
print(df.shape)           # Dimensões (linhas, colunas)

# Seleção
print(df['nome'])                        # Coluna
print(df[['nome', 'idade']])             # Múltiplas colunas
print(df.iloc[0])                        # Linha por posição
print(df.loc[0])                         # Linha por índice
print(df.iloc[0:2, 0:2])                 # Fatiamento

# Filtro
jovens = df[df['idade'] < 30]
sp = df[df['cidade'] == 'SP']
filtro = df[(df['idade'] > 25) & (df['salario'] > 6000)]

# Agregações
media_idade = df['idade'].mean()
salario_max = df['salario'].max()
agrupado = df.groupby('cidade')['salario'].mean()

# Transformações
df['idade_dobro'] = df['idade'] * 2
df['maior_idade'] = df['idade'] > 18

# Ordenação
df_sorted = df.sort_values('idade', ascending=False)

# Operações com NaN
df_clean = df.dropna()           # Remove NaN
df_filled = df.fillna(0)         # Preenche NaN

# Arquivos
df.to_csv('dados.csv', index=False)
df.to_excel('dados.xlsx', index=False)
df.to_json('dados.json')

df_csv = pd.read_csv('dados.csv')
df_excel = pd.read_excel('dados.xlsx', sheet_name='Planilha1')
df_json = pd.read_json('dados.json')
```

### 17.2 NumPy - Arrays Numéricos

```python
import numpy as np

# Criar arrays
arr = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))
eye = np.eye(3)  # Matriz identidade
range_arr = np.arange(0, 10, 2)  # [0,2,4,6,8]
linspace = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]
random = np.random.rand(3, 3)    # Números aleatórios

# Operações
print(arr + 10)           # Adição
print(arr * 2)            # Multiplicação
print(arr ** 2)           # Potência
print(np.sqrt(arr))       # Raiz quadrada
print(np.exp(arr))        # Exponencial
print(np.sin(arr))        # Seno

# Estatísticas
print(arr.mean())         # Média
print(arr.std())          # Desvio padrão
print(arr.sum())          # Soma
print(arr.min())          # Mínimo
print(arr.max())          # Máximo

# Indexação e fatiamento
print(arr[2])             # Terceiro elemento
print(arr[1:4])           # Fatiamento
print(arr[arr > 2])       # Filtro booleano

# Operações matriciais
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)              # Multiplicação matricial
print(A.dot(B))           # Mesmo que acima
print(A.T)                # Transposta
print(np.linalg.inv(A))   # Inversa
print(np.linalg.det(A))   # Determinante

# Broadcasting
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20, 30])
print(A + B)  # [[11,22,33], [14,25,36]]
```

---

## 18. JSON E APIs

```python
import json
import requests
from pathlib import Path

# JSON básico
data = {
    "nome": "João",
    "idade": 30,
    "cidades": ["São Paulo", "Rio"],
    "endereco": {
        "rua": "Av. Paulista",
        "numero": 1000
    }
}

# Serialização
json_str = json.dumps(data, indent=2, ensure_ascii=False)
json.dump(data, open('dados.json', 'w', encoding='utf-8'), indent=2)

# Deserialização
data_back = json.loads(json_str)
data_back = json.load(open('dados.json', 'r', encoding='utf-8'))

# JSON com tipos personalizados
from datetime import datetime

def json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Tipo {type(obj)} não serializável")

json_str = json.dumps({"data": datetime.now()}, default=json_serializer)

# Classe customizada com JSON
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def to_json(self):
        return {"nome": self.nome, "idade": self.idade}
    
    @classmethod
    def from_json(cls, data):
        return cls(data['nome'], data['idade'])

# API Requests
response = requests.get('https://api.exemplo.com/dados')
print(response.status_code)      # 200
print(response.headers)          # Cabeçalhos
print(response.json())           # JSON para dict

# POST
dados = {"nome": "João", "idade": 30}
response = requests.post(
    'https://api.exemplo.com/usuarios',
    json=dados,
    headers={'Authorization': 'Bearer token'}
)

# Parâmetros
params = {'q': 'python', 'page': 1}
response = requests.get('https://api.exemplo.com/search', params=params)

# Autenticação
response = requests.get('https://api.exemplo.com', auth=('user', 'pass'))

# Timeout e tratamento
try:
    response = requests.get('https://api.exemplo.com', timeout=5)
    response.raise_for_status()  # Levanta exceção para códigos de erro
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")

# Sessão (reutiliza conexão)
session = requests.Session()
session.headers.update({'User-Agent': 'MeuApp/1.0'})
response = session.get('https://api.exemplo.com')
```

---

## 19. TESTES E DEBUGGING

### 19.1 Unittest

```python
import unittest
from unittest.mock import Mock, patch

class TestMinhaFuncao(unittest.TestCase):
    def setUp(self):
        """Executa antes de cada teste"""
        self.dados = [1, 2, 3]
    
    def tearDown(self):
        """Executa após cada teste"""
        pass
    
    def test_soma(self):
        self.assertEqual(2 + 2, 4)
        self.assertNotEqual(2 + 2, 5)
    
    def test_lista(self):
        self.assertIn(2, self.dados)
        self.assertIsInstance(self.dados, list)
    
    def test_excecao(self):
        with self.assertRaises(ZeroDivisionError):
            x = 1 / 0
    
    def test_mock(self):
        # Criar mock
        mock_obj = Mock()
        mock_obj.metodo.return_value = 42
        self.assertEqual(mock_obj.metodo(), 42)
        
        # Verificar chamada
        mock_obj.metodo(1, 2)
        mock_obj.metodo.assert_called_with(1, 2)
    
    @patch('requests.get')
    def test_com_patch(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"ok": True}
        
        # Código que usa requests.get
        resultado = meu_codigo()
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()
```

### 19.2 Pytest (Recomendado)

```python
import pytest

# Teste simples
def test_soma():
    assert 2 + 2 == 4

# Fixture
@pytest.fixture
def dados():
    return [1, 2, 3]

def test_lista(dados):
    assert len(dados) == 3
    assert 2 in dados

# Parâmetros
@pytest.mark.parametrize("a,b,esperado", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
])
def test_soma_parametrizada(a, b, esperado):
    assert a + b == esperado

# Exceções
def test_excecao():
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0

# Skip
@pytest.mark.skip(reason="Ainda não implementado")
def test_nao_implementado():
    pass

# Mock com pytest-mock
def test_mock(mocker):
    mock = mocker.patch('requests.get')
    mock.return_value.status_code = 200
    # Código que usa requests.get
    assert resultado.status_code == 200

# Executar: pytest arquivo.py -v
```

### 19.3 Debugging

```python
import pdb
import logging

# PDB (Python Debugger)
def funcao_complexa(a, b):
    pdb.set_trace()  # Ponto de parada
    resultado = a + b
    return resultado

# Comandos PDB:
# n (next) - Próxima linha
# s (step) - Entra em função
# c (continue) - Continua até próximo breakpoint
# p var - Imprime variável
# q (quit) - Sai
# l (list) - Mostra código
# b linha - Adiciona breakpoint

# Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.debug("Mensagem de debug")
logger.info("Informação")
logger.warning("Aviso")
logger.error("Erro")
logger.critical("Crítico")

# Logging em módulos
def minha_funcao():
    logger.debug("Entrando na função")
    try:
        resultado = 10 / 0
    except Exception as e:
        logger.exception("Erro na função")
        raise
    return resultado

# Assertions
def dividir(a, b):
    assert b != 0, "Divisor não pode ser zero"
    return a / b
```

---

## 20. BOAS PRÁTICAS E PERFORMANCE

### 20.1 Performance e Otimização

```python
import timeit
import cProfile
import pstats
from functools import lru_cache

# Medir tempo
def medir_tempo():
    inicio = timeit.default_timer()
    # Código
    fim = timeit.default_timer()
    print(f"Tempo: {fim - inicio:.4f}s")

# timeit module
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Média: {tempo/10000:.6f}s")

# Profile
def funcao_para_perfil():
    resultado = []
    for i in range(1000):
        resultado.append(i ** 2)
    return resultado

# cProfile
cProfile.run('funcao_para_perfil()', 'stats.prof')
p = pstats.Stats('stats.prof')
p.sort_stats('cumulative').print_stats(10)

# Dicas de performance
# 1. Usar compreensões em vez de loops
# Ruim
soma = 0
for i in range(1000):
    soma += i ** 2

# Bom
soma = sum(i ** 2 for i in range(1000))

# 2. Usar built-in functions
# Ruim
max_val = 0
for x in lista:
    if x > max_val:
        max_val = x

# Bom
max_val = max(lista)

# 3. Evitar concatenação de strings em loops
# Ruim
resultado = ""
for s in strings:
    resultado += s

# Bom
resultado = "".join(strings)

# 4. Usar generators para grandes volumes
# Ruim
grande_lista = [processar(x) for x in range(1000000)]

# Bom
grande_gen = (processar(x) for x in range(1000000))

# 5. Cache de resultados
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 6. Usar array.array para grandes listas numéricas
import array
arr = array.array('i', range(1000000))

# 7. Evitar atributos desnecessários em classes
class Otimizado:
    __slots__ = ['nome', 'idade']  # Economiza memória
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

### 20.2 Estilo e Formatação (PEP 8)

```python
# Nomes
variavel_publica = "snake_case"
_privado = "underscore"
CONSTANTE = "UPPERCASE"
ClasseExemplo = "CamelCase"
funcao_exemplo = "snake_case"

# Docstrings
def minha_funcao(param1: str, param2: int) -> bool:
    """
    Descrição resumida.

    Descrição detalhada da função e seu comportamento.

    Args:
        param1: Descrição do primeiro parâmetro
        param2: Descrição do segundo parâmetro

    Returns:
        Descrição do retorno

    Raises:
        ValueError: Se algo der errado

    Examples:
        >>> minha_funcao("teste", 5)
        True
    """
    return True

# Imports (organizados)
# 1. Biblioteca padrão
import os
import sys
from datetime import datetime

# 2. Bibliotecas de terceiros
import numpy as np
import pandas as pd

# 3. Módulos locais
from meu_modulo import minha_funcao

# Line length (máximo 79 caracteres)
# Ruim
resultado = uma_funcao_com_nome_muito_longo(argumento1, argumento2, argumento3, argumento4, argumento5)

# Bom
resultado = uma_funcao_com_nome_muito_longo(
    argumento1, argumento2, argumento3,
    argumento4, argumento5
)

# Espaçamento
# Após vírgula
lista = [1, 2, 3, 4]

# Operadores
x = (y + z) * (a - b)  # Espaços ao redor de operadores

# Comentários
# Comentário de linha
"""Comentário de bloco
múltiplas linhas"""

# Type hints (recomendado desde Python 3.5)
def processar(dados: list[int]) -> dict[str, float]:
    pass
```

### 20.3 Segurança

```python
import hashlib
import secrets
import getpass

# Hash de senhas
senha = "minha_senha_secreta"
hash_obj = hashlib.sha256(senha.encode())
hash_hex = hash_obj.hexdigest()
print(hash_hex)

# Salt para hashes
import bcrypt  # pip install bcrypt
salt = bcrypt.gensalt()
hash_senha = bcrypt.hashpw(senha.encode(), salt)

# Verificar
if bcrypt.checkpw(senha.encode(), hash_senha):
    print("Senha correta")

# Token seguro
token = secrets.token_hex(32)  # 64 caracteres
token_url = secrets.token_urlsafe(32)

# Entrada segura
senha = getpass.getpass("Digite sua senha: ")

# Evitar eval e exec com entrada de usuário
# Perigoso: eval(input("Digite expressão: "))
# Seguro: usar ast.literal_eval para estruturas simples

from ast import literal_eval
dados = literal_eval("{'a': 1, 'b': 2}")  # Seguro

# Path traversal
import os
caminho_usuario = "../../../etc/passwd"
caminho_seguro = os.path.realpath(os.path.join('/safe/dir', caminho_usuario))
if not caminho_seguro.startswith('/safe/dir'):
    raise ValueError("Caminho inválido")
```

---

## 📊 QUADRO RESUMO

| Categoria | Principais Comandos |
|-----------|-------------------|
| **Variáveis** | `x = 10`, `nome = "João"` |
| **Listas** | `lista.append()`, `lista.pop()`, `lista[1:3]` |
| **Dict** | `dict["chave"]`, `dict.get()`, `dict.items()` |
| **Strings** | `"texto".upper()`, `f"{var}"`, `" ".join()` |
| **Condições** | `if`, `elif`, `else`, `match/case` |
| **Loops** | `for i in range()`, `while`, `break`, `continue` |
| **Funções** | `def func():`, `return`, `lambda` |
| **Classes** | `class MinhaClasse:`, `def __init__`, `self` |
| **Arquivos** | `with open() as f:`, `f.read()`, `f.write()` |
| **Exceções** | `try/except/finally`, `raise` |
| **Import** | `import modulo`, `from modulo import item` |
| **List Comp** | `[x**2 for x in range(10)]` |
| **Geradores** | `(x**2 for x in range(10))`, `yield` |
| **Decoradores** | `@decorator` |
| **Async** | `async def`, `await`, `asyncio.run()` |
| **Type Hints** | `def func(x: int) -> str:` |
| **Testes** | `assert`, `pytest`, `unittest` |

---

Este cheat sheet contém mais de **300 exemplos práticos** cobrindo desde fundamentos até tópicos avançados. Para aprofundamento em qualquer tópico específico, consulte a [documentação oficial do Python](https://docs.python.org/pt-br/3/).

**Dica:** Salve este documento como um arquivo `.md` ou imprima para consulta rápida!