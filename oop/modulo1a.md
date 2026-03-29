# 🎯 Módulo 1: Fundamentos da POO em Python

Perfeito! Vamos começar nossa jornada no mundo da Programação Orientada a Objetos! 

## **Aula 1: Introdução à POO vs Programação Estruturada**

### 📖 **O que é Programação Orientada a Objetos?**

POO é um paradigma de programação que organiza o código em torno de "objetos" que contêm dados (atributos) e comportamentos (métodos), em vez de funções e lógica discretas.

### **Comparação: Estruturado vs POO**

**Programação Estruturada:**
```python
# Dados separados das funções
nome_aluno = "João"
notas_aluno = [8.5, 7.0, 9.0]

def calcular_media(notas):
    return sum(notas) / len(notas)

def aluno_aprovado(media):
    return media >= 7.0

# Uso
media = calcular_media(notas_aluno)
status = "Aprovado" if aluno_aprovado(media) else "Reprovado"
print(f"{nome_aluno}: {media:.1f} - {status}")
```

**Programação Orientada a Objetos:**
```python
# Dados e comportamentos juntos!
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def esta_aprovado(self):
        return self.calcular_media() >= 7.0
    
    def status(self):
        media = self.calcular_media()
        situacao = "Aprovado" if self.esta_aprovado() else "Reprovado"
        return f"{self.nome}: {media:.1f} - {situacao}"

# Uso - muito mais intuitivo!
aluno = Aluno("João", [8.5, 7.0, 9.0])
print(aluno.status())
```

### 🎯 **Por que usar POO?**

1. **Organização**: Código mais estruturado e lógico
2. **Reutilização**: Classes podem ser reutilizadas em vários lugares
3. **Manutenibilidade**: Mais fácil de dar manutenção e estender
4. **Modelagem do mundo real**: Representa melhor problemas do mundo real

---

## **Aula 2: Classes e Objetos - Primeiros Passos**

### 📖 **Conceitos Fundamentais**

- **Classe**: É um "molde" ou "planta" para criar objetos
- **Objeto**: É uma "instância" criada a partir de uma classe

### **Criando nossa primeira classe**

```python
# Classe vazia (mínima possível)
class PrimeiraClasse:
    pass  # pass significa "não faça nada"

# Criando objetos (instâncias)
obj1 = PrimeiraClasse()
obj2 = PrimeiraClasse()

print(type(obj1))  # <class '__main__.PrimeiraClasse'>
print(obj1)  # <__main__.PrimeiraClasse object at 0x...>
```

### **Classe com atributos simples**

```python
class Carro:
    def __init__(self):
        self.marca = "Ford"
        self.modelo = "Ka"
        self.ano = 2020

# Criando objetos
carro1 = Carro()
carro2 = Carro()

print(f"Carro 1: {carro1.marca} {carro1.modelo} {carro1.ano}")
print(f"Carro 2: {carro2.marca} {carro2.modelo} {carro2.ano}")
```

**Problema**: Todos os carros são iguais! Vamos resolver isso na próxima aula...

---

## **Aula 3: Método `__init__` e Atributos de Instância**

### 📖 **O método especial `__init__`**

O `__init__` é o **construtor** da classe - é executado automaticamente quando criamos um objeto.

```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0  # valor padrão
    
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"Vrum! Velocidade: {self.velocidade} km/h")
    
    def frear(self, decremento):
        self.velocidade = max(0, self.velocidade - decremento)
        print(f"Freou! Velocidade: {self.velocidade} km/h")

# Agora podemos criar carros diferentes!
carro1 = Carro("Fiat", "Uno", 2019)
carro2 = Carro("Volkswagen", "Gol", 2022)
carro3 = Carro("Chevrolet", "Onix", 2023)

print(f"Carro 1: {carro1.marca} {carro1.modelo} {carro1.ano}")
print(f"Carro 2: {carro2.marca} {carro2.modelo} {carro2.ano}")

# Testando métodos
carro1.acelerar(30)
carro1.acelerar(20)
carro1.frear(15)
```

### 🎯 **Exercício prático 1: Classe Pessoa**

```python
class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.energia = 100
    
    def apresentar(self):
        return f"Olá! Me chamo {self.nome}, tenho {self.idade} anos e moro em {self.cidade}."
    
    def trabalhar(self, horas):
        gasto_energia = horas * 10
        self.energia = max(0, self.energia - gasto_energia)
        return f"{self.nome} trabalhou {horas}h. Energia restante: {self.energia}%"
    
    def dormir(self, horas):
        ganho_energia = horas * 15
        self.energia = min(100, self.energia + ganho_energia)
        return f"{self.nome} dormiu {horas}h. Energia atual: {self.energia}%"

# Testando
p1 = Pessoa("Ana", 25, "São Paulo")
print(p1.apresentar())
print(p1.trabalhar(4))
print(p1.dormir(8))
```

---

## **Aula 4: Atributos de Classe vs Atributos de Instância**

### 📖 **Entendendo a diferença**

```python
class Estudante:
    # Atributo de CLASSE (compartilhado por todos os objetos)
    escola = "Python Academy"
    total_estudantes = 0
    
    def __init__(self, nome, matricula):
        # Atributos de INSTÂNCIA (cada objeto tem o seu)
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        
        # Acessando atributo de classe
        Estudante.total_estudantes += 1
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    @classmethod
    def mudar_escola(cls, nova_escola):
        cls.escola = nova_escola

# Criando estudantes
est1 = Estudante("João", "2024001")
est2 = Estudante("Maria", "2024002")

# Atributos de instância são diferentes
print(f"Estudante 1: {est1.nome} - {est1.matricula}")
print(f"Estudante 2: {est2.nome} - {est2.matricula}")

# Atributo de classe é o mesmo para todos
print(f"Escola do {est1.nome}: {est1.escola}")
print(f"Escola do {est2.nome}: {est2.escola}")
print(f"Total de estudantes: {Estudante.total_estudantes}")

# Mudando atributo de classe
Estudante.mudar_escola("Python Master")
print(f"Nova escola: {est1.escola}")  # Mudou para todos!
```

### 🎯 **Quando usar cada um?**

| Atributo de Classe | Atributo de Instância |
|-------------------|----------------------|
| Valores compartilhados | Valores únicos por objeto |
| Configurações globais | Dados específicos |
| Contadores | Estado individual |
| Constantes | Variáveis mutáveis |

---

## **Aula 5: Métodos de Instância**

### 📖 **Métodos que operam nos dados do objeto**

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.transacoes = []
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: +R${valor:.2f}")
            return True
        return False
    
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f"Saque: -R${valor:.2f}")
            return True
        return False
    
    def ver_extrato(self):
        print(f"\n=== EXTRATO DE {self.titular} ===")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("Últimas transações:")
        for transacao in self.transacoes[-5:]:  # últimas 5
            print(f"  {transacao}")
    
    def pode_comprar(self, valor):
        return self.saldo >= valor

# Testando
conta = ContaBancaria("Carlos", 1000)
conta.depositar(500)
conta.sacar(200)
conta.sacar(50)
conta.ver_extrato()
print(f"Pode comprar algo de R$800? {conta.pode_comprar(800)}")
print(f"Pode comprar algo de R$1500? {conta.pode_comprar(1500)}")
```

---

## **Aula 6: Parâmetro `self` - Entendendo sua Importância**

### 📖 **O que é `self`?**

`self` é uma referência ao próprio objeto. É o primeiro parâmetro de todos os métodos de instância.

```python
class ExplicacaoSelf:
    def __init__(self, valor):
        print(f"Criando objeto na posição de memória: {id(self)}")
        self.valor = valor
    
    def mostrar(self):
        print(f"self é: {self}")
        print(f"valor deste objeto é: {self.valor}")
    
    def comparar(self, outro):
        if self.valor == outro.valor:
            print(f"{self.valor} é igual a {outro.valor}")
        else:
            print(f"{self.valor} é diferente de {outro.valor}")

# Criando objetos
obj1 = ExplicacaoSelf(10)
obj2 = ExplicacaoSelf(20)

print(f"obj1 está em: {id(obj1)}")
print(f"obj2 está em: {id(obj2)}")

obj1.mostrar()
obj2.mostrar()

obj1.comparar(obj2)
```

### 🎯 **Regra de ouro**: Dentro da classe, sempre use `self` para acessar atributos e métodos!

---

## **Aula 7: Encapsulamento Básico (Convenções)**

### 📖 **Convenções de nomenclatura em Python**

Python não tem modificadores de acesso "fortes" como outras linguagens, mas usa convenções:

```python
class BancoSeguro:
    def __init__(self, titular, saldo):
        self.titular = titular           # Público (pode acessar fora)
        self._saldo = saldo              # "Protegido" (convenção: não acessar fora)
        self.__senha = "1234"             # "Privado" (name mangling)
    
    def get_saldo(self):
        return self._saldo
    
    def __validar_senha(self, senha):    # Método "privado"
        return senha == self.__senha
    
    def sacar(self, valor, senha):
        if self.__validar_senha(senha):
            if valor <= self._saldo:
                self._saldo -= valor
                return True
        return False

# Testando
conta = BancoSeguro("João", 1000)

# Acessando atributo público (OK)
print(conta.titular)  # João

# Acessando "protegido" (possível, mas NÃO RECOMENDADO)
print(conta._saldo)  # 1000 (funciona, mas é má prática)

# Acessando "privado" (dá erro - name mangling)
# print(conta.__senha)  # AttributeError!

# Mas ainda é possível acessar (por baixo dos panos)
print(conta._BancoSeguro__senha)  # 1234 (NÃO FAÇA ISSO!)

# Forma correta de interagir
conta.sacar(500, "1234")
print(f"Saldo após saque: {conta.get_saldo()}")
```

---

## **Aula 8: Propriedades com `@property`**

### 📖 **Getters e Setters elegantes em Python**

```python
class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter para celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        """Setter com validação"""
        if valor < -273.15:
            raise ValueError("Temperatura não pode ser menor que -273.15°C (zero absoluto)")
        self._celsius = valor
    
    @property
    def fahrenheit(self):
        """Propriedade calculada"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Converte Fahrenheit para Celsius"""
        self.celsius = (valor - 32) * 5/9
    
    def __str__(self):
        return f"{self.celsius:.1f}°C = {self.fahrenheit:.1f}°F"

# Usando de forma intuitiva!
temp = Temperatura(25)

print(temp.celsius)     # 25 (acessando como atributo)
print(temp.fahrenheit)  # 77.0 (propriedade calculada)

temp.celsius = 30       # Usando setter
print(temp)             # 30.0°C = 86.0°F

temp.fahrenheit = 100   # Configurando via Fahrenheit
print(temp)             # 37.8°C = 100.0°F

# temp.celsius = -300   # ValueError!
```

---

## **Aula 9: Getters e Setters em Python**

### 📖 **Comparação de estilos**

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco
        self._desconto = 0
    
    # Estilo Java (não-pythônico)
    def get_preco(self):
        return self._preco
    
    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self._preco = novo_preco
        else:
            raise ValueError("Preço deve ser positivo")
    
    # Estilo Python com @property (pythônico)
    @property
    def preco(self):
        return self._preco * (1 - self._desconto)
    
    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self._preco = valor
        else:
            raise ValueError("Preço deve ser positivo")
    
    @property
    def desconto(self):
        return self._desconto * 100
    
    @desconto.setter
    def desconto(self, percentual):
        if 0 <= percentual <= 50:
            self._desconto = percentual / 100
        else:
            raise ValueError("Desconto deve ser entre 0% e 50%")
    
    def __str__(self):
        preco_original = self._preco
        preco_final = self.preco
        return f"{self.nome}: R${preco_final:.2f} (de R${preco_original:.2f})"

# Testando
produto = Produto("Notebook", 3000)
print(produto.preco)  # 3000 (com getter)

produto.desconto = 10  # Aplicando 10% de desconto
print(produto)  # Notebook: R$2700.00 (de R$3000.00)

# produto.desconto = 60  # ValueError!
```

---

## **Aula 10: Projeto Prático 1 - Classe Pessoa Avançada**

### 🏆 **Projeto completo com tudo que aprendemos**

```python
from datetime import datetime
import re

class Pessoa:
    # Atributos de classe
    especie = "Humano"
    total_pessoas = 0
    
    def __init__(self, nome, data_nascimento, cpf, email):
        # Atributos públicos
        self.nome = nome
        
        # Atributos "protegidos" (com validação)
        self._data_nascimento = self._validar_data(data_nascimento)
        self._cpf = self._validar_cpf(cpf)
        self._email = self._validar_email(email)
        
        # Atributos privados
        self.__id = Pessoa.total_pessoas + 1
        self.__contato_emergencia = None
        self.__historico = []
        
        # Incrementa contador
        Pessoa.total_pessoas += 1
        
        # Registra criação
        self._adicionar_ao_historico("Pessoa criada")
    
    # Propriedades
    @property
    def idade(self):
        """Calcula idade baseado na data de nascimento"""
        hoje = datetime.now()
        nascimento = datetime.strptime(self._data_nascimento, "%d/%m/%Y")
        idade = hoje.year - nascimento.year
        
        # Ajuste se ainda não fez aniversário este ano
        if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
            idade -= 1
        
        return idade
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo_email):
        self._email = self._validar_email(novo_email)
        self._adicionar_ao_historico(f"Email alterado para {novo_email}")
    
    @property
    def contato_emergencia(self):
        return self.__contato_emergencia
    
    @contato_emergencia.setter
    def contato_emergencia(self, contato):
        if isinstance(contato, dict) and 'nome' in contato and 'telefone' in contato:
            self.__contato_emergencia = contato
            self._adicionar_ao_historico(f"Contato de emergência definido: {contato['nome']}")
        else:
            raise ValueError("Contato deve ser um dicionário com 'nome' e 'telefone'")
    
    @property
    def id(self):
        return self.__id
    
    # Métodos de validação (privados)
    def _validar_data(self, data):
        """Valida formato da data"""
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data deve estar no formato DD/MM/AAAA")
    
    def _validar_cpf(self, cpf):
        """Validação básica de CPF"""
        cpf_limpo = re.sub(r'[^0-9]', '', cpf)
        if len(cpf_limpo) != 11:
            raise ValueError("CPF deve ter 11 dígitos")
        return cpf_limpo
    
    def _validar_email(self, email):
        """Validação básica de email"""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(padrao, email):
            raise ValueError("Email inválido")
        return email
    
    def _adicionar_ao_historico(self, evento):
        """Adiciona evento ao histórico privado"""
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__historico.append(f"[{timestamp}] {evento}")
    
    # Métodos públicos
    def aniversario(self):
        """Comemora aniversário"""
        self._adicionar_ao_historico("Fez aniversário!")
        return f"🎂 Parabéns, {self.nome}! Agora você tem {self.idade} anos!"
    
    def mostrar_historico(self, ultimos=5):
        """Mostra últimas entradas do histórico"""
        print(f"\n=== HISTÓRICO DE {self.nome.upper()} ===")
        for evento in self.__historico[-ultimos:]:
            print(evento)
    
    def cpf_mascarado(self):
        """Retorna CPF com máscara"""
        return f"***.{self._cpf[3:6]}.{self._cpf[6:9]}-**"
    
    def __str__(self):
        """Representação amigável do objeto"""
        return f"👤 {self.nome} ({self.idade} anos) - ID: {self.__id}"
    
    def __repr__(self):
        """Representação técnica do objeto"""
        return f"Pessoa(nome='{self.nome}', cpf='{self.cpf_mascarado()}')"
    
    # Método de classe
    @classmethod
    def from_string(cls, string_dados):
        """Cria pessoa a partir de string (método factory)"""
        # Formato esperado: "Nome;DD/MM/AAAA;CPF;email"
        nome, data, cpf, email = string_dados.split(';')
        return cls(nome, data, cpf, email)
    
    @classmethod
    def resumo(cls):
        """Mostra resumo da classe"""
        return f"👥 Total de pessoas criadas: {cls.total_pessoas}"


# ===== TESTANDO NOSSA CLASSE =====

print("=== CRIANDO PESSOAS ===\n")

# Criando pessoas de diferentes formas
pessoa1 = Pessoa("João Silva", "15/05/1990", "123.456.789-00", "joao@email.com")
pessoa2 = Pessoa.from_string("Maria Santos;20/12/1985;98765432100;maria@email.com")

# Testando propriedades
print(pessoa1)
print(pessoa2)
print(f"Email da Maria: {pessoa2.email}")

# Testando idade calculada
print(f"\nIdade do João: {pessoa1.idade} anos")

# Modificando email
pessoa1.email = "joao.silva@novoemail.com"

# Adicionando contato de emergência
pessoa1.contato_emergencia = {
    'nome': 'Maria Silva',
    'telefone': '(11) 99999-9999',
    'parentesco': 'Mãe'
}

# Testando métodos
print(pessoa1.aniversario())
print(f"CPF mascarado: {pessoa1.cpf_mascarado()}")

# Mostrando histórico
pessoa1.mostrar_historico()

# Testando resumo da classe
print(f"\n{Pessoa.resumo()}")

# Testando representações
print(f"\nRepresentação string: {pessoa2}")
print(f"Representação técnica: {repr(pessoa2)}")

# ===== DESAFIO EXTRA =====

class Professor(Pessoa):
    """Extensão da classe Pessoa para professores"""
    def __init__(self, nome, data_nascimento, cpf, email, materia, salario):
        super().__init__(nome, data_nascimento, cpf, email)
        self.materia = materia
        self._salario = salario
        self._turmas = []
    
    @property
    def salario_anual(self):
        return self._salario * 13  # 13º salário incluído
    
    def adicionar_turma(self, turma):
        self._turmas.append(turma)
        self._adicionar_ao_historico(f"Nova turma atribuída: {turma}")
    
    def __str__(self):
        return f"👨‍🏫 Prof. {self.nome} - {self.materia}"

# Testando Professor
print("\n=== TESTANDO HERANÇA ===")
prof = Professor("Carlos Matemático", "10/03/1980", "11122233344", 
                 "carlos@escola.com", "Matemática", 5000)
print(prof)
print(f"Salário anual: R${prof.salario_anual:.2f}")
prof.adicionar_turma("Turma A - 9º ano")
prof.mostrar_historico()
```

### 📝 **Exercícios para praticar:**

1. **Adicione validação de telefone** à classe Pessoa
2. **Crie um método** que calcula quantos dias faltam para o próximo aniversário
3. **Implemente um sistema de tags/etiquetas** para categorizar pessoas
4. **Crie a classe Aluno** que herda de Pessoa, adicionando matrícula e notas
5. **Adicione um método** que permite comparar duas pessoas pela idade

### ✅ **Checklist do Módulo 1**
- [ ] Entendi a diferença entre classe e objeto
- [ ] Sei criar classes com __init__
- [ ] Compreendo atributos de classe vs instância
- [ ] Crio métodos de instância com self
- [ ] Uso convenções de encapsulamento
- [ ] Implemento propriedades com @property
- [ ] Completei o projeto Classe Pessoa

---

**Parabéns!** 🎉 Você completou o Módulo 1! Agora você já entende os fundamentos da POO em Python. Na próximo módulo, vamos explorar **Herança e Polimorfismo** para criar hierarquias de classes mais complexas e poderosas!

Tem alguma dúvida sobre o que vimos até aqui? Ou podemos prosseguir para o Módulo 2?
