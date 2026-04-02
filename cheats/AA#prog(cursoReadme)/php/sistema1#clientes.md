
# prompt: 
### Pode fazer um miniprojeto de php com mysql de um sistema de clientes, com tela de cadastro, tela consulta podendo ter ações para editar, visualizar e excluir registros, usando o bootstrap para da um boa aparência ao sistema. Detalhe tambem a estrutura de arquivos do projeto, bem explicado. 

Claro! Abaixo está um miniprojeto em PHP com MySQL para um sistema de gerenciamento de clientes. Inclui telas para cadastro, consulta com ações de editar, visualizar e excluir registros, utilizando o Bootstrap para uma boa aparência. Também detalharei a estrutura de arquivos do projeto.

---

## Estrutura de Arquivos do Projeto

```
projeto_clientes/
├── index.php
├── adicionar_cliente.php
├── editar_cliente.php
├── visualizar_cliente.php
├── excluir_cliente.php
├── db.php
├── header.php
├── footer.php
├── css/
│   └── custom.css
```

### Descrição dos Arquivos

* **index.php**: Página principal que lista todos os clientes e permite ações de editar, visualizar e excluir.
* **adicionar_cliente.php**: Formulário para adicionar um novo cliente.
* **editar_cliente.php**: Formulário para editar um cliente existente.
* **visualizar_cliente.php**: Exibe detalhes de um cliente específico.
* **excluir_cliente.php**: Script para excluir um cliente do banco de dados.
* **db.php**: Arquivo de conexão com o banco de dados.
* **header.php** e **footer.php**: Cabeçalho e rodapé compartilhados entre as páginas para manter consistência.
* **css/custom.css**: Arquivo para estilos CSS personalizados.

---

## Configuração do Banco de Dados

Crie um banco de dados chamado `sistema_clientes` e uma tabela `clientes` com o seguinte script SQL:

```sql
CREATE DATABASE sistema_clientes;

USE sistema_clientes;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    endereco VARCHAR(255)
);
```

---

## Arquivos do Projeto

### db.php

Conexão com o banco de dados.

```php
<?php
$servername = "localhost";
$username = "seu_usuario";
$password = "sua_senha";
$dbname = "sistema_clientes";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Falha na conexão: " . $conn->connect_error);
}
?>
```

---

### header.php

Cabeçalho padrão para todas as páginas.

```php
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Gerenciamento de Clientes</title>
    <!-- CSS do Bootstrap -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <!-- CSS Personalizado -->
    <link rel="stylesheet" href="css/custom.css">
</head>
<body>
<div class="container">
    <h1 class="mt-5">Sistema de Gerenciamento de Clientes</h1>
```

---

### footer.php

Rodapé padrão para todas as páginas.

```php
</div>
<!-- JS do Bootstrap e dependências -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
</body>
</html>
```

---

### index.php

Página principal que lista os clientes.

```php
<?php include 'header.php'; ?>
<?php include 'db.php'; ?>

<a href="adicionar_cliente.php" class="btn btn-primary mb-3">Adicionar Novo Cliente</a>

<table class="table table-bordered">
    <thead>
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Email</th>
            <th>Telefone</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
    <?php
    $sql = "SELECT * FROM clientes";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while($cliente = $result->fetch_assoc()) {
            echo "<tr>
                <td>".$cliente['id']."</td>
                <td>".$cliente['nome']."</td>
                <td>".$cliente['email']."</td>
                <td>".$cliente['telefone']."</td>
                <td>
                    <a href='visualizar_cliente.php?id=".$cliente['id']."' class='btn btn-info btn-sm'>Visualizar</a>
                    <a href='editar_cliente.php?id=".$cliente['id']."' class='btn btn-warning btn-sm'>Editar</a>
                    <a href='excluir_cliente.php?id=".$cliente['id']."' class='btn btn-danger btn-sm' onclick='return confirm(\"Tem certeza que deseja excluir?\")'>Excluir</a>
                </td>
            </tr>";
        }
    } else {
        echo "<tr><td colspan='5'>Nenhum cliente encontrado.</td></tr>";
    }
    $conn->close();
    ?>
    </tbody>
</table>

<?php include 'footer.php'; ?>
```

---

### adicionar_cliente.php

Formulário para adicionar um novo cliente.

```php
<?php include 'header.php'; ?>
<?php include 'db.php'; ?>

<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $telefone = $_POST['telefone'];
    $endereco = $_POST['endereco'];
    
    $sql = "INSERT INTO clientes (nome, email, telefone, endereco) VALUES ('$nome', '$email', '$telefone', '$endereco')";
    if ($conn->query($sql) === TRUE) {
        echo "<div class='alert alert-success'>Novo cliente adicionado com sucesso.</div>";
    } else {
        echo "Erro: " . $sql . "<br>" . $conn->error;
    }
}
?>

<form action="adicionar_cliente.php" method="post">
    <div class="form-group">
        <label>Nome</label>
        <input type="text" name="nome" class="form-control" required>
    </div>
    <div class="form-group">
        <label>Email</label>
        <input type="email" name="email" class="form-control" required>
    </div>
    <div class="form-group">
        <label>Telefone</label>
        <input type="text" name="telefone" class="form-control">
    </div>
    <div class="form-group">
        <label>Endereço</label>
        <textarea name="endereco" class="form-control"></textarea>
    </div>
    <button type="submit" class="btn btn-primary">Adicionar Cliente</button>
</form>

<?php include 'footer.php'; ?>
```

---

### editar_cliente.php

Formulário para editar um cliente existente.

```php
<?php include 'header.php'; ?>
<?php include 'db.php'; ?>

<?php
$id = $_GET['id'];

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $telefone = $_POST['telefone'];
    $endereco = $_POST['endereco'];
    
    $sql = "UPDATE clientes SET nome='$nome', email='$email', telefone='$telefone', endereco='$endereco' WHERE id=$id";
    if ($conn->query($sql) === TRUE) {
        echo "<div class='alert alert-success'>Cliente atualizado com sucesso.</div>";
    } else {
        echo "Erro ao atualizar registro: " . $conn->error;
    }
}

$sql = "SELECT * FROM clientes WHERE id=$id";
$result = $conn->query($sql);
$cliente = $result->fetch_assoc();
?>

<form action="editar_cliente.php?id=<?php echo $id; ?>" method="post">
    <div class="form-group">
        <label>Nome</label>
        <input type="text" name="nome" class="form-control" value="<?php echo $cliente['nome']; ?>" required>
    </div>
    <div class="form-group">
        <label>Email</label>
        <input type="email" name="email" class="form-control" value="<?php echo $cliente['email']; ?>" required>
    </div>
    <div class="form-group">
        <label>Telefone</label>
        <input type="text" name="telefone" class="form-control" value="<?php echo $cliente['telefone']; ?>">
    </div>
    <div class="form-group">
        <label>Endereço</label>
        <textarea name="endereco" class="form-control"><?php echo $cliente['endereco']; ?></textarea>
    </div>
    <button type="submit" class="btn btn-primary">Atualizar Cliente</button>
</form>

<?php include 'footer.php'; ?>
```

---

### visualizar_cliente.php

Exibe detalhes de um cliente.

```php
<?php include 'header.php'; ?>
<?php include 'db.php'; ?>

<?php
$id = $_GET['id'];
$sql = "SELECT * FROM clientes WHERE id=$id";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    $cliente = $result->fetch_assoc();
} else {
    echo "<div class='alert alert-danger'>Cliente não encontrado.</div>";
    exit;
}
?>

<h2>Detalhes do Cliente</h2>
<p><strong>Nome:</strong> <?php echo $cliente['nome']; ?></p>
<p><strong>Email:</strong> <?php echo $cliente['email']; ?></p>
<p><strong>Telefone:</strong> <?php echo $cliente['telefone']; ?></p>
<p><strong>Endereço:</strong> <?php echo $cliente['endereco']; ?></p>

<a href="index.php" class="btn btn-secondary">Voltar à Lista</a>

<?php include 'footer.php'; ?>
```

---

### excluir_cliente.php

Script para excluir um cliente.

```php
<?php include 'db.php'; ?>

<?php
$id = $_GET['id'];
$sql = "DELETE FROM clientes WHERE id=$id";
if ($conn->query($sql) === TRUE) {
    header("Location: index.php");
} else {
    echo "Erro ao excluir registro: " . $conn->error;
}
?>
```

---

## Considerações Finais

* **Segurança**: Para produção, é importante utilizar **prepared statements** para prevenir SQL Injection.
* **Validação**: Adicione validações adicionais nos formulários conforme necessário.
* **Configurações**: Certifique-se de ajustar as credenciais do banco de dados no arquivo `db.php`.
* **Estilos**: Utilize o arquivo `css/custom.css` para adicionar estilos personalizados ao projeto.

---

Com essa estrutura, você terá um sistema básico de gerenciamento de clientes em PHP com MySQL e uma interface agradável utilizando Bootstrap. Sinta-se à vontade para expandir o projeto conforme suas necessidades.

Se tiver alguma dúvida ou precisar de ajuda adicional, estou à disposição!
