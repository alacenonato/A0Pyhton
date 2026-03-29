## pode fazer um curso de Python, de oop, dividido em módulos e aulas, com todos os conceitos e mostrando o que eu posso fazer em oop no Python, do zero ao avançado, com projetos finais de as clássicas classes(exemplo employee e acount) e suas Variações 

Claro! Vou criar um curso completo de **Programação Orientada a Objetos (POO) em Python**, do zero ao avançado, com módulos, aulas e projetos práticos.

## **Curso Completo de POO em Python**

### **Módulo 1: Fundamentos da POO em Python**
*Aulas 1-10*

**Aula 1:** Introdução à POO vs Programação Estruturada
**Aula 2:** Classes e Objetos - Primeiros passos
```python
class PrimeiraClasse:
    pass

obj = PrimeiraClasse()
```

**Aula 3:** Método `__init__` e atributos de instância
**Aula 4:** Atributos de classe vs atributos de instância
**Aula 5:** Métodos de instância
**Aula 6:** Parâmetro `self` - entendendo sua importância
**Aula 7:** Encapsulamento básico (convenções)
**Aula 8:** Propriedades com `@property`
**Aula 9:** Getters e Setters em Python
**Aula 10:** Projeto Prático 1 - Classe `Pessoa`

### **Módulo 2: Herança e Polimorfismo**
*Aulas 11-20*

**Aula 11:** Herança simples
**Aula 12:** Sobrescrita de métodos
**Aula 13:** Função `super()`
**Aula 14:** Herança múltipla
**Aula 15:** Method Resolution Order (MRO)
**Aula 16:** Polimorfismo - conceito e aplicação
**Aula 17:** Duck Typing em Python
**Aula 18:** Classes abstratas com `ABC`
**Aula 19:** Métodos abstratos
**Aula 20:** Projeto Prático 2 - Sistema de Funcionários

### **Módulo 3: Encapsulamento Avançado e Propriedades**
*Aulas 21-25*

**Aula 21:** Modificadores de acesso (público, protegido, privado)
**Aula 22:** Name Mangling
**Aula 23:** Property decorator avançado
**Aula 24:** Computed attributes
**Aula 25:** Projeto Prático 3 - Classe `ContaBancária` com validações

### **Módulo 4: Métodos Especiais (Magic Methods)**
*Aulas 26-32*

**Aula 26:** `__str__` e `__repr__`
**Aula 27:** `__len__`, `__getitem__`, `__setitem__`
**Aula 28:** `__call__` - Tornando objetos chamáveis
**Aula 29:** `__eq__`, `__lt__`, `__gt__` - Comparações
**Aula 30:** `__add__`, `__sub__` - Operadores aritméticos
**Aula 31:** `__enter__` e `__exit__` - Context Managers
**Aula 32:** Projeto Prático 4 - Classe `Vetor` matemático

### **Módulo 5: Composição e Agregação**
*Aulas 33-37*

**Aula 33:** Composição vs Agregação
**Aula 34:** Relacionamentos entre classes
**Aula 35:** Classes como atributos
**Aula 36:** Listas de objetos
**Aula 37:** Projeto Prático 5 - Sistema Escolar

### **Módulo 6: Decoradores e POO**
*Aulas 38-42*

**Aula 38:** Decoradores em classes
**Aula 39:** `@staticmethod`
**Aula 40:** `@classmethod`
**Aula 41:** Factory methods com classmethod
**Aula 42:** Projeto Prático 6 - Sistema de Datas

### **Módulo 7: Tratamento de Exceções em POO**
*Aulas 43-47*

**Aula 43:** Exceções built-in
**Aula 44:** Criando exceções personalizadas
**Aula 45:** Tratamento de erros em métodos
**Aula 46:** Boas práticas de validação
**Aula 47:** Projeto Prático 7 - Validações robustas

### **Módulo 8: Design Patterns em Python**
*Aulas 48-53*

**Aula 48:** Singleton Pattern
**Aula 49:** Factory Pattern
**Aula 50:** Observer Pattern
**Aula 51:** Strategy Pattern
**Aula 52:** Decorator Pattern
**Aula 53:** Projeto Prático 8 - Implementando Patterns

### **Módulo 9: Tópicos Avançados**
*Aulas 54-60*

**Aula 54:** Metaclasses
**Aula 55:** Descriptors
**Aula 56:** Slots para otimização
**Aula 57:** Mixins
**Aula 58:** Type Hints em classes
**Aula 59:** Dataclasses
**Aula 60:** Projeto Prático 9 - Framework ORM simples

---

## **PROJETOS PRÁTICOS DETALHADOS**

### **Projeto 1: Classe Pessoa (Módulo 1)**
```python
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf  # encapsulado
    
    def aniversario(self):
        self.idade += 1
    
    def get_cpf(self):
        return f"***.{self.__cpf[-8:-3]}.{self.__cpf[-3:]}-**"
    
    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"

# Variação: PessoaFisica, PessoaJuridica
```

### **Projeto 2: Sistema de Funcionários (Módulo 2)**
```python
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    @abstractmethod
    def calcular_salario(self):
        pass
    
    def __str__(self):
        return f"{self.nome}: R$ {self.calcular_salario():.2f}"

class FuncionarioCLT(Funcionario):
    def calcular_salario(self):
        return self.salario_base - (self.salario_base * 0.1)  # -10% impostos

class FuncionarioPJ(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome, 0)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas
    
    def calcular_salario(self):
        return self.valor_hora * self.horas_trabalhadas

class Gerente(FuncionarioCLT):
    def calcular_salario(self):
        return super().calcular_salario() + 2000  # bônus
```

### **Projeto 3: Conta Bancária (Módulo 3)**
```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial
        self.__transacoes = []
        self.__ativa = True
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def ativa(self):
        return self.__ativa
    
    @ativa.setter
    def ativa(self, status):
        if not isinstance(status, bool):
            raise ValueError("Status deve ser booleano")
        self.__ativa = status
    
    def depositar(self, valor):
        if not self.__ativa:
            raise Exception("Conta inativa")
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        
        self.__saldo += valor
        self.__transacoes.append(f"Depósito: +{valor}")
    
    def sacar(self, valor):
        if not self.__ativa:
            raise Exception("Conta inativa")
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente")
        
        self.__saldo -= valor
        self.__transacoes.append(f"Saque: -{valor}")
    
    def extrato(self):
        return self.__transacoes.copy()

# Variações: ContaCorrente, ContaPoupanca, ContaInvestimento
```

### **Projeto 4: Classe Vetor (Módulo 4)**
```python
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vetor({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vetor(self.x - other.x, self.y - other.y)
    
    def __mul__(self, escalar):
        return Vetor(self.x * escalar, self.y * escalar)
    
    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return abs(self) < abs(other)
```

### **Projeto 5: Sistema Escolar (Módulo 5)**
```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
    
    def matricular(self, aluno):
        self.alunos.append(aluno)
    
    def media_turma(self):
        if not self.alunos:
            return 0
        total = sum(sum(aluno.notas) / len(aluno.notas) 
                    for aluno in self.alunos if aluno.notas)
        return total / len(self.alunos)

class Turma:
    def __init__(self, codigo):
        self.codigo = codigo
        self.disciplinas = []
        self.professor = None
    
    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
```

### **Projeto 6: Sistema de Datas (Módulo 6)**
```python
from datetime import datetime

class Data:
    formato_padrao = "%d/%m/%Y"
    
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    @classmethod
    def hoje(cls):
        hoje = datetime.now()
        return cls(hoje.day, hoje.month, hoje.year)
    
    @classmethod
    def from_string(cls, data_str, formato=formato_padrao):
        data = datetime.strptime(data_str, formato)
        return cls(data.day, data.month, data.year)
    
    @staticmethod
    def is_bissexto(ano):
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"
```

### **Projeto 7: Validações com Exceções Personalizadas**
```python
class ValidacaoError(Exception):
    pass

class EmailInvalidoError(ValidacaoError):
    pass

class CpfInvalidoError(ValidacaoError):
    pass

class Usuario:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = self._validar_email(email)
        self.cpf = self._validar_cpf(cpf)
    
    def _validar_email(self, email):
        if "@" not in email or "." not in email:
            raise EmailInvalidoError(f"Email inválido: {email}")
        return email
    
    def _validar_cpf(self, cpf):
        cpf = cpf.replace(".", "").replace("-", "")
        if len(cpf) != 11 or not cpf.isdigit():
            raise CpfInvalidoError(f"CPF inválido: {cpf}")
        return cpf
```

### **Projeto 8: Sistema de Notificações (Observer Pattern)**
```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, mensagem):
        pass

class UsuarioObserver(Observer):
    def __init__(self, nome):
        self.nome = nome
    
    def update(self, mensagem):
        print(f"{self.nome} recebeu: {mensagem}")

class SistemaNotificacoes:
    def __init__(self):
        self._observers = []
    
    def adicionar_observer(self, observer):
        self._observers.append(observer)
    
    def remover_observer(self, observer):
        self._observers.remove(observer)
    
    def notificar(self, mensagem):
        for observer in self._observers:
            observer.update(mensagem)
```

### **Projeto 9: Mini ORM com Descriptors**
```python
class Field:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.valor = None
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.valor
    
    def __set__(self, instance, valor):
        if not isinstance(valor, self.tipo):
            raise TypeError(f"{self.nome} deve ser {self.tipo}")
        self.valor = valor

class Model:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def save(self):
        campos = []
        valores = []
        for key, value in self.__class__.__dict__.items():
            if isinstance(value, Field):
                campos.append(key)
                valor = getattr(self, key)
                valores.append(repr(valor))
        
        sql = f"INSERT INTO {self.__class__.__name__} ({', '.join(campos)}) VALUES ({', '.join(valores)})"
        print(f"Executando: {sql}")
        return sql

class Pessoa(Model):
    nome = Field("nome", str)
    idade = Field("idade", int)

# Uso:
# p = Pessoa(nome="João", idade=30)
# p.save()
```

### **Projeto 10: Sistema Bancário Completo (Projeto Final)**
```python
from datetime import datetime
from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.data = datetime.now()
    
    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M')} - {self.tipo}: R$ {self.valor:.2f}"

class Conta(ABC):
    def __init__(self, cliente, agencia, numero):
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        self._saldo = 0
        self._transacoes = []
        self._ativa = True
    
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, valor):
        if not self._ativa:
            raise Exception("Conta inativa")
        if valor <= 0:
            raise ValueError("Valor de depósito deve ser positivo")
        
        self._saldo += valor
        self._transacoes.append(Transacao("Depósito", valor))
        return True
    
    def sacar(self, valor):
        if not self._ativa:
            raise Exception("Conta inativa")
        if valor <= 0:
            raise ValueError("Valor de saque deve ser positivo")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente")
        
        self._saldo -= valor
        self._transacoes.append(Transacao("Saque", valor))
        return True
    
    def extrato(self):
        return self._transacoes.copy()
    
    @abstractmethod
    def calcular_rendimento(self):
        pass

class ContaCorrente(Conta):
    def __init__(self, cliente, agencia, numero, limite_cheque_especial=1000):
        super().__init__(cliente, agencia, numero)
        self.limite_cheque_especial = limite_cheque_especial
        self.taxa_manutencao = 20
    
    def sacar(self, valor):
        if not self._ativa:
            raise Exception("Conta inativa")
        if valor <= 0:
            raise ValueError("Valor de saque deve ser positivo")
        
        saldo_disponivel = self._saldo + self.limite_cheque_especial
        if valor > saldo_disponivel:
            raise ValueError("Saldo + limite insuficiente")
        
        self._saldo -= valor
        self._transacoes.append(Transacao("Saque", valor))
        return True
    
    def calcular_rendimento(self):
        return self._saldo * 0.001  # Rendimento de 0.1%

class ContaPoupanca(Conta):
    def __init__(self, cliente, agencia, numero, aniversario):
        super().__init__(cliente, agencia, numero)
        self.aniversario = aniversario
        self.taxa_rendimento = 0.005  # 0.5%
    
    def calcular_rendimento(self):
        return self._saldo * self.taxa_rendimento

class ContaInvestimento(Conta):
    def __init__(self, cliente, agencia, numero, perfil="conservador"):
        super().__init__(cliente, agencia, numero)
        self.perfil = perfil
        self.investimentos = []
        
        self.taxas = {
            "conservador": 0.01,
            "moderado": 0.03,
            "agressivo": 0.06
        }
    
    def calcular_rendimento(self):
        return self._saldo * self.taxas.get(self.perfil, 0.01)

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
        self.agencia_principal = "0001"
    
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        return cliente
    
    def criar_conta(self, cliente, tipo, **kwargs):
        numero_conta = str(len(self.contas) + 1).zfill(6)
        
        if tipo == "corrente":
            conta = ContaCorrente(cliente, self.agencia_principal, numero_conta, **kwargs)
        elif tipo == "poupanca":
            conta = ContaPoupanca(cliente, self.agencia_principal, numero_conta, **kwargs)
        elif tipo == "investimento":
            conta = ContaInvestimento(cliente, self.agencia_principal, numero_conta, **kwargs)
        else:
            raise ValueError("Tipo de conta inválido")
        
        cliente.contas.append(conta)
        self.contas.append(conta)
        return conta
    
    def transferir(self, conta_origem, conta_destino, valor):
        if conta_origem.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False
    
    def relatorio_geral(self):
        print(f"\n=== RELATÓRIO DO BANCO {self.nome} ===\n")
        for cliente in self.clientes:
            print(f"Cliente: {cliente.nome} (CPF: {cliente.cpf})")
            for conta in cliente.contas:
                print(f"  Conta {conta.numero}: R$ {conta.saldo:.2f}")
            print()

# Exemplo de uso:
if __name__ == "__main__":
    # Criando banco
    banco = Banco("Python Bank")
    
    # Criando clientes
    cliente1 = Cliente("João Silva", "123.456.789-00", "Rua A, 123")
    cliente2 = Cliente("Maria Santos", "987.654.321-00", "Rua B, 456")
    
    banco.adicionar_cliente(cliente1)
    banco.adicionar_cliente(cliente2)
    
    # Criando contas
    conta_corrente = banco.criar_conta(cliente1, "corrente")
    conta_poupanca = banco.criar_conta(cliente2, "poupanca", aniversario=15)
    conta_investimento = banco.criar_conta(cliente1, "investimento", perfil="moderado")
    
    # Operações
    conta_corrente.depositar(1000)
    conta_corrente.sacar(200)
    banco.transferir(conta_corrente, conta_poupanca, 300)
    
    # Relatórios
    banco.relatorio_geral()
    
    print(f"Rendimento CC: R$ {conta_corrente.calcular_rendimento():.2f}")
    print(f"Rendimento CP: R$ {conta_poupanca.calcular_rendimento():.2f}")
    print(f"Extrato CC:")
    for transacao in conta_corrente.extrato()[-3:]:
        print(f"  {transacao}")
```

---

## **Recursos Extras Incluídos no Curso:**

1. **Exercícios práticos** após cada aula
2. **Desafios de código** para fixação
3. **Quizzes** de múltipla escolha
4. **Projetos integradores** a cada 3 módulos
5. **Material complementar** com:
   - Boas práticas de código
   - PEP 8 para classes
   - Documentação com docstrings
   - Testes unitários para POO

## **Pré-requisitos:**
- Conhecimento básico de Python (variáveis, loops, condicionais, funções)
- Editor de código (VS Code recomendado)
- Python 3.8+

## **Carga Horária Estimada:**
- **Vídeo-aulas:** 20 horas
- **Prática e projetos:** 40 horas
- **Total:** 60 horas

Este curso foi estruturado para levar você do básico ao avançado em POO com Python, com foco em exemplos práticos e projetos reais que você encontrará no mercado de trabalho.
