## vamos para módulo 1, com bastante exemplos, exercícios e questionário final, aprender os conceitos, como num curso da alura 

# **MÓDULO 1: Fundamentos da Programação Orientada a Objetos**

## 🎯 **Objetivos do Módulo**
Ao final deste módulo, você será capaz de:
- Entender o que é Programação Orientada a Objetos
- Diferenciar programação procedural de OOP
- Compreender os 4 pilares da OOP
- Identificar classes e objetos na vida real
- Criar sua primeira classe em Python

---

## 📖 **1.1 O que é Programação Orientada a Objetos (OOP)?**

### **Conceito**
A Programação Orientada a Objetos é um paradigma de programação que organiza o código em "objetos" que contêm **dados** (atributos) e **comportamentos** (métodos).

### **Analogia da Vida Real**
Pense em um **carro**:
- **Atributos (dados):** cor, modelo, ano, velocidade atual
- **Métodos (comportamentos):** acelerar(), frear(), buzinar()

### **Exemplo Prático**

```python
# PROGRAMAÇÃO PROCEDURAL (ANTES)
def calcular_area_retangulo(largura, altura):
    return largura * altura

def calcular_perimetro_retangulo(largura, altura):
    return 2 * (largura + altura)

# Uso
largura = 5
altura = 3
area = calcular_area_retangulo(largura, altura)
perimetro = calcular_perimetro_retangulo(largura, altura)

# ------------------------------------------------------------

# PROGRAMÇÃO ORIENTADA A OBJETOS (DEPOIS)
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

# Uso
meu_retangulo = Retangulo(5, 3)
area = meu_retangulo.calcular_area()
perimetro = meu_retangulo.calcular_perimetro()
```

### **Vantagens da OOP:**
1. **Organização:** Código mais limpo e estruturado
2. **Reuso:** Classes podem ser reaproveitadas
3. **Manutenção:** Mais fácil de modificar e corrigir
4. **Abstração:** Esconde detalhes complexos
5. **Modularidade:** Divide problemas grandes em pequenos

---

## 🔄 **1.2 Programação Procedural vs OOP**

### **Exemplo Comparativo: Sistema de Livros**

```python
# ========== VERSÃO PROCEDURAL ==========
livros = []
autores = []

def adicionar_livro_procedural(titulo, autor, paginas):
    livro = {
        'titulo': titulo,
        'autor': autor,
        'paginas': paginas,
        'lido': False
    }
    livros.append(livro)

def marcar_como_lido_procedural(titulo):
    for livro in livros:
        if livro['titulo'] == titulo:
            livro['lido'] = True
            return True
    return False

def listar_livros_nao_lidos_procedural():
    return [livro for livro in livros if not livro['lido']]

# Uso
adicionar_livro_procedural("Python Básico", "João Silva", 300)
marcar_como_lido_procedural("Python Básico")

# ========== VERSÃO OOP ==========
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.lido = False
    
    def marcar_como_lido(self):
        self.lido = True
        print(f"Livro '{self.titulo}' marcado como lido!")
    
    def informacoes(self):
        status = "Lido" if self.lido else "Não lido"
        return f"{self.titulo} - {self.autor} ({self.paginas} páginas) - {status}"

class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca!")
    
    def buscar_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

# Uso
meu_livro = Livro("Python Avançado", "Maria Santos", 450)
minha_biblioteca = Biblioteca()
minha_biblioteca.adicionar_livro(meu_livro)
meu_livro.marcar_como_lido()
print(meu_livro.informacoes())
```

### **Diferenças Principais:**

| **Aspecto** | **Procedural** | **OOP** |
|------------|---------------|---------|
| **Foco** | Funções e procedimentos | Objetos e suas interações |
| **Dados** | Separados das funções | Integrados aos objetos |
| **Estado** | Passado como parâmetro | Mantido no objeto |
| **Reuso** | Cópia de funções | Herança de classes |
| **Complexidade** | Pode ficar confuso | Mais organizado |

---

## 🏛️ **1.3 Os 4 Pilares da OOP**

### **1. ENCAPSULAMENTO**
Agrupar dados e métodos que operam nesses dados em uma única unidade (classe), e restringir o acesso a alguns componentes.

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular          # Público
        self._saldo = saldo_inicial     # Protegido (convenção)
        self.__senha = "1234"           # Privado
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor} realizado!")
        else:
            print("Valor inválido!")
    
    def ver_saldo(self):
        return f"Saldo: R${self._saldo}"
    
    # Método público para acessar dado privado com validação
    def alterar_senha(self, senha_atual, nova_senha):
        if senha_atual == self.__senha:
            self.__senha = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("Senha atual incorreta!")

# Uso
minha_conta = ContaBancaria("Carlos", 1000)
minha_conta.depositar(500)
print(minha_conta.ver_saldo())
# minha_conta.__senha  # Erro! Atributo privado
```

### **2. ABSTRAÇÃO**
Esconder detalhes complexos e mostrar apenas o essencial.

```python
from abc import ABC, abstractmethod

# Classe abstrata - define o "contrato"
class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

# Classes concretas - implementam os detalhes
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14159 * (self.raio ** 2)
    
    def calcular_perimetro(self):
        return 2 * 3.14159 * self.raio

# Uso - não precisa saber como calcula, só usa o método
formas = [Retangulo(5, 3), Circulo(4)]
for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")
    print(f"Perímetro: {forma.calcular_perimetro():.2f}")
    print("-" * 20)
```

### **3. HERANÇA**
Permite que uma classe herde atributos e métodos de outra classe.

```python
# Classe Pai/Base
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_som(self):
        print("Som genérico de animal")
    
    def dormir(self):
        print(f"{self.nome} está dormindo...")

# Classes Filhas/Derivadas
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)  # Chama construtor da classe pai
        self.raca = raca
    
    def fazer_som(self):  # Sobrescreve método da classe pai
        print("Au Au!")
    
    def buscar_bola(self):
        print(f"{self.nome} está buscando a bola!")

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor
    
    def fazer_som(self):
        print("Miau!")
    
    def arranhar_moveis(self):
        print(f"{self.nome} está arranhando os móveis!")

# Uso
rex = Cachorro("Rex", 3, "Labrador")
mingau = Gato("Mingau", 2, "Branco")

animais = [rex, mingau]
for animal in animais:
    print(f"Nome: {animal.nome}")
    animal.fazer_som()
    animal.dormir()
    
    # Verifica o tipo para métodos específicos
    if isinstance(animal, Cachorro):
        animal.buscar_bola()
    elif isinstance(animal, Gato):
        animal.arranhar_moveis()
    
    print("-" * 20)
```

### **4. POLIMORFISMO**
Objetos de diferentes classes podem ser tratados de forma similar.

```python
# Polimorfismo com herança
class InstrumentoMusical:
    def tocar(self):
        raise NotImplementedError("Subclasses devem implementar este método")

class Violao(InstrumentoMusical):
    def tocar(self):
        return "Strum strum strum..."

class Piano(InstrumentoMusical):
    def tocar(self):
        return "Plink plink plonk..."

class Bateria(InstrumentoMusical):
    def tocar(self):
        return "Boom crash bang!"

# Polimorfismo - mesma interface, comportamentos diferentes
orquestra = [Violao(), Piano(), Bateria()]
for instrumento in orquestra:
    print(instrumento.tocar())

# Polimorfismo sem herança (Duck Typing)
class Carro:
    def mover(self):
        return "Vrum vrum! Carro em movimento."

class Aviao:
    def mover(self):
        return "Zooooom! Avião decolando."

class Barco:
    def mover(self):
        return "Glub glub! Barco navegando."

# Todos têm método mover(), então funcionam da mesma forma
veiculos = [Carro(), Aviao(), Barco()]
for veiculo in veiculos:
    print(veiculo.mover())
```

---

## 🏗️ **1.4 Classes vs Objetos**

### **Conceitos:**
- **Classe:** Molde/planta/blueprint que define atributos e métodos
- **Objeto:** Instância concreta criada a partir da classe

### **Analogia:**
- **Classe = Receita de bolo**
- **Objeto = Bolo assado**

### **Exemplo Detalhado:**

```python
# DEFINIÇÃO DA CLASSE (molde)
class Celular:
    # Atributo de classe (compartilhado por todas as instâncias)
    fabricante = "TechWorld"
    
    def __init__(self, modelo, memoria, cor):
        # Atributos de instância (únicos para cada objeto)
        self.modelo = modelo
        self.memoria = memoria
        self.cor = cor
        self.ligado = False
        self.bateria = 100
    
    # Métodos de instância
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo} está ligando...")
        else:
            print("O celular já está ligado!")
    
    def usar(self, minutos):
        if self.ligado:
            consumo = minutos * 0.5
            self.bateria = max(0, self.bateria - consumo)
            print(f"Usou por {minutos} minutos. Bateria: {self.bateria:.1f}%")
        else:
            print("Ligue o celular primeiro!")
    
    # Método estático (não precisa da instância)
    @staticmethod
    def info_empresa():
        return "TechWorld - Fabricante de eletrônicos desde 2000"
    
    # Método de classe
    @classmethod
    def mudar_fabricante(cls, novo_nome):
        cls.fabricante = novo_nome
        print(f"Fabricante alterado para: {novo_nome}")

# CRIANDO OBJETOS (instâncias)
celular1 = Celular("Galaxy X", 128, "Preto")
celular2 = Celular("iPhone Pro", 256, "Branco")
celular3 = Celular("Moto G", 64, "Azul")

# Usando os objetos
print(f"Celular 1: {celular1.modelo}, Cor: {celular1.cor}")
print(f"Celular 2: {celular1.modelo}, Cor: {celular2.cor}")
print(f"Celular 3: {celular1.modelo}, Cor: {celular3.cor}")

print(f"\nFabricante (atributo de classe): {celular1.fabricante}")
print(Celular.info_empresa())

celular1.ligar()
celular1.usar(30)
```

---

## 🔧 **1.5 Atributos e Métodos**

### **Tipos de Atributos:**
```python
class Estudante:
    # 1. Atributo de classe (compartilhado)
    escola = "Escola Python"
    total_estudantes = 0
    
    def __init__(self, nome, idade):
        # 2. Atributos de instância (únicos)
        self.nome = nome
        self.idade = idade
        self.notas = []
        
        # Atualiza atributo de classe
        Estudante.total_estudantes += 1
    
    # 3. Atributo privado (convenção)
    def _calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0
    
    # Métodos de instância
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print(f"Nota {nota} adicionada para {self.nome}")
        else:
            print("Nota inválida!")
    
    def situacao(self):
        media = self._calcular_media()
        if media >= 7:
            return f"Aprovado com média {media:.1f}"
        elif media >= 5:
            return f"Recuperação com média {media:.1f}"
        else:
            return f"Reprovado com média {media:.1f}"
```

### **Tipos de Métodos:**
```python
class Calculadora:
    # 1. Método de instância (precisa do self)
    def somar(self, a, b):
        return a + b
    
    # 2. Método de classe (precisa do cls)
    @classmethod
    def historico_uso(cls):
        return f"Calculadora usada {cls.contador} vezes"
    
    # 3. Método estático (não precisa de self nem cls)
    @staticmethod
    def ajuda():
        return """
        Operações disponíveis:
        - Soma: a + b
        - Subtração: a - b
        - Multiplicação: a * b
        - Divisão: a / b
        """

# Uso
calc = Calculadora()
print(calc.somar(5, 3))          # Método de instância
print(Calculadora.ajuda())       # Método estático
```

---

## 🏋️ **EXERCÍCIOS PRÁTICOS**

### **Exercício 1: Classe Pessoa**
Crie uma classe `Pessoa` com:
- Atributos: nome, idade, profissão
- Métodos: apresentar(), aniversario(), mudar_profissao()

```python
# SOLUÇÃO DO EXERCÍCIO 1
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}."
    
    def aniversario(self):
        self.idade += 1
        print(f"Feliz aniversário! Agora {self.nome} tem {self.idade} anos.")
    
    def mudar_profissao(self, nova_profissao):
        antiga = self.profissao
        self.profissao = nova_profissao
        print(f"{self.nome} mudou de {antiga} para {nova_profissao}.")

# Teste
p1 = Pessoa("Ana", 25, "Engenheira")
print(p1.apresentar())
p1.aniversario()
p1.mudar_profissao("Arquiteta")
print(p1.apresentar())
```

### **Exercício 2: Sistema de Produtos**
Crie um sistema de produtos de loja:
- Classe `Produto` com: nome, preço, quantidade_estoque
- Métodos: vender(), repor(), calcular_valor_total()

```python
# SOLUÇÃO DO EXERCÍCIO 2
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def vender(self, quantidade_vendida):
        if quantidade_vendida <= self.quantidade:
            self.quantidade -= quantidade_vendida
            valor_total = quantidade_vendida * self.preco
            print(f"Vendido {quantidade_vendida} unidades de {self.nome}. Total: R${valor_total:.2f}")
            return valor_total
        else:
            print(f"Estoque insuficiente! Temos apenas {self.quantidade} unidades.")
            return 0
    
    def repor(self, quantidade_reposta):
        self.quantidade += quantidade_reposta
        print(f"Reposto {quantidade_reposta} unidades de {self.nome}. Estoque atual: {self.quantidade}")
    
    def calcular_valor_total(self):
        return self.quantidade * self.preco
    
    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} - Estoque: {self.quantidade}"

# Teste
produto1 = Produto("Notebook", 3500.00, 10)
produto2 = Produto("Mouse", 89.90, 50)

print(produto1)
produto1.vender(3)
produto1.repor(5)
print(f"Valor total em estoque: R${produto1.calcular_valor_total():.2f}")
```

### **Exercício 3: Sistema de Banco com os 4 Pilares**
Crie um sistema bancário simples demonstrando os 4 pilares.

```python
# SOLUÇÃO DO EXERCÍCIO 3
# ABSTRAÇÃO
class Conta(ABC):
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo  # ENCAPSULAMENTO
    
    @abstractmethod
    def sacar(self, valor):
        pass
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False
    
    def ver_saldo(self):
        return self._saldo

# HERANÇA
class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=1000):
        super().__init__(titular, saldo)
        self.limite = limite
    
    # POLIMORFISMO
    def sacar(self, valor):
        if valor > 0 and (self._saldo + self.limite) >= valor:
            self._saldo -= valor
            return True
        return False

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0, rendimento=0.005):
        super().__init__(titular, saldo)
        self.rendimento = rendimento
    
    # POLIMORFISMO
    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            return True
        return False
    
    def aplicar_rendimento(self):
        self._saldo += self._saldo * self.rendimento

# Teste
contas = [
    ContaCorrente("João", 1000, 500),
    ContaPoupanca("Maria", 2000)
]

# POLIMORFISMO na prática
for conta in contas:
    conta.depositar(100)
    conta.sacar(50)
    print(f"{conta.titular}: R${conta.ver_saldo():.2f}")
```

---

## 📝 **QUESTIONÁRIO FINAL DO MÓDULO 1**

### **Questões Teóricas:**

1. **O que é Programação Orientada a Objetos?**
   a) Um tipo de compilador
   b) Um paradigma que organiza código em objetos
   c) Uma linguagem de programação
   d) Um banco de dados

2. **Qual NÃO é um pilar da OOP?**
   a) Encapsulamento
   b) Abstração
   c) Iteração
   d) Polimorfismo

3. **Qual a diferença entre classe e objeto?**
   a) Classe é instância, objeto é molde
   b) São a mesma coisa
   c) Classe é molde, objeto é instância
   d) Classe é método, objeto é atributo

4. **O que é encapsulamento?**
   a) Mostrar todos os detalhes
   b) Agrupar dados e métodos, restringindo acesso
   c) Criar várias classes
   d) Herdar atributos

5. **Polimorfismo permite que:**
   a) Objetos de diferentes classes sejam tratados igualmente
   b) Classes tenham sempre o mesmo comportamento
   c) Objetos não possam ser modificados
   d) Todos os métodos sejam públicos

### **Questões Práticas:**

6. **Analise o código e responda:**
```python
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
    
    def buzinar(self):
        return "Beep beep!"

meu_carro = Carro("Fusca", 1970)
```
**Qual é a classe e qual é o objeto no código acima?**

7. **Qual pilar da OOP está sendo demonstrado?**
```python
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
```

8. **O que o símbolo `_` (underscore) antes de um atributo indica em Python?**

9. **Qual a diferença entre método de instância e método estático?**

10. **Por que a OOP é considerada mais organizada que a programação procedural para projetos grandes?**

### **Respostas do Questionário:**

1. **b) Um paradigma que organiza código em objetos**
2. **c) Iteração**
3. **c) Classe é molde, objeto é instância**
4. **b) Agrupar dados e métodos, restringindo acesso**
5. **a) Objetos de diferentes classes sejam tratados igualmente**
6. **Classe: Carro, Objeto: meu_carro**
7. **Polimorfismo (e Herança)**
8. **Indica que o atributo é protegido (convenção, não impede acesso)**
9. **Método de instância precisa do objeto (self), estático não precisa**
10. **Porque organiza o código em unidades autocontidas (objetos), facilita reuso, manutenção e compreensão do sistema**

---

## 🎓 **Desafio Final do Módulo 1**

Crie um sistema completo de uma **Biblioteca Pessoal** que deve conter:

1. Classe `Livro` com:
   - Atributos: titulo, autor, ano, paginas, lido (booleano)
   - Métodos: ler(), info(), tempo_medio_leitura()

2. Classe `Biblioteca` com:
   - Atributo: colecao (lista de livros)
   - Métodos: adicionar_livro(), remover_livro(), buscar_por_autor(), livros_nao_lidos(), estatisticas()

3. Demonstre todos os 4 pilares da OOP no sistema.

**Bônus:** Adicione uma classe `Ebook` que herda de `Livro` e adiciona atributos como tamanho_arquivo e formato.

```python
# ESQUELETO PARA COMEÇAR
class Livro:
    def __init__(self, titulo, autor, ano, paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.paginas = paginas
        self.lido = False
    
    def ler(self):
        # Implemente aqui
        pass
    
    # Adicione outros métodos

# Sua implementação aqui...
```

---

## 📚 **Recursos Adicionais**

### **Para Praticar:**
1. Implemente um sistema de agenda de contatos
2. Crie um jogo de RPG simples com personagens
3. Faça um sistema de pedidos de restaurante

### **Dicas Importantes:**
- Comece sempre identificando os "nouns" (substantivos) - eles provavelmente serão classes
- Pense em "what does it have?" (atributos) e "what can it do?" (métodos)
- Use nomes descritivos para classes (substantivos) e métodos (verbos)

### **Próximo Módulo:**
No **Módulo 2**, vamos aprofundar na sintaxe de classes em Python, métodos especiais, e construir sistemas mais complexos!

---

🎉 **Parabéns por completar o Módulo 1!** Você agora tem uma base sólida dos conceitos fundamentais de OOP. Continue praticando e no próximo módulo vamos colocar a mão na massa com Python!
