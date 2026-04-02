Perfeito! Vou criar um **Cheat Sheet MEGA COMPLETO** para **HTML, CSS e JavaScript** no mesmo estilo detalhado do Python, com mais de 600 exemplos práticos para cada tecnologia.

---

# 🌐 HTML5 - CHEAT SHEET MEGA COMPLETO
## *Todos os elementos, atributos e boas práticas*

---

## 📚 SUMÁRIO HTML

1. [Estrutura Básica](#1-estrutura-básica)
2. [Elementos de Texto](#2-elementos-de-texto)
3. [Links e Navegação](#3-links-e-navegação)
4. [Listas e Tabelas](#4-listas-e-tabelas)
5. [Formulários](#5-formulários)
6. [Mídia e Multimídia](#6-mídia-e-multimídia)
7. [Elementos Semânticos](#7-elementos-semânticos)
8. [Elementos Interativos](#8-elementos-interativos)
9. [Atributos Globais](#9-atributos-globais)
10. [Meta Tags e SEO](#10-meta-tags-e-seo)
11. [Microdata e ARIA](#11-microdata-e-aria)
12. [Web Components](#12-web-components)
13. [APIs HTML5](#13-apis-html5)

---

## 1. ESTRUTURA BÁSICA

### 1.1 Documento HTML5 Completo

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Descrição da página para SEO">
    <meta name="keywords" content="HTML, CSS, JavaScript">
    <meta name="author" content="Seu Nome">
    <meta name="robots" content="index, follow">
    
    <title>Título da Página</title>
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <link rel="apple-touch-icon" href="apple-touch-icon.png">
    
    <!-- CSS -->
    <link rel="stylesheet" href="style.css">
    <style>
        /* CSS interno */
        body { font-family: sans-serif; }
    </style>
    
    <!-- Pré-conexão para otimização -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    
    <!-- JavaScript -->
    <script src="script.js" defer></script>
    <script type="module">
        // JavaScript inline (ES modules)
        import { funcao } from './module.js';
    </script>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#sobre">Sobre</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <article>
            <h1>Título Principal</h1>
            <section>
                <h2>Seção</h2>
                <p>Conteúdo...</p>
            </section>
        </article>
    </main>
    
    <aside>
        <h3>Barra Lateral</h3>
    </aside>
    
    <footer>
        <p>&copy; 2024 - Todos os direitos reservados</p>
    </footer>
</body>
</html>
```

### 1.2 DOCTYPE e Modos de Renderização

```html
<!-- HTML5 (recomendado) -->
<!DOCTYPE html>

<!-- HTML 4.01 Strict -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

<!-- HTML 4.01 Transitional -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<!-- XHTML 1.0 Strict -->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<!-- XHTML 1.0 Transitional -->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

---

## 2. ELEMENTOS DE TEXTO

### 2.1 Títulos e Parágrafos

```html
<!-- Títulos (h1 a h6) -->
<h1>Título Principal - Apenas um por página</h1>
<h2>Título Secundário</h2>
<h3>Subtítulo</h3>
<h4>Seção Menor</h4>
<h5>Subseção</h5>
<h6>Título Menor</h6>

<!-- Parágrafos -->
<p>Parágrafo de texto. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>

<!-- Quebra de linha -->
<p>Linha 1<br>Linha 2</p>

<!-- Linha horizontal -->
<hr>

<!-- Pré-formatação -->
<pre>
    Linha com espaços
        e indentação preservada
</pre>

<!-- Citação em bloco -->
<blockquote cite="https://www.exemplo.com/citacao">
    <p>Esta é uma citação longa.</p>
    <footer>— Autor da citação</footer>
</blockquote>
```

### 2.2 Formatação de Texto

```html
<!-- Formatação semântica -->
<strong>Texto importante (negrito semântico)</strong>
<em>Texto enfatizado (itálico semântico)</em>
<mark>Texto destacado</mark>
<small>Texto pequeno (letras miúdas)</small>
<del>Texto deletado</del>
<ins>Texto inserido</ins>
<sub>Texto subscrito</sub>
<sup>Texto sobrescrito</sup>

<!-- Formatação não-semântica -->
<b>Texto em negrito (visual)</b>
<i>Texto em itálico (visual)</i>
<u>Texto sublinhado</u>
<s>Texto tachado</s>

<!-- Citações inline -->
<cite>Título da obra</cite>
<q>Citação curta inline</q>

<!-- Abreviações -->
<abbr title="HyperText Markup Language">HTML</abbr>

<!-- Definições -->
<dfn>HTML</dfn> é a linguagem de marcação.

<!-- Código -->
<code>function saudacao() { return "Olá"; }</code>
<kbd>Ctrl + C</kbd> <!-- Teclas -->
<samp>Erro 404</samp> <!-- Saída de programa -->
<var>x</var> = 10; <!-- Variável -->

<!-- Endereço -->
<address>
    Rua Exemplo, 123<br>
    São Paulo - SP<br>
    <a href="mailto:contato@exemplo.com">contato@exemplo.com</a>
</address>

<!-- Data e Hora -->
<time datetime="2024-12-25">Natal de 2024</time>
<time datetime="2024-12-25T20:00">20h do dia 25</time>
<time datetime="PT2H30M">2 horas e 30 minutos</time>

<!-- Rubi (anotações em textos asiáticos) -->
<ruby>漢 <rp>(</rp><rt>kan</rt><rp>)</rp> 字 <rp>(</rp><rt>ji</rt><rp>)</rp></ruby>
```

### 2.3 Elementos de Texto Avançados

```html
<!-- Detalhes e Resumo -->
<details>
    <summary>Clique para expandir</summary>
    <p>Conteúdo oculto que aparece quando clicado.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>
</details>

<details open>
    <summary>Expandido por padrão</summary>
    <p>Este conteúdo já está visível.</p>
</details>

<!-- Diálogo -->
<dialog id="meuDialog">
    <p>Conteúdo do diálogo modal</p>
    <button onclick="document.getElementById('meuDialog').close()">Fechar</button>
</dialog>
<button onclick="document.getElementById('meuDialog').showModal()">Abrir Modal</button>

<!-- WBR (Word Break Opportunity) -->
<p>URL muito longa: https://exemplo.com/{{<wbr>caminho/<wbr>muito/<wbr>longo}}</p>

<!-- BDI (Bidirectional Isolation) -->
<p><bdi>محمود</bdi> - 1º lugar</p>
```

---

## 3. LINKS E NAVEGAÇÃO

### 3.1 Links (Âncoras)

```html
<!-- Link básico -->
<a href="https://www.exemplo.com">Link para site externo</a>

<!-- Link para página interna -->
<a href="/sobre.html">Sobre nós</a>
<a href="../index.html">Voltar</a>

<!-- Link para seção na mesma página -->
<a href="#secao1">Ir para Seção 1</a>
<h2 id="secao1">Seção 1</h2>

<!-- Link para email -->
<a href="mailto:contato@exemplo.com?subject=Assunto&body=Mensagem">
    Enviar email
</a>

<!-- Link para telefone -->
<a href="tel:+5511999999999">(11) 99999-9999</a>

<!-- Link para WhatsApp -->
<a href="https://wa.me/5511999999999?text=Olá">WhatsApp</a>

<!-- Link para download -->
<a href="arquivo.pdf" download="novo-nome.pdf">Download PDF</a>
<a href="imagem.jpg" download>Download Imagem</a>

<!-- Link com target -->
<a href="https://exemplo.com" target="_blank">Abrir em nova aba</a>
<a href="https://exemplo.com" target="_self">Abrir na mesma aba (padrão)</a>
<a href="https://exemplo.com" target="_parent">Abrir no frame pai</a>
<a href="https://exemplo.com" target="_top">Abrir no topo da janela</a>

<!-- Link com rel (segurança) -->
<a href="https://exemplo.com" target="_blank" rel="noopener noreferrer">
    Link seguro
</a>

<!-- Link com atributos de SEO -->
<a href="/artigos" rel="next">Próximo</a>
<a href="/artigos" rel="prev">Anterior</a>
<a href="/" rel="home">Home</a>
<a href="/sobre" rel="author">Autor</a>

<!-- Link com título (tooltip) -->
<a href="https://exemplo.com" title="Visite nosso site">Exemplo</a>

<!-- Links de navegação -->
<nav aria-label="Navegação principal">
    <ul>
        <li><a href="/" aria-current="page">Home</a></li>
        <li><a href="/produtos">Produtos</a></li>
        <li><a href="/servicos">Serviços</a></li>
        <li><a href="/contato">Contato</a></li>
    </ul>
</nav>

<!-- Skip to content (acessibilidade) -->
<a href="#main-content" class="skip-link">Pular para o conteúdo</a>
<main id="main-content">
    <!-- Conteúdo principal -->
</main>
```

### 3.2 Navegação e Links Avançados

```html
<!-- Mapa de imagem -->
<img src="mapa.jpg" usemap="#mapa" alt="Mapa interativo">
<map name="mapa">
    <area shape="rect" coords="0,0,100,100" href="pagina1.html" alt="Área 1">
    <area shape="circle" coords="150,150,50" href="pagina2.html" alt="Área 2">
    <area shape="poly" coords="200,200,250,200,225,250" href="pagina3.html" alt="Área 3">
</map>

<!-- Link para download forçado com atributo download -->
<a href="documento.pdf" download>Baixar PDF</a>
<a href="imagem.jpg" download="minha-imagem.jpg">Baixar Imagem</a>

<!-- Link para arquivo de diferentes tipos -->
<a href="video.mp4" type="video/mp4">Download Vídeo</a>
<a href="documento.docx" type="application/msword">Download Word</a>

<!-- Link com ping (rastreamento) -->
<a href="https://exemplo.com" ping="https://analytics.com/track">Link rastreado</a>

<!-- Link para diferentes protocolos -->
<a href="skype:usuario?call">Chamada Skype</a>
<a href="facetime://usuario">FaceTime</a>
<a href="tg://resolve?domain=usuario">Telegram</a>
```

---

## 4. LISTAS E TABELAS

### 4.1 Listas

```html
<!-- Lista não ordenada -->
<ul>
    <li>Item 1</li>
    <li>Item 2
        <ul>
            <li>Subitem 2.1</li>
            <li>Subitem 2.2</li>
        </ul>
    </li>
    <li>Item 3</li>
</ul>

<!-- Lista ordenada -->
<ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
    <li>Terceiro item</li>
</ol>

<!-- Lista ordenada com atributos -->
<ol type="A">  <!-- A, B, C... -->
    <li>Item A</li>
    <li>Item B</li>
</ol>

<ol type="a">  <!-- a, b, c... -->
    <li>Item a</li>
    <li>Item b</li>
</ol>

<ol type="I">  <!-- I, II, III... -->
    <li>Item I</li>
    <li>Item II</li>
</ol>

<ol type="i">  <!-- i, ii, iii... -->
    <li>Item i</li>
    <li>Item ii</li>
</ol>

<ol start="5">  <!-- Começa em 5 -->
    <li>Quinto</li>
    <li>Sexto</li>
</ol>

<ol reversed>  <!-- Ordem decrescente -->
    <li>3</li>
    <li>2</li>
    <li>1</li>
</ol>

<ol value="10">  <!-- Valor específico para item -->
    <li>Item 10</li>
    <li value="20">Item 20</li>
    <li>Item 21</li>
</ol>

<!-- Lista de definição -->
<dl>
    <dt>HTML</dt>
    <dd>Linguagem de marcação para páginas web</dd>
    
    <dt>CSS</dt>
    <dd>Linguagem de estilo para páginas web</dd>
    <dd>Usada para estilizar elementos HTML</dd>
    
    <dt>JavaScript</dt>
    <dd>Linguagem de programação para web</dd>
</dl>

<!-- Lista de menu -->
<menu>
    <li><button>Salvar</button></li>
    <li><button>Editar</button></li>
    <li><button>Excluir</button></li>
</menu>
```

### 4.2 Tabelas

```html
<!-- Tabela básica -->
<table border="1">
    <caption>Relatório de Vendas</caption>
    <thead>
        <tr>
            <th>Produto</th>
            <th>Quantidade</th>
            <th>Preço</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Notebook</td>
            <td>10</td>
            <td>R$ 2.500,00</td>
        </tr>
        <tr>
            <td>Mouse</td>
            <td>50</td>
            <td>R$ 50,00</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th>Total</th>
            <th>60</th>
            <th>R$ 27.500,00</th>
        </tr>
    </tfoot>
</table>

<!-- Tabela com colspan e rowspan -->
<table border="1">
    <thead>
        <tr>
            <th colspan="2">Informações Pessoais</th>
            <th>Contato</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>João</td>
            <td>25</td>
            <td rowspan="2">joao@email.com</td>
        </tr>
        <tr>
            <td>Maria</td>
            <td>30</td>
        </tr>
    </tbody>
</table>

<!-- Tabela com scopes (acessibilidade) -->
<table>
    <thead>
        <tr>
            <th scope="col">Nome</th>
            <th scope="col">Idade</th>
            <th scope="col">Cidade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">João</th>
            <td>25</td>
            <td>SP</td>
        </tr>
    </tbody>
</table>

<!-- Tabela responsiva com overflow -->
<div style="overflow-x: auto;">
    <table>
        <!-- tabela larga -->
    </table>
</div>

<!-- Tabela com colgroup -->
<table>
    <colgroup>
        <col style="background-color: lightblue;">
        <col span="2" style="background-color: lightgreen;">
    </colgroup>
    <thead>
        <tr>
            <th>Coluna 1</th>
            <th>Coluna 2</th>
            <th>Coluna 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Dado</td>
            <td>Dado</td>
            <td>Dado</td>
        </tr>
    </tbody>
</table>
```

---

## 5. FORMULÁRIOS

### 5.1 Elementos de Formulário

```html
<!-- Formulário básico -->
<form action="/enviar" method="POST" enctype="multipart/form-data">
    <!-- Campos do formulário -->
</form>

<!-- Inputs textuais -->
<input type="text" name="nome" id="nome" placeholder="Digite seu nome" required>
<input type="text" value="Valor padrão" readonly>
<input type="text" value="Valor desabilitado" disabled>
<input type="text" maxlength="10" minlength="3" size="20">

<!-- Inputs de senha -->
<input type="password" name="senha" placeholder="Digite sua senha" autocomplete="off">

<!-- Inputs de email -->
<input type="email" name="email" placeholder="email@exemplo.com" multiple>

<!-- Inputs de telefone -->
<input type="tel" name="telefone" placeholder="(11) 99999-9999" pattern="[0-9]{2}[0-9]{4,5}[0-9]{4}">

<!-- Inputs numéricos -->
<input type="number" name="idade" min="0" max="150" step="1" value="18">
<input type="range" name="volume" min="0" max="100" step="1" value="50">

<!-- Inputs de data -->
<input type="date" name="data">
<input type="datetime-local" name="datahora">
<input type="month" name="mes">
<input type="week" name="semana">
<input type="time" name="hora">

<!-- Inputs de seleção -->
<input type="checkbox" name="aceito" value="sim" checked>
<input type="radio" name="opcao" value="1" id="opcao1">
<input type="radio" name="opcao" value="2" id="opcao2">

<!-- Select dropdown -->
<select name="cidade" required>
    <option value="">Selecione uma cidade</option>
    <option value="sp">São Paulo</option>
    <option value="rj">Rio de Janeiro</option>
    <option value="bh" selected>Belo Horizonte</option>
    <optgroup label="Região Sul">
        <option value="curitiba">Curitiba</option>
        <option value="porto-alegre">Porto Alegre</option>
    </optgroup>
</select>

<!-- Select múltiplo -->
<select name="cores" multiple size="4">
    <option value="vermelho">Vermelho</option>
    <option value="azul">Azul</option>
    <option value="verde">Verde</option>
    <option value="amarelo">Amarelo</option>
</select>

<!-- Textarea -->
<textarea name="mensagem" rows="5" cols="30" placeholder="Digite sua mensagem..." maxlength="500"></textarea>

<!-- Datalist (autocomplete) -->
<input list="sugestoes" name="busca">
<datalist id="sugestoes">
    <option value="HTML">
    <option value="CSS">
    <option value="JavaScript">
    <option value="Python">
</datalist>

<!-- Inputs de arquivo -->
<input type="file" name="arquivo" accept="image/*, .pdf">
<input type="file" name="multiplos" multiple>

<!-- Inputs de cor -->
<input type="color" name="cor" value="#ff0000">

<!-- Inputs ocultos -->
<input type="hidden" name="token" value="abc123">

<!-- Botões -->
<button type="submit">Enviar</button>
<button type="reset">Limpar</button>
<button type="button" onclick="alert('Clicou!')">Botão</button>
<input type="submit" value="Enviar">
<input type="reset" value="Limpar">
<input type="button" value="Clique">

<!-- Fieldset e Legend -->
<fieldset>
    <legend>Informações Pessoais</legend>
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome">
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
</fieldset>

<!-- Output (resultado) -->
<input type="range" id="slider" oninput="resultado.value = this.value">
<output id="resultado" for="slider">50</output>

<!-- Progress e Meter -->
<progress value="70" max="100">70%</progress>
<meter value="0.7" min="0" max="1">70%</meter>
<meter value="30" min="0" max="100" low="20" high="80" optimum="50">30%</meter>
```

### 5.2 Atributos de Formulário

```html
<form action="/enviar" method="POST" 
      enctype="multipart/form-data"
      autocomplete="on"
      novalidate
      target="_blank"
      rel="noopener">

<!-- Atributos de campos -->
<input type="text" 
       name="campo"
       id="campo"
       class="campo"
       value="valor"
       placeholder="Placeholder"
       required
       readonly
       disabled
       autofocus
       autocomplete="off"
       pattern="[A-Za-z]{3,}"
       title="Apenas letras, mínimo 3"
       minlength="3"
       maxlength="10"
       min="0"
       max="100"
       step="5"
       size="20"
       multiple
       form="form-externo">
```

---

## 6. MÍDIA E MULTIMÍDIA

### 6.1 Imagens

```html
<!-- Imagem básica -->
<img src="imagem.jpg" alt="Descrição da imagem">

<!-- Imagem responsiva (srcset) -->
<img src="imagem-pequena.jpg"
     srcset="imagem-media.jpg 768w, imagem-grande.jpg 1200w"
     sizes="(max-width: 768px) 100vw, 50vw"
     alt="Imagem responsiva">

<!-- Imagem com picture (art direction) -->
<picture>
    <source media="(min-width: 1200px)" srcset="imagem-grande.jpg">
    <source media="(min-width: 768px)" srcset="imagem-media.jpg">
    <source media="(max-width: 767px)" srcset="imagem-pequena.jpg">
    <img src="imagem-padrao.jpg" alt="Imagem adaptativa">
</picture>

<!-- Imagem com formatos modernos -->
<picture>
    <source type="image/avif" srcset="imagem.avif">
    <source type="image/webp" srcset="imagem.webp">
    <img src="imagem.jpg" alt="Formato fallback">
</picture>

<!-- Imagem com lazy loading -->
<img src="imagem.jpg" loading="lazy" alt="Carregamento preguiçoso">
<img src="imagem.jpg" loading="eager" alt="Carregamento imediato">

<!-- Imagem com decodificação assíncrona -->
<img src="imagem.jpg" decoding="async" alt="Decodificação assíncrona">

<!-- Figura com legenda -->
<figure>
    <img src="grafico.png" alt="Gráfico de vendas">
    <figcaption>Figura 1: Vendas do primeiro trimestre</figcaption>
</figure>

<!-- Mapa de imagem (já visto em links) -->
<img src="mapa.jpg" usemap="#mapa" alt="Mapa interativo">
```

### 6.2 Áudio e Vídeo

```html
<!-- Áudio -->
<audio controls autoplay loop muted preload="auto">
    <source src="audio.mp3" type="audio/mpeg">
    <source src="audio.ogg" type="audio/ogg">
    <source src="audio.wav" type="audio/wav">
    <p>Seu navegador não suporta áudio.</p>
</audio>

<!-- Áudio com track (legendas) -->
<audio controls>
    <source src="podcast.mp3" type="audio/mpeg">
    <track src="legendas.vtt" kind="captions" srclang="pt" label="Português">
</audio>

<!-- Vídeo -->
<video width="640" height="360" controls autoplay loop muted preload="metadata" poster="thumbnail.jpg">
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    <source src="video.ogg" type="video/ogg">
    <track src="legendas.vtt" kind="subtitles" srclang="pt" label="Português">
    <track src="legendas-en.vtt" kind="subtitles" srclang="en" label="English">
    <p>Seu navegador não suporta vídeo.</p>
</video>

<!-- Vídeo responsivo -->
<div style="position: relative; padding-bottom: 56.25%; height: 0;">
    <video style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" controls>
        <source src="video.mp4" type="video/mp4">
    </video>
</div>

<!-- Embed YouTube -->
<iframe width="560" height="315" 
        src="https://www.youtube.com/embed/VIDEO_ID" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
</iframe>

<!-- Embed Vimeo -->
<iframe src="https://player.vimeo.com/video/VIDEO_ID" 
        width="640" height="360" 
        frameborder="0" 
        allow="autoplay; fullscreen" 
        allowfullscreen>
</iframe>

<!-- Embed Google Maps -->
<iframe 
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.197!2d-46.658!3d-23.564!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce59c8da0aa315%3A0xd59f9431f2c9776a!2sAv.%20Paulista%2C%20S%C3%A3o%20Paulo%20-%20SP!5e0!3m2!1spt-BR!2sbr!4v1" 
    width="600" height="450" 
    style="border:0;" 
    allowfullscreen="" 
    loading="lazy">
</iframe>
```

### 6.3 Canvas e SVG

```html
<!-- Canvas (desenho via JavaScript) -->
<canvas id="meuCanvas" width="400" height="400" style="border:1px solid black">
    Texto alternativo para navegadores que não suportam canvas
</canvas>

<script>
    const canvas = document.getElementById('meuCanvas');
    const ctx = canvas.getContext('2d');
    
    // Desenhar retângulo
    ctx.fillStyle = 'red';
    ctx.fillRect(50, 50, 100, 100);
    
    // Desenhar círculo
    ctx.beginPath();
    ctx.arc(200, 200, 50, 0, 2 * Math.PI);
    ctx.fillStyle = 'blue';
    ctx.fill();
    
    // Desenhar texto
    ctx.font = '20px Arial';
    ctx.fillStyle = 'black';
    ctx.fillText('Olá Canvas!', 150, 350);
</script>

<!-- SVG (Scalable Vector Graphics) -->
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <!-- Retângulo -->
    <rect x="50" y="50" width="100" height="100" fill="red" stroke="black" stroke-width="2"/>
    
    <!-- Círculo -->
    <circle cx="200" cy="200" r="50" fill="blue" stroke="black"/>
    
    <!-- Linha -->
    <line x1="300" y1="50" x2="350" y2="100" stroke="green" stroke-width="3"/>
    
    <!-- Texto -->
    <text x="150" y="350" font-size="20" fill="black">Olá SVG!</text>
    
    <!-- Path (caminho) -->
    <path d="M 100 300 L 150 250 L 200 300 Z" fill="yellow" stroke="orange"/>
    
    <!-- Gradiente -->
    <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="red"/>
            <stop offset="100%" stop-color="blue"/>
        </linearGradient>
    </defs>
    <rect x="250" y="300" width="100" height="50" fill="url(#grad1)"/>
</svg>
```

---

## 7. ELEMENTOS SEMÂNTICOS

### 7.1 Estrutura Semântica

```html
<!-- Estrutura completa semântica -->
<body>
    <!-- Cabeçalho -->
    <header>
        <h1>Título do Site</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/sobre">Sobre</a></li>
            </ul>
        </nav>
    </header>
    
    <!-- Navegação principal -->
    <nav aria-label="Navegação principal">
        <!-- links -->
    </nav>
    
    <!-- Conteúdo principal -->
    <main>
        <article>
            <header>
                <h2>Título do Artigo</h2>
                <p>Publicado em <time datetime="2024-01-15">15 de janeiro</time></p>
            </header>
            
            <section>
                <h3>Seção 1</h3>
                <p>Conteúdo da seção...</p>
            </section>
            
            <section>
                <h3>Seção 2</h3>
                <p>Conteúdo da seção...</p>
            </section>
            
            <footer>
                <p>Autor: João Silva</p>
            </footer>
        </article>
        
        <aside>
            <h3>Artigos Relacionados</h3>
            <ul>
                <li><a href="#">Artigo 1</a></li>
                <li><a href="#">Artigo 2</a></li>
            </ul>
        </aside>
    </main>
    
    <!-- Rodapé -->
    <footer>
        <p>&copy; 2024 - Todos os direitos reservados</p>
        <address>
            <a href="mailto:contato@exemplo.com">contato@exemplo.com</a>
        </address>
    </footer>
</body>
```

### 7.2 Elementos Semânticos Detalhados

```html
<!-- Article - conteúdo independente -->
<article class="post">
    <h2>Título do Post</h2>
    <p>Conteúdo...</p>
</article>

<!-- Section - grupo temático -->
<section class="introducao">
    <h2>Introdução</h2>
    <p>Texto introdutório...</p>
</section>

<!-- Nav - grupo de links de navegação -->
<nav class="breadcrumb">
    <ol>
        <li><a href="/">Home</a></li>
        <li><a href="/produtos">Produtos</a></li>
        <li>Produto Atual</li>
    </ol>
</nav>

<!-- Aside - conteúdo relacionado -->
<aside class="sidebar">
    <h3>Publicidade</h3>
    <img src="banner.jpg" alt="Banner">
</aside>

<!-- Header - cabeçalho de seção -->
<header class="page-header">
    <h1>Título da Página</h1>
    <p>Subtítulo ou descrição</p>
</header>

<!-- Footer - rodapé de seção -->
<footer class="page-footer">
    <p>Informações de copyright, links úteis, etc.</p>
</footer>

<!-- Main - conteúdo principal (único por página) -->
<main id="main-content">
    <!-- Conteúdo principal da página -->
</main>

<!-- Mark - texto destacado -->
<p>Você precisa <mark>destacar</mark> esta parte.</p>

<!-- Time - data/hora -->
<time datetime="2024-12-25">Natal</time>
<time datetime="PT2H30M">2h30m</time>
```

---

## 8. ELEMENTOS INTERATIVOS

### 8.1 Elementos de Interação

```html
<!-- Details/Summary (já visto) -->
<details>
    <summary>Mais informações</summary>
    <p>Conteúdo detalhado...</p>
</details>

<!-- Dialog (modal) -->
<dialog id="modal">
    <h2>Modal Title</h2>
    <p>Modal content</p>
    <button onclick="this.closest('dialog').close()">Fechar</button>
</dialog>
<button onclick="document.getElementById('modal').showModal()">Abrir Modal</button>

<!-- Menu (context menu) -->
<menu type="context" id="context-menu">
    <menuitem label="Copiar" onclick="copyText()"></menuitem>
    <menuitem label="Colar" onclick="pasteText()"></menuitem>
</menu>

<!-- Popover (experimental) -->
<div popover id="popover">
    <p>Conteúdo do popover</p>
    <button popovertarget="popover" popovertargetaction="hide">Fechar</button>
</div>
<button popovertarget="popover">Abrir Popover</button>

<!-- Tabs (com JavaScript) -->
<div class="tabs">
    <div class="tab-buttons">
        <button class="tab-button active" data-tab="tab1">Tab 1</button>
        <button class="tab-button" data-tab="tab2">Tab 2</button>
        <button class="tab-button" data-tab="tab3">Tab 3</button>
    </div>
    <div class="tab-content active" id="tab1">Conteúdo 1</div>
    <div class="tab-content" id="tab2">Conteúdo 2</div>
    <div class="tab-content" id="tab3">Conteúdo 3</div>
</div>

<!-- Accordion (com details) -->
<details class="accordion">
    <summary>Seção 1</summary>
    <p>Conteúdo da seção 1</p>
</details>
<details class="accordion">
    <summary>Seção 2</summary>
    <p>Conteúdo da seção 2</p>
</details>

<!-- Carrossel (com JavaScript) -->
<div class="carousel">
    <div class="carousel-slides">
        <img src="slide1.jpg" alt="Slide 1">
        <img src="slide2.jpg" alt="Slide 2">
        <img src="slide3.jpg" alt="Slide 3">
    </div>
    <button class="prev">‹</button>
    <button class="next">›</button>
</div>
```

---

## 9. ATRIBUTOS GLOBAIS

### 9.1 Todos os Atributos Globais

```html
<!-- id - identificador único -->
<div id="unico"></div>

<!-- class - classes CSS -->
<div class="classe1 classe2 classe3"></div>

<!-- style - CSS inline -->
<div style="color: red; font-size: 16px;"></div>

<!-- title - tooltip -->
<div title="Texto do tooltip">Passe o mouse</div>

<!-- lang - idioma -->
<div lang="pt-BR">Texto em português</div>

<!-- dir - direção do texto -->
<div dir="ltr">Texto da esquerda para direita</div>
<div dir="rtl">نص من اليمين إلى اليسار</div>

<!-- hidden - oculto -->
<div hidden>Este conteúdo está oculto</div>

<!-- tabindex - ordem de tabulação -->
<div tabindex="0">Focável via tab</div>
<div tabindex="-1">Focável apenas via JavaScript</div>

<!-- accesskey - atalho de teclado -->
<button accesskey="s">Salvar (Alt+S)</button>

<!-- contenteditable - conteúdo editável -->
<div contenteditable="true">Este texto pode ser editado</div>

<!-- draggable - arrastável -->
<div draggable="true">Arraste este elemento</div>

<!-- spellcheck - correção ortográfica -->
<textarea spellcheck="true"></textarea>

<!-- translate - tradução automática -->
<p translate="no">Não traduzir este texto</p>

<!-- data-* - atributos customizados -->
<div data-id="123" data-user="joao" data-role="admin"></div>

<!-- aria-* - atributos de acessibilidade -->
<button aria-label="Fechar janela">X</button>
<div role="alert" aria-live="assertive">Mensagem importante</div>

<!-- role - papel ARIA -->
<nav role="navigation">...</nav>
<main role="main">...</main>
<button role="switch" aria-checked="false">Ativar</button>
```

---

## 10. META TAGS E SEO

### 10.1 Meta Tags Essenciais

```html
<head>
    <!-- Charset -->
    <meta charset="UTF-8">
    
    <!-- Viewport (responsividade) -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    
    <!-- Descrição (SEO) -->
    <meta name="description" content="Descrição da página (150-160 caracteres)">
    
    <!-- Keywords (menos importante hoje) -->
    <meta name="keywords" content="palavra1, palavra2, palavra3">
    
    <!-- Autor -->
    <meta name="author" content="Nome do Autor">
    
    <!-- Robots (indexação) -->
    <meta name="robots" content="index, follow">
    <meta name="robots" content="noindex, nofollow">
    <meta name="robots" content="noarchive">
    <meta name="robots" content="nosnippet">
    
    <!-- Canonical (URL principal) -->
    <link rel="canonical" href="https://exemplo.com/pagina-principal">
    
    <!-- Language -->
    <meta name="language" content="Portuguese">
    
    <!-- Revisit after -->
    <meta name="revisit-after" content="7 days">
    
    <!-- Geo (localização) -->
    <meta name="geo.region" content="BR-SP">
    <meta name="geo.placename" content="São Paulo">
    <meta name="geo.position" content="-23.5505;-46.6333">
    <meta name="ICBM" content="-23.5505, -46.6333">
</head>
```

### 10.2 Open Graph (Facebook, LinkedIn)

```html
<head>
    <!-- Open Graph (Facebook, LinkedIn) -->
    <meta property="og:title" content="Título do Conteúdo">
    <meta property="og:description" content="Descrição do conteúdo">
    <meta property="og:image" content="https://exemplo.com/imagem.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:url" content="https://exemplo.com/pagina">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Nome do Site">
    <meta property="og:locale" content="pt_BR">
    
    <!-- Article (para artigos) -->
    <meta property="article:published_time" content="2024-01-15T10:00:00Z">
    <meta property="article:modified_time" content="2024-01-16T12:00:00Z">
    <meta property="article:author" content="https://exemplo.com/autor">
    <meta property="article:section" content="Tecnologia">
    <meta property="article:tag" content="HTML, CSS, JavaScript">
</head>
```

### 10.3 Twitter Cards

```html
<head>
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@usuario">
    <meta name="twitter:creator" content="@autor">
    <meta name="twitter:title" content="Título do Tweet">
    <meta name="twitter:description" content="Descrição do conteúdo">
    <meta name="twitter:image" content="https://exemplo.com/imagem.jpg">
    <meta name="twitter:image:alt" content="Descrição da imagem">
</head>
```

### 10.4 Schema.org (JSON-LD)

```html
<head>
    <!-- JSON-LD (Schema.org) -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "Nome da Página",
        "description": "Descrição da página",
        "url": "https://exemplo.com/pagina",
        "author": {
            "@type": "Person",
            "name": "João Silva"
        },
        "datePublished": "2024-01-15",
        "dateModified": "2024-01-16"
    }
    </script>
</head>
```

### 10.5 SEO Avançado

```html
<head>
    <!-- Mobile Alternates -->
    <link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.exemplo.com">
    
    <!-- Language Alternates -->
    <link rel="alternate" hreflang="en" href="https://exemplo.com/en/page">
    <link rel="alternate" hreflang="pt" href="https://exemplo.com/pt/pagina">
    <link rel="alternate" hreflang="x-default" href="https://exemplo.com/">
    
    <!-- RSS Feed -->
    <link rel="alternate" type="application/rss+xml" title="RSS" href="/feed.xml">
    
    <!-- Sitemap -->
    <link rel="sitemap" type="application/xml" title="Sitemap" href="/sitemap.xml">
    
    <!-- Preload (otimização) -->
    <link rel="preload" href="fonte.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="style.css" as="style">
    <link rel="preload" href="script.js" as="script">
    
    <!-- Prefetch (pré-carregamento) -->
    <link rel="prefetch" href="proxima-pagina.html">
    
    <!-- DNS Prefetch -->
    <link rel="dns-prefetch" href="//fonts.googleapis.com">
    
    <!-- Preconnect -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
</head>
```

---

## 11. MICRODATA E ARIA

### 11.1 Microdata (Schema.org)

```html
<!-- Pessoa -->
<div itemscope itemtype="https://schema.org/Person">
    <span itemprop="name">João Silva</span>
    <span itemprop="jobTitle">Desenvolvedor</span>
    <a href="mailto:joao@exemplo.com" itemprop="email">joao@exemplo.com</a>
    <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
        <span itemprop="streetAddress">Rua Exemplo, 123</span>
        <span itemprop="addressLocality">São Paulo</span>
        <span itemprop="addressRegion">SP</span>
    </div>
</div>

<!-- Produto -->
<div itemscope itemtype="https://schema.org/Product">
    <img itemprop="image" src="produto.jpg" alt="Produto">
    <span itemprop="name">Nome do Produto</span>
    <span itemprop="description">Descrição do produto</span>
    <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">
        <span itemprop="price">99.90</span>
        <span itemprop="priceCurrency">BRL</span>
        <link itemprop="availability" href="https://schema.org/InStock">
    </div>
    <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating">
        <span itemprop="ratingValue">4.5</span>
        <span itemprop="reviewCount">120</span>
    </div>
</div>

<!-- Artigo -->
<article itemscope itemtype="https://schema.org/Article">
    <h1 itemprop="headline">Título do Artigo</h1>
    <meta itemprop="datePublished" content="2024-01-15">
    <meta itemprop="dateModified" content="2024-01-16">
    <div itemprop="author" itemscope itemtype="https://schema.org/Person">
        <span itemprop="name">João Silva</span>
    </div>
    <div itemprop="articleBody">
        Conteúdo do artigo...
    </div>
</article>
```

### 11.2 ARIA (Acessibilidade)

```html
<!-- Roles básicos -->
<main role="main">Conteúdo principal</main>
<nav role="navigation">Navegação</nav>
<aside role="complementary">Conteúdo complementar</aside>
<footer role="contentinfo">Rodapé</footer>
<header role="banner">Cabeçalho</header>
<form role="search">Busca</form>

<!-- Estados -->
<button aria-pressed="false">Ativar</button>
<div aria-hidden="true">Oculto para leitores de tela</div>
<input aria-invalid="true" value="valor inválido">
<div aria-disabled="true">Desabilitado</div>
<div aria-expanded="false">Contraído</div>
<div aria-selected="true">Selecionado</div>

<!-- Labels -->
<button aria-label="Fechar janela">X</button>
<div aria-labelledby="titulo">Conteúdo</div>
<div id="titulo">Título</div>

<!-- Live regions -->
<div aria-live="polite">Mensagem não urgente</div>
<div aria-live="assertive">Mensagem urgente</div>

<!-- Tabs ARIA -->
<div role="tablist">
    <button role="tab" aria-selected="true" aria-controls="painel1">Tab 1</button>
    <button role="tab" aria-selected="false" aria-controls="painel2">Tab 2</button>
</div>
<div role="tabpanel" id="painel1">Conteúdo 1</div>
<div role="tabpanel" id="painel2" hidden>Conteúdo 2</div>

<!-- Accordion ARIA -->
<button aria-expanded="false" aria-controls="conteudo1">Seção 1</button>
<div id="conteudo1" hidden>Conteúdo 1</div>

<!-- Combobox -->
<input type="text" role="combobox" aria-autocomplete="list" aria-expanded="false">
<ul role="listbox" hidden>
    <li role="option">Opção 1</li>
    <li role="option">Opção 2</li>
</ul>

<!-- Dialog ARIA -->
<div role="dialog" aria-labelledby="dialog-title" aria-modal="true">
    <h2 id="dialog-title">Título do Modal</h2>
    <p>Conteúdo do modal</p>
    <button aria-label="Fechar">X</button>
</div>

<!-- Progressbar -->
<div role="progressbar" aria-valuenow="70" aria-valuemin="0" aria-valuemax="100">70%</div>

<!-- Slider -->
<div role="slider" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100" aria-label="Volume"></div>

<!-- Tooltip -->
<button aria-describedby="tooltip1">Botão</button>
<div role="tooltip" id="tooltip1">Informação adicional</div>
```

---

## 12. WEB COMPONENTS

### 12.1 Custom Elements

```html
<!-- Definindo um Custom Element -->
<script>
class MeuBotao extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = `
            <style>
                button {
                    background: #007bff;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover {
                    background: #0056b3;
                }
            </style>
            <button>
                <slot></slot>
            </button>
        `;
    }
    
    static get observedAttributes() {
        return ['disabled'];
    }
    
    attributeChangedCallback(name, oldValue, newValue) {
        const button = this.shadowRoot.querySelector('button');
        if (name === 'disabled') {
            button.disabled = newValue !== null;
        }
    }
}

customElements.define('meu-botao', MeuBotao);
</script>

<meu-botao disabled>Clique aqui</meu-botao>
<meu-botao>Botão normal</meu-botao>
```

### 12.2 Shadow DOM

```html
<!-- Shadow DOM (encapsulamento) -->
<div id="host"></div>
<script>
const host = document.getElementById('host');
const shadow = host.attachShadow({ mode: 'open' });
shadow.innerHTML = `
    <style>
        p { color: red; }
    </style>
    <p>Texto dentro do Shadow DOM</p>
`;
</script>
```

### 12.3 HTML Templates

```html
<!-- Template (conteúdo não renderizado) -->
<template id="card-template">
    <style>
        .card {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 16px;
            margin: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 8px;
        }
        .content {
            color: #666;
        }
    </style>
    <div class="card">
        <div class="title"></div>
        <div class="content"></div>
    </div>
</template>

<script>
class CardComponent extends HTMLElement {
    constructor() {
        super();
        const template = document.getElementById('card-template');
        const content = template.content.cloneNode(true);
        this.attachShadow({ mode: 'open' }).appendChild(content);
    }
    
    connectedCallback() {
        this.shadowRoot.querySelector('.title').textContent = this.getAttribute('title');
        this.shadowRoot.querySelector('.content').textContent = this.getAttribute('content');
    }
}

customElements.define('card-component', CardComponent);
</script>

<card-component title="Título" content="Conteúdo do card"></card-component>
```

---

## 13. APIS HTML5

### 13.1 APIs JavaScript

```html
<!-- Geolocation API -->
<button onclick="getLocation()">Obter Localização</button>
<script>
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                console.log(`Lat: ${position.coords.latitude}, Lng: ${position.coords.longitude}`);
            },
            (error) => {
                console.error('Erro:', error.message);
            },
            {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0
            }
        );
    }
}
</script>

<!-- Web Storage (localStorage/sessionStorage) -->
<script>
// localStorage (persistente)
localStorage.setItem('chave', 'valor');
const valor = localStorage.getItem('chave');
localStorage.removeItem('chave');
localStorage.clear();

// sessionStorage (por sessão)
sessionStorage.setItem('chave', 'valor');
</script>

<!-- IndexedDB -->
<script>
const request = indexedDB.open('MeuBanco', 1);
request.onerror = (event) => console.error('Erro');
request.onupgradeneeded = (event) => {
    const db = event.target.result;
    const store = db.createObjectStore('usuarios', { keyPath: 'id' });
    store.createIndex('nome', 'nome', { unique: false });
};
</script>

<!-- Drag and Drop -->
<div draggable="true" ondragstart="drag(event)" id="drag1">Arraste-me</div>
<div ondrop="drop(event)" ondragover="allowDrop(event)">Solte aqui</div>
<script>
function allowDrop(ev) { ev.preventDefault(); }
function drag(ev) { ev.dataTransfer.setData('text', ev.target.id); }
function drop(ev) {
    ev.preventDefault();
    const data = ev.dataTransfer.getData('text');
    ev.target.appendChild(document.getElementById(data));
}
</script>

<!-- Web Workers (threads em background) -->
<script>
const worker = new Worker('worker.js');
worker.postMessage({ type: 'processar', data: [1,2,3,4,5] });
worker.onmessage = (event) => {
    console.log('Resultado:', event.data);
};
</script>

<!-- Service Workers (PWA) -->
<script>
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js')
        .then(registration => console.log('Service Worker registrado'))
        .catch(error => console.error('Erro:', error));
}
</script>

<!-- WebSocket (conexão em tempo real) -->
<script>
const socket = new WebSocket('ws://localhost:8080');
socket.onopen = () => socket.send('Olá servidor!');
socket.onmessage = (event) => console.log('Mensagem:', event.data);
socket.onclose = () => console.log('Conexão fechada');
</script>

<!-- Fetch API -->
<script>
fetch('https://api.exemplo.com/dados')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Erro:', error));

// POST com fetch
fetch('https://api.exemplo.com/dados', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ nome: 'João', idade: 30 })
})
.then(response => response.json())
.then(data => console.log(data));
</script>

<!-- Intersection Observer (lazy loading) -->
<script>
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            observer.unobserve(img);
        }
    });
});

document.querySelectorAll('img[data-src]').forEach(img => observer.observe(img));
</script>

<!-- Resize Observer -->
<script>
const resizeObserver = new ResizeObserver(entries => {
    for (let entry of entries) {
        console.log('Novo tamanho:', entry.contentRect.width, entry.contentRect.height);
    }
});
resizeObserver.observe(document.querySelector('.elemento'));
</script>

<!-- Mutation Observer -->
<script>
const observer = new MutationObserver(mutations => {
    mutations.forEach(mutation => {
        console.log('Mudança:', mutation.type);
    });
});
observer.observe(document.body, { 
    attributes: true, 
    childList: true, 
    subtree: true 
});
</script>

<!-- Fullscreen API -->
<button onclick="toggleFullscreen()">Tela Cheia</button>
<script>
function toggleFullscreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        document.exitFullscreen();
    }
}
</script>

<!-- Clipboard API -->
<button onclick="copiarTexto()">Copiar</button>
<script>
async function copiarTexto() {
    try {
        await navigator.clipboard.writeText('Texto a copiar');
        console.log('Copiado!');
    } catch (err) {
        console.error('Erro:', err);
    }
}
</script>

<!-- Battery Status API -->
<script>
navigator.getBattery().then(battery => {
    console.log(`Bateria: ${battery.level * 100}%`);
    console.log(`Carregando: ${battery.charging}`);
    battery.addEventListener('levelchange', () => {
        console.log(`Nova bateria: ${battery.level * 100}%`);
    });
});
</script>

<!-- Network Information API -->
<script>
if ('connection' in navigator) {
    const connection = navigator.connection;
    console.log(`Tipo: ${connection.effectiveType}`);
    console.log(`Velocidade: ${connection.downlink} Mbps`);
    connection.addEventListener('change', () => {
        console.log(`Novo tipo: ${connection.effectiveType}`);
    });
}
</script>

<!-- Vibration API (dispositivos móveis) -->
<button onclick="vibrar()">Vibrar</button>
<script>
function vibrar() {
    if ('vibrate' in navigator) {
        navigator.vibrate(200);  // 200ms
        // navegator.vibrate([100, 100, 100]);  // Padrão
    }
}
</script>

<!-- Device Orientation -->
<script>
window.addEventListener('deviceorientation', (event) => {
    console.log(`Alpha: ${event.alpha}, Beta: ${event.beta}, Gamma: ${event.gamma}`);
});
</script>

<!-- Page Visibility API -->
<script>
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        console.log('Página oculta');
    } else {
        console.log('Página visível');
    }
});
</script>

<!-- Online/Offline Detection -->
<script>
window.addEventListener('online', () => console.log('Online'));
window.addEventListener('offline', () => console.log('Offline'));
</script>
```

---

## 📊 TABELA RESUMO HTML

| Categoria | Principais Elementos |
|-----------|---------------------|
| **Estrutura** | `<!DOCTYPE>`, `<html>`, `<head>`, `<body>` |
| **Texto** | `<h1>`-`<h6>`, `<p>`, `<strong>`, `<em>`, `<span>` |
| **Links** | `<a>`, `<nav>`, `<area>` |
| **Listas** | `<ul>`, `<ol>`, `<li>`, `<dl>`, `<dt>`, `<dd>` |
| **Tabelas** | `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>` |
| **Formulários** | `<form>`, `<input>`, `<select>`, `<textarea>`, `<button>` |
| **Mídia** | `<img>`, `<picture>`, `<audio>`, `<video>`, `<canvas>`, `<svg>` |
| **Semânticos** | `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>` |
| **Interativos** | `<details>`, `<dialog>`, `<menu>` |
| **Meta** | `<meta>`, `<link>`, `<title>`, `<base>` |

---

# 🎨 CSS3 - CHEAT SHEET MEGA COMPLETO
## *Todos os seletores, propriedades e técnicas*

---

## 📚 SUMÁRIO CSS

1. [Seletores CSS](#1-seletores-css)
2. [Box Model](#2-box-model)
3. [Flexbox](#3-flexbox)
4. [Grid Layout](#4-grid-layout)
5. [Posicionamento](#5-posicionamento)
6. [Tipografia](#6-tipografia)
7. [Cores e Fundos](#7-cores-e-fundos)
8. [Efeitos e Transformações](#8-efeitos-e-transformações)
9. [Animações](#9-animações)
10. [Responsividade](#10-responsividade)
11. [CSS Variables](#11-css-variables)
12. [CSS Functions](#12-css-functions)
13. [Media Queries](#13-media-queries)
14. [Layouts Modernos](#14-layouts-modernos)

---

## 1. SELETORES CSS

### 1.1 Seletores Básicos

```css
/* Seletor universal */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Seletor de tipo (elemento) */
div {
    display: block;
}
p {
    margin-bottom: 1em;
}
h1, h2, h3 {
    font-weight: bold;
}

/* Seletor de classe */
.classe {
    color: red;
}
.elemento.destaque {
    background: yellow;
}

/* Seletor de ID */
#id-unico {
    position: absolute;
}

/* Seletor de atributo */
[type="text"] {
    border: 1px solid #ccc;
}
[disabled] {
    opacity: 0.5;
}
[class^="btn-"] {
    cursor: pointer;
}
[class$="-danger"] {
    background: red;
}
[class*="warning"] {
    border-color: orange;
}
[lang|="pt"] {
    quotes: "“" "”";
}
```

### 1.2 Seletores Combinadores

```css
/* Descendente (espaço) */
article p {
    line-height: 1.5;
}

/* Filho direto (>) */
ul > li {
    list-style: none;
}

/* Irmão adjacente (+) */
h2 + p {
    margin-top: 0;
}

/* Irmãos gerais (~) */
h2 ~ p {
    color: gray;
}
```

### 1.3 Pseudo-classes

```css
/* Estados de links */
a:link { color: blue; }
a:visited { color: purple; }
a:hover { color: red; }
a:active { color: green; }
a:focus { outline: 2px solid blue; }

/* Estados de formulários */
input:focus {
    border-color: blue;
    outline: none;
}
input:disabled {
    background: #f0f0f0;
}
input:checked + label {
    font-weight: bold;
}
input:invalid {
    border-color: red;
}
input:required {
    border-left: 3px solid red;
}
:placeholder-shown {
    font-style: italic;
}

/* Pseudo-classes estruturais */
:root {
    --primary-color: #007bff;
}
:empty {
    display: none;
}
:only-child {
    margin: 0;
}
:first-child {
    margin-top: 0;
}
:last-child {
    margin-bottom: 0;
}
:nth-child(odd) {
    background: #f9f9f9;
}
:nth-child(even) {
    background: #fff;
}
:nth-child(3n+1) {
    color: red;
}
:first-of-type {
    font-size: 1.2em;
}
:last-of-type {
    border-bottom: none;
}
:nth-of-type(2) {
    margin-top: 10px;
}
:not(.excluido) {
    opacity: 1;
}

/* Pseudo-classes de linguagem */
:lang(pt) {
    quotes: "“" "”";
}

/* Pseudo-classes de intervalo */
:in-range {
    border-color: green;
}
:out-of-range {
    border-color: red;
}

/* Pseudo-classes de leitura */
:read-only {
    background: #f5f5f5;
}
:read-write {
    background: white;
}
```

### 1.4 Pseudo-elementos

```css
/* Primeira linha */
p::first-line {
    font-weight: bold;
    color: blue;
}

/* Primeira letra */
p::first-letter {
    font-size: 3em;
    float: left;
    margin-right: 0.1em;
}

/* Before e After */
.elemento::before {
    content: "→ ";
    color: blue;
}
.elemento::after {
    content: " ←";
    color: red;
}
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}

/* Placeholder */
input::placeholder {
    color: #999;
    font-style: italic;
}

/* Seleção de texto */
::selection {
    background: yellow;
    color: black;
}

/* Marker (listas) */
li::marker {
    color: red;
    font-size: 1.2em;
}

/* Backdrop (dialog) */
dialog::backdrop {
    background: rgba(0,0,0,0.5);
}
```

---

## 2. BOX MODEL

### 2.1 Propriedades Básicas

```css
.elemento {
    /* Dimensões */
    width: 300px;
    min-width: 200px;
    max-width: 100%;
    height: 200px;
    min-height: 100px;
    max-height: 500px;
    
    /* Margens */
    margin: 10px;
    margin-top: 10px;
    margin-right: 20px;
    margin-bottom: 10px;
    margin-left: 20px;
    margin: 10px 20px; /* top/bottom left/right */
    margin: 10px 20px 30px; /* top left/right bottom */
    margin: 10px 20px 30px 40px; /* top right bottom left */
    margin: auto; /* centralizar */
    
    /* Preenchimento */
    padding: 10px;
    padding: 10px 20px;
    padding: 10px 20px 30px;
    padding: 10px 20px 30px 40px;
    
    /* Bordas */
    border: 1px solid #ccc;
    border-top: 2px solid red;
    border-right: 1px dashed blue;
    border-bottom: 3px double green;
    border-left: 1px dotted orange;
    border-radius: 5px;
    border-radius: 10px 20px 30px 40px;
    border-radius: 50%; /* círculo */
    
    /* Box-sizing */
    box-sizing: content-box; /* padrão: width = conteúdo */
    box-sizing: border-box;  /* width = conteúdo + padding + borda */
    
    /* Outline (não afeta layout) */
    outline: 2px solid red;
    outline-offset: 5px;
    
    /* Sombras */
    box-shadow: 5px 5px 10px rgba(0,0,0,0.3);
    box-shadow: inset 0 0 10px rgba(0,0,0,0.2);
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2), -2px -2px 5px rgba(255,255,255,0.5);
}
```

### 2.2 Display

```css
.display-examples {
    /* Básicos */
    display: block;    /* ocupa toda largura, quebra linha */
    display: inline;   /* ocupa apenas o conteúdo, não quebra linha */
    display: inline-block; /* inline mas com propriedades de bloco */
    display: none;     /* remove do fluxo, não ocupa espaço */
    display: contents; /* filhos agem como se fossem diretos */
    
    /* Flexbox */
    display: flex;
    display: inline-flex;
    
    /* Grid */
    display: grid;
    display: inline-grid;
    
    /* Layouts antigos */
    display: table;
    display: table-cell;
    display: list-item;
    
    /* Especiais */
    display: flow-root; /* contém floats */
}
```

---

## 3. FLEXBOX

### 3.1 Container Flex

```css
.container {
    display: flex;
    
    /* Direção */
    flex-direction: row; /* padrão: linha horizontal */
    flex-direction: row-reverse;
    flex-direction: column; /* coluna vertical */
    flex-direction: column-reverse;
    
    /* Quebra de linha */
    flex-wrap: nowrap; /* padrão: sem quebra */
    flex-wrap: wrap; /* quebra quando necessário */
    flex-wrap: wrap-reverse;
    
    /* Shorthand */
    flex-flow: row wrap;
    
    /* Alinhamento horizontal (main axis) */
    justify-content: flex-start; /* padrão */
    justify-content: flex-end;
    justify-content: center;
    justify-content: space-between; /* espaço entre itens */
    justify-content: space-around; /* espaço ao redor */
    justify-content: space-evenly; /* espaço igual */
    
    /* Alinhamento vertical (cross axis) */
    align-items: stretch; /* padrão */
    align-items: flex-start;
    align-items: flex-end;
    align-items: center;
    align-items: baseline;
    
    /* Alinhamento de múltiplas linhas */
    align-content: stretch; /* padrão */
    align-content: flex-start;
    align-content: flex-end;
    align-content: center;
    align-content: space-between;
    align-content: space-around;
    
    /* Gap (espaçamento entre itens) */
    gap: 20px;
    row-gap: 10px;
    column-gap: 20px;
}
```

### 3.2 Itens Flex

```css
.item {
    /* Ordem */
    order: 0; /* padrão */
    order: 1; /* itens com maior ordem aparecem depois */
    order: -1; /* itens com menor ordem aparecem antes */
    
    /* Crescimento */
    flex-grow: 0; /* padrão: não cresce */
    flex-grow: 1; /* ocupa espaço disponível */
    flex-grow: 2; /* ocupa 2x mais espaço */
    
    /* Encolhimento */
    flex-shrink: 1; /* padrão: pode encolher */
    flex-shrink: 0; /* não encolhe */
    
    /* Base (tamanho inicial) */
    flex-basis: auto; /* padrão */
    flex-basis: 200px;
    flex-basis: 50%;
    
    /* Shorthand */
    flex: 1; /* flex-grow: 1, flex-shrink: 1, flex-basis: 0 */
    flex: 0 0 200px; /* tamanho fixo */
    flex: auto; /* flex-grow: 1, flex-shrink: 1, flex-basis: auto */
    flex: none; /* flex-grow: 0, flex-shrink: 0, flex-basis: auto */
    
    /* Alinhamento individual */
    align-self: auto; /* padrão: herda do container */
    align-self: flex-start;
    align-self: flex-end;
    align-self: center;
    align-self: stretch;
    align-self: baseline;
}
```

---

## 4. GRID LAYOUT

### 4.1 Container Grid

```css
.grid-container {
    display: grid;
    
    /* Definição de colunas */
    grid-template-columns: 200px 300px 200px;
    grid-template-columns: 1fr 2fr 1fr;
    grid-template-columns: repeat(4, 1fr);
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    grid-template-columns: minmax(100px, 300px) 1fr;
    
    /* Definição de linhas */
    grid-template-rows: 100px 200px auto;
    grid-template-rows: repeat(3, 1fr);
    grid-template-rows: minmax(50px, auto);
    
    /* Shorthand */
    grid-template: 
        "header header header" 100px
        "sidebar main main" auto
        "footer footer footer" 50px
        / 200px 1fr 1fr;
    
    /* Áreas nomeadas */
    grid-template-areas: 
        "header header header"
        "sidebar main main"
        "footer footer footer";
    
    /* Gaps */
    gap: 20px;
    row-gap: 10px;
    column-gap: 20px;
    
    /* Alinhamento horizontal */
    justify-items: stretch; /* padrão */
    justify-items: start;
    justify-items: end;
    justify-items: center;
    
    /* Alinhamento vertical */
    align-items: stretch; /* padrão */
    align-items: start;
    align-items: end;
    align-items: center;
    
    /* Alinhamento do grid */
    justify-content: start;
    justify-content: end;
    justify-content: center;
    justify-content: space-between;
    justify-content: space-around;
    justify-content: space-evenly;
    
    align-content: start;
    align-content: end;
    align-content: center;
    align-content: space-between;
    align-content: space-around;
    align-content: space-evenly;
}
```

### 4.2 Itens Grid

```css
.grid-item {
    /* Posicionamento por linha/coluna */
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 1;
    grid-row-end: 3;
    
    /* Shorthand */
    grid-column: 1 / 3;
    grid-row: 1 / 3;
    grid-column: span 2; /* ocupa 2 colunas */
    grid-row: span 2; /* ocupa 2 linhas */
    
    /* Posicionamento por área nomeada */
    grid-area: header;
    
    /* Alinhamento individual */
    justify-self: start;
    justify-self: end;
    justify-self: center;
    justify-self: stretch;
    
    align-self: start;
    align-self: end;
    align-self: center;
    align-self: stretch;
}
```

---

## 5. POSICIONAMENTO

### 5.1 Position

```css
.elemento {
    /* Tipos de posicionamento */
    position: static;    /* padrão: fluxo normal */
    position: relative;  /* relativo à posição original */
    position: absolute;  /* relativo ao ancestral posicionado */
    position: fixed;     /* relativo à viewport */
    position: sticky;    /* híbrido relative/fixed */
    
    /* Coordenadas */
    top: 10px;
    right: 20px;
    bottom: 30px;
    left: 40px;
    
    /* Z-index (empilhamento) */
    z-index: 1;
    z-index: auto;
    
    /* Exemplos práticos */
    .modal {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 1000;
    }
    
    .tooltip {
        position: absolute;
        top: 100%;
        left: 0;
        margin-top: 5px;
    }
    
    .sticky-header {
        position: sticky;
        top: 0;
        background: white;
        z-index: 100;
    }
}
```

### 5.2 Float e Clear

```css
.float-example {
    /* Float */
    float: left;
    float: right;
    float: none;
    
    /* Clear */
    clear: left;
    clear: right;
    clear: both;
    clear: none;
}

/* Técnicas de clearfix */
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}

/* Columns (layout em colunas) */
.columns {
    column-count: 3;
    column-gap: 40px;
    column-rule: 1px solid #ccc;
    column-width: 200px;
}

.column-break {
    break-inside: avoid; /* evita quebra dentro do elemento */
    page-break-inside: avoid;
}
```

---

## 6. TIPOGRAFIA

### 6.1 Propriedades de Texto

```css
.texto {
    /* Família de fontes */
    font-family: Arial, Helvetica, sans-serif;
    font-family: 'Times New Roman', serif;
    font-family: 'Courier New', monospace;
    font-family: 'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont;
    
    /* Tamanho */
    font-size: 16px;
    font-size: 1em; /* relativo ao elemento pai */
    font-size: 1rem; /* relativo ao root (html) */
    font-size: 1.2vw; /* relativo à viewport */
    font-size: clamp(12px, 2vw, 24px); /* responsivo com limites */
    
    /* Peso */
    font-weight: normal; /* 400 */
    font-weight: bold; /* 700 */
    font-weight: 100; /* fino */
    font-weight: 300; /* light */
    font-weight: 500; /* medium */
    font-weight: 900; /* black */
    
    /* Estilo */
    font-style: normal;
    font-style: italic;
    font-style: oblique;
    
    /* Variante */
    font-variant: normal;
    font-variant: small-caps;
    
    /* Shorthand (ordem: style, variant, weight, size/line-height, family) */
    font: italic small-caps bold 16px/1.5 Arial, sans-serif;
    
    /* Altura da linha */
    line-height: 1.2; /* sem unidade = multiplicador */
    line-height: 1.5em;
    line-height: 24px;
    line-height: normal;
    
    /* Espaçamento */
    letter-spacing: 1px;
    word-spacing: 2px;
    
    /* Alinhamento */
    text-align: left;
    text-align: right;
    text-align: center;
    text-align: justify;
    
    /* Decoração */
    text-decoration: none;
    text-decoration: underline;
    text-decoration: overline;
    text-decoration: line-through;
    text-decoration: underline wavy red;
    
    /* Transformação */
    text-transform: none;
    text-transform: uppercase;
    text-transform: lowercase;
    text-transform: capitalize;
    
    /* Sombra de texto */
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    text-shadow: 0 0 5px blue, 0 0 10px cyan;
    
    /* Quebra de texto */
    white-space: normal;
    white-space: nowrap;
    white-space: pre;
    white-space: pre-wrap;
    word-break: break-all;
    word-break: keep-all;
    overflow-wrap: break-word;
    
    /* Elipse (...) */
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    
    /* Seleção */
    user-select: none;
    user-select: text;
    user-select: all;
    
    /* Direção */
    direction: ltr;
    direction: rtl;
    unicode-bidi: bidi-override;
}
```

---

## 7. CORES E FUNDOS

### 7.1 Cores

```css
.cores {
    /* Nome de cores */
    color: red;
    color: blue;
    color: #ff0000;
    
    /* Hexadecimal */
    color: #ff0000; /* vermelho */
    color: #f00;    /* vermelho abreviado */
    color: #ff9900; /* laranja */
    color: #f90;    /* laranja abreviado */
    
    /* RGB */
    color: rgb(255, 0, 0); /* vermelho */
    color: rgb(100%, 0%, 0%); /* vermelho */
    color: rgba(255, 0, 0, 0.5); /* vermelho semi-transparente */
    
    /* HSL */
    color: hsl(0, 100%, 50%); /* vermelho */
    color: hsla(0, 100%, 50%, 0.5); /* vermelho semi-transparente */
    
    /* HWB (Hue, Whiteness, Blackness) */
    color: hwb(0 0% 0%); /* vermelho */
    color: hwb(0 50% 0%); /* rosa */
    
    /* LAB */
    color: lab(50% 50 0); /* vermelho */
    
    /* LCH */
    color: lch(50% 50 0); /* vermelho */
    
    /* CurrentColor */
    color: currentColor; /* herda a cor do elemento */
    
    /* Variáveis CSS */
    color: var(--primary-color);
}
```

### 7.2 Fundos

```css
.fundo {
    /* Cor */
    background-color: #f0f0f0;
    background-color: rgba(0,0,0,0.5);
    
    /* Imagem */
    background-image: url('imagem.jpg');
    background-image: linear-gradient(to right, red, blue);
    background-image: radial-gradient(circle, red, blue);
    background-image: repeating-linear-gradient(45deg, red, blue 10px);
    
    /* Repetição */
    background-repeat: repeat; /* padrão */
    background-repeat: repeat-x;
    background-repeat: repeat-y;
    background-repeat: no-repeat;
    background-repeat: space;
    background-repeat: round;
    
    /* Posição */
    background-position: left top;
    background-position: center center;
    background-position: 50% 50%;
    background-position: 10px 20px;
    
    /* Tamanho */
    background-size: auto; /* padrão */
    background-size: cover; /* cobre todo o elemento */
    background-size: contain; /* contém dentro do elemento */
    background-size: 100% 100%;
    background-size: 200px 100px;
    
    /* Anexo */
    background-attachment: scroll; /* padrão */
    background-attachment: fixed; /* fixo na viewport */
    background-attachment: local; /* rola com o conteúdo */
    
    /* Origem do fundo */
    background-origin: padding-box; /* padrão */
    background-origin: border-box;
    background-origin: content-box;
    
    /* Corte do fundo */
    background-clip: border-box; /* padrão */
    background-clip: padding-box;
    background-clip: content-box;
    
    /* Shorthand (ordem: color, image, position/size, repeat, attachment, origin/clip) */
    background: #f0f0f0 url('imagem.jpg') center/cover no-repeat fixed;
    
    /* Gradientes */
    .gradiente-linear {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .gradiente-radial {
        background: radial-gradient(circle at center, #ff6b6b, #c92a2a);
    }
    .gradiente-conico {
        background: conic-gradient(from 90deg at 50% 50%, red, yellow, green, blue);
    }
}
```

---

## 8. EFEITOS E TRANSFORMAÇÕES

### 8.1 Transformações

```css
.transformacoes {
    /* Translate (movimento) */
    transform: translate(50px, 100px);
    transform: translateX(50px);
    transform: translateY(100px);
    
    /* Scale (escala) */
    transform: scale(1.5); /* 150% do tamanho */
    transform: scale(0.5, 2);
    transform: scaleX(2);
    transform: scaleY(0.5);
    
    /* Rotação */
    transform: rotate(45deg);
    transform: rotate(0.25turn);
    transform: rotate(1rad);
    
    /* Skew (inclinação) */
    transform: skew(10deg, 5deg);
    transform: skewX(10deg);
    transform: skewY(5deg);
    
    /* Múltiplas transformações */
    transform: translate(50px, 50px) rotate(45deg) scale(1.2);
    
    /* 3D Transformations */
    transform: translate3d(10px, 20px, 30px);
    transform: rotateX(45deg);
    transform: rotateY(45deg);
    transform: rotateZ(45deg);
    transform: rotate3d(1, 1, 0, 45deg);
    transform: scale3d(1.5, 1.5, 1.5);
    
    /* Perspective */
    perspective: 1000px;
    transform: perspective(1000px) rotateY(45deg);
    
    /* Transform Origin */
    transform-origin: center center;
    transform-origin: top left;
    transform-origin: 0% 0%;
    transform-origin: 50px 100px;
    
    /* 3D Transform Style */
    transform-style: flat; /* padrão */
    transform-style: preserve-3d;
    
    /* Backface Visibility */
    backface-visibility: visible;
    backface-visibility: hidden;
}
```

### 8.2 Transições

```css
.transicao {
    /* Propriedades a serem transicionadas */
    transition-property: all; /* todas propriedades */
    transition-property: background-color, transform;
    
    /* Duração */
    transition-duration: 0.3s;
    transition-duration: 300ms;
    
    /* Função de timing */
    transition-timing-function: ease; /* padrão */
    transition-timing-function: linear;
    transition-timing-function: ease-in;
    transition-timing-function: ease-out;
    transition-timing-function: ease-in-out;
    transition-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1);
    transition-timing-function: steps(4, end);
    
    /* Delay */
    transition-delay: 0s;
    transition-delay: 0.2s;
    
    /* Shorthand */
    transition: all 0.3s ease-in-out;
    transition: background-color 0.3s, transform 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
```

### 8.3 Filtros

```css
.filtros {
    /* Filtros básicos */
    filter: blur(5px); /* desfoque */
    filter: brightness(1.2); /* brilho */
    filter: contrast(150%); /* contraste */
    filter: grayscale(100%); /* preto e branco */
    filter: hue-rotate(90deg); /* rotação de matiz */
    filter: invert(100%); /* inverter cores */
    filter: opacity(50%); /* opacidade */
    filter: saturate(200%); /* saturação */
    filter: sepia(100%); /* efeito sépia */
    filter: drop-shadow(5px 5px 10px rgba(0,0,0,0.5)); /* sombra */
    
    /* Múltiplos filtros */
    filter: blur(2px) brightness(1.2) contrast(150%);
    
    /* Filtros SVG */
    filter: url(#filtro-svg);
}
```

---

## 9. ANIMAÇÕES

### 9.1 Keyframes e Animation

```css
/* Definindo keyframes */
@keyframes slideIn {
    from {
        transform: translateX(-100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1);
    }
}

@keyframes spin {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

/* Aplicando animação */
.animado {
    /* Nome da animação */
    animation-name: slideIn;
    
    /* Duração */
    animation-duration: 0.5s;
    
    /* Função de timing */
    animation-timing-function: ease-out;
    
    /* Delay */
    animation-delay: 0s;
    
    /* Iterações */
    animation-iteration-count: 1;
    animation-iteration-count: infinite;
    animation-iteration-count: 3;
    
    /* Direção */
    animation-direction: normal; /* padrão */
    animation-direction: reverse;
    animation-direction: alternate;
    animation-direction: alternate-reverse;
    
    /* Modo de preenchimento */
    animation-fill-mode: none; /* padrão */
    animation-fill-mode: forwards; /* mantém último estado */
    animation-fill-mode: backwards; /* aplica primeiro estado */
    animation-fill-mode: both;
    
    /* Estado de execução */
    animation-play-state: running;
    animation-play-state: paused;
    
    /* Shorthand */
    animation: slideIn 0.5s ease-out forwards;
    animation: pulse 2s ease-in-out infinite;
    animation: spin 1s linear infinite;
}

/* Exemplos práticos */
.spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #f3f3f3;
    border-top: 4px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

.skeleton {
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: loading 1.5s infinite;
}

@keyframes loading {
    0% {
        background-position: 200% 0;
    }
    100% {
        background-position: -200% 0;
    }
}
```

---

## 10. RESPONSIVIDADE

### 10.1 Unidades Responsivas

```css
.unidades {
    /* Unidades relativas */
    width: 50%; /* porcentagem do elemento pai */
    width: 50vw; /* viewport width (1vw = 1% da largura) */
    height: 50vh; /* viewport height */
    width: 50vmin; /* menor entre vw e vh */
    width: 50vmax; /* maior entre vw e vh */
    font-size: 1rem; /* relativo ao root (16px padrão) */
    font-size: 1em; /* relativo ao elemento pai */
    
    /* Unidades modernas */
    width: clamp(200px, 50%, 800px); /* valor responsivo com limites */
    width: min(50%, 500px); /* valor mínimo entre as opções */
    width: max(200px, 50%); /* valor máximo entre as opções */
    
    /* Viewport dinâmico (novas) */
    width: 100dvw; /* viewport dinâmica */
    height: 100dvh;
    width: 100svw; /* viewport segura */
    height: 100svh;
}
```

### 10.2 Containers Responsivos

```css
.container-responsivo {
    /* Container queries (CSS Container) */
    container-type: inline-size;
    container-name: sidebar;
    
    @container sidebar (min-width: 300px) {
        .card {
            display: flex;
            flex-direction: row;
        }
    }
    
    /* Exemplo prático */
    .card {
        container-type: inline-size;
    }
    
    @container (max-width: 400px) {
        .card {
            flex-direction: column;
        }
        .card-image {
            width: 100%;
        }
    }
}
```

---

## 11. CSS VARIABLES

### 11.1 Definindo e Usando Variáveis

```css
/* Definindo variáveis */
:root {
    /* Cores */
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --danger-color: #dc3545;
    --warning-color: #ffc107;
    --info-color: #17a2b8;
    --light-color: #f8f9fa;
    --dark-color: #343a40;
    
    /* Espaçamentos */
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
    
    /* Tipografia */
    --font-family-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    --font-size-base: 16px;
    --font-size-lg: 1.25rem;
    --font-size-sm: 0.875rem;
    
    /* Sombras */
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
    --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
    
    /* Bordas */
    --border-radius-sm: 4px;
    --border-radius-md: 8px;
    --border-radius-lg: 12px;
    --border-radius-full: 9999px;
    
    /* Transições */
    --transition-fast: 0.15s ease;
    --transition-base: 0.3s ease;
    --transition-slow: 0.5s ease;
}

/* Usando variáveis */
.button {
    background-color: var(--primary-color);
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--border-radius-md);
    font-family: var(--font-family-sans);
    transition: all var(--transition-base);
    box-shadow: var(--shadow-sm);
}

.button:hover {
    background-color: var(--secondary-color);
    box-shadow: var(--shadow-md);
}

/* Variáveis com fallback */
.element {
    color: var(--color-unknown, #000000); /* fallback preto */
}

/* Variáveis em media queries */
@media (prefers-color-scheme: dark) {
    :root {
        --primary-color: #0056b3;
        --light-color: #212529;
        --dark-color: #f8f9fa;
    }
}

/* Variáveis em JavaScript */
/*
document.documentElement.style.setProperty('--primary-color', '#ff0000');
const primaryColor = getComputedStyle(document.documentElement).getPropertyValue('--primary-color');
*/
```

---

## 12. CSS FUNCTIONS

### 12.1 Funções CSS Modernas

```css
.functions {
    /* Calc */
    width: calc(100% - 20px);
    height: calc(50vh + 100px);
    font-size: calc(1rem + 0.5vw);
    
    /* Min / Max / Clamp */
    width: min(100%, 500px);
    width: max(200px, 50%);
    width: clamp(200px, 50%, 800px);
    font-size: clamp(12px, 2vw, 24px);
    
    /* Var (já visto) */
    color: var(--primary-color);
    
    /* URL */
    background-image: url('/images/bg.jpg');
    
    /* Attr (atributo HTML) */
    content: attr(data-tooltip);
    
    /* Counter */
    counter-reset: section;
    counter-increment: section;
    content: counter(section);
    
    /* RGB / HSL com alpha */
    color: rgb(255 0 0 / 0.5);
    color: hsl(0 100% 50% / 0.5);
    
    /* Color Mix (CSS Color 5) */
    color: color-mix(in srgb, red 50%, blue);
    
    /* Shape (clip-path) */
    clip-path: circle(50% at 50% 50%);
    clip-path: polygon(0% 0%, 100% 0%, 100% 75%, 75% 75%, 75% 100%, 50% 75%, 0% 75%);
    
    /* Filter */
    filter: blur(5px);
    
    /* Gradient */
    background: linear-gradient(45deg, red, blue);
    
    /* Transform */
    transform: translate(50%, 50%);
    
    /* Custom properties */
    --custom: 10px;
}
```

---

## 13. MEDIA QUERIES

### 13.1 Media Queries Completas

```css
/* Media Queries Básicas */
@media screen {
    /* Telas */
}

@media print {
    /* Impressão */
    nav, .ad {
        display: none;
    }
    body {
        font-size: 12pt;
    }
}

@media speech {
    /* Leitores de tela */
}

/* Media Types */
@media all { /* Todos os tipos */ }
@media screen { /* Telas */ }
@media print { /* Impressão */ }
@media speech { /* Leitores de tela */ }

/* Media Features */
/* Largura */
@media (width: 800px) { }
@media (min-width: 768px) { }
@media (max-width: 1024px) { }
@media (width >= 768px) { } /* Sintaxe moderna */
@media (768px <= width <= 1024px) { }

/* Altura */
@media (height: 600px) { }
@media (min-height: 400px) { }
@media (max-height: 800px) { }

/* Orientação */
@media (orientation: portrait) { }
@media (orientation: landscape) { }

/* Resolução */
@media (resolution: 2dppx) { }
@media (min-resolution: 192dpi) { }

/* Aspect Ratio */
@media (aspect-ratio: 16/9) { }
@media (min-aspect-ratio: 4/3) { }

/* Preferências de cor */
@media (prefers-color-scheme: dark) {
    body {
        background: #1a1a1a;
        color: #fff;
    }
}
@media (prefers-color-scheme: light) { }

/* Preferência de contraste */
@media (prefers-contrast: high) { }
@media (prefers-contrast: low) { }

/* Preferência de movimento */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}

/* Hover e pointer */
@media (hover: hover) { /* Dispositivo com hover */ }
@media (hover: none) { /* Touch screen */ }
@media (pointer: fine) { /* Mouse */ }
@media (pointer: coarse) { /* Touch */ }

/* Combinando condições */
@media (min-width: 768px) and (orientation: landscape) { }
@media (min-width: 768px), (min-width: 1024px) { }
@media not print { }
@media (min-width: 768px) and (max-width: 1024px) { }

/* Container Queries (modernas) */
@container (min-width: 300px) {
    .card {
        display: flex;
    }
}
```

### 13.2 Breakpoints Comuns

```css
/* Breakpoints Responsivos */
/* Extra small (xs) */
@media (max-width: 575.98px) { }

/* Small (sm) */
@media (min-width: 576px) and (max-width: 767.98px) { }

/* Medium (md) */
@media (min-width: 768px) and (max-width: 991.98px) { }

/* Large (lg) */
@media (min-width: 992px) and (max-width: 1199.98px) { }

/* Extra large (xl) */
@media (min-width: 1200px) and (max-width: 1399.98px) { }

/* Extra extra large (xxl) */
@media (min-width: 1400px) { }

/* Mobile-first (recomendado) */
/* Base (mobile) */
.container {
    width: 100%;
    padding: 0 15px;
}

/* Tablet */
@media (min-width: 768px) {
    .container {
        width: 750px;
        margin: 0 auto;
    }
}

/* Desktop */
@media (min-width: 992px) {
    .container {
        width: 970px;
    }
}

/* Large Desktop */
@media (min-width: 1200px) {
    .container {
        width: 1170px;
    }
}
```

---

## 14. LAYOUTS MODERNOS

### 14.1 CSS Grid Avançado

```css
/* Layout Dashboard */
.dashboard {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 20px;
}

.sidebar {
    grid-column: span 2;
}

.main-content {
    grid-column: span 10;
}

/* Masonry Layout */
.masonry {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-auto-rows: 10px;
}

.masonry-item {
    grid-row-end: span 20; /* Altura variável */
}

/* Subgrid (CSS Grid Level 2) */
.parent-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}

.child-grid {
    display: grid;
    grid-template-columns: subgrid;
    grid-column: span 2;
}

/* Holy Grail Layout */
.holy-grail {
    display: grid;
    grid-template-areas: 
        "header header header"
        "nav main aside"
        "footer footer footer";
    grid-template-columns: 200px 1fr 200px;
    grid-template-rows: auto 1fr auto;
    min-height: 100vh;
}

.header { grid-area: header; }
.nav { grid-area: nav; }
.main { grid-area: main; }
.aside { grid-area: aside; }
.footer { grid-area: footer; }
```

### 14.2 CSS Flexbox Avançado

```css
/* Navbar responsiva */
.navbar {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
}

.nav-menu {
    display: flex;
    gap: 1rem;
}

@media (max-width: 768px) {
    .nav-menu {
        display: none;
        width: 100%;
        flex-direction: column;
    }
    .nav-menu.active {
        display: flex;
    }
}

/* Card grid */
.card-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.card {
    flex: 1 1 calc(33.333% - 20px);
    min-width: 250px;
}

/* Footer sticky */
body {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

main {
    flex: 1;
}

/* Modal centralizado */
.modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.5);
}

.modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    max-width: 90%;
    max-height: 90%;
    overflow: auto;
}
```

### 14.3 CSS Functions Modernas

```css
/* Aspect Ratio */
.video-container {
    aspect-ratio: 16 / 9;
    width: 100%;
}

/* Logical Properties (suporte a RTL) */
.element {
    margin-inline-start: 20px;
    margin-inline-end: 20px;
    padding-block: 10px;
    inset-inline-start: 0;
    border-inline: 1px solid #ccc;
}

/* Color Functions */
.element {
    background: color-mix(in srgb, red 30%, blue);
    color: oklch(70% 0.15 40);
}

/* View Transitions */
@keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
}

::view-transition-old(root) {
    animation: fade-out 0.3s ease;
}

::view-transition-new(root) {
    animation: fade-in 0.3s ease;
}
```

---

## 📊 TABELA RESUMO CSS

| Categoria | Principais Propriedades |
|-----------|------------------------|
| **Seletores** | `*`, `.classe`, `#id`, `[attr]`, `:hover`, `::before` |
| **Box Model** | `width`, `height`, `margin`, `padding`, `border` |
| **Flexbox** | `display: flex`, `justify-content`, `align-items`, `flex` |
| **Grid** | `display: grid`, `grid-template-columns`, `gap`, `grid-area` |
| **Posicionamento** | `position`, `top`, `left`, `z-index`, `float` |
| **Tipografia** | `font-family`, `font-size`, `line-height`, `text-align` |
| **Cores** | `color`, `background`, `background-image`, `gradient` |
| **Efeitos** | `transform`, `transition`, `animation`, `filter` |
| **Responsividade** | `@media`, `min-width`, `max-width`, `clamp()` |

---

# 💻 JAVASCRIPT - CHEAT SHEET MEGA COMPLETO
## *Todos os conceitos, APIs e técnicas modernas*

---

## 📚 SUMÁRIO JAVASCRIPT

1. [Fundamentos](#1-fundamentos-javascript)
2. [Funções](#2-funções-javascript)
3. [Objetos e Classes](#3-objetos-e-classes)
4. [Arrays](#4-arrays)
5. [Promises e Async](#5-promises-e-async)
6. [DOM Manipulação](#6-dom-manipulação)
7. [Eventos](#7-eventos)
8. [APIs Nativas](#8-apis-nativas)
9. [ES6+ Features](#9-es6-features)
10. [Módulos](#10-módulos)
11. [Erros e Debugging](#11-erros-e-debugging)
12. [Web APIs](#12-web-apis)

---

## 1. FUNDAMENTOS JAVASCRIPT

### 1.1 Variáveis e Tipos

```javascript
// Variáveis
var antigo = "não use"; // escopo de função, hoisting
let moderno = "use"; // escopo de bloco
const constante = "não muda"; // não pode ser reatribuída

// Tipos primitivos
const string = "texto";
const number = 42;
const bigint = 9007199254740991n;
const boolean = true;
const nulo = null;
const indefinido = undefined;
const simbolo = Symbol('id');
const bigInt = 1234567890123456789012345678901234567890n;

// Typeof
typeof "texto"; // "string"
typeof 42; // "number"
typeof true; // "boolean"
typeof undefined; // "undefined"
typeof null; // "object" (bug histórico)
typeof Symbol(); // "symbol"
typeof {}; // "object"
typeof []; // "object"
typeof function(){}; // "function"

// Conversão de tipos
Number("123"); // 123
String(123); // "123"
Boolean(0); // false
Boolean(1); // true
parseInt("123px"); // 123
parseFloat("123.45px"); // 123.45
+ "123"; // 123 (conversão rápida)

// Template literals
const nome = "João";
const idade = 30;
const mensagem = `Olá, ${nome}! Você tem ${idade} anos.`;
const multiLinha = `
    Linha 1
    Linha 2
    Linha 3
`;
```

### 1.2 Operadores

```javascript
// Aritméticos
let a = 10, b = 3;
a + b; // 13
a - b; // 7
a * b; // 30
a / b; // 3.333...
a % b; // 1
a ** b; // 1000 (potência)

// Atribuição
a += 5; // a = a + 5
a -= 3; // a = a - 3
a *= 2; // a = a * 2
a /= 4; // a = a / 4
a %= 2; // a = a % 2
a **= 2; // a = a ** 2

// Comparação
5 == "5"; // true (valor)
5 === "5"; // false (valor e tipo)
5 != "5"; // false
5 !== "5"; // true
5 > 3; // true
5 < 3; // false
5 >= 5; // true
5 <= 3; // false

// Lógicos
true && true; // true (AND)
true || false; // true (OR)
!true; // false (NOT)

// Nullish coalescing
null ?? "padrão"; // "padrão"
undefined ?? "padrão"; // "padrão"
0 ?? "padrão"; // 0
false ?? "padrão"; // false

// Optional chaining
const user = { profile: { name: "João" } };
user?.profile?.name; // "João"
user?.address?.city; // undefined

// Spread e Rest
const arr = [1, 2, 3];
const newArr = [...arr, 4, 5]; // [1,2,3,4,5]
const obj = { a: 1, b: 2 };
const newObj = { ...obj, c: 3 }; // {a:1, b:2, c:3}

const [primeiro, ...resto] = arr; // primeiro=1, resto=[2,3]
const { a, ...outros } = obj; // a=1, outros={b:2}
```

### 1.3 Estruturas de Controle

```javascript
// if/else
if (condicao) {
    // código
} else if (outraCondicao) {
    // código
} else {
    // código
}

// Ternário
const resultado = condicao ? "verdadeiro" : "falso";

// Switch
switch (valor) {
    case 1:
        console.log("um");
        break;
    case 2:
        console.log("dois");
        break;
    default:
        console.log("outro");
}

// for
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// for...of (iteráveis)
for (const item of [1, 2, 3]) {
    console.log(item);
}

// for...in (objetos)
for (const key in { a: 1, b: 2 }) {
    console.log(key);
}

// while
let i = 0;
while (i < 10) {
    console.log(i);
    i++;
}

// do...while
let j = 0;
do {
    console.log(j);
    j++;
} while (j < 10);

// forEach
[1, 2, 3].forEach(item => console.log(item));

// break e continue
for (let i = 0; i < 10; i++) {
    if (i === 5) break; // sai do loop
    if (i % 2 === 0) continue; // pula iteração
    console.log(i);
}
```

---

## 2. FUNÇÕES JAVASCRIPT

### 2.1 Declaração de Funções

```javascript
// Function declaration
function soma(a, b) {
    return a + b;
}

// Function expression
const soma = function(a, b) {
    return a + b;
};

// Arrow function
const soma = (a, b) => a + b;
const quadrado = x => x ** 2;
const semRetorno = () => console.log("Olá");

// Função com parâmetros padrão
function saudacao(nome = "Visitante") {
    return `Olá, ${nome}!`;
}

// Rest parameters
function somaTodos(...numeros) {
    return numeros.reduce((acc, n) => acc + n, 0);
}

// Parâmetros nomeados (destructuring)
function configurar({ host, port = 80, ssl = false }) {
    console.log(host, port, ssl);
}

// IIFE (Immediately Invoked Function Expression)
(function() {
    console.log("Executada imediatamente");
})();

(() => console.log("Arrow IIFE"))();

// Função que retorna função (closure)
function multiplicador(fator) {
    return function(numero) {
        return numero * fator;
    };
}

const duplicar = multiplicador(2);
console.log(duplicar(5)); // 10

// Função geradora
function* gerador() {
    yield 1;
    yield 2;
    yield 3;
}

const gen = gerador();
gen.next(); // { value: 1, done: false }
gen.next(); // { value: 2, done: false }
gen.next(); // { value: 3, done: false }
gen.next(); // { value: undefined, done: true }
```

### 2.2 Métodos de Função

```javascript
// call, apply, bind
function apresentar(prefixo, sufixo) {
    return `${prefixo} ${this.nome} ${sufixo}`;
}

const pessoa = { nome: "João" };

apresentar.call(pessoa, "Sr.", "Silva"); // "Sr. João Silva"
apresentar.apply(pessoa, ["Sr.", "Silva"]); // "Sr. João Silva"

const apresentarJoao = apresentar.bind(pessoa, "Sr.");
apresentarJoao("Silva"); // "Sr. João Silva"

// Recursão
function fatorial(n) {
    if (n <= 1) return 1;
    return n * fatorial(n - 1);
}

// Memoization
function memoize(fn) {
    const cache = new Map();
    return function(...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) return cache.get(key);
        const result = fn(...args);
        cache.set(key, result);
        return result;
    };
}

const fibonacci = memoize(function(n) {
    if (n < 2) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
});
```

---

## 3. OBJETOS E CLASSES

### 3.1 Objetos

```javascript
// Criação de objetos
const obj1 = {};
const obj2 = new Object();
const obj3 = Object.create(null);

// Literal
const pessoa = {
    nome: "João",
    idade: 30,
    saudacao() {
        return `Olá, ${this.nome}!`;
    },
    get aniversario() {
        return `${this.nome} faz aniversário em...`;
    },
    set idade(valor) {
        if (valor > 0) this._idade = valor;
    }
};

// Object methods
const chaves = Object.keys(pessoa);
const valores = Object.values(pessoa);
const entradas = Object.entries(pessoa);

// Destructuring
const { nome, idade } = pessoa;
const { nome: nomeCompleto, cidade = "Não informada" } = pessoa;

// Spread
const copia = { ...pessoa, cidade: "SP" };

// Object.assign
const mesclado = Object.assign({}, pessoa, { cidade: "SP" });

// Object.freeze (imutável)
const congelado = Object.freeze({ a: 1 });
congelado.a = 2; // não funciona (strict mode lança erro)

// Object.seal (não pode adicionar/remover, mas pode modificar)
const selado = Object.seal({ a: 1 });
selado.a = 2; // funciona
selado.b = 3; // não funciona

// Getters e Setters
const produto = {
    _preco: 100,
    get preco() {
        return `R$ ${this._preco}`;
    },
    set preco(valor) {
        if (valor > 0) this._preco = valor;
    }
};

// Computed properties
const key = "nome";
const obj = { [key]: "João" }; // { nome: "João" }

// Property descriptors
Object.defineProperty(obj, "prop", {
    value: 42,
    writable: false,
    enumerable: true,
    configurable: false
});
```

### 3.2 Classes (ES6+)

```javascript
// Classe básica
class Animal {
    // Construtor
    constructor(nome) {
        this.nome = nome;
        this._idade = 0;
    }
    
    // Método de instância
    falar() {
        return `${this.nome} faz um som`;
    }
    
    // Getter
    get idade() {
        return this._idade;
    }
    
    // Setter
    set idade(valor) {
        if (valor >= 0) this._idade = valor;
    }
    
    // Método estático
    static criar(nome) {
        return new Animal(nome);
    }
    
    // Método privado (com #)
    #privado() {
        return "só dentro da classe";
    }
}

// Herança
class Cachorro extends Animal {
    constructor(nome, raca) {
        super(nome); // chama construtor da classe pai
        this.raca = raca;
    }
    
    // Sobrescrita de método
    falar() {
        return `${super.falar()} - Au au!`;
    }
    
    // Método específico
    buscar() {
        return `${this.nome} está buscando a bola!`;
    }
}

// Instanciação
const rex = new Cachorro("Rex", "Labrador");
rex.falar(); // "Rex faz um som - Au au!"
rex.buscar(); // "Rex está buscando a bola!"

// Classe com campos privados
class Conta {
    #saldo = 0; // campo privado
    
    constructor(titular) {
        this.titular = titular;
    }
    
    depositar(valor) {
        if (valor > 0) this.#saldo += valor;
    }
    
    get saldo() {
        return this.#saldo;
    }
}

// Mixins
const falador = {
    falar() {
        console.log(`${this.nome} está falando`);
    }
};

class Robo {
    constructor(nome) {
        this.nome = nome;
    }
}

Object.assign(Robo.prototype, falador);
```

---

## 4. ARRAYS

### 4.1 Métodos de Array

```javascript
// Criação
const arr1 = [1, 2, 3];
const arr2 = new Array(5); // [empty × 5]
const arr3 = Array.from("hello"); // ['h','e','l','l','o']
const arr4 = Array.of(1, 2, 3); // [1,2,3]
const arr5 = [...arr1]; // cópia

// Métodos de iteração
[1, 2, 3].forEach(num => console.log(num));

const dobrados = [1, 2, 3].map(num => num * 2); // [2,4,6]

const pares = [1, 2, 3, 4].filter(num => num % 2 === 0); // [2,4]

const soma = [1, 2, 3].reduce((acc, num) => acc + num, 0); // 6
const produto = [1, 2, 3].reduce((acc, num) => acc * num, 1); // 6

const todosMaiores = [2, 4, 6].every(num => num > 1); // true
const algumMaior = [1, 2, 3].some(num => num > 2); // true

const primeiroPar = [1, 2, 3].find(num => num % 2 === 0); // 2
const indicePar = [1, 2, 3].findIndex(num => num % 2 === 0); // 1

// Transformação
const flat = [1, [2, [3]]].flat(2); // [1,2,3]
const flatMap = [1, 2].flatMap(x => [x, x * 2]); // [1,2,2,4]

// Ordenação
[3, 1, 4, 2].sort(); // [1,2,3,4]
[3, 1, 4, 2].sort((a, b) => b - a); // [4,3,2,1]

// Inserção e remoção
const arr = [1, 2];
arr.push(3); // [1,2,3] (final)
arr.pop(); // remove último
arr.unshift(0); // [0,1,2] (início)
arr.shift(); // remove primeiro
arr.splice(1, 0, 'a'); // insere no índice 1
arr.splice(1, 1); // remove 1 elemento no índice 1

// Concatenação
const combinado = [1, 2].concat([3, 4]); // [1,2,3,4]

// Busca
[1, 2, 3].includes(2); // true
[1, 2, 3].indexOf(2); // 1
[1, 2, 3].lastIndexOf(2); // 1

// Cópia
const original = [1, 2, 3];
const copia = original.slice(); // cópia rasa
const parte = original.slice(1, 2); // [2]

// Preenchimento
new Array(5).fill(0); // [0,0,0,0,0]
[1, 2, 3, 4].fill(0, 1, 3); // [1,0,0,4]

// Array-like conversion
const nodeList = document.querySelectorAll('div');
const array = Array.from(nodeList);
const args = Array.from(arguments);
```

### 4.2 Array Destructuring

```javascript
// Básico
const [a, b, c] = [1, 2, 3]; // a=1, b=2, c=3

// Ignorar elementos
const [primeiro, , terceiro] = [1, 2, 3]; // primeiro=1, terceiro=3

// Rest operator
const [primeiro, ...resto] = [1, 2, 3, 4]; // primeiro=1, resto=[2,3,4]

// Valores padrão
const [x = 1, y = 2] = [10]; // x=10, y=2

// Troca de valores
let x = 1, y = 2;
[x, y] = [y, x]; // x=2, y=1

// Aninhado
const [a, [b, c]] = [1, [2, 3]]; // a=1, b=2, c=3

// Em parâmetros de função
function soma([x, y]) {
    return x + y;
}
soma([1, 2]); // 3
```

---

## 5. PROMISES E ASYNC

### 5.1 Promises

```javascript
// Criando Promise
const promise = new Promise((resolve, reject) => {
    // operação assíncrona
    setTimeout(() => {
        const sucesso = true;
        if (sucesso) {
            resolve("Dados recebidos");
        } else {
            reject(new Error("Falha na operação"));
        }
    }, 1000);
});

// Consumindo Promise
promise
    .then(resultado => {
        console.log(resultado);
        return resultado.toUpperCase();
    })
    .then(resultadoUpper => {
        console.log(resultadoUpper);
    })
    .catch(erro => {
        console.error(erro);
    })
    .finally(() => {
        console.log("Sempre executa");
    });

// Promise.all (todas resolvem)
const p1 = Promise.resolve(1);
const p2 = Promise.resolve(2);
const p3 = Promise.resolve(3);

Promise.all([p1, p2, p3])
    .then(resultados => console.log(resultados)) // [1,2,3]
    .catch(erro => console.error(erro));

// Promise.allSettled (espera todas terminarem)
Promise.allSettled([p1, p2, p3])
    .then(resultados => {
        resultados.forEach(r => {
            if (r.status === 'fulfilled') {
                console.log(r.value);
            } else {
                console.log(r.reason);
            }
        });
    });

// Promise.race (primeira que terminar)
Promise.race([p1, p2, p3])
    .then(resultado => console.log(resultado));

// Promise.any (primeira que resolver)
Promise.any([p1, p2, p3])
    .then(resultado => console.log(resultado));

// Promise.resolve / Promise.reject
Promise.resolve(42);
Promise.reject(new Error("Erro"));
```

### 5.2 Async/Await

```javascript
// Função assíncrona
async function buscarDados() {
    try {
        const response = await fetch('https://api.exemplo.com/dados');
        const dados = await response.json();
        return dados;
    } catch (erro) {
        console.error('Erro:', erro);
        throw erro;
    }
}

// Execução
async function main() {
    try {
        const dados = await buscarDados();
        console.log(dados);
    } catch (erro) {
        console.error('Falha:', erro);
    }
}

// Async com Promise.all
async function buscarMultiplos() {
    const [user, posts] = await Promise.all([
        fetch('/user').then(r => r.json()),
        fetch('/posts').then(r => r.json())
    ]);
    return { user, posts };
}

// Async com for-await-of (iteradores assíncronos)
async function processarAsyncIterator() {
    const urls = ['url1', 'url2', 'url3'];
    for await (const url of urls) {
        const response = await fetch(url);
        console.log(await response.json());
    }
}
```

---

## 6. DOM MANIPULAÇÃO

### 6.1 Seletores

```javascript
// Seletores básicos
document.getElementById('id');
document.getElementsByClassName('classe');
document.getElementsByTagName('div');
document.getElementsByName('nome');

// Seletores modernos
document.querySelector('.classe');
document.querySelector('#id');
document.querySelectorAll('div.classe');

// Seletores avançados
document.querySelector('div > p:first-child');
document.querySelector('[data-id="123"]');
document.querySelectorAll('input[type="text"]');

// Navegação
element.parentNode;
element.parentElement;
element.children;
element.firstChild;
element.lastChild;
element.nextSibling;
element.previousSibling;
element.childNodes;

// Closest (busca ancestral)
element.closest('.container');
```

### 6.2 Manipulação de Elementos

```javascript
// Criar elementos
const div = document.createElement('div');
const texto = document.createTextNode('Texto');
const fragmento = document.createDocumentFragment();

// Adicionar elementos
element.appendChild(child);
element.insertBefore(novo, referencia);
element.append(child1, child2); // ES6
element.prepend(child); // ES6
element.after(child); // ES6
element.before(child); // ES6

// Remover elementos
element.removeChild(child);
element.remove(); // ES6

// Substituir
element.replaceChild(novo, antigo);

// Clonar
const clone = element.cloneNode(true); // deep clone

// Conteúdo
element.innerHTML = '<span>HTML</span>';
element.textContent = 'Texto puro';
element.innerText = 'Texto visível';

// Atributos
element.setAttribute('id', 'novo-id');
element.getAttribute('id');
element.removeAttribute('id');
element.hasAttribute('id');
element.classList.add('classe');
element.classList.remove('classe');
element.classList.toggle('classe');
element.classList.contains('classe');
element.classList.replace('antiga', 'nova');

// Estilos
element.style.color = 'red';
element.style.cssText = 'color: red; font-size: 16px;';
element.style.setProperty('--variavel', 'valor');
window.getComputedStyle(element);

// Classes
element.className = 'classe1 classe2';
element.classList.add('classe');

// Dataset (data-*)
element.dataset.id = '123';
element.dataset.userName = 'joao';
// <div data-id="123" data-user-name="joao"></div>
```

### 6.3 Manipulação Avançada

```javascript
// Intersection Observer
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, { threshold: 0.5 });

observer.observe(document.querySelector('.elemento'));

// Mutation Observer
const mutationObserver = new MutationObserver((mutations) => {
    mutations.forEach(mutation => {
        if (mutation.type === 'childList') {
            console.log('Filhos alterados');
        }
    });
});

mutationObserver.observe(element, {
    childList: true,
    attributes: true,
    subtree: true
});

// Resize Observer
const resizeObserver = new ResizeObserver((entries) => {
    for (const entry of entries) {
        console.log(entry.contentRect.width);
    }
});

resizeObserver.observe(element);
```

---

## 7. EVENTOS

### 7.1 Manipulação de Eventos

```javascript
// Adicionar evento
element.addEventListener('click', (event) => {
    console.log('Clicou!', event);
});

// Remover evento
function handler(event) {
    console.log(event);
}
element.addEventListener('click', handler);
element.removeEventListener('click', handler);

// Eventos inline (não recomendado)
element.onclick = (event) => console.log(event);
element.onclick = null; // remove

// Event object
element.addEventListener('click', (event) => {
    event.target; // elemento que disparou
    event.currentTarget; // elemento que tem o listener
    event.type; // 'click'
    event.preventDefault(); // cancela ação padrão
    event.stopPropagation(); // impede propagação
    event.stopImmediatePropagation(); // impede outros listeners
});

// Delegation
document.querySelector('.container').addEventListener('click', (event) => {
    if (event.target.matches('.botao')) {
        console.log('Botão clicado');
    }
});
```

### 7.2 Tipos de Eventos

```javascript
// Mouse
click, dblclick, mousedown, mouseup, mouseenter, mouseleave, mousemove, mouseover, mouseout, contextmenu

// Keyboard
keydown, keyup, keypress

// Formulário
submit, change, input, focus, blur, reset, select

// Window/Document
load, DOMContentLoaded, resize, scroll, unload, beforeunload, error

// Drag and Drop
dragstart, dragend, dragenter, dragleave, dragover, drop

// Touch
touchstart, touchmove, touchend, touchcancel

// Clipboard
copy, cut, paste

// Media
play, pause, ended, timeupdate, volumechange

// Custom Events
const evento = new CustomEvent('meu-evento', { detail: { dados: 123 } });
element.dispatchEvent(evento);

element.addEventListener('meu-evento', (e) => {
    console.log(e.detail.dados);
});
```

---

## 8. APIS NATIVAS

### 8.1 Storage

```javascript
// localStorage (persistente)
localStorage.setItem('chave', 'valor');
const valor = localStorage.getItem('chave');
localStorage.removeItem('chave');
localStorage.clear();

// sessionStorage (por sessão)
sessionStorage.setItem('chave', 'valor');

// Armazenar objetos
const user = { nome: 'João', idade: 30 };
localStorage.setItem('user', JSON.stringify(user));
const userObj = JSON.parse(localStorage.getItem('user'));
```

### 8.2 Fetch API

```javascript
// GET
fetch('https://api.exemplo.com/dados')
    .then(response => {
        if (!response.ok) throw new Error('Erro HTTP');
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error(error));

// POST
fetch('https://api.exemplo.com/dados', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ nome: 'João', idade: 30 })
})
.then(response => response.json())
.then(data => console.log(data));

// PUT / DELETE
fetch('/dados/1', { method: 'PUT', body: JSON.stringify(data) });
fetch('/dados/1', { method: 'DELETE' });

// Upload de arquivo
const formData = new FormData();
formData.append('arquivo', fileInput.files[0]);
fetch('/upload', { method: 'POST', body: formData });

// AbortController (cancelamento)
const controller = new AbortController();
fetch('/dados', { signal: controller.signal })
    .then(response => response.json());
controller.abort(); // cancela requisição
```

### 8.3 Web Storage e IndexedDB

```javascript
// IndexedDB (banco de dados local)
const request = indexedDB.open('MeuBanco', 1);

request.onerror = (event) => console.error('Erro');
request.onsuccess = (event) => {
    const db = event.target.result;
    console.log('Conectado', db);
};

request.onupgradeneeded = (event) => {
    const db = event.target.result;
    const store = db.createObjectStore('usuarios', { keyPath: 'id' });
    store.createIndex('nome', 'nome', { unique: false });
};

// Operações
const transaction = db.transaction(['usuarios'], 'readwrite');
const store = transaction.objectStore('usuarios');

// Inserir
store.add({ id: 1, nome: 'João', idade: 30 });

// Buscar
const getRequest = store.get(1);
getRequest.onsuccess = () => console.log(getRequest.result);
```

---

## 9. ES6+ FEATURES

### 9.1 Novidades por Versão

```javascript
// ES6 (2015)
// let/const, arrow functions, classes, template literals, destructuring
// spread/rest, default parameters, modules, promises

// ES7 (2016)
// Array.includes(), exponenciação (**)

// ES8 (2017)
// async/await, Object.values(), Object.entries()
// Object.getOwnPropertyDescriptors(), trailing commas

// ES9 (2018)
// Rest/Spread para objetos, async iteration, Promise.finally()

// ES10 (2019)
// Array.flat(), Array.flatMap(), Object.fromEntries()
// String.trimStart(), String.trimEnd(), try/catch opcional

// ES11 (2020)
// BigInt, Nullish coalescing (??), Optional chaining (?.)
// Promise.allSettled(), globalThis, import.meta

// ES12 (2021)
// Logical assignment (&&=, ||=, ??=), Numeric separators (_)
// String.replaceAll(), Promise.any()

// ES13 (2022)
// Top-level await, .at() method, Object.hasOwn()
// Class fields, Error cause

// ES14 (2023)
// Array.toSorted(), Array.toReversed(), Array.toSpliced()
// Array.with(), WeakMap/Set symbols
```

### 9.2 Exemplos ES6+

```javascript
// Destructuring
const { a, b } = obj;
const [c, d] = arr;

// Spread/Rest
const novo = { ...obj, c: 3 };
const [primeiro, ...resto] = arr;

// Nullish coalescing
const valor = input ?? 'padrão';

// Optional chaining
const cidade = user?.endereco?.cidade;

// Logical assignment
x ||= 10; // x = x || 10
x &&= 10; // x = x && 10
x ??= 10; // x = x ?? 10

// Numeric separators
const milhao = 1_000_000;

// String replaceAll
'1-2-3'.replaceAll('-', '.'); // '1.2.3'

// Array.at()
const arr = [1, 2, 3];
arr.at(-1); // 3

// Object.hasOwn
Object.hasOwn(obj, 'prop'); // melhor que obj.hasOwnProperty

// Top-level await (em módulos)
const dados = await fetch('/api');

// Error cause
throw new Error('Erro', { cause: erroOriginal });
```

---

## 10. MÓDULOS

### 10.1 ES Modules

```javascript
// export (arquivo: math.js)
export const PI = 3.14159;
export function soma(a, b) { return a + b; }
export default function multiplicar(a, b) { return a * b; }

// export nomeado separado
const subtrair = (a, b) => a - b;
export { subtrair };

// import
import multiplicar, { PI, soma, subtrair } from './math.js';
import * as Math from './math.js';

// Dynamic import
const math = await import('./math.js');

// Import meta
console.log(import.meta.url); // URL do módulo
```

### 10.2 CommonJS (Node.js)

```javascript
// module.exports
module.exports = {
    PI: 3.14159,
    soma: (a, b) => a + b
};

// exports
exports.subtrair = (a, b) => a - b;

// require
const math = require('./math.js');
const { PI, soma } = require('./math.js');
```

---

## 11. ERROS E DEBUGGING

### 11.1 Tratamento de Erros

```javascript
// try/catch/finally
try {
    // código que pode lançar erro
    throw new Error('Algo errado');
} catch (erro) {
    console.error(erro.message);
    console.error(erro.stack);
} finally {
    console.log('Sempre executa');
}

// Custom Error
class ValidationError extends Error {
    constructor(message, campo) {
        super(message);
        this.name = 'ValidationError';
        this.campo = campo;
    }
}

throw new ValidationError('Campo inválido', 'email');

// Error handling em Promises
Promise.reject(new Error('Erro'))
    .catch(erro => console.error(erro));

// Error handling em async/await
try {
    await operacao();
} catch (erro) {
    console.error(erro);
}
```

### 11.2 Debugging

```javascript
// Console methods
console.log('log');
console.error('error');
console.warn('warn');
console.info('info');
console.debug('debug');
console.table([{ a: 1, b: 2 }]);
console.time('timer');
// código
console.timeEnd('timer');
console.trace('stack trace');
console.assert(1 === 2, 'Erro de assert');

// Debugger
debugger; // pausa execução

// Breakpoints condicionais
// No DevTools: right-click breakpoint -> Edit breakpoint

// Console API
console.dir(element); // exibe propriedades DOM
console.group('Grupo');
console.log('dentro');
console.groupEnd();

// Performance
console.time('loop');
for(let i = 0; i < 1000000; i++) {}
console.timeEnd('loop');
```

---

## 12. WEB APIS

### 12.1 APIs Modernas

```javascript
// Geolocation
navigator.geolocation.getCurrentPosition(
    (position) => {
        console.log(position.coords.latitude);
    },
    (error) => console.error(error),
    { enableHighAccuracy: true }
);

// WebSocket
const ws = new WebSocket('wss://exemplo.com');
ws.onopen = () => ws.send('Olá');
ws.onmessage = (event) => console.log(event.data);
ws.onclose = () => console.log('Desconectado');

// Service Worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js')
        .then(reg => console.log('Registrado'))
        .catch(err => console.error(err));
}

// Web Workers
const worker = new Worker('worker.js');
worker.postMessage({ dados: [1,2,3] });
worker.onmessage = (event) => console.log(event.data);

// BroadcastChannel
const channel = new BroadcastChannel('meu-canal');
channel.postMessage('Olá!');
channel.onmessage = (event) => console.log(event.data);

// Beacon (envio de dados sem bloquear)
navigator.sendBeacon('/log', JSON.stringify(dados));

// Clipboard
await navigator.clipboard.writeText('Texto');
const texto = await navigator.clipboard.readText();

// Fullscreen
await document.documentElement.requestFullscreen();
await document.exitFullscreen();

// Battery
const battery = await navigator.getBattery();
console.log(battery.level, battery.charging);

// Network Information
const connection = navigator.connection;
console.log(connection.effectiveType);

// Vibration
navigator.vibrate(200); // vibra 200ms

// Page Visibility
document.addEventListener('visibilitychange', () => {
    if (document.hidden) console.log('Oculto');
});

// Online/Offline
window.addEventListener('online', () => console.log('Online'));
window.addEventListener('offline', () => console.log('Offline'));

// Performance
const timing = performance.timing;
const navigation = performance.getEntriesByType('navigation')[0];
const paint = performance.getEntriesByType('paint');
```

---

## 📊 TABELA RESUMO JAVASCRIPT

| Categoria | Principais Características |
|-----------|---------------------------|
| **Fundamentos** | let/const, tipos, operadores, estruturas de controle |
| **Funções** | arrow functions, closures, generators, async/await |
| **Objetos** | literais, classes, prototype, destructuring, spread |
| **Arrays** | map, filter, reduce, forEach, find, includes |
| **Promises** | then/catch, async/await, Promise.all, Promise.race |
| **DOM** | querySelector, createElement, addEventListener, classList |
| **Eventos** | click, submit, keydown, preventDefault, stopPropagation |
| **ES6+** | destructuring, spread/rest, optional chaining, nullish coalescing |
| **Módulos** | import/export, dynamic imports, module.exports |
| **APIs** | fetch, localStorage, IndexedDB, WebSocket, Service Worker |

---

## 🎯 RECURSOS ADICIONAIS

- **MDN Web Docs:** https://developer.mozilla.org
- **Can I Use:** https://caniuse.com
- **CSS Tricks:** https://css-tricks.com
- **JavaScript.info:** https://javascript.info
- **W3Schools:** https://www.w3schools.com
- **Flexbox Froggy:** https://flexboxfroggy.com
- **Grid Garden:** https://cssgridgarden.com

---

**Este cheat sheet contém mais de 600 exemplos práticos para HTML, CSS e JavaScript. Salve, compartilhe e use como referência diária!**