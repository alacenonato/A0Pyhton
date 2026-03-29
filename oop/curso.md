## pode fazer um curso de Python, de oop, dividido em módulos, com todos os conceitos e que pode fazer oop em Python, do zero ao avançado, com projeto final com as clássicas classes employee e acount e suas Variações 

# Curso Completo de Programação Orientada a Objetos em Python

## 📚 Estrutura do Curso
**Nível:** Iniciante ao Avançado  
**Duração estimada:** 6-8 semanas  
**Pré-requisitos:** Conhecimentos básicos de Python

---

## 📋 Módulos do Curso

### **MÓDULO 1: Fundamentos da OOP**
**Duração:** 1 semana
- **1.1** O que é Programação Orientada a Objetos
- **1.2** Paradigmas de programação: procedural vs OOP
- **1.3** Os 4 pilares da OOP:
  - Encapsulamento
  - Abstração
  - Herança
  - Polimorfismo
- **1.4** Classes vs Objetos
- **1.5** Atributos e métodos
- **Exercícios práticos:** Criar classe `Pessoa` com atributos básicos

### **MÓDULO 2: Classes e Objetos em Python**
**Duração:** 1 semana
- **2.1** Sintaxe de classes em Python
- **2.2** Método `__init__` e construtores
- **2.3** Métodos de instância vs métodos de classe
- **2.4** Atributos de instância vs atributos de classe
- **2.5** Método `__str__` e representação de objetos
- **Exercícios práticos:** Implementar classe `Carro` com métodos básicos

### **MÓDULO 3: Encapsulamento e Propriedades**
**Duração:** 1 semana
- **3.1** Modificadores de acesso em Python
- **3.2** Getter e setter com `@property`
- **3.3** Atributos privados (`_` e `__`)
- **3.4** Propriedades dinâmicas
- **3.5** Validação em setters
- **Exercícios práticos:** Criar classe `ContaBancaria` com saldo privado

### **MÓDULO 4: Herança e Composição**
**Duração:** 1.5 semanas
- **4.1** Herança simples e múltipla
- **4.2** Método `super()`
- **4.3** Overriding de métodos
- **4.4** Classes abstratas com `ABC` e `@abstractmethod`
- **4.5** Composição vs Herança
- **4.6** Métodos `isinstance()` e `issubclass()`
- **Exercícios práticos:** Sistema de formas geométricas

### **MÓDULO 5: Polimorfismo e Métodos Especiais**
**Duração:** 1 semana
- **5.1** Polimorfismo em funções e métodos
- **5.2** Duck typing
- **5.3** Métodos mágicos (dunder methods):
  - `__len__`, `__getitem__`, `__setitem__`
  - `__eq__`, `__lt__`, `__gt__`
  - `__add__`, `__sub__`, `__mul__`
- **5.4** Sobrecarga de operadores
- **Exercícios práticos:** Implementar classe `Vetor` com operações matemáticas

### **MÓDULO 6: Tópicos Avançados**
**Duração:** 1.5 semanas
- **6.1** Mixins e múltipla herança
- **6.2** Decoradores de classe
- **6.3** Metaclasses (conceitos básicos)
- **6.4** Padrões de projeto simples:
  - Singleton
  - Factory
  - Strategy
- **6.5** Serialização de objetos com `pickle`
- **Exercícios práticos:** Implementar padrão Singleton

---

## 🎓 PROJETO FINAL: Sistema de Gerenciamento Empresarial

### **Descrição do Projeto**
Implementar um sistema completo de gerenciamento de funcionários e contas bancárias, demonstrando todos os conceitos aprendidos.

### **Estrutura do Projeto:**

#### **Parte 1: Sistema de Funcionários (Employee System)**
```python
# Classe Base
class Employee:
    def __init__(self, name, employee_id, base_salary):
        self._name = name
        self._employee_id = employee_id
        self._base_salary = base_salary
        self._bonus = 0
    
    @property
    def name(self):
        return self._name
    
    @property
    def employee_id(self):
        return self._employee_id
    
    def calculate_salary(self):
        """Método abstrato (será implementado nas subclasses)"""
        raise NotImplementedError("Subclasses devem implementar este método")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self._name} (ID: {self._employee_id})"

# Subclasses
class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, team_size):
        super().__init__(name, employee_id, base_salary)
        self._team_size = team_size
        self._bonus_percentage = 0.15
    
    def calculate_salary(self):
        bonus = self._base_salary * self._bonus_percentage
        team_bonus = self._team_size * 100
        return self._base_salary + bonus + team_bonus

class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, programming_languages):
        super().__init__(name, employee_id, base_salary)
        self._programming_languages = programming_languages
        self._bonus_per_language = 500
    
    def calculate_salary(self):
        language_bonus = len(self._programming_languages) * self._bonus_per_language
        return self._base_salary + language_bonus

class Intern(Employee):
    def __init__(self, name, employee_id, base_salary, university):
        super().__init__(name, employee_id, base_salary)
        self._university = university
        self._stipend = 500
    
    def calculate_salary(self):
        return self._base_salary + self._stipend
```

#### **Parte 2: Sistema Bancário (Account System)**
```python
from abc import ABC, abstractmethod
from datetime import datetime

# Classe Abstrata
class Account(ABC):
    _account_counter = 1000  # Atributo de classe
    
    def __init__(self, owner, initial_balance=0):
        self._account_number = Account._generate_account_number()
        self._owner = owner
        self._balance = initial_balance
        self._transactions = []
        self._created_at = datetime.now()
    
    @classmethod
    def _generate_account_number(cls):
        num = cls._account_counter
        cls._account_counter += 1
        return num
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._add_transaction("Deposit", amount)
            return True
        return False
    
    def _add_transaction(self, transaction_type, amount):
        transaction = {
            'date': datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'balance_after': self._balance
        }
        self._transactions.append(transaction)
    
    def get_transaction_history(self):
        return self._transactions.copy()
    
    def __str__(self):
        return f"{self.__class__.__name__} #{self._account_number} - {self._owner}: ${self._balance:.2f}"

# Subclasses de Conta
class SavingsAccount(Account):
    def __init__(self, owner, initial_balance=0, interest_rate=0.02):
        super().__init__(owner, initial_balance)
        self._interest_rate = interest_rate
        self._min_balance = 100
    
    def withdraw(self, amount):
        if amount > 0 and self._balance - amount >= self._min_balance:
            self._balance -= amount
            self._add_transaction("Withdrawal", -amount)
            return True
        return False
    
    def apply_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        self._add_transaction("Interest", interest)
        return interest

class CheckingAccount(Account):
    def __init__(self, owner, initial_balance=0, overdraft_limit=500):
        super().__init__(owner, initial_balance)
        self._overdraft_limit = overdraft_limit
        self._transaction_fee = 1.5
    
    def withdraw(self, amount):
        total_amount = amount + self._transaction_fee
        if amount > 0 and self._balance + self._overdraft_limit >= total_amount:
            self._balance -= total_amount
            self._add_transaction("Withdrawal", -amount)
            self._add_transaction("Fee", -self._transaction_fee)
            return True
        return False

class BusinessAccount(Account):
    def __init__(self, owner, initial_balance=0, company_name=""):
        super().__init__(owner, initial_balance)
        self._company_name = company_name
        self._monthly_fee = 25
    
    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            self._add_transaction("Withdrawal", -amount)
            return True
        return False
    
    def apply_monthly_fee(self):
        if self._balance >= self._monthly_fee:
            self._balance -= self._monthly_fee
            self._add_transaction("Monthly Fee", -self._monthly_fee)
            return True
        return False
```

#### **Parte 3: Sistema Integrado**
```python
class Bank:
    def __init__(self, name):
        self._name = name
        self._accounts = {}
        self._employees = {}
    
    def add_account(self, account):
        self._accounts[account.account_number] = account
    
    def add_employee(self, employee):
        self._employees[employee.employee_id] = employee
    
    def get_total_deposits(self):
        return sum(account.balance for account in self._accounts.values())
    
    def get_employee_payroll(self):
        payroll = {}
        for emp_id, employee in self._employees.items():
            payroll[emp_id] = {
                'name': employee.name,
                'salary': employee.calculate_salary()
            }
        return payroll
    
    def transfer(self, from_account_num, to_account_num, amount):
        from_account = self._accounts.get(from_account_num)
        to_account = self._accounts.get(to_account_num)
        
        if not from_account or not to_account:
            return False
        
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False

# Exemplo de uso integrado
def main():
    # Criar banco
    bank = Bank("Python Bank")
    
    # Criar funcionários
    manager = Manager("Alice Silva", "EMP001", 5000, 5)
    developer = Developer("Bob Souza", "EMP002", 4000, ["Python", "JavaScript"])
    intern = Intern("Carlos Lima", "EMP003", 1500, "Universidade Python")
    
    # Adicionar funcionários ao banco
    bank.add_employee(manager)
    bank.add_employee(developer)
    bank.add_employee(intern)
    
    # Criar contas bancárias
    savings = SavingsAccount("Alice Silva", 5000)
    checking = CheckingAccount("Bob Souza", 3000)
    business = BusinessAccount("Tech Solutions", 10000, "Tech Solutions Inc.")
    
    # Adicionar contas ao banco
    bank.add_account(savings)
    bank.add_account(checking)
    bank.add_account(business)
    
    # Operações
    savings.deposit(1000)
    checking.withdraw(500)
    bank.transfer(savings.account_number, checking.account_number, 200)
    
    # Demonstrar polimorfismo
    employees = [manager, developer, intern]
    for employee in employees:
        print(f"{employee.name}: R${employee.calculate_salary():.2f}")
    
    # Demonstrar encapsulamento
    print(f"\nTotal em depósitos: R${bank.get_total_deposits():.2f}")

if __name__ == "__main__":
    main()
```

---

## 📈 Tópicos Adicionais Sugeridos

### **Exercícios de Fixação por Módulo:**
1. Implementar um sistema de biblioteca
2. Criar um sistema de e-commerce com produtos e carrinho
3. Desenvolver um jogo simples com personagens

### **Boas Práticas:**
- Type hints em classes
- Docstrings e documentação
- Testes unitários para classes
- Princípios SOLID aplicados ao Python

### **Recursos Recomendados:**
- Livro: "Python Object-Oriented Programming" de Steven F. Lott
- Documentação oficial: Python Data Model
- Repositório com exemplos completos

---

## 🎯 Avaliação Final
1. Implementar todas as classes do projeto
2. Adicionar funcionalidades extras:
   - Serialização dos dados
   - Interface de linha de comando
   - Persistência em arquivos JSON
3. Escrever testes unitários
4. Documentar com docstrings

Este curso cobre desde os conceitos mais básicos até tópicos avançados de OOP em Python, com um projeto prático que integra todos os conceitos aprendidos.
