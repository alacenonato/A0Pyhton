---

# 💱 Conversor de Moedas PRO (Python + PySide6)

Aplicação desktop desenvolvida em Python com interface gráfica moderna para conversão de moedas em tempo real.

---

# 🚀 Funcionalidades

* 🔄 Atualização automática de cotações
* 💱 Conversão de Real (BRL) para:

  * Dólar (USD)
  * Euro (EUR)
  * Libra (GBP)
* 📊 Histórico de conversões
* 🌙 Tema escuro (Dark Mode)
* 📁 Exportação:

  * Excel (.xlsx)
  * PDF (.pdf)
* 🖥️ Interface gráfica moderna (PySide6)

---

# 🧠 Tecnologias utilizadas

* Python 3
* PySide6 (interface gráfica)
* Requests (consumo de API)
* OpenPyXL (exportação Excel)
* ReportLab (exportação PDF)

---

# 📦 Instalação

## 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/conversor-moedas-pro.git
cd conversor-moedas-pro
```

---

## 2. Criar ambiente virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux
```

---

## 3. Instalar dependências

```bash
pip install PySide6 requests openpyxl reportlab
```

---

# ❓ Por que instalar essas dependências?

Cada biblioteca tem um papel específico no funcionamento do sistema:

### 🔹 PySide6

Responsável por toda a interface gráfica.

Sem ela:

* Não existe janela
* Não existe botão
* Não existe interação visual

👉 É o "frontend" do aplicativo desktop.

---

### 🔹 Requests

Responsável por buscar os dados da internet.

Neste projeto:

* Faz requisição HTTP para a API de moedas
* Recebe dados em JSON

Sem ela:

* As cotações não seriam atualizadas
* O sistema ficaria com valores fixos

---

### 🔹 OpenPyXL

Responsável por gerar arquivos Excel (.xlsx).

Sem ela:

* Não seria possível exportar o histórico para Excel

---

### 🔹 ReportLab

Responsável por gerar arquivos PDF.

Sem ela:

* Não seria possível exportar o histórico em PDF

---

# ▶️ Como executar

```bash
python app.py
```

---

# 🧩 Estrutura do código

## Classe principal: Conversor

A aplicação é baseada em Programação Orientada a Objetos (POO).

```python
class Conversor(QWidget):
```

Ela representa toda a janela do sistema.

---

## 🧱 Método `__init__`

Responsável por:

* Criar a interface
* Definir layout
* Configurar eventos
* Iniciar atualização automática

---

## 🧩 Widgets (Componentes)

* QLabel → textos
* QLineEdit → entrada de valor
* QComboBox → seleção de moeda
* QPushButton → botões
* QTextEdit → histórico

---

## 🔄 Atualização automática (QTimer)

```python
self.timer = QTimer()
self.timer.timeout.connect(self.atualizar_cotacao)
self.timer.start(10000)
```

Executa a função `atualizar_cotacao()` a cada 10 segundos.

---

## 🌐 Método `atualizar_cotacao`

* Faz requisição para API
* Atualiza as cotações em tempo real

---

## 💱 Método `converter`

Responsável por:

* Ler valor digitado
* Identificar moeda selecionada
* Calcular conversão
* Exibir resultado
* Salvar no histórico

---

## 📊 Histórico

```python
self.historico.append(registro)
```

Armazena todas as conversões realizadas durante a execução.

---

## 📁 Exportação Excel

```python
Workbook()
```

* Cria planilha
* Salva cada linha do histórico

---

## 📄 Exportação PDF

```python
SimpleDocTemplate()
```

* Cria documento PDF
* Adiciona cada conversão como parágrafo

---

## 🌙 Tema escuro

Aplicado com:

```python
self.setStyleSheet(...)
```

Define:

* Cor de fundo
* Estilo dos botões
* Aparência geral

---

# 🧠 Conceitos aplicados

* Programação Orientada a Objetos (POO)
* Consumo de API REST
* Manipulação de JSON
* Interface gráfica (GUI)
* Automação com Timer
* Exportação de arquivos
* Tratamento de erros

---

# 📦 Gerar executável

Instalar:

```bash
pip install pyinstaller
```

Gerar:

```bash
pyinstaller --onefile --windowed app.py
```

---

# 📌 Melhorias futuras

* Banco de dados (SQLite)
* Login de usuário
* Gráficos de moedas
* Mais moedas disponíveis
* Deploy web (Flask)

---

# 👨‍💻 Autor

Projeto desenvolvido para aprendizado e portfólio em Python.

---

# ⭐ Contribuição

Sinta-se livre para melhorar o projeto e enviar sugestões!

---

# 🚀 Resultado

Tenho:

* Código profissional ✅
* Documentação profissional ✅
* Projeto de portfólio forte ✅

---




