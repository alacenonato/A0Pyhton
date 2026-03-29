Excelente! Vamos começar o **Módulo 2: Herança e Polimorfismo**.

Como você já tem uma base do Módulo 1 (criação de classes, `__init__`, métodos e encapsulamento básico), agora vamos avançar para um dos pilares mais poderosos da POO: a **reutilização de código** através da herança.

## Módulo 2: Herança e Polimorfismo

### Aula 11: Herança Simples

**Conceito:**
Herança é um mecanismo que permite que uma classe (filha) herde atributos e métodos de outra classe (pai). Isso evita a duplicação de código e estabelece uma relação de "é um" (ex: `Cachorro` **é um** `Animal`).

```python
# Classe base (Pai/Superclasse)
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_som(self):
        return "Algum som genérico de animal"
    
    def info(self):
        return f"{self.nome}, {self.idade} anos"

# Classe derivada (Filha/Subclasse)
class Cachorro(Animal):  # Herda de Animal
    def fazer_som(self):  # Sobrescrita de método
        return "Au au!"
    
    def abanar_rabo(self):  # Método específico da subclasse
        return f"{self.nome} está abanando o rabo!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
    
    def arranhar_moveis(self):
        return f"{self.nome} está arranhando o sofá!"

# Testando
rex = Cachorro("Rex", 3)
mingau = Gato("Mingau", 2)

print(rex.info())           # Herdado de Animal
print(rex.fazer_som())      # Sobrescrito
print(rex.abanar_rabo())    # Próprio da classe

print(mingau.info())        # Herdado
print(mingau.fazer_som())   # Sobrescrito
print(mingau.arranhar_moveis())
```

---

### Aula 12: Sobrescrita de Métodos (Override)

**Conceito:**
A classe filha pode fornecer uma implementação específica para um método já existente na classe pai. Isso é chamado de sobrescrita.

```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
    
    def acelerar(self, incremento):
        self.velocidade += incremento
        return f"Acelerando para {self.velocidade} km/h"
    
    def descricao(self):
        return f"Veículo: {self.marca} {self.modelo}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        # Chamando o construtor da classe pai
        super().__init__(marca, modelo)
        self.portas = portas
    
    def acelerar(self, incremento):
        # Sobrescrita completa
        self.velocidade += incremento * 1.2  # Carro acelera mais rápido
        return f"Carro acelerando para {self.velocidade:.0f} km/h"
    
    def descricao(self):
        # Usando método da classe pai e complementando
        return f"{super().descricao()} - {self.portas} portas"

class Moto(Veiculo):
    def acelerar(self, incremento):
        self.velocidade += incremento * 0.8  # Moto acelera mais devagar?
        return f"Moto acelerando para {self.velocidade:.0f} km/h"

# Testando
carro = Carro("Toyota", "Corolla", 4)
moto = Moto("Honda", "CB500")

print(carro.descricao())
print(carro.acelerar(50))

print(moto.descricao())
print(moto.acelerar(50))
```

---

### Aula 13: A Função `super()`

**Conceito:**
`super()` permite chamar métodos da classe pai explicitamente. É essencial quando queremos estender (e não substituir completamente) o comportamento herdado.

```python
class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    def calcular_pagamento(self):
        return self.salario_base
    
    def __str__(self):
        return f"Funcionário: {self.nome}"

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        # super() chama o __init__ da classe pai
        super().__init__(nome, salario_base)
        self.bonus = bonus
    
    def calcular_pagamento(self):
        # super() chama o método da classe pai e complementa
        pagamento_base = super().calcular_pagamento()
        return pagamento_base + self.bonus
    
    def __str__(self):
        # Usando a representação da classe pai
        return f"{super().__str__()} (Gerente com bônus de R${self.bonus})"

class Estagiario(Funcionario):
    def __init__(self, nome, salario_base, desconto_estagio=200):
        super().__init__(nome, salario_base)
        self.desconto_estagio = desconto_estagio
    
    def calcular_pagamento(self):
        return super().calcular_pagamento() - self.desconto_estagio

# Testando
func = Funcionario("João", 2000)
gerente = Gerente("Maria", 5000, 1500)
estag = Estagiario("Pedro", 1200)

print(f"{func}: R${func.calcular_pagamento():.2f}")
print(f"{gerente}: R${gerente.calcular_pagamento():.2f}")
print(f"{estag}: R${estag.calcular_pagamento():.2f}")
```

**Importante:** Sempre use `super()` em vez de chamar a classe pai diretamente (`ClassePai.metodo(self)`). O `super()` lida corretamente com herança múltipla e torna o código mais manutenível.

---

### Aula 14: Herança Múltipla

**Conceito:**
Python permite que uma classe herde de múltiplas classes pais. Isso é poderoso, mas requer cuidado para evitar ambiguidades.

```python
class Trabalhador:
    def __init__(self, profissao):
        self.profissao = profissao
    
    def trabalhar(self):
        return f"Trabalhando como {self.profissao}"

class Estudante:
    def __init__(self, curso):
        self.curso = curso
    
    def estudar(self):
        return f"Estudando {self.curso}"

class Estagiario(Trabalhador, Estudante):
    def __init__(self, nome, profissao, curso, horas_trabalho):
        # Inicializando as classes pai
        Trabalhador.__init__(self, profissao)
        Estudante.__init__(self, curso)
        self.nome = nome
        self.horas_trabalho = horas_trabalho
    
    def rotina(self):
        return f"{self.nome}: {self.trabalhar()} e {self.estudar()}"

# Testando
estag = Estagiario("Ana", "Assistente", "Engenharia", 6)
print(estag.rotina())
print(f"Profissão: {estag.profissao}")
print(f"Curso: {estag.curso}")
```

**Exemplo mais complexo - Classe Mista:**

```python
class Eletronico:
    def __init__(self, tensao):
        self.tensao = tensao
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
        return "Aparelho ligado"
    
    def desligar(self):
        self.ligado = False
        return "Aparelho desligado"

class Comunicacao:
    def __init__(self, protocolo):
        self.protocolo = protocolo
    
    def enviar_dados(self, dados):
        return f"Enviando dados via {self.protocolo}: {dados}"

class Smartphone(Eletronico, Comunicacao):
    def __init__(self, tensao, protocolo, modelo):
        Eletronico.__init__(self, tensao)
        Comunicacao.__init__(self, protocolo)
        self.modelo = modelo
    
    def fazer_chamada(self, numero):
        if self.ligado:
            return f"Chamando {numero}..."
        return "Aparelho desligado. Ligue primeiro."

iphone = Smartphone(110, "5G", "iPhone 15")
print(iphone.ligar())
print(iphone.enviar_dados("Foto"))
print(iphone.fazer_chamada("99999-9999"))
```

---

### Aula 15: Method Resolution Order (MRO)

**Conceito:**
MRO é a ordem em que Python procura métodos em uma hierarquia de classes, especialmente importante em herança múltipla.

```python
class A:
    def metodo(self):
        return "Método de A"

class B(A):
    def metodo(self):
        return "Método de B"

class C(A):
    def metodo(self):
        return "Método de C"

class D(B, C):  # Herda de B e C (que herdam de A)
    pass

# Verificando a MRO
print("MRO de D:")
for classe in D.__mro__:
    print(f"  {classe.__name__}")

print(f"\nChamando metodo(): {D().metodo()}")

# Exemplo mais complexo
class X:
    def acao(self):
        return "X"

class Y:
    def acao(self):
        return "Y"

class Z(X, Y):
    pass

class W(Y, X):
    pass

print(f"Z.acao(): {Z().acao()}")  # Vai executar X.acao() (X vem primeiro)
print(f"W.acao(): {W().acao()}")  # Vai executar Y.acao() (Y vem primeiro)

# Visualizando MRO
print("\nMRO de Z:", [cls.__name__ for cls in Z.__mro__])
print("MRO de W:", [cls.__name__ for cls in W.__mro__])
```

**Regra do MRO (Algoritmo C3):**
1. Uma classe sempre aparece antes de seus pais
2. Se múltiplos pais, a ordem de herança é respeitada
3. Mantém consistência em toda hierarquia

---

### Aula 16: Polimorfismo - Conceito e Aplicação

**Conceito:**
Polimorfismo significa "muitas formas". Em POO, é a capacidade de objetos de diferentes classes responderem ao mesmo método de maneiras diferentes.

```python
class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio ** 2

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2

# Função polimórfica - aceita qualquer objeto que tenha método area()
def calcular_area_total(forms):
    total = 0
    for forma in forms:
        total += forma.area()
    return total

# Criando lista de formas diferentes
formas = [
    Retangulo(10, 5),
    Circulo(3),
    Triangulo(6, 4),
    Retangulo(7, 3)
]

# Mesma chamada, comportamentos diferentes
for forma in formas:
    print(f"{forma.__class__.__name__}: {forma.area():.2f}")

print(f"Área total: {calcular_area_total(formas):.2f}")
```

---

### Aula 17: Duck Typing em Python

**Conceito:**
"Duck typing" vem do ditado: "Se anda como um pato, nada como um pato e grasna como um pato, então é um pato". Em Python, não verificamos o tipo do objeto, mas sim se ele tem os métodos/atributos que precisamos.

```python
class Pato:
    def falar(self):
        return "Quack!"
    
    def andar(self):
        return "Andando como pato"

class Pessoa:
    def falar(self):
        return "Olá, eu sou uma pessoa!"
    
    def andar(self):
        return "Andando sobre duas pernas"

class Carro:
    def buzinar(self):
        return "Bip bip!"
    
    def andar(self):
        return "Rodas girando"

# Função que usa duck typing - não importa a classe, só se tem os métodos
def fazer_barulho(objeto):
    if hasattr(objeto, 'falar'):
        return objeto.falar()
    elif hasattr(objeto, 'buzinar'):
        return objeto.buzinar()
    else:
        return "Não sei fazer barulho"

def fazer_andar(objeto):
    # Duck typing - se tem método andar, podemos usar
    if hasattr(objeto, 'andar'):
        return objeto.andar()
    return "Não sei andar"

# Testando
pato = Pato()
pessoa = Pessoa()
carro = Carro()

print(f"Pato: {fazer_barulho(pato)}")
print(f"Pessoa: {fazer_barulho(pessoa)}")
print(f"Carro: {fazer_barulho(carro)}")

print(f"\nAndar pato: {fazer_andar(pato)}")
print(f"Andar pessoa: {fazer_andar(pessoa)}")
print(f"Andar carro: {fazer_andar(carro)}")
```

---

### Aula 18: Classes Abstratas com ABC

**Conceito:**
Classes abstratas são "modelos" para outras classes. Elas não podem ser instanciadas diretamente e definem métodos que **devem** ser implementados pelas classes filhas.

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Herda de ABC para ser abstrata
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def fazer_som(self):
        """Método abstrato - deve ser implementado pelas filhas"""
        pass
    
    @abstractmethod
    def mover(self):
        pass
    
    # Método concreto (não abstrato) - pode ser usado diretamente
    def dormir(self):
        return f"{self.nome} está dormindo..."

class Cachorro(Animal):
    def fazer_som(self):  # Obrigatório implementar
        return "Au au!"
    
    def mover(self):      # Obrigatório implementar
        return "Correndo com 4 patas"

class Peixe(Animal):
    def fazer_som(self):
        return "Glub glub"
    
    def mover(self):
        return "Nadando"

# Testando
# animal = Animal("Genérico")  # Erro! Não pode instanciar classe abstrata

rex = Cachorro("Rex")
nemo = Peixe("Nemo")

print(rex.fazer_som())
print(rex.mover())
print(rex.dormir())

print(nemo.fazer_som())
print(nemo.mover())
```

---

### Aula 19: Métodos Abstratos

**Conceito:**
Métodos abstratos são como "contratos" que as classes filhas devem cumprir. Podemos ter diferentes níveis de abstração.

```python
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self, cor):
        self.cor = cor
    
    @abstractmethod
    def calcular_area(self):
        """Calcula a área da forma"""
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        """Calcula o perímetro da forma"""
        pass
    
    # Método concreto - já tem implementação
    def descricao(self):
        return f"Sou uma forma {self.cor} com área {self.calcular_area():.2f}"

class Quadrado(FormaGeometrica):
    def __init__(self, cor, lado):
        super().__init__(cor)
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado

class CirculoAbstrato(FormaGeometrica):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio
    
    def calcular_area(self):
        return 3.14 * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * 3.14 * self.raio

# Testando
quadrado = Quadrado("vermelho", 5)
circulo = CirculoAbstrato("azul", 3)

print(quadrado.descricao())
print(f"Perímetro: {quadrado.calcular_perimetro()}")

print(circulo.descricao())
print(f"Perímetro: {circulo.calcular_perimetro():.2f}")
```

---

### Aula 20: Projeto Prático 2 - Sistema de Funcionários

Agora vamos consolidar tudo que aprendemos com um sistema completo!

```python
from abc import ABC, abstractmethod
from datetime import datetime

# ========== CLASSE ABSTRATA BASE ==========
class Funcionario(ABC):
    def __init__(self, nome, cpf, data_admissao):
        self.nome = nome
        self.cpf = cpf
        self.data_admissao = data_admissao
        self._bonificacoes = []
    
    @abstractmethod
    def calcular_salario(self):
        """Calcula o salário do funcionário"""
        pass
    
    def adicionar_bonificacao(self, valor, motivo):
        self._bonificacoes.append({
            'valor': valor,
            'motivo': motivo,
            'data': datetime.now()
        })
    
    def calcular_total_bonificacoes(self):
        return sum(b['valor'] for b in self._bonificacoes)
    
    def tempo_servico(self):
        """Calcula anos de serviço"""
        dias = (datetime.now() - self.data_admissao).days
        return round(dias / 365, 1)
    
    def __str__(self):
        return f"{self.nome} - {self.__class__.__name__}"

# ========== FUNCIONÁRIOS CLT ==========
class FuncionarioCLT(Funcionario):
    def __init__(self, nome, cpf, data_admissao, salario_base, vale_transporte=True):
        super().__init__(nome, cpf, data_admissao)
        self.salario_base = salario_base
        self.vale_transporte = vale_transporte
    
    def calcular_salario(self):
        salario = self.salario_base
        
        # Desconto INSS (simplificado)
        inss = salario * 0.08
        salario -= inss
        
        # Desconto Vale Transporte (6% se optante)
        if self.vale_transporte:
            vt = self.salario_base * 0.06
            salario -= vt
        
        # Adiciona bonificações
        salario += self.calcular_total_bonificacoes()
        
        return salario
    
    def __str__(self):
        return f"{super().__str__()} - R$ {self.calcular_salario():.2f}"

class Desenvolvedor(FuncionarioCLT):
    def __init__(self, nome, cpf, data_admissao, salario_base, linguagens, vale_transporte=True):
        super().__init__(nome, cpf, data_admissao, salario_base, vale_transporte)
        self.linguagens = linguagens
        self.projetos = []
    
    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)
    
    def calcular_salario(self):
        salario = super().calcular_salario()
        
        # Bônus por projetos concluídos
        bonus_projetos = len(self.projetos) * 100
        salario += bonus_projetos
        
        return salario

class Gerente(FuncionarioCLT):
    def __init__(self, nome, cpf, data_admissao, salario_base, departamento, vale_transporte=True):
        super().__init__(nome, cpf, data_admissao, salario_base, vale_transporte)
        self.departamento = departamento
        self.equipe = []
    
    def adicionar_funcionario(self, funcionario):
        self.equipe.append(funcionario)
    
    def calcular_salario(self):
        salario = super().calcular_salario()
        
        # Bônus por gerenciar equipe
        bonus_gestao = len(self.equipe) * 150
        salario += bonus_gestao
        
        return salario

# ========== FUNCIONÁRIOS PJ ==========
class FuncionarioPJ(Funcionario):
    def __init__(self, nome, cpf, data_admissao, valor_hora):
        super().__init__(nome, cpf, data_admissao)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = 0
    
    def registrar_horas(self, horas):
        self.horas_trabalhadas += horas
    
    def calcular_salario(self):
        return (self.valor_hora * self.horas_trabalhadas) + self.calcular_total_bonificacoes()

class Consultor(FuncionarioPJ):
    def __init__(self, nome, cpf, data_admissao, valor_hora, especialidade):
        super().__init__(nome, cpf, data_admissao, valor_hora)
        self.especialidade = especialidade
    
    def calcular_salario(self):
        salario = super().calcular_salario()
        
        # Consultores têm hora mais valorizada
        if self.horas_trabalhadas > 160:  # Horas extras
            salario *= 1.1  # 10% de bônus
        
        return salario

# ========== FUNCIONÁRIOS TERCEIRIZADOS ==========
class Terceirizado(Funcionario):
    def __init__(self, nome, cpf, data_admissao, empresa_terceira, valor_contrato):
        super().__init__(nome, cpf, data_admissao)
        self.empresa_terceira = empresa_terceira
        self.valor_contrato = valor_contrato
    
    def calcular_salario(self):
        # Terceirizados recebem um valor fixo do contrato
        return self.valor_contrato

# ========== SISTEMA DE GESTÃO ==========
class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
    
    def contratar(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"{funcionario.nome} contratado para {self.nome}")
    
    def demitir(self, funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            print(f"{funcionario.nome} demitido de {self.nome}")
    
    def folha_pagamento(self):
        total = 0
        print(f"\n=== FOLHA DE PAGAMENTO - {self.nome} ===")
        for func in self.funcionarios:
            salario = func.calcular_salario()
            print(f"  {func.nome}: R$ {salario:.2f}")
            total += salario
        print(f"  {'='*30}")
        print(f"  TOTAL: R$ {total:.2f}")
        return total

class Empresa:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.departamentos = []
    
    def criar_departamento(self, nome):
        dept = Departamento(nome)
        self.departamentos.append(dept)
        return dept
    
    def relatorio_geral(self):
        print(f"\n{'='*50}")
        print(f"RELATÓRIO GERAL - {self.nome}")
        print(f"{'='*50}")
        
        total_empresa = 0
        for dept in self.departamentos:
            total_dept = dept.folha_pagamento()
            total_empresa += total_dept
        
        print(f"\nTOTAL DA EMPRESA: R$ {total_empresa:.2f}")
        
        # Estatísticas
        total_func = sum(len(d.funcionarios) for d in self.departamentos)
        print(f"Total de funcionários: {total_func}")
        
        return total_empresa

# ========== EXEMPLO DE USO ==========
if __name__ == "__main__":
    # Criando empresa
    techcorp = Empresa("TechCorp Solutions", "12.345.678/0001-90")
    
    # Criando departamentos
    ti = techcorp.criar_departamento("Tecnologia")
    rh = techcorp.criar_departamento("Recursos Humanos")
    vendas = techcorp.criar_departamento("Vendas")
    
    # Contratando funcionários (com datas)
    data_admissao = datetime(2020, 3, 15)
    
    # Desenvolvedores
    dev1 = Desenvolvedor(
        "Ana Silva", 
        "123.456.789-00", 
        data_admissao, 
        5000, 
        ["Python", "JavaScript", "SQL"]
    )
    dev1.adicionar_projeto("Sistema Web")
    dev1.adicionar_projeto("API REST")
    dev1.adicionar_bonificacao(300, "Projeto entregue antes do prazo")
    
    dev2 = Desenvolvedor(
        "Carlos Santos", 
        "987.654.321-00", 
        datetime(2021, 6, 10), 
        4500, 
        ["Java", "Spring"]
    )
    
    # Gerente
    gerente_ti = Gerente(
        "Mariana Costa", 
        "456.789.123-00", 
        datetime(2019, 1, 5), 
        8000, 
        "Tecnologia"
    )
    gerente_ti.adicionar_funcionario(dev1)
    gerente_ti.adicionar_funcionario(dev2)
    gerente_ti.adicionar_bonificacao(1000, "Bônus anual")
    
    # Consultor PJ
    consultor = Consultor(
        "Roberto Alves", 
        "789.123.456-00", 
        datetime(2023, 1, 10), 
        120,  # R$ 120/hora
        "Segurança da Informação"
    )
    consultor.registrar_horas(160)
    consultor.registrar_horas(20)  # Horas extras
    
    # Terceirizado
    terceirizado = Terceirizado(
        "João Lima", 
        "321.654.987-00", 
        datetime(2023, 5, 20), 
        "Limpeza Express Ltda", 
        1800
    )
    
    # Contratando
    ti.contratar(dev1)
    ti.contratar(dev2)
    ti.contratar(gerente_ti)
    ti.contratar(consultor)
    ti.contratar(terceirizado)
    
    # RH contratando
    analista_rh = FuncionarioCLT("Paula Mendes", "159.753.486-00", datetime(2022, 2, 1), 3500)
    rh.contratar(analista_rh)
    
    # Vendas contratando
    vendedor1 = FuncionarioCLT("Pedro Souza", "951.753.852-00", datetime(2023, 3, 1), 2500, False)
    vendedor2 = FuncionarioCLT("Lucia Ferreira", "852.963.741-00", datetime(2023, 6, 1), 2800)
    vendas.contratar(vendedor1)
    vendas.contratar(vendedor2)
    
    # Gerando relatórios
    techcorp.relatorio_geral()
    
    # Demonstração de polimorfismo
    print("\n=== DEMONSTRAÇÃO DE POLIMORFISMO ===")
    funcionarios = [dev1, gerente_ti, consultor, terceirizado, analista_rh]
    
    for func in funcionarios:
        print(f"{func.nome} ({func.__class__.__name__}):")
        print(f"  Salário: R$ {func.calcular_salario():.2f}")
        print(f"  Tempo de serviço: {func.tempo_servico()} anos")
        if hasattr(func, 'linguagens'):
            print(f"  Linguagens: {', '.join(func.linguagens)}")
        print()
```

---

### Exercícios do Módulo 2

1. **Básico:** Crie uma hierarquia de `Veiculo` com classes `Carro` e `Moto`. Cada uma deve ter um método `calcular_consumo` diferente.

2. **Intermediário:** Implemente um sistema de `ContaBancaria` com classes `ContaCorrente` e `ContaPoupanca`. Use métodos abstratos para `sacar` e `calcular_rendimento`.

3. **Avançado:** Crie um sistema de `Notificacao` usando herança múltipla. Combine classes `EmailNotificador` e `SMSNotificador` para criar `NotificadorCompleto`.

4. **Desafio:** Implemente um mini framework de validação usando classes abstratas, onde cada validador (CPF, Email, Idade) deve implementar um método `validar`.

---

### Resumo do Módulo 2

| Conceito | Descrição | Uso Principal |
|----------|-----------|---------------|
| Herança Simples | Classe filha herda da classe pai | Reutilização de código |
| `super()` | Chama métodos da classe pai | Estender comportamento |
| Sobrescrita | Redefinir métodos na filha | Especialização |
| Herança Múltipla | Herdar de várias classes | Combinar funcionalidades |
| MRO | Ordem de resolução de métodos | Resolver ambiguidades |
| Polimorfismo | Mesmo método, comportamentos diferentes | Flexibilidade |
| Duck Typing | "Se parece com pato..." | Pythonic way |
| Classes Abstratas | Classes que não podem ser instanciadas | Definir contratos |
| Métodos Abstratos | Métodos que devem ser implementados | Garantir implementação |

**Próximo Módulo:** Vamos aprofundar em Encapsulamento Avançado, modificadores de acesso e propriedades!

Quer que eu continue para o Módulo 3 ou prefere praticar mais com os exercícios do Módulo 2?
