Perfeito! Vou criar um **Cheat Sheet MEGA COMPLETO de WordPress** no mesmo estilo detalhado dos anteriores, cobrindo desde os fundamentos até desenvolvimento avançado, com exemplos práticos, códigos, hooks, plugins e muito mais.

---

# 🚀 WORDPRESS - CHEAT SHEET MEGA COMPLETO
## *Guia Definitivo para Dominar o WordPress*

---

## 📚 SUMÁRIO

1. [Fundamentos do WordPress](#1-fundamentos-do-wordpress)
2. [WordPress.com vs WordPress.org](#2-wordpresscom-vs-wordpressorg)
3. [Instalação e Configuração](#3-instalação-e-configuração)
4. [Painel de Controle (Dashboard)](#4-painel-de-controle-dashboard)
5. [Tipos de Conteúdo](#5-tipos-de-conteúdo)
6. [Temas e Design](#6-temas-e-design)
7. [Plugins Essenciais](#7-plugins-essenciais)
8. [Desenvolvimento de Plugins](#8-desenvolvimento-de-plugins)
9. [Desenvolvimento de Temas](#9-desenvolvimento-de-temas)
10. [Hooks: Actions e Filters](#10-hooks-actions-e-filters)
11. [Custom Post Types e Taxonomias](#11-custom-post-types-e-taxonomias)
12. [Advanced Custom Fields (ACF)](#12-advanced-custom-fields-acf)
13. [WP_Query e Loops Personalizados](#13-wp_query-e-loops-personalizados)
14. [API REST do WordPress](#14-api-rest-do-wordpress)
15. [Segurança no WordPress](#15-segurança-no-wordpress)
16. [Otimização de Performance](#16-otimização-de-performance)
17. [SEO no WordPress](#17-seo-no-wordpress)
18. [WooCommerce](#18-woocommerce)
19. [Banco de Dados](#19-banco-de-dados)
20. [WP-CLI (Command Line Interface)](#20-wp-cli-command-line-interface)
21. [Multisite Network](#21-multisite-network)
22. [Gutenberg e Block Editor](#22-gutenberg-e-block-editor)
23. [Manutenção e Backup](#23-manutenção-e-backup)
24. [Recursos e Comunidade](#24-recursos-e-comunidade)

---

## 1. FUNDAMENTOS DO WORDPRESS

### 1.1 O que é WordPress?

```text
WORDPRESS = Sistema de Gerenciamento de Conteúdo (CMS) Open Source

CARACTERÍSTICAS PRINCIPAIS:
├── Gratuito e de código aberto (GPL)
├── Mais de 43% de todos os sites na internet
├── Criado em PHP com MySQL/MariaDB
├── Altamente extensível (plugins e temas)
├── Comunidade global imensa
└── Utilizado por blogs, sites corporativos, e-commerces, portais, etc.

VANTAGENS:
├── Fácil para iniciantes (sem código)
├── Poderoso para desenvolvedores (com código)
├── SEO-friendly por padrão
├── Responsivo (mobile-first)
├── Integrações com tudo (redes sociais, CRMs, etc.)
└── Suporte multilíngue (mais de 60 idiomas)
```

### 1.2 Arquitetura do WordPress

```text
ARQUITETURA DE ARQUIVOS:

wp-content/
├── themes/
│   ├── twentytwentyfour/     (tema padrão)
│   └── meu-tema/             (tema personalizado)
├── plugins/
│   ├── akismet/              (plugin padrão)
│   └── meu-plugin/           (plugin personalizado)
├── uploads/                  (arquivos de mídia)
│   ├── 2024/01/              (organizado por ano/mês)
│   └── 2024/02/
├── languages/                (traduções)
└── upgrade/                  (arquivos temporários de atualização)

ARQUIVOS PRINCIPAIS DO CORE:
├── index.php                 (ponto de entrada principal)
├── wp-config.php             (configurações do site)
├── wp-load.php               (carrega o WordPress)
├── wp-blog-header.php        (carrega o ambiente WordPress)
├── wp-login.php              (página de login)
├── wp-admin/                 (painel administrativo)
├── wp-includes/              (arquivos essenciais do core)
└── xmlrpc.php                (API XML-RPC, muitas vezes desabilitada)
```

### 1.3 Banco de Dados - Principais Tabelas

```sql
-- Tabelas Principais
wp_users                    -- Usuários do site
wp_usermeta                 -- Metadados dos usuários
wp_posts                    -- Todas as postagens (posts, páginas, CPTs)
wp_postmeta                 -- Metadados das postagens
wp_terms                    -- Termos de taxonomias (categorias, tags)
wp_term_taxonomy            -- Relaciona termos com taxonomias
wp_term_relationships       -- Relaciona posts com termos
wp_comments                 -- Comentários
wp_commentmeta              -- Metadados dos comentários
wp_options                  -- Configurações do site
wp_links                    -- Links (blogroll)

-- Prefixo padrão é "wp_", pode ser alterado na instalação
```

---

## 2. WORDPRESS.COM VS WORDPRESS.ORG

### 2.1 Comparação Completa

| Característica | WordPress.com | WordPress.org |
|----------------|---------------|---------------|
| **Custo** | Gratuito (plano básico) + planos pagos | Software gratuito + custo de hospedagem |
| **Hospedagem** | Inclusa | Você contrata |
| **Domínio** | subdominio.wordpress.com (grátis) ou personalizado (pago) | Você compra separadamente |
| **Plugins** | Limitado (apenas planos pagos) | Ilimitado |
| **Temas** | Limitados (mais opções em planos pagos) | Milhares (gratuitos e premium) |
| **Publicidade** | Exibe anúncios (plano gratuito) | Sem anúncios |
| **Monetização** | Restrita (planos pagos necessários) | Livre |
| **SEO** | Recursos básicos | Controle total + plugins SEO |
| **Customização** | Limitada (sem código) | Ilimitada (PHP, CSS, JS) |
| **Comércio** | Apenas planos Business/Commerce | WooCommerce completo |
| **Backup** | Automático | Você gerencia |
| **Suporte** | Suporte oficial | Comunidade + documentação |

### 2.2 Quando Escolher Cada Um

```text
ESCOLHA WORDPRESS.COM SE:
├── Você quer algo rápido e sem complicações
├── Não precisa de plugins customizados
├── Apenas um blog pessoal ou site simples
├── Não quer se preocupar com hospedagem e manutenção
└── Orçamento limitado inicial

ESCOLHA WORDPRESS.ORG SE:
├── Você quer controle total sobre seu site
├── Precisa de plugins específicos (WooCommerce, SEO, etc.)
├── Vai monetizar o site
├── Tem conhecimentos técnicos ou contratará um desenvolvedor
├── Precisa de design personalizado
└── Planeja escalar o site no futuro
```

---

## 3. INSTALAÇÃO E CONFIGURAÇÃO

### 3.1 Requisitos Mínimos

```text
REQUISITOS TÉCNICOS:

PHP: 7.4 ou superior (recomendado 8.0+)
MySQL: 5.7 ou superior / MariaDB 10.3+
HTTPS: Recomendado para segurança
Memória: 128MB mínimo (256MB+ recomendado)

EXTENSÕES PHP NECESSÁRIAS:
├── mysqli
├── json
├── openssl
├── mbstring
├── fileinfo
├── curl
├── zip
├── dom
├── xml
└── imagick ou gd (para manipulação de imagens)
```

### 3.2 Instalação Rápida (Autoinstalador)

```text
PASSO A PASSO (HOSTING COM AUTOINSTALADOR):

1. Acesse o painel de controle do seu hosting (cPanel, DirectAdmin)
2. Localize "Autoinstalladores" ou "Softaculous"
3. Clique em WordPress
4. Preencha:
   ├── Domínio: escolha o domínio para instalação
   ├── Diretório: deixe em branco (raiz) ou digite uma pasta
   ├── Nome do Site: título do seu site
   ├── Descrição do Site: slogan/descrição
   ├── Admin Username: usuário administrador
   ├── Admin Password: senha forte
   ├── Admin Email: email para notificações
5. Clique em "Instalar"
6. Aguarde a conclusão (2-5 minutos)
7. Acesse seu site em: https://seudominio.com
8. Acesse o admin em: https://seudominio.com/wp-admin
```

### 3.3 Instalação Manual

```bash
# 1. Baixar WordPress
wget https://wordpress.org/latest.zip
unzip latest.zip
cd wordpress

# 2. Criar banco de dados MySQL
mysql -u root -p
CREATE DATABASE wordpress_db;
CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'senha_forte';
GRANT ALL PRIVILEGES ON wordpress_db.* TO 'wpuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# 3. Copiar arquivos para o servidor
cp -r * /caminho/do/servidor/

# 4. Configurar wp-config.php
cp wp-config-sample.php wp-config.php
# Editar wp-config.php com credenciais do banco

# 5. Definir permissões (Linux)
chmod 755 wp-content
chmod 644 wp-config.php

# 6. Executar instalação via navegador
# Acessar: https://seudominio.com/wp-admin/install.php
```

### 3.4 wp-config.php - Configurações Essenciais

```php
<?php
// Configurações do banco de dados
define('DB_NAME', 'wordpress_db');
define('DB_USER', 'wpuser');
define('DB_PASSWORD', 'senha_forte');
define('DB_HOST', 'localhost');
define('DB_CHARSET', 'utf8mb4');
define('DB_COLLATE', '');

// Chaves de segurança (gerar em: https://api.wordpress.org/secret-key/1.1/salt/)
define('AUTH_KEY',         'coloque sua chave única aqui');
define('SECURE_AUTH_KEY',  'coloque sua chave única aqui');
define('LOGGED_IN_KEY',    'coloque sua chave única aqui');
define('NONCE_KEY',        'coloque sua chave única aqui');
define('AUTH_SALT',        'coloque sua chave única aqui');
define('SECURE_AUTH_SALT', 'coloque sua chave única aqui');
define('LOGGED_IN_SALT',   'coloque sua chave única aqui');
define('NONCE_SALT',       'coloque sua chave única aqui');

// Prefixo da tabela (segurança)
$table_prefix = 'wp_';

// Debug (ativar apenas em desenvolvimento)
define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);
define('WP_DEBUG_DISPLAY', false);

// Memória
define('WP_MEMORY_LIMIT', '256M');
define('WP_MAX_MEMORY_LIMIT', '512M');

// URLs (para migrações)
define('WP_HOME', 'https://seudominio.com');
define('WP_SITEURL', 'https://seudominio.com');

// Desabilitar edição de temas/plugins no admin
define('DISALLOW_FILE_EDIT', true);

// Desabilitar instalação de temas/plugins
define('DISALLOW_FILE_MODS', true);

// Otimizações
define('WP_POST_REVISIONS', 5);        // Limitar revisões
define('EMPTY_TRASH_DAYS', 30);        // Dias no lixo
define('AUTOSAVE_INTERVAL', 300);      // Autosave a cada 5 minutos

// SSL no admin
define('FORCE_SSL_ADMIN', true);

// Conteúdo do WordPress (mudar diretórios)
define('WP_CONTENT_DIR', dirname(__FILE__) . '/meu-content');
define('WP_CONTENT_URL', 'https://seudominio.com/meu-content');

/* Isto é tudo, pode parar de editar! */
require_once(ABSPATH . 'wp-settings.php');
```

---

## 4. PAINEL DE CONTROLE (DASHBOARD)

### 4.1 Menu Principal - Funcionalidades

```text
DASHBOARD
├── Início: Visão geral do site, atividades recentes
├── Atualizações: Status de atualizações do core, plugins, temas

POSTS
├── Todas as Postagens: Gerenciar posts existentes
├── Adicionar Nova: Criar nova postagem
├── Categorias: Gerenciar categorias de posts
├── Tags: Gerenciar tags de posts

MÍDIA
├── Biblioteca: Gerenciar imagens, vídeos, arquivos
├── Adicionar Nova: Upload de novos arquivos

PÁGINAS
├── Todas as Páginas: Gerenciar páginas estáticas
├── Adicionar Nova: Criar nova página

COMENTÁRIOS
├── Aprovar, responder, marcar como spam

APARÊNCIA
├── Temas: Instalar e ativar temas
├── Personalizar: Customizador ao vivo
├── Editor de Site: Edição full-site (FSE)
├── Widgets: Gerenciar áreas de widget
├── Menus: Criar e editar menus de navegação
└── Fundo: Customizar fundo (depende do tema)

PLUGINS
├── Plugins Instalados: Gerenciar plugins
├── Adicionar Novo: Instalar novos plugins
└── Editor de Plugins: Editar código (se habilitado)

USUÁRIOS
├── Todos os Usuários: Gerenciar usuários
├── Adicionar Novo: Criar novo usuário
└── Seu Perfil: Editar informações pessoais

FERRAMENTAS
├── Ferramentas Disponíveis: Importar, exportar, etc.
├── Importar: Migrar de outras plataformas
├── Exportar: Exportar conteúdo
├── Saúde do Site: Verificar problemas técnicos
└── Exportar Dados Pessoais: GDPR

AJUSTES
├── Gerais: Título, tagline, timezone, idioma
├── Escrita: Configurações de publicação
├── Leitura: Página inicial, feeds, visibilidade
├── Discussão: Configurações de comentários
├── Mídia: Tamanhos de imagem
├── Permalinks: Estrutura de URLs (SEO)
└── Privacidade: Política de privacidade (GDPR)
```

### 4.2 Perfis de Usuário e Capacidades

```text
PERFIS DE USUÁRIO:

SUPER ADMIN (MULTISITE):
├── Gerenciar rede inteira
├── Instalar temas e plugins globalmente
└── Apenas em instalações Multisite

ADMINISTRADOR:
├── Acesso total ao site
├── Instalar/ativar/desativar temas e plugins
├── Criar/editar/excluir usuários
├── Alterar todas as configurações
└── Publicar, editar, excluir qualquer conteúdo

EDITOR:
├── Publicar e gerenciar posts de qualquer usuário
├── Moderar comentários
├── Criar/editar páginas
├── Gerenciar categorias e tags
└── Upload de mídia

AUTOR:
├── Publicar e gerenciar apenas seus próprios posts
├── Upload de mídia
└── Editar seus próprios posts

COLABORADOR:
├── Escrever e editar seus próprios posts (rascunhos)
├── Não pode publicar
├── Não pode fazer upload de mídia
└── Editar apenas seus próprios rascunhos

ASSINANTE:
├── Ler conteúdo
├── Gerenciar seu próprio perfil
└── Acesso apenas ao leitor

CÓDIGO DE CAPACIDADES (PARA DESENVOLVEDORES):
add_role('cliente', 'Cliente', array(
    'read' => true,
    'edit_posts' => false,
    'upload_files' => true,
    'view_woocommerce_reports' => false
));

remove_role('subscriber');
```

---

## 5. TIPOS DE CONTEÚDO

### 5.1 Posts vs Páginas

| Característica | Posts (Post) | Páginas (Page) |
|----------------|--------------|----------------|
| **Uso** | Conteúdo dinâmico (blog, notícias) | Conteúdo estático (sobre, contato) |
| **Organização** | Por data, categorias, tags | Hierárquica (páginas filhas) |
| **Autoria** | Exibe autor e data | Não exibe autor/data |
| **Feed RSS** | Incluído | Excluído |
| **Comentários** | Habilitados por padrão | Desabilitados por padrão |
| **Ordenação** | Cronológica (mais recente primeiro) | Ordem definida pelo usuário |
| **URL** | /ano/mes/dia/titulo/ (padrão) | /nome-da-pagina/ |

### 5.2 Custom Post Types (CPT)

```php
<?php
// Registrar Custom Post Type no functions.php
function criar_cpt_produtos() {
    $labels = array(
        'name'               => 'Produtos',
        'singular_name'      => 'Produto',
        'menu_name'          => 'Produtos',
        'add_new'            => 'Adicionar Novo',
        'add_new_item'       => 'Adicionar Novo Produto',
        'edit_item'          => 'Editar Produto',
        'new_item'           => 'Novo Produto',
        'view_item'          => 'Ver Produto',
        'search_items'       => 'Buscar Produtos',
        'not_found'          => 'Nenhum produto encontrado',
        'not_found_in_trash' => 'Nenhum produto na lixeira',
    );
    
    $args = array(
        'labels'              => $labels,
        'public'              => true,
        'has_archive'         => true,
        'rewrite'             => array('slug' => 'produtos'),
        'supports'            => array('title', 'editor', 'thumbnail', 'excerpt'),
        'menu_icon'           => 'dashicons-cart',
        'show_in_rest'        => true,  // Gutenberg
        'hierarchical'        => false,
        'show_in_menu'        => true,
        'show_in_nav_menus'   => true,
        'can_export'          => true,
    );
    
    register_post_type('produto', $args);
}
add_action('init', 'criar_cpt_produtos');
```

### 5.3 Taxonomias Personalizadas

```php
<?php
// Registrar Taxonomia Personalizada
function criar_taxonomia_categorias_produtos() {
    $labels = array(
        'name'              => 'Categorias de Produtos',
        'singular_name'     => 'Categoria',
        'search_items'      => 'Buscar Categorias',
        'all_items'         => 'Todas Categorias',
        'parent_item'       => 'Categoria Pai',
        'parent_item_colon' => 'Categoria Pai:',
        'edit_item'         => 'Editar Categoria',
        'update_item'       => 'Atualizar Categoria',
        'add_new_item'      => 'Adicionar Nova Categoria',
        'new_item_name'     => 'Nova Categoria',
        'menu_name'         => 'Categorias',
    );
    
    $args = array(
        'labels'            => $labels,
        'public'            => true,
        'hierarchical'      => true,      // Como categorias (hierárquico)
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array('slug' => 'categoria-produto'),
        'show_in_rest'      => true,      // Gutenberg
    );
    
    register_taxonomy('categoria_produto', 'produto', $args);
}
add_action('init', 'criar_taxonomia_categorias_produtos');
```

### 5.4 Post Formats

```php
<?php
// Ativar Post Formats no tema
add_theme_support('post-formats', array(
    'aside', 'gallery', 'link', 'image', 
    'quote', 'status', 'video', 'audio', 'chat'
));

// No template (single.php, content.php)
if (has_post_format('video')) {
    // Exibir conteúdo para vídeo
    echo '<div class="video-format">';
    the_content();
    echo '</div>';
} elseif (has_post_format('quote')) {
    // Exibir formato citação
    echo '<blockquote>';
    the_content();
    echo '</blockquote>';
} else {
    // Formato padrão
    the_content();
}
```

---

## 6. TEMAS E DESIGN

### 6.1 Estrutura de um Tema WordPress

```text
meu-tema/
├── style.css                 (obrigatório - cabeçalho do tema)
├── index.php                 (obrigatório - template principal)
├── functions.php             (funções do tema)
├── header.php                (cabeçalho do site)
├── footer.php                (rodapé do site)
├── sidebar.php               (barra lateral)
├── single.php                (template de post único)
├── page.php                  (template de página)
├── archive.php               (arquivos de posts)
├── category.php              (arquivo de categoria)
├── tag.php                   (arquivo de tag)
├── search.php                (resultados de busca)
├── 404.php                   (página de erro)
├── comments.php              (comentários)
├── front-page.php            (página inicial)
├── home.php                  (blog)
├── taxonomy.php              (taxonomias)
├── author.php                (arquivo de autor)
├── date.php                  (arquivo por data)
├── attachment.php            (anexos)
├── screenshot.png            (thumbnail do tema)
└── assets/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── images/
```

### 6.2 Cabeçalho style.css (Obrigatório)

```css
/*
Theme Name: Meu Tema
Theme URI: https://meusite.com/meu-tema
Author: Seu Nome
Author URI: https://meusite.com
Description: Descrição do tema
Version: 1.0.0
License: GPL v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: meu-tema
Domain Path: /languages
Tags: blog, e-commerce, portfolio, responsive, custom-menu, featured-images

Requires at least: 5.0
Tested up to: 6.4
Requires PHP: 7.4
*/

/* Estilos principais do tema */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
```

### 6.3 functions.php - Funções Essenciais

```php
<?php
/**
 * Funções do Tema Meu Tema
 */

// 1. Configurações de suporte do tema
function meu_tema_setup() {
    // Suporte a tradução
    load_theme_textdomain('meu-tema', get_template_directory() . '/languages');
    
    // Suporte a título dinâmico
    add_theme_support('title-tag');
    
    // Suporte a post thumbnail (imagem destacada)
    add_theme_support('post-thumbnails');
    
    // Suporte a HTML5
    add_theme_support('html5', array(
        'search-form', 'comment-form', 'comment-list', 
        'gallery', 'caption', 'style', 'script'
    ));
    
    // Suporte a custom logo
    add_theme_support('custom-logo', array(
        'height'      => 100,
        'width'       => 400,
        'flex-height' => true,
        'flex-width'  => true,
    ));
    
    // Suporte a menus
    register_nav_menus(array(
        'primary' => __('Menu Principal', 'meu-tema'),
        'footer'  => __('Menu Rodapé', 'meu-tema'),
        'social'  => __('Menu Social', 'meu-tema'),
    ));
    
    // Suporte a widgets
    add_theme_support('widgets');
    
    // Tamanhos de imagem personalizados
    add_image_size('destaque', 1200, 600, true);
    add_image_size('thumb-small', 300, 200, true);
    add_image_size('thumb-medium', 600, 400, true);
}
add_action('after_setup_theme', 'meu_tema_setup');

// 2. Registrar áreas de widget
function meu_tema_widgets_init() {
    register_sidebar(array(
        'name'          => __('Sidebar Principal', 'meu-tema'),
        'id'            => 'sidebar-1',
        'description'   => __('Área de widgets da barra lateral', 'meu-tema'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));
    
    register_sidebar(array(
        'name'          => __('Rodapé', 'meu-tema'),
        'id'            => 'footer-1',
        'description'   => __('Área de widgets do rodapé', 'meu-tema'),
        'before_widget' => '<div class="col-md-3"><div id="%1$s" class="widget %2$s">',
        'after_widget'  => '</div></div>',
        'before_title'  => '<h4 class="widget-title">',
        'after_title'   => '</h4>',
    ));
}
add_action('widgets_init', 'meu_tema_widgets_init');

// 3. Carregar CSS e JS
function meu_tema_scripts() {
    // CSS principal
    wp_enqueue_style('meu-tema-style', get_stylesheet_uri(), array(), '1.0.0');
    
    // CSS adicional
    wp_enqueue_style('meu-tema-main', get_template_directory_uri() . '/assets/css/main.css', array(), '1.0.0');
    
    // JavaScript
    wp_enqueue_script('meu-tema-navigation', get_template_directory_uri() . '/assets/js/navigation.js', array(), '1.0.0', true);
    
    // Para comentários
    if (is_singular() && comments_open() && get_option('thread_comments')) {
        wp_enqueue_script('comment-reply');
    }
}
add_action('wp_enqueue_scripts', 'meu_tema_scripts');

// 4. Configuração do editor de blocos (Gutenberg)
function meu_tema_gutenberg_setup() {
    add_theme_support('align-wide');
    add_theme_support('responsive-embeds');
    add_theme_support('editor-styles');
    add_editor_style('assets/css/editor-style.css');
    
    // Cores personalizadas
    add_theme_support('editor-color-palette', array(
        array(
            'name'  => __('Azul', 'meu-tema'),
            'slug'  => 'azul',
            'color' => '#0073aa',
        ),
        array(
            'name'  => __('Vermelho', 'meu-tema'),
            'slug'  => 'vermelho',
            'color' => '#dc3232',
        ),
    ));
}
add_action('after_setup_theme', 'meu_tema_gutenberg_setup');
```

### 6.4 Template Hierarchy (Ordem de Carregamento)

```text
ORDEM DE PRIORIDADE DOS TEMPLATES:

FRONT PAGE (Página Inicial):
1. front-page.php
2. home.php
3. index.php

SINGLE POST (Post Único):
1. single-{post-type}-{slug}.php
2. single-{post-type}.php
3. single.php
4. singular.php
5. index.php

PAGE (Página Estática):
1. custom-template.php (selecionado no admin)
2. page-{slug}.php
3. page-{id}.php
4. page.php
5. singular.php
6. index.php

ARCHIVE (Arquivos):
1. category-{slug}.php | tag-{slug}.php | taxonomy-{taxonomy}-{term}.php
2. category-{id}.php | tag-{id}.php
3. category.php | tag.php | taxonomy.php
4. archive.php
5. index.php

AUTHOR (Autor):
1. author-{nicename}.php
2. author-{id}.php
3. author.php
4. archive.php
5. index.php

DATE (Data):
1. date.php
2. archive.php
3. index.php

SEARCH (Busca):
1. search.php
2. index.php

404 (Erro):
1. 404.php
2. index.php

ATTACHMENT (Anexos):
1. mime-type.php (ex: image.php, video.php)
2. attachment.php
3. single.php
4. index.php
```

### 6.5 Templates Básicos - Códigos Essenciais

```php
<?php
// header.php
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<header id="masthead" class="site-header">
    <div class="container">
        <div class="site-branding">
            <?php if (has_custom_logo()) : ?>
                <?php the_custom_logo(); ?>
            <?php else : ?>
                <h1 class="site-title">
                    <a href="<?php echo esc_url(home_url('/')); ?>" rel="home">
                        <?php bloginfo('name'); ?>
                    </a>
                </h1>
                <p class="site-description"><?php bloginfo('description'); ?></p>
            <?php endif; ?>
        </div>
        
        <nav id="site-navigation" class="main-navigation">
            <?php
            wp_nav_menu(array(
                'theme_location' => 'primary',
                'menu_id'        => 'primary-menu',
                'container'      => false,
                'fallback_cb'    => false,
            ));
            ?>
        </nav>
    </div>
</header>

<?php
// index.php ou archive.php
get_header(); ?>

<main id="primary" class="site-main">
    <div class="container">
        <?php if (have_posts()) : ?>
            <?php while (have_posts()) : the_post(); ?>
                <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                    <header class="entry-header">
                        <?php the_title('<h2 class="entry-title"><a href="' . esc_url(get_permalink()) . '">', '</a></h2>'); ?>
                        <div class="entry-meta">
                            <span class="posted-on">
                                <?php echo get_the_date(); ?>
                            </span>
                            <span class="byline">
                                <?php _e('por', 'meu-tema'); ?> 
                                <?php the_author_posts_link(); ?>
                            </span>
                        </div>
                    </header>
                    
                    <?php if (has_post_thumbnail()) : ?>
                        <div class="post-thumbnail">
                            <a href="<?php the_permalink(); ?>">
                                <?php the_post_thumbnail('medium'); ?>
                            </a>
                        </div>
                    <?php endif; ?>
                    
                    <div class="entry-content">
                        <?php the_excerpt(); ?>
                        <a href="<?php the_permalink(); ?>" class="read-more">
                            <?php _e('Leia mais', 'meu-tema'); ?>
                        </a>
                    </div>
                    
                    <footer class="entry-footer">
                        <span class="cat-links">
                            <?php _e('Categorias:', 'meu-tema'); ?> 
                            <?php the_category(', '); ?>
                        </span>
                        <span class="tags-links">
                            <?php the_tags(__('Tags:', 'meu-tema'), ', '); ?>
                        </span>
                    </footer>
                </article>
            <?php endwhile; ?>
            
            <?php the_posts_pagination(array(
                'mid_size'  => 2,
                'prev_text' => __('Anterior'),
                'next_text' => __('Próximo'),
            )); ?>
            
        <?php else : ?>
            <p><?php _e('Nenhum post encontrado.', 'meu-tema'); ?></p>
        <?php endif; ?>
    </div>
</main>

<?php get_sidebar(); ?>
<?php get_footer(); ?>

<?php
// footer.php
<footer id="colophon" class="site-footer">
    <div class="container">
        <div class="footer-widgets">
            <?php if (is_active_sidebar('footer-1')) : ?>
                <?php dynamic_sidebar('footer-1'); ?>
            <?php endif; ?>
        </div>
        <div class="site-info">
            <p>&copy; <?php echo date('Y'); ?> <?php bloginfo('name'); ?>.
            <?php _e('Todos os direitos reservados.', 'meu-tema'); ?></p>
        </div>
    </div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
```

---

## 7. PLUGINS ESSENCIAIS

### 7.1 Plugins por Categoria

```text
SEGURANÇA:
├── Wordfence Security: Firewall, scanner de malware, login security
├── Sucuri Security: Monitoramento, hardening, scanner
├── iThemes Security: Proteção de login, banimento, 2FA
├── WPS Hide Login: Personalizar URL de login
└── Really Simple SSL: Configurar SSL automaticamente

BACKUP:
├── UpdraftPlus: Backups automáticos na nuvem (Google Drive, Dropbox)
├── BackupBuddy: Backup completo com restauração
├── Duplicator: Migração e backup
└── All-in-One WP Migration: Migração fácil com exportação

PERFORMANCE:
├── WP Rocket: Cache, minificação, lazy load (premium)
├── W3 Total Cache: Cache completo (gratuito)
├── LiteSpeed Cache: Otimização para servidores LiteSpeed
├── Autoptimize: Minificação de CSS/JS
├── Smush: Otimização de imagens
├── ShortPixel: Compressão avançada de imagens
└── Asset CleanUp: Desabilitar scripts desnecessários

SEO:
├── Yoast SEO: SEO completo (sitemap, meta tags, análise)
├── Rank Math: Alternativa moderna ao Yoast
├── All in One SEO: Pacote completo de SEO
└── SEOPress: SEO avançado

FORMULÁRIOS:
├── Contact Form 7: Formulários simples
├── WPForms: Formulários drag-and-drop
├── Gravity Forms: Formulários avançados com integrações
├── Ninja Forms: Formulários com lógica condicional
└── Elementor Pro: Formulários com builder

E-COMMERCE:
├── WooCommerce: Plataforma de e-commerce completa
├── Easy Digital Downloads: Venda de produtos digitais
└── MemberPress: Assinaturas e membros

CONSTRUTORES DE PÁGINAS:
├── Elementor (Pro): Construtor visual mais popular
├── Beaver Builder: Construtor confiável
├── Divi Builder: Builder do tema Divi
└── WPBakery Page Builder: Construtor clássico

TRADUÇÃO:
├── WPML: Plugin de tradução completo (premium)
├── Polylang: Alternativa gratuita ao WPML
├── Loco Translate: Editar traduções de temas/plugins
└── Weglot: Tradução automática

GESTÃO DE CONTEÚDO:
├── Advanced Custom Fields (ACF): Campos personalizados
├── Custom Post Type UI: Criar CPTs via interface
├── Pods: Framework de conteúdo personalizado
└── Meta Box: Campos personalizados

MÍDIA:
├── Regenerate Thumbnails: Regenerar miniaturas
├── Enable Media Replace: Substituir arquivos sem perder referências
├── Modula: Galerias de imagens responsivas
└── WP Media Folder: Organizar mídia em pastas

SOCIAL:
├── Monarch: Botões de compartilhamento (Elegant Themes)
├── Social Warfare: Botões de compartilhamento otimizados
├── MashShare: Botões de compartilhamento com contagem
└── Revive Old Posts: Compartilhar posts antigos automaticamente

ANALYTICS:
├── MonsterInsights: Integração Google Analytics
├── Site Kit by Google: Ferramentas do Google unificadas
└── Matomo Analytics: Alternativa open source ao GA

MIGRAÇÃO:
├── All-in-One WP Migration: Migração completa
├── Duplicator: Clone e migração
└── WP Migrate DB: Migração de banco de dados

MANTENIMENTO:
├── WP-Optimize: Limpeza de banco de dados
├── Advanced Database Cleaner: Limpeza de transientes e revisões
├── Broken Link Checker: Verificar links quebrados
└── Redirection: Gerenciamento de redirecionamentos 301
```

### 7.2 Instalação de Plugins via Código

```php
<?php
// Ativar/instalar plugin via código
function ativar_plugin_necessario() {
    $plugin = 'elementor/elementor.php';
    
    if (!is_plugin_active($plugin)) {
        // Ativar se já instalado
        activate_plugin($plugin);
    }
}
add_action('admin_init', 'ativar_plugin_necessario');

// Forçar instalação de plugin
function forcar_instalar_plugin() {
    $plugin_slug = 'elementor';
    
    if (!file_exists(WP_PLUGIN_DIR . '/elementor/elementor.php')) {
        include_once ABSPATH . 'wp-admin/includes/plugin-install.php';
        include_once ABSPATH . 'wp-admin/includes/file.php';
        include_once ABSPATH . 'wp-admin/includes/misc.php';
        
        $api = plugins_api('plugin_information', array(
            'slug'   => $plugin_slug,
            'fields' => array('sections' => false)
        ));
        
        $upgrader = new Plugin_Upgrader();
        $upgrader->install($api->download_link);
        activate_plugin($plugin_slug . '/' . $plugin_slug . '.php');
    }
}
```

---

## 8. DESENVOLVIMENTO DE PLUGINS

### 8.1 Estrutura Básica de um Plugin

```php
<?php
/*
Plugin Name: Meu Primeiro Plugin
Plugin URI: https://meusite.com/meu-plugin
Description: Um plugin simples para demonstração
Version: 1.0.0
Author: Seu Nome
Author URI: https://meusite.com
License: GPL v2 or later
Text Domain: meu-plugin
Domain Path: /languages
*/

// Prevenir acesso direto
if (!defined('ABSPATH')) {
    exit;
}

// Definir constantes
define('MPP_VERSION', '1.0.0');
define('MPP_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('MPP_PLUGIN_URL', plugin_dir_url(__FILE__));

// Carregar traduções
function mpp_load_textdomain() {
    load_plugin_textdomain('meu-plugin', false, dirname(plugin_basename(__FILE__)) . '/languages');
}
add_action('plugins_loaded', 'mpp_load_textdomain');

// Ativação do plugin
function mpp_activate() {
    // Criar tabelas personalizadas
    global $wpdb;
    $charset_collate = $wpdb->get_charset_collate();
    
    $table_name = $wpdb->prefix . 'meu_plugin_dados';
    $sql = "CREATE TABLE $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        nome varchar(100) NOT NULL,
        data datetime DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
    ) $charset_collate;";
    
    require_once ABSPATH . 'wp-admin/includes/upgrade.php';
    dbDelta($sql);
    
    // Adicionar opção padrão
    add_option('mpp_opcao_padrao', 'valor_padrao');
}
register_activation_hook(__FILE__, 'mpp_activate');

// Desativação do plugin
function mpp_deactivate() {
    // Limpar agendamentos, etc.
    wp_clear_scheduled_hook('mpp_evento_diario');
}
register_deactivation_hook(__FILE__, 'mpp_deactivate');

// Desinstalação do plugin
function mpp_uninstall() {
    // Remover tabelas e opções
    global $wpdb;
    $table_name = $wpdb->prefix . 'meu_plugin_dados';
    $wpdb->query("DROP TABLE IF EXISTS $table_name");
    delete_option('mpp_opcao_padrao');
}
register_uninstall_hook(__FILE__, 'mpp_uninstall');

// Adicionar menu no admin
function mpp_add_admin_menu() {
    add_menu_page(
        'Meu Plugin',
        'Meu Plugin',
        'manage_options',
        'meu-plugin',
        'mpp_admin_page',
        'dashicons-admin-plugins',
        80
    );
    
    add_submenu_page(
        'meu-plugin',
        'Configurações',
        'Configurações',
        'manage_options',
        'meu-plugin-settings',
        'mpp_settings_page'
    );
}
add_action('admin_menu', 'mpp_add_admin_menu');

// Página principal do admin
function mpp_admin_page() {
    ?>
    <div class="wrap">
        <h1><?php _e('Meu Plugin', 'meu-plugin'); ?></h1>
        <p><?php _e('Bem-vindo ao painel do plugin!', 'meu-plugin'); ?></p>
    </div>
    <?php
}

// Página de configurações
function mpp_settings_page() {
    ?>
    <div class="wrap">
        <h1><?php _e('Configurações', 'meu-plugin'); ?></h1>
        <form method="post" action="options.php">
            <?php
            settings_fields('mpp_settings_group');
            do_settings_sections('meu-plugin-settings');
            submit_button();
            ?>
        </form>
    </div>
    <?php
}

// Registrar configurações
function mpp_register_settings() {
    register_setting('mpp_settings_group', 'mpp_opcao_texto');
    
    add_settings_section(
        'mpp_main_section',
        'Configurações Principais',
        'mpp_section_callback',
        'meu-plugin-settings'
    );
    
    add_settings_field(
        'mpp_opcao_texto',
        'Texto de Exemplo',
        'mpp_text_field_callback',
        'meu-plugin-settings',
        'mpp_main_section'
    );
}
add_action('admin_init', 'mpp_register_settings');

function mpp_section_callback() {
    echo '<p>Configure as opções do plugin abaixo:</p>';
}

function mpp_text_field_callback() {
    $value = get_option('mpp_opcao_texto', '');
    echo '<input type="text" name="mpp_opcao_texto" value="' . esc_attr($value) . '">';
}
```

### 8.2 Adicionar Shortcodes

```php
<?php
// Shortcode básico
function mpp_hello_shortcode($atts) {
    // Atributos padrão
    $atts = shortcode_atts(array(
        'name' => 'Visitante',
        'color' => 'blue',
    ), $atts, 'mpp_hello');
    
    return '<span style="color:' . esc_attr($atts['color']) . ';">Olá, ' . esc_html($atts['name']) . '!</span>';
}
add_shortcode('mpp_hello', 'mpp_hello_shortcode');

// Shortcode com conteúdo
function mpp_box_shortcode($atts, $content = null) {
    $atts = shortcode_atts(array(
        'title' => 'Caixa',
        'class' => '',
    ), $atts, 'mpp_box');
    
    return '<div class="box ' . esc_attr($atts['class']) . '">
                <h3>' . esc_html($atts['title']) . '</h3>
                <div class="box-content">' . do_shortcode($content) . '</div>
            </div>';
}
add_shortcode('mpp_box', 'mpp_box_shortcode');

// Shortcode com saída em buffer
function mpp_complex_shortcode($atts) {
    ob_start();
    ?>
    <div class="complex-shortcode">
        <?php echo esc_html($atts['content']); ?>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode('mpp_complex', 'mpp_complex_shortcode');
```

---

## 9. DESENVOLVIMENTO DE TEMAS

### 9.1 Hierarquia de Arquivos (Detalhada)

```text
TEMPLATES HIERÁRQUICOS - ORDEM COMPLETA:

PÁGINA INICIAL (FRONT PAGE):
front-page.php
home.php (selecionado como "Página estática: Posts")
index.php

PÁGINA ESTÁTICA (PAGE):
{page-template}.php (template personalizado)
page-{slug}.php
page-{id}.php
page.php
singular.php
index.php

POST ÚNICO (SINGLE):
single-{post-type}-{slug}.php
single-{post-type}.php
single.php
singular.php
index.php

POST TYPE ARCHIVE:
archive-{post-type}.php
archive.php
index.php

CATEGORIA:
category-{slug}.php
category-{id}.php
category.php
archive.php
index.php

TAG:
tag-{slug}.php
tag-{id}.php
tag.php
archive.php
index.php

TAXONOMIA:
taxonomy-{taxonomy}-{term}.php
taxonomy-{taxonomy}.php
taxonomy.php
archive.php
index.php

AUTOR:
author-{nicename}.php
author-{id}.php
author.php
archive.php
index.php

DATA:
date.php
archive.php
index.php

BUSCA:
search.php
index.php

404:
404.php
index.php

ANEXOS:
{attachment-mime-type}.php (ex: image.php, video.php)
attachment.php
single.php
index.php

EMBED:
embed.php
index.php
```

### 9.2 Template Tags Essenciais

```php
<?php
// Tags de conteúdo
the_title();                    // Título do post
the_content();                  // Conteúdo do post
the_excerpt();                  // Resumo do post
the_permalink();                // Link permanente
the_ID();                       // ID do post
the_author();                   // Nome do autor
the_author_posts_link();        // Link para posts do autor
the_date();                     // Data do post
the_time('d/m/Y');              // Data formatada
the_category(', ');             // Categorias
the_tags('Tags: ', ', ', '');   // Tags
the_post_thumbnail();           // Imagem destacada
the_post_thumbnail('medium');   // Imagem com tamanho específico
the_meta();                     // Campos personalizados

// Tags de condição
is_home();                      // Página inicial (blog)
is_front_page();                // Página inicial (estática)
is_single();                    // Post único
is_page();                      // Página
is_page('sobre');               // Página específica
is_category();                  // Arquivo de categoria
is_tag();                       // Arquivo de tag
is_archive();                   // Qualquer arquivo
is_search();                    // Página de busca
is_404();                       // Página 404
is_author();                    // Arquivo de autor
is_attachment();                // Anexo
is_singular();                  // Qualquer conteúdo único
is_sticky();                    // Post fixo

// Tags de loops
have_posts();                   // Verifica se há posts
the_post();                     // Configura o próximo post
rewind_posts();                 // Reinicia o loop
wp_reset_postdata();            // Reseta dados do post

// Tags de site
bloginfo('name');               // Nome do site
bloginfo('description');        // Descrição do site
bloginfo('url');                // URL do site
bloginfo('template_url');       // URL do tema
bloginfo('stylesheet_url');     // URL do CSS principal
bloginfo('charset');            // Charset
bloginfo('version');            // Versão do WordPress
wp_title();                     // Título da página

// Tags de usuário
wp_get_current_user();          // Usuário atual
get_current_user_id();          // ID do usuário atual
is_user_logged_in();            // Verifica se está logado

// Tags de navegação
wp_nav_menu(array('theme_location' => 'primary'));  // Menu
get_search_form();              // Formulário de busca
next_post_link();               // Link do próximo post
previous_post_link();           // Link do post anterior
posts_nav_link();               // Navegação de posts

// Tags de comentários
comments_template();            // Template de comentários
comments_open();                // Verifica se comentários estão abertos
have_comments();                // Verifica se há comentários
wp_list_comments();             // Lista comentários
comment_form();                 // Formulário de comentários

// Tags de mídia
wp_get_attachment_url();        // URL do anexo
wp_get_attachment_image();      // Imagem do anexo
the_attachment_link();          // Link do anexo
```

### 9.3 Exemplo de Template Completo (single.php)

```php
<?php
/**
 * Template para post único
 */

get_header(); ?>

<main id="primary" class="site-main">
    <div class="container">
        <?php while (have_posts()) : the_post(); ?>
            
            <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                
                <header class="entry-header">
                    <?php the_title('<h1 class="entry-title">', '</h1>'); ?>
                    
                    <div class="entry-meta">
                        <span class="posted-on">
                            <?php _e('Publicado em', 'meu-tema'); ?> 
                            <a href="<?php the_permalink(); ?>">
                                <time datetime="<?php echo get_the_date('c'); ?>">
                                    <?php echo get_the_date(); ?>
                                </time>
                            </a>
                        </span>
                        
                        <span class="byline">
                            <?php _e('por', 'meu-tema'); ?> 
                            <?php the_author_posts_link(); ?>
                        </span>
                        
                        <span class="cat-links">
                            <?php _e('em', 'meu-tema'); ?> 
                            <?php the_category(', '); ?>
                        </span>
                        
                        <?php if (comments_open()) : ?>
                            <span class="comments-link">
                                <?php comments_popup_link(
                                    __('0 comentários', 'meu-tema'),
                                    __('1 comentário', 'meu-tema'),
                                    __('% comentários', 'meu-tema')
                                ); ?>
                            </span>
                        <?php endif; ?>
                    </div>
                </header>
                
                <?php if (has_post_thumbnail()) : ?>
                    <div class="post-thumbnail">
                        <?php the_post_thumbnail('large'); ?>
                    </div>
                <?php endif; ?>
                
                <div class="entry-content">
                    <?php the_content(); ?>
                    
                    <?php
                    wp_link_pages(array(
                        'before' => '<div class="page-links">' . __('Páginas:', 'meu-tema'),
                        'after'  => '</div>',
                    ));
                    ?>
                </div>
                
                <footer class="entry-footer">
                    <?php if (has_tag()) : ?>
                        <div class="tags-links">
                            <?php the_tags(__('Tags: ', 'meu-tema'), ', '); ?>
                        </div>
                    <?php endif; ?>
                </footer>
                
                <?php
                // Navegação entre posts
                the_post_navigation(array(
                    'prev_text' => '<span class="nav-subtitle">' . __('Post anterior', 'meu-tema') . '</span> <span class="nav-title">%title</span>',
                    'next_text' => '<span class="nav-subtitle">' . __('Próximo post', 'meu-tema') . '</span> <span class="nav-title">%title</span>',
                ));
                ?>
                
                <?php
                // Comentários
                if (comments_open() || get_comments_number()) :
                    comments_template();
                endif;
                ?>
                
            </article>
            
        <?php endwhile; ?>
    </div>
</main>

<?php
get_sidebar();
get_footer();
```

---

## 10. HOOKS: ACTIONS E FILTERS

### 10.1 Actions - Adicionar Código em Pontos Específicos

```php
<?php
// Actions mais comuns

// Adicionar código no head
function mpp_add_google_analytics() {
    ?>
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXX-X"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'UA-XXXXX-X');
    </script>
    <?php
}
add_action('wp_head', 'mpp_add_google_analytics');

// Adicionar código no footer
function mpp_add_custom_script() {
    echo '<script>console.log("Carregado no footer");</script>';
}
add_action('wp_footer', 'mpp_add_custom_script');

// Enviar email quando post for publicado
function mpp_notify_on_publish($ID, $post) {
    if ($post->post_type == 'post' && $post->post_status == 'publish') {
        $to = get_option('admin_email');
        $subject = 'Novo post publicado: ' . $post->post_title;
        $message = 'Um novo post foi publicado no seu site: ' . get_permalink($ID);
        wp_mail($to, $subject, $message);
    }
}
add_action('publish_post', 'mpp_notify_on_publish', 10, 2);

// Registrar usuário após cadastro
function mpp_user_registered($user_id) {
    update_user_meta($user_id, 'user_registered_date', current_time('mysql'));
    update_user_meta($user_id, 'user_registered_ip', $_SERVER['REMOTE_ADDR']);
}
add_action('user_register', 'mpp_user_registered');

// Adicionar coluna no admin de posts
function mpp_add_custom_column($columns) {
    $columns['views'] = 'Visualizações';
    return $columns;
}
add_filter('manage_posts_columns', 'mpp_add_custom_column');

function mpp_display_custom_column($column, $post_id) {
    if ($column == 'views') {
        $views = get_post_meta($post_id, 'post_views', true);
        echo $views ? $views : '0';
    }
}
add_action('manage_posts_custom_column', 'mpp_display_custom_column', 10, 2);

// Modificar conteúdo do post
function mpp_add_signature($content) {
    if (is_single()) {
        $signature = '<div class="post-signature">' . get_option('blog_signature') . '</div>';
        $content .= $signature;
    }
    return $content;
}
add_filter('the_content', 'mpp_add_signature');

// Redirecionar após login
function mpp_custom_login_redirect($redirect_to, $request, $user) {
    if (isset($user->roles) && is_array($user->roles)) {
        if (in_array('subscriber', $user->roles)) {
            return home_url('/minha-conta');
        }
    }
    return $redirect_to;
}
add_filter('login_redirect', 'mpp_custom_login_redirect', 10, 3);

// Modificar excerpt length
function mpp_custom_excerpt_length($length) {
    return 20; // 20 palavras
}
add_filter('excerpt_length', 'mpp_custom_excerpt_length');

// Modificar excerpt more
function mpp_custom_excerpt_more($more) {
    return '... <a href="' . get_permalink() . '">[Leia mais]</a>';
}
add_filter('excerpt_more', 'mpp_custom_excerpt_more');
```

### 10.2 Lista de Actions Importantes

```text
ACTIONS PRINCIPAIS (ORDEM DE EXECUÇÃO):

INICIALIZAÇÃO:
muplugins_loaded      - Plugins must-use carregados
plugins_loaded        - Plugins carregados
sanitize_comment_cookies - Cookies de comentários
setup_theme           - Tema carregado
after_setup_theme     - Tema configurado
init                  - WordPress inicializado
widgets_init          - Widgets registrados

HEADER:
wp_head               - No <head> do site
wp_enqueue_scripts    - Carregar scripts e CSS
wp_print_styles       - Imprimir estilos
wp_print_scripts      - Imprimir scripts

CONTEÚDO:
the_post              - Post carregado
the_content           - Antes do conteúdo ser exibido
wp_footer             - Antes do </body>

PUBLICAÇÃO:
publish_post          - Quando post é publicado
save_post             - Quando post é salvo
wp_insert_post        - Quando post é inserido
delete_post           - Quando post é deletado

USUÁRIOS:
user_register         - Usuário registrado
profile_update        - Perfil atualizado
wp_login              - Usuário logado
wp_logout             - Usuário deslogado

ADMIN:
admin_init            - Admin inicializado
admin_menu            - Menu admin carregado
admin_enqueue_scripts - Scripts no admin
admin_notices         - Notificações no admin
```

### 10.3 Filters - Modificar Dados

```php
<?php
// Filters mais comuns

// Modificar título
function mpp_custom_title($title, $id) {
    if (is_single() && get_post_type($id) == 'post') {
        $title = 'Artigo: ' . $title;
    }
    return $title;
}
add_filter('the_title', 'mpp_custom_title', 10, 2);

// Modificar URL do avatar
function mpp_custom_avatar($avatar, $id_or_email, $size, $default, $alt) {
    $custom_avatar = get_user_meta($id_or_email, 'custom_avatar', true);
    if ($custom_avatar) {
        return '<img src="' . $custom_avatar . '" width="' . $size . '" height="' . $size . '" alt="' . $alt . '">';
    }
    return $avatar;
}
add_filter('get_avatar', 'mpp_custom_avatar', 10, 5);

// Modificar query principal
function mpp_modify_main_query($query) {
    if (!is_admin() && $query->is_main_query() && is_home()) {
        $query->set('posts_per_page', 5);
        $query->set('cat', '-1'); // Excluir categoria ID 1
    }
}
add_action('pre_get_posts', 'mpp_modify_main_query');

// Adicionar atributos ao body_class
function mpp_add_body_class($classes) {
    if (is_single()) {
        $classes[] = 'single-post';
        $classes[] = 'post-id-' . get_the_ID();
    }
    if (is_user_logged_in()) {
        $classes[] = 'logged-in';
    }
    return $classes;
}
add_filter('body_class', 'mpp_add_body_class');

// Modificar URL de permalink
function mpp_custom_permalink($permalink, $post) {
    if ($post->post_type == 'produto') {
        $permalink = home_url('/loja/' . $post->post_name);
    }
    return $permalink;
}
add_filter('post_type_link', 'mpp_custom_permalink', 10, 2);
```

### 10.4 Lista de Filters Importantes

```text
FILTERS PRINCIPAIS:

CONTEÚDO:
the_title             - Título do post
the_content           - Conteúdo do post
the_excerpt           - Resumo do post
the_permalink         - Link permanente
post_thumbnail_html   - HTML da imagem destacada
excerpt_length        - Tamanho do resumo
excerpt_more          - Texto do "Leia mais"

TAGS HTML:
wp_title              - Título da página
body_class            - Classes do body
post_class            - Classes do post
comment_class         - Classes do comentário
nav_menu_css_class    - Classes dos menus

URLs:
home_url              - URL da home
site_url              - URL do site
admin_url             - URL do admin
login_url             - URL do login
logout_url            - URL do logout
the_permalink         - Permalink do post

USUÁRIOS:
get_avatar            - Avatar do usuário
user_contactmethods   - Campos de contato do usuário

GERAL:
wp_mail               - Configuração de email
upload_dir            - Diretório de upload
cron_schedules        - Agendamentos cron
widget_text           - Texto de widget

ADMIN:
admin_footer_text     - Texto no rodapé do admin
update_footer         - Versão no admin
screen_options_show_screen - Opções de tela
```

---

## 11. CUSTOM POST TYPES E TAXONOMIAS

### 11.1 Criar CPT Completo (functions.php)

```php
<?php
// Custom Post Type: Portfólio
function criar_cpt_portfolio() {
    $labels = array(
        'name'               => 'Portfólio',
        'singular_name'      => 'Item',
        'menu_name'          => 'Portfólio',
        'name_admin_bar'     => 'Portfólio',
        'add_new'            => 'Adicionar Novo',
        'add_new_item'       => 'Adicionar Novo Item',
        'edit_item'          => 'Editar Item',
        'new_item'           => 'Novo Item',
        'view_item'          => 'Ver Item',
        'search_items'       => 'Buscar Itens',
        'not_found'          => 'Nenhum item encontrado',
        'not_found_in_trash' => 'Nenhum item na lixeira',
        'parent_item_colon'  => 'Item Pai:',
    );
    
    $args = array(
        'labels'              => $labels,
        'public'              => true,
        'publicly_queryable'  => true,
        'show_ui'             => true,
        'show_in_menu'        => true,
        'query_var'           => true,
        'rewrite'             => array('slug' => 'portfolio'),
        'capability_type'     => 'post',
        'has_archive'         => true,
        'hierarchical'        => false,
        'menu_position'       => 5,
        'menu_icon'           => 'dashicons-format-gallery',
        'supports'            => array('title', 'editor', 'thumbnail', 'excerpt', 'revisions'),
        'show_in_rest'        => true, // Gutenberg
        'rest_base'           => 'portfolio',
    );
    
    register_post_type('portfolio', $args);
}
add_action('init', 'criar_cpt_portfolio', 0);

// Taxonomia para Portfólio: Categorias
function criar_taxonomia_portfolio_categorias() {
    $labels = array(
        'name'              => 'Categorias',
        'singular_name'     => 'Categoria',
        'search_items'      => 'Buscar Categorias',
        'all_items'         => 'Todas Categorias',
        'parent_item'       => 'Categoria Pai',
        'parent_item_colon' => 'Categoria Pai:',
        'edit_item'         => 'Editar Categoria',
        'update_item'       => 'Atualizar Categoria',
        'add_new_item'      => 'Adicionar Nova Categoria',
        'new_item_name'     => 'Nova Categoria',
        'menu_name'         => 'Categorias',
    );
    
    $args = array(
        'labels'            => $labels,
        'hierarchical'      => true,
        'public'            => true,
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array('slug' => 'portfolio-categoria'),
        'show_in_rest'      => true,
    );
    
    register_taxonomy('portfolio_categoria', array('portfolio'), $args);
}
add_action('init', 'criar_taxonomia_portfolio_categorias', 0);
```

### 11.2 Template para Custom Post Type

```php
<?php
// single-portfolio.php
get_header(); ?>

<main id="primary" class="site-main">
    <div class="container">
        <?php while (have_posts()) : the_post(); ?>
            
            <article id="post-<?php the_ID(); ?>" <?php post_class('portfolio-item'); ?>>
                
                <?php if (has_post_thumbnail()) : ?>
                    <div class="portfolio-thumbnail">
                        <?php the_post_thumbnail('large'); ?>
                    </div>
                <?php endif; ?>
                
                <header class="entry-header">
                    <h1 class="entry-title"><?php the_title(); ?></h1>
                    
                    <?php
                    $terms = get_the_terms(get_the_ID(), 'portfolio_categoria');
                    if ($terms && !is_wp_error($terms)) :
                    ?>
                        <div class="portfolio-categories">
                            <?php _e('Categorias:', 'meu-tema'); ?>
                            <?php foreach ($terms as $term) : ?>
                                <a href="<?php echo get_term_link($term); ?>">
                                    <?php echo $term->name; ?>
                                </a>
                            <?php endforeach; ?>
                        </div>
                    <?php endif; ?>
                </header>
                
                <div class="entry-content">
                    <?php the_content(); ?>
                    
                    <?php
                    // Campos personalizados (ACF)
                    $cliente = get_field('cliente');
                    $ano = get_field('ano');
                    $url_projeto = get_field('url_projeto');
                    
                    if ($cliente || $ano || $url_projeto) :
                    ?>
                        <div class="portfolio-meta">
                            <h3><?php _e('Informações do Projeto', 'meu-tema'); ?></h3>
                            <ul>
                                <?php if ($cliente) : ?>
                                    <li><strong>Cliente:</strong> <?php echo $cliente; ?></li>
                                <?php endif; ?>
                                <?php if ($ano) : ?>
                                    <li><strong>Ano:</strong> <?php echo $ano; ?></li>
                                <?php endif; ?>
                                <?php if ($url_projeto) : ?>
                                    <li><strong>URL:</strong> <a href="<?php echo $url_projeto; ?>" target="_blank">Visitar Projeto</a></li>
                                <?php endif; ?>
                            </ul>
                        </div>
                    <?php endif; ?>
                </div>
                
            </article>
            
        <?php endwhile; ?>
    </div>
</main>

<?php
get_footer();
```

---

## 12. ADVANCED CUSTOM FIELDS (ACF)

### 12.1 Instalação e Configuração Básica

```php
<?php
// functions.php - Registrar campos via código

// Grupo de campos para posts
if (function_exists('acf_add_local_field_group')) {
    acf_add_local_field_group(array(
        'key' => 'group_1',
        'title' => 'Informações do Post',
        'fields' => array(
            array(
                'key' => 'field_1',
                'label' => 'Subtítulo',
                'name' => 'subtitulo',
                'type' => 'text',
                'instructions' => 'Digite um subtítulo para o post',
                'required' => 0,
            ),
            array(
                'key' => 'field_2',
                'label' => 'Cor de Destaque',
                'name' => 'cor_destaque',
                'type' => 'color_picker',
                'default_value' => '#0073aa',
            ),
            array(
                'key' => 'field_3',
                'label' => 'Galeria de Imagens',
                'name' => 'galeria',
                'type' => 'gallery',
                'instructions' => 'Selecione imagens para a galeria',
                'return_format' => 'array',
            ),
        ),
        'location' => array(
            array(
                array(
                    'param' => 'post_type',
                    'operator' => '==',
                    'value' => 'post',
                ),
            ),
        ),
        'menu_order' => 0,
        'position' => 'normal',
        'style' => 'default',
        'label_placement' => 'top',
        'instruction_placement' => 'label',
        'hide_on_screen' => '',
        'active' => true,
        'description' => '',
    ));
    
    // Grupo para página inicial
    acf_add_local_field_group(array(
        'key' => 'group_home',
        'title' => 'Configurações da Home',
        'fields' => array(
            array(
                'key' => 'field_home_hero',
                'label' => 'Hero Section',
                'name' => 'hero_section',
                'type' => 'group',
                'sub_fields' => array(
                    array(
                        'key' => 'field_hero_title',
                        'label' => 'Título',
                        'name' => 'titulo',
                        'type' => 'text',
                    ),
                    array(
                        'key' => 'field_hero_subtitle',
                        'label' => 'Subtítulo',
                        'name' => 'subtitulo',
                        'type' => 'textarea',
                    ),
                    array(
                        'key' => 'field_hero_image',
                        'label' => 'Imagem',
                        'name' => 'imagem',
                        'type' => 'image',
                        'return_format' => 'url',
                    ),
                    array(
                        'key' => 'field_hero_button_text',
                        'label' => 'Texto do Botão',
                        'name' => 'botao_texto',
                        'type' => 'text',
                    ),
                    array(
                        'key' => 'field_hero_button_url',
                        'label' => 'URL do Botão',
                        'name' => 'botao_url',
                        'type' => 'url',
                    ),
                ),
            ),
            array(
                'key' => 'field_home_destaques',
                'label' => 'Destaques',
                'name' => 'destaques',
                'type' => 'repeater',
                'sub_fields' => array(
                    array(
                        'key' => 'field_destaque_icon',
                        'label' => 'Ícone',
                        'name' => 'icone',
                        'type' => 'text',
                    ),
                    array(
                        'key' => 'field_destaque_title',
                        'label' => 'Título',
                        'name' => 'titulo',
                        'type' => 'text',
                    ),
                    array(
                        'key' => 'field_destaque_text',
                        'label' => 'Texto',
                        'name' => 'texto',
                        'type' => 'textarea',
                    ),
                ),
                'min' => 3,
                'max' => 6,
            ),
        ),
        'location' => array(
            array(
                array(
                    'param' => 'page_template',
                    'operator' => '==',
                    'value' => 'page-home.php',
                ),
            ),
        ),
    ));
}
```

### 12.2 Exibindo Campos no Tema

```php
<?php
// No template (single.php, page.php, etc.)

// Campo texto simples
$subtitulo = get_field('subtitulo');
if ($subtitulo) {
    echo '<h2 class="post-subtitle">' . esc_html($subtitulo) . '</h2>';
}

// Campo de cor
$cor_destaque = get_field('cor_destaque');
if ($cor_destaque) {
    echo '<style>.post-title { color: ' . esc_attr($cor_destaque) . '; }</style>';
}

// Galeria
$galeria = get_field('galeria');
if ($galeria) {
    echo '<div class="gallery">';
    foreach ($galeria as $imagem) {
        echo '<div class="gallery-item">';
        echo '<img src="' . esc_url($imagem['url']) . '" alt="' . esc_attr($imagem['alt']) . '">';
        if ($imagem['caption']) {
            echo '<p class="gallery-caption">' . esc_html($imagem['caption']) . '</p>';
        }
        echo '</div>';
    }
    echo '</div>';
}

// Grupo de campos (hero section)
$hero = get_field('hero_section');
if ($hero) {
    ?>
    <section class="hero">
        <div class="hero-content">
            <h1><?php echo esc_html($hero['titulo']); ?></h1>
            <p><?php echo esc_html($hero['subtitulo']); ?></p>
            <?php if ($hero['botao_texto'] && $hero['botao_url']) : ?>
                <a href="<?php echo esc_url($hero['botao_url']); ?>" class="hero-button">
                    <?php echo esc_html($hero['botao_texto']); ?>
                </a>
            <?php endif; ?>
        </div>
        <?php if ($hero['imagem']) : ?>
            <div class="hero-image">
                <img src="<?php echo esc_url($hero['imagem']); ?>" alt="Hero Image">
            </div>
        <?php endif; ?>
    </section>
    <?php
}

// Repeater field (destaques)
$destaques = get_field('destaques');
if ($destaques) {
    echo '<div class="destaques-grid">';
    foreach ($destaques as $destaque) {
        echo '<div class="destaque-item">';
        if ($destaque['icone']) {
            echo '<div class="destaque-icon">' . esc_html($destaque['icone']) . '</div>';
        }
        echo '<h3>' . esc_html($destaque['titulo']) . '</h3>';
        echo '<p>' . esc_html($destaque['texto']) . '</p>';
        echo '</div>';
    }
    echo '</div>';
}
```

---

## 13. WP_QUERY E LOOPS PERSONALIZADOS

### 13.1 WP_Query Básico

```php
<?php
// Query simples
$args = array(
    'post_type'      => 'post',
    'posts_per_page' => 5,
    'orderby'        => 'date',
    'order'          => 'DESC',
    'category_name'  => 'noticias',
);

$query = new WP_Query($args);

if ($query->have_posts()) :
    while ($query->have_posts()) : $query->the_post();
        // Exibir conteúdo
        the_title();
        the_excerpt();
    endwhile;
    wp_reset_postdata();
endif;
```

### 13.2 Parâmetros Avançados do WP_Query

```php
<?php
// Todos os parâmetros
$args = array(
    // POST TYPES
    'post_type' => array('post', 'page', 'produto'),
    'post_status' => 'publish',
    'post_parent' => 0,  // Páginas sem pai
    
    // TAXONOMIAS
    'tax_query' => array(
        'relation' => 'AND',
        array(
            'taxonomy' => 'category',
            'field'    => 'slug',
            'terms'    => array('noticias', 'destaques'),
            'operator' => 'IN',
        ),
        array(
            'taxonomy' => 'post_tag',
            'field'    => 'id',
            'terms'    => array(5, 10),
            'operator' => 'NOT IN',
        ),
    ),
    
    // META QUERY (Campos personalizados)
    'meta_query' => array(
        'relation' => 'OR',
        array(
            'key'     => 'destaque',
            'value'   => 'sim',
            'compare' => '=',
        ),
        array(
            'key'     => 'visualizacoes',
            'value'   => 100,
            'type'    => 'NUMERIC',
            'compare' => '>',
        ),
    ),
    
    // ORDENAÇÃO
    'orderby' => array(
        'meta_value_num' => 'DESC',
        'date' => 'ASC',
    ),
    'meta_key' => 'visualizacoes',  // Para ordenar por meta field
    
    // PAGINAÇÃO
    'posts_per_page' => 10,
    'paged' => get_query_var('paged') ? get_query_var('paged') : 1,
    'offset' => 0,
    
    // DATAS
    'date_query' => array(
        array(
            'after'     => '2024-01-01',
            'before'    => '2024-12-31',
            'inclusive' => true,
        ),
    ),
    
    // AUTOR
    'author' => 1,  // ID do autor
    'author_name' => 'joao',
    
    // BUSCA
    's' => 'palavra-chave',
    
    // EXCLUSÃO
    'post__not_in' => array(10, 20, 30),
    'post__in' => array(1, 2, 3),
    
    // PERFORMANCE
    'no_found_rows' => false,  // True para não contar total
    'update_post_meta_cache' => true,
    'update_post_term_cache' => true,
);

$query = new WP_Query($args);
```

### 13.3 Loop Personalizado com Paginação

```php
<?php
// Template de arquivo com paginação
$paged = (get_query_var('paged')) ? get_query_var('paged') : 1;

$args = array(
    'post_type'      => 'portfolio',
    'posts_per_page' => 12,
    'paged'          => $paged,
    'orderby'        => 'menu_order',
    'order'          => 'ASC',
);

$portfolio_query = new WP_Query($args);

if ($portfolio_query->have_posts()) : ?>
    <div class="portfolio-grid">
        <?php while ($portfolio_query->have_posts()) : $portfolio_query->the_post(); ?>
            <div class="portfolio-item">
                <?php if (has_post_thumbnail()) : ?>
                    <a href="<?php the_permalink(); ?>">
                        <?php the_post_thumbnail('medium'); ?>
                    </a>
                <?php endif; ?>
                <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
            </div>
        <?php endwhile; ?>
    </div>
    
    <?php
    // Paginação
    $big = 999999999;
    $pagination = paginate_links(array(
        'base'      => str_replace($big, '%#%', esc_url(get_pagenum_link($big))),
        'format'    => '?paged=%#%',
        'current'   => max(1, $paged),
        'total'     => $portfolio_query->max_num_pages,
        'prev_text' => '« Anterior',
        'next_text' => 'Próximo »',
        'type'      => 'list',
    ));
    
    if ($pagination) {
        echo '<nav class="pagination">' . $pagination . '</nav>';
    }
    ?>
    
<?php else : ?>
    <p><?php _e('Nenhum item encontrado.', 'meu-tema'); ?></p>
<?php endif;

wp_reset_postdata();
```

---

## 14. API REST DO WORDPRESS

### 14.1 Endpoints Nativos

```text
ENDPOINTS NATIVOS:

POSTS:
GET    /wp-json/wp/v2/posts
GET    /wp-json/wp/v2/posts/{id}
POST   /wp-json/wp/v2/posts
PUT    /wp-json/wp/v2/posts/{id}
DELETE /wp-json/wp/v2/posts/{id}

PÁGINAS:
GET    /wp-json/wp/v2/pages
GET    /wp-json/wp/v2/pages/{id}

CATEGORIAS:
GET    /wp-json/wp/v2/categories
GET    /wp-json/wp/v2/categories/{id}

TAGS:
GET    /wp-json/wp/v2/tags
GET    /wp-json/wp/v2/tags/{id}

USUÁRIOS:
GET    /wp-json/wp/v2/users
GET    /wp-json/wp/v2/users/{id}

COMENTÁRIOS:
GET    /wp-json/wp/v2/comments
GET    /wp-json/wp/v2/comments/{id}

MÍDIA:
GET    /wp-json/wp/v2/media
GET    /wp-json/wp/v2/media/{id}

TAXONOMIAS:
GET    /wp-json/wp/v2/taxonomies
GET    /wp-json/wp/v2/taxonomies/{taxonomy}

CUSTOM POST TYPES:
GET    /wp-json/wp/v2/{post_type}
GET    /wp-json/wp/v2/{post_type}/{id}
```

### 14.2 Criar Endpoints Personalizados

```php
<?php
// Registrar rota personalizada
add_action('rest_api_init', function () {
    register_rest_route('meu-plugin/v1', '/posts-populares/', array(
        'methods' => 'GET',
        'callback' => 'mpp_get_popular_posts',
        'permission_callback' => '__return_true',
        'args' => array(
            'limit' => array(
                'validate_callback' => function($param, $request, $key) {
                    return is_numeric($param) && $param <= 50;
                },
                'default' => 10,
            ),
        ),
    ));
    
    register_rest_route('meu-plugin/v1', '/contato/', array(
        'methods' => 'POST',
        'callback' => 'mpp_send_contact',
        'permission_callback' => '__return_true',
        'args' => array(
            'nome' => array(
                'required' => true,
                'validate_callback' => function($param, $request, $key) {
                    return !empty($param);
                },
            ),
            'email' => array(
                'required' => true,
                'validate_callback' => function($param, $request, $key) {
                    return is_email($param);
                },
            ),
            'mensagem' => array(
                'required' => true,
            ),
        ),
    ));
});

function mpp_get_popular_posts($request) {
    $limit = $request->get_param('limit') ?: 10;
    
    $args = array(
        'post_type'      => 'post',
        'posts_per_page' => $limit,
        'meta_key'       => 'post_views',
        'orderby'        => 'meta_value_num',
        'order'          => 'DESC',
    );
    
    $query = new WP_Query($args);
    $posts = array();
    
    foreach ($query->posts as $post) {
        $posts[] = array(
            'id' => $post->ID,
            'title' => $post->post_title,
            'link' => get_permalink($post),
            'views' => get_post_meta($post->ID, 'post_views', true),
            'date' => get_the_date('c', $post),
        );
    }
    
    $response = new WP_REST_Response($posts);
    $response->set_status(200);
    
    return $response;
}

function mpp_send_contact($request) {
    $nome = sanitize_text_field($request->get_param('nome'));
    $email = sanitize_email($request->get_param('email'));
    $mensagem = sanitize_textarea_field($request->get_param('mensagem'));
    
    $to = get_option('admin_email');
    $subject = "Contato via site: $nome";
    $body = "Nome: $nome\nEmail: $email\n\nMensagem:\n$mensagem";
    $headers = array("Reply-To: $email");
    
    $sent = wp_mail($to, $subject, $body, $headers);
    
    if ($sent) {
        return new WP_REST_Response(array(
            'success' => true,
            'message' => 'Mensagem enviada com sucesso!'
        ), 200);
    } else {
        return new WP_REST_Response(array(
            'success' => false,
            'message' => 'Erro ao enviar mensagem.'
        ), 500);
    }
}
```

### 14.3 Autenticação na API REST

```php
<?php
// Autenticação por Application Password (WordPress 5.6+)
// Gerar senha de aplicação em: /wp-admin/users.php?page=application-passwords

// Autenticação JWT (com plugin JWT Authentication for WP-API)
// Instalar e configurar

// Exemplo de consumo da API com autenticação
function mpp_api_consume() {
    $url = 'https://seusite.com/wp-json/wp/v2/posts';
    $response = wp_remote_get($url, array(
        'headers' => array(
            'Authorization' => 'Bearer ' . get_option('mpp_api_token'),
        ),
        'timeout' => 30,
    ));
    
    if (is_wp_error($response)) {
        return false;
    }
    
    return json_decode(wp_remote_retrieve_body($response), true);
}
```

---

## 15. SEGURANÇA NO WORDPRESS

### 15.1 Medidas Essenciais de Segurança

```php
<?php
// wp-config.php - Hardening

// Desabilitar edição de arquivos
define('DISALLOW_FILE_EDIT', true);

// Desabilitar instalação de plugins/temas
define('DISALLOW_FILE_MODS', true);

// Chaves de segurança únicas
define('AUTH_KEY',         'gerar no https://api.wordpress.org/secret-key/1.1/salt/');
define('SECURE_AUTH_KEY',  '...');
define('LOGGED_IN_KEY',    '...');
define('NONCE_KEY',        '...');
define('AUTH_SALT',        '...');
define('SECURE_AUTH_SALT', '...');
define('LOGGED_IN_SALT',   '...');
define('NONCE_SALT',       '...');

// Forçar SSL no admin
define('FORCE_SSL_ADMIN', true);

// Prevenir acesso a wp-config.php via navegador
# .htaccess
<files wp-config.php>
    order allow,deny
    deny from all
</files>

// Proteger wp-admin com senha extra (.htaccess)
<FilesMatch "wp-login.php">
    AuthName "Admin Access"
    AuthType Basic
    AuthUserFile /path/to/.htpasswd
    Require valid-user
</FilesMatch>

// Desabilitar XML-RPC (se não for usado)
add_filter('xmlrpc_enabled', '__return_false');

// Remover versão do WordPress do header
remove_action('wp_head', 'wp_generator');

// Desabilitar REST API para não logados (se necessário)
add_filter('rest_authentication_errors', function($result) {
    if (!is_user_logged_in()) {
        return new WP_Error('rest_forbidden', 'Acesso negado.', array('status' => 401));
    }
    return $result;
});

// Limitar tentativas de login
// Plugin: Limit Login Attempts Reloaded

// Forçar senhas fortes
add_action('user_profile_update_errors', 'mpp_force_strong_password', 0, 3);
function mpp_force_strong_password($errors, $update, $user) {
    if (isset($user->user_pass) && !preg_match('/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$/', $user->user_pass)) {
        $errors->add('pass', 'A senha deve ter no mínimo 8 caracteres, incluindo maiúscula, minúscula e número.');
    }
}

// Desabilitar execução de PHP em diretórios de upload
# .htaccess dentro de /wp-content/uploads/
<Files *.php>
    deny from all
</Files>

// Mudar prefixo do banco de dados
$table_prefix = 'wp_'; // Alterar na instalação

// Desabilitar enumerar usuários via API
add_filter('rest_endpoints', function($endpoints) {
    if (isset($endpoints['/wp/v2/users'])) {
        unset($endpoints['/wp/v2/users']);
    }
    return $endpoints;
});

// Remover erros de login que revelam usuário
add_filter('login_errors', function($error) {
    return 'Credenciais inválidas.';
});
```

### 15.2 Monitoramento e Backups

```php
<?php
// functions.php - Monitoramento de segurança

// Log de tentativas de login falhas
function mpp_log_failed_login($username) {
    $log = get_option('mpp_failed_logins', array());
    $log[] = array(
        'username' => $username,
        'ip' => $_SERVER['REMOTE_ADDR'],
        'time' => current_time('mysql'),
    );
    // Manter apenas últimos 100 registros
    $log = array_slice($log, -100);
    update_option('mpp_failed_logins', $log);
}
add_action('wp_login_failed', 'mpp_log_failed_login');

// Alertar admin após múltiplas falhas
function mpp_check_failed_logins() {
    $log = get_option('mpp_failed_logins', array());
    $recent = array_slice($log, -5);
    $ip_count = array_count_values(array_column($recent, 'ip'));
    
    foreach ($ip_count as $ip => $count) {
        if ($count >= 5) {
            $to = get_option('admin_email');
            $subject = 'Alerta de Segurança: Múltiplas tentativas de login';
            $message = "Houve $count tentativas de login falhas do IP: $ip";
            wp_mail($to, $subject, $message);
        }
    }
}
add_action('wp_login', 'mpp_check_failed_logins');

// Backup automático do banco de dados (simplificado)
function mpp_auto_backup() {
    global $wpdb;
    $backup_dir = WP_CONTENT_DIR . '/backups/';
    
    if (!file_exists($backup_dir)) {
        wp_mkdir_p($backup_dir);
    }
    
    $filename = $backup_dir . 'backup-' . date('Y-m-d-H-i-s') . '.sql';
    $tables = $wpdb->get_results('SHOW TABLES', ARRAY_N);
    
    $output = '';
    foreach ($tables as $table) {
        $table_name = $table[0];
        $output .= "DROP TABLE IF EXISTS $table_name;\n";
        $create = $wpdb->get_row("SHOW CREATE TABLE $table_name", ARRAY_N);
        $output .= $create[1] . ";\n\n";
        
        $rows = $wpdb->get_results("SELECT * FROM $table_name", ARRAY_A);
        foreach ($rows as $row) {
            $values = array_map(function($value) use ($wpdb) {
                return $wpdb->prepare('%s', $value);
            }, array_values($row));
            $output .= "INSERT INTO $table_name VALUES (" . implode(',', $values) . ");\n";
        }
        $output .= "\n";
    }
    
    file_put_contents($filename, $output);
    
    // Manter apenas últimos 7 backups
    $backups = glob($backup_dir . 'backup-*.sql');
    usort($backups, function($a, $b) {
        return filemtime($b) - filemtime($a);
    });
    foreach (array_slice($backups, 7) as $old_backup) {
        unlink($old_backup);
    }
}
// Agendar backup diário
if (!wp_next_scheduled('mpp_daily_backup')) {
    wp_schedule_event(time(), 'daily', 'mpp_daily_backup');
}
add_action('mpp_daily_backup', 'mpp_auto_backup');
```

---

## 16. OTIMIZAÇÃO DE PERFORMANCE

### 16.1 Técnicas de Otimização

```php
<?php
// functions.php - Otimizações de performance

// 1. Remover query strings de assets estáticos
function mpp_remove_query_strings() {
    if (!is_admin()) {
        add_filter('script_loader_src', 'mpp_remove_query_strings_split', 15);
        add_filter('style_loader_src', 'mpp_remove_query_strings_split', 15);
    }
}
function mpp_remove_query_strings_split($src) {
    $output = preg_split("/(&ver|\?ver)/", $src);
    return $output[0];
}
add_action('init', 'mpp_remove_query_strings');

// 2. Desabilitar emojis
remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('wp_print_styles', 'print_emoji_styles');
remove_action('admin_print_scripts', 'print_emoji_detection_script');
remove_action('admin_print_styles', 'print_emoji_styles');

// 3. Desabilitar oEmbed
remove_action('wp_head', 'wp_oembed_add_discovery_links');
remove_action('wp_head', 'wp_oembed_add_host_js');

// 4. Desabilitar WP REST API links no header
remove_action('wp_head', 'rest_output_link_wp_head');
remove_action('wp_head', 'wp_resource_hints', 2);

// 5. Desabilitar WPML CSS
define('ICL_DONT_LOAD_LANGUAGE_SELECTOR_CSS', true);
define('ICL_DONT_LOAD_NAVIGATION_CSS', true);
define('ICL_DONT_LOAD_CONTENT_CSS', true);

// 6. Lazy load nativo (WordPress 5.5+)
add_filter('wp_lazy_loading_enabled', '__return_true');

// 7. Carregar scripts apenas onde necessário
function mpp_conditional_scripts() {
    if (!is_page('contato')) {
        wp_dequeue_script('contact-form-7');
        wp_dequeue_style('contact-form-7');
    }
}
add_action('wp_enqueue_scripts', 'mpp_conditional_scripts', 100);

// 8. Otimizar imagens via código
function mpp_optimize_uploaded_image($file) {
    $image = wp_get_image_editor($file['file']);
    if (!is_wp_error($image)) {
        $image->set_quality(85);
        $image->save($file['file']);
    }
    return $file;
}
add_filter('wp_handle_upload', 'mpp_optimize_uploaded_image');

// 9. Remover scripts desnecessários do WooCommerce
add_action('wp_enqueue_scripts', 'mpp_dequeue_woo_scripts', 99);
function mpp_dequeue_woo_scripts() {
    if (!is_woocommerce()) {
        wp_dequeue_script('wc-cart-fragments');
        wp_dequeue_style('woocommerce-general');
        wp_dequeue_style('woocommerce-layout');
        wp_dequeue_style('woocommerce-smallscreen');
    }
}

// 10. Adicionar cache para consultas
function mpp_cached_query($args, $cache_key, $expiration = 3600) {
    $cached = get_transient($cache_key);
    
    if (false === $cached) {
        $query = new WP_Query($args);
        $cached = $query->posts;
        set_transient($cache_key, $cached, $expiration);
    }
    
    return $cached;
}

// 11. Otimizar consultas principais
add_action('pre_get_posts', 'mpp_optimize_main_query');
function mpp_optimize_main_query($query) {
    if ($query->is_main_query() && !is_admin()) {
        // Limitar número de posts no archive
        if (is_archive()) {
            $query->set('posts_per_page', 12);
        }
        
        // Não carregar meta data se não for necessário
        if (is_home()) {
            $query->set('update_post_meta_cache', false);
            $query->set('update_post_term_cache', false);
        }
    }
}
```

### 16.2 Configurações de Cache (wp-config.php)

```php
<?php
// wp-config.php - Configurações de cache

// Definir constante para cache de transientes
define('WP_CACHE', true);  // Para plugins de cache como WP Rocket

// Configurar Redis (se disponível)
define('WP_REDIS_HOST', '127.0.0.1');
define('WP_REDIS_PORT', 6379);
define('WP_REDIS_DATABASE', 0);
define('WP_REDIS_TIMEOUT', 1);
define('WP_REDIS_READ_TIMEOUT', 1);

// Configurar Object Cache
define('WP_REDIS_SELECTIVE_FLUSH', true);

// Desabilitar revisões
define('WP_POST_REVISIONS', false);  // ou número limitado

// Desabilitar lixeira automática
define('EMPTY_TRASH_DAYS', 0);

// Aumentar memória para processamento
define('WP_MEMORY_LIMIT', '256M');
define('WP_MAX_MEMORY_LIMIT', '512M');
```

### 16.3 .htaccess para Performance

```apache
# .htaccess - Configurações de cache de navegador
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/gif "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType text/javascript "access plus 1 month"
    ExpiresByType application/pdf "access plus 1 month"
    ExpiresByType image/x-icon "access plus 1 year"
    ExpiresDefault "access plus 2 days"
</IfModule>

# Compressão Gzip
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/json
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>

# Headers de cache
<IfModule mod_headers.c>
    <FilesMatch "\.(ico|pdf|flv|jpg|jpeg|png|gif|js|css|swf)$">
        Header set Cache-Control "max-age=2592000, public"
    </FilesMatch>
    <FilesMatch "\.(html|htm|xml|txt)$">
        Header set Cache-Control "max-age=7200, public"
    </FilesMatch>
</IfModule>
```

---

## 17. SEO NO WORDPRESS

### 17.1 Otimização On-Page

```php
<?php
// functions.php - SEO otimizations

// Adicionar meta description automática
function mpp_add_meta_description() {
    if (is_single() || is_page()) {
        $excerpt = get_the_excerpt();
        if ($excerpt) {
            echo '<meta name="description" content="' . esc_attr(substr($excerpt, 0, 160)) . '">' . "\n";
        }
    } elseif (is_home() || is_front_page()) {
        $description = get_bloginfo('description');
        if ($description) {
            echo '<meta name="description" content="' . esc_attr($description) . '">' . "\n";
        }
    } elseif (is_category()) {
        $description = category_description();
        if ($description) {
            echo '<meta name="description" content="' . esc_attr(substr($description, 0, 160)) . '">' . "\n";
        }
    }
}
add_action('wp_head', 'mpp_add_meta_description', 1);

// Adicionar meta robots
function mpp_add_meta_robots() {
    if (is_search() || is_404() || is_author() || is_date()) {
        echo '<meta name="robots" content="noindex, follow">' . "\n";
    } else {
        echo '<meta name="robots" content="index, follow">' . "\n";
    }
}
add_action('wp_head', 'mpp_add_meta_robots');

// Adicionar canonical URL
function mpp_add_canonical_url() {
    if (is_single() || is_page()) {
        echo '<link rel="canonical" href="' . get_permalink() . '">' . "\n";
    } elseif (is_home()) {
        echo '<link rel="canonical" href="' . home_url() . '">' . "\n";
    } elseif (is_category() || is_tag()) {
        echo '<link rel="canonical" href="' . get_term_link(get_queried_object()) . '">' . "\n";
    }
}
add_action('wp_head', 'mpp_add_canonical_url');

// Adicionar schema.org para posts
function mpp_add_schema_org() {
    if (is_single()) {
        $author = get_the_author();
        $date = get_the_date('c');
        $modified = get_the_modified_date('c');
        ?>
        <script type="application/ld+json">
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": "<?php the_title_attribute(); ?>",
            "description": "<?php echo esc_js(get_the_excerpt()); ?>",
            "author": {
                "@type": "Person",
                "name": "<?php echo esc_js($author); ?>"
            },
            "datePublished": "<?php echo $date; ?>",
            "dateModified": "<?php echo $modified; ?>",
            "mainEntityOfPage": "<?php the_permalink(); ?>"
        }
        </script>
        <?php
    }
}
add_action('wp_head', 'mpp_add_schema_org');
```

### 17.2 Estrutura de URLs (Permalinks)

```php
<?php
// Configurar estrutura de permalinks via código
function mpp_custom_permalinks() {
    global $wp_rewrite;
    
    // Estrutura de posts
    $wp_rewrite->set_permalink_structure('/%postname%/');
    
    // Estrutura de categorias
    $wp_rewrite->set_category_base('categoria');
    
    // Estrutura de tags
    $wp_rewrite->set_tag_base('tag');
    
    // Estrutura de CPT
    add_rewrite_rule('^portfolio/([^/]+)/?$', 'index.php?portfolio=$matches[1]', 'top');
}
add_action('init', 'mpp_custom_permalinks');

// Adicionar trailing slash
function mpp_add_trailing_slash($url) {
    if (is_admin()) {
        return $url;
    }
    if (strpos($url, '?') !== false) {
        $url_parts = explode('?', $url);
        $url = trailingslashit($url_parts[0]) . '?' . $url_parts[1];
    } else {
        $url = trailingslashit($url);
    }
    return $url;
}
add_filter('user_trailingslashit', 'mpp_add_trailing_slash');

// Redirecionar URLs antigas para novas
function mpp_redirect_old_permalinks() {
    if (is_404()) {
        $request_uri = $_SERVER['REQUEST_URI'];
        $new_url = str_replace('/blog/', '/', $request_uri);
        if ($new_url != $request_uri) {
            wp_redirect(home_url($new_url), 301);
            exit;
        }
    }
}
add_action('template_redirect', 'mpp_redirect_old_permalinks');
```

---

## 18. WOOCOMMERCE

### 18.1 Configurações Essenciais

```php
<?php
// functions.php - Personalizações WooCommerce

// Ativar suporte a miniaturas de produtos
add_theme_support('woocommerce');
add_theme_support('wc-product-gallery-zoom');
add_theme_support('wc-product-gallery-lightbox');
add_theme_support('wc-product-gallery-slider');

// Remover CSS padrão do WooCommerce
add_filter('woocommerce_enqueue_styles', '__return_false');

// Adicionar CSS personalizado
function mpp_woo_custom_css() {
    wp_enqueue_style('mpp-woo', get_template_directory_uri() . '/assets/css/woocommerce.css', array(), '1.0.0');
}
add_action('wp_enqueue_scripts', 'mpp_woo_custom_css');

// Número de produtos por página
add_filter('loop_shop_per_page', function($cols) {
    return 12;
}, 20);

// Colunas de produtos
add_filter('loop_shop_columns', function($columns) {
    return 4;
});

// Modificar texto do botão "Adicionar ao carrinho"
add_filter('woocommerce_product_single_add_to_cart_text', function($text) {
    return __('Comprar Agora', 'meu-tema');
});

// Modificar texto do botão na loja
add_filter('woocommerce_product_add_to_cart_text', function($text, $product) {
    if ($product->is_type('simple')) {
        return __('Comprar', 'meu-tema');
    }
    return $text;
}, 10, 2);

// Adicionar campos personalizados no checkout
add_filter('woocommerce_checkout_fields', function($fields) {
    $fields['billing']['billing_phone']['required'] = true;
    $fields['billing']['billing_cpf'] = array(
        'label' => __('CPF', 'meu-tema'),
        'placeholder' => __('000.000.000-00', 'meu-tema'),
        'required' => true,
        'class' => array('form-row-wide'),
        'priority' => 25,
    );
    return $fields;
});

// Validar campo CPF
add_action('woocommerce_checkout_process', function() {
    if (empty($_POST['billing_cpf'])) {
        wc_add_notice(__('Por favor, informe seu CPF.'), 'error');
    }
});

// Salvar campo CPF no pedido
add_action('woocommerce_checkout_update_order_meta', function($order_id, $data) {
    if (!empty($_POST['billing_cpf'])) {
        update_post_meta($order_id, '_billing_cpf', sanitize_text_field($_POST['billing_cpf']));
    }
}, 10, 2);

// Exibir CPF no admin do pedido
add_action('woocommerce_admin_order_data_after_billing_address', function($order) {
    $cpf = get_post_meta($order->get_id(), '_billing_cpf', true);
    if ($cpf) {
        echo '<p><strong>CPF:</strong> ' . esc_html($cpf) . '</p>';
    }
});
```

### 18.2 Campos Personalizados de Produto

```php
<?php
// functions.php - Campos personalizados para produtos

// Adicionar campo de SKU personalizado
add_action('woocommerce_product_options_general_product_data', function() {
    global $post;
    
    woocommerce_wp_text_input(array(
        'id' => '_custom_sku',
        'label' => __('SKU Personalizado', 'meu-tema'),
        'description' => __('Código interno do produto', 'meu-tema'),
        'desc_tip' => true,
    ));
});

// Salvar campo personalizado
add_action('woocommerce_process_product_meta', function($post_id) {
    if (isset($_POST['_custom_sku'])) {
        update_post_meta($post_id, '_custom_sku', sanitize_text_field($_POST['_custom_sku']));
    }
});

// Adicionar campo de tempo de entrega
add_action('woocommerce_product_options_general_product_data', function() {
    woocommerce_wp_text_input(array(
        'id' => '_delivery_time',
        'label' => __('Tempo de Entrega', 'meu-tema'),
        'placeholder' => __('Ex: 5 dias úteis', 'meu-tema'),
        'description' => __('Tempo estimado de entrega', 'meu-tema'),
    ));
});

// Exibir tempo de entrega no front-end
add_action('woocommerce_single_product_summary', function() {
    global $product;
    $delivery_time = get_post_meta($product->get_id(), '_delivery_time', true);
    if ($delivery_time) {
        echo '<div class="delivery-time"><strong>Entrega:</strong> ' . esc_html($delivery_time) . '</div>';
    }
}, 25);
```

### 18.3 Cálculos e Descontos

```php
<?php
// functions.php - Regras de desconto

// Desconto por quantidade
add_action('woocommerce_before_calculate_totals', function($cart) {
    if (is_admin() && !defined('DOING_AJAX')) return;
    
    foreach ($cart->get_cart() as $cart_item_key => $cart_item) {
        $product = $cart_item['data'];
        $quantity = $cart_item['quantity'];
        
        if ($quantity >= 10) {
            $product->set_price($product->get_regular_price() * 0.9); // 10% desconto
        } elseif ($quantity >= 5) {
            $product->set_price($product->get_regular_price() * 0.95); // 5% desconto
        }
    }
});

// Frete grátis para produtos específicos
add_filter('woocommerce_package_rates', function($rates, $package) {
    $free_shipping_products = array(123, 456, 789); // IDs dos produtos
    
    $has_free_product = false;
    foreach ($package['contents'] as $item) {
        if (in_array($item['product_id'], $free_shipping_products)) {
            $has_free_product = true;
            break;
        }
    }
    
    if ($has_free_product) {
        foreach ($rates as $rate_id => $rate) {
            if ('free_shipping' === $rate->method_id) {
                $rates[$rate_id]->cost = 0;
                $rates[$rate_id]->taxes = array();
            }
        }
    }
    
    return $rates;
}, 10, 2);
```

---

## 19. BANCO DE DADOS

### 19.1 Consultas Personalizadas com $wpdb

```php
<?php
// Consultas personalizadas com $wpdb

global $wpdb;

// 1. Buscar posts por meta field
$results = $wpdb->get_results("
    SELECT p.ID, p.post_title, pm.meta_value as views
    FROM {$wpdb->posts} p
    INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
    WHERE p.post_type = 'post'
    AND p.post_status = 'publish'
    AND pm.meta_key = 'post_views'
    ORDER BY CAST(pm.meta_value AS UNSIGNED) DESC
    LIMIT 10
");

// 2. Contar posts por categoria
$categories = $wpdb->get_results("
    SELECT t.name, COUNT(*) as count
    FROM {$wpdb->terms} t
    INNER JOIN {$wpdb->term_taxonomy} tt ON t.term_id = tt.term_id
    INNER JOIN {$wpdb->term_relationships} tr ON tt.term_taxonomy_id = tr.term_taxonomy_id
    WHERE tt.taxonomy = 'category'
    GROUP BY t.term_id
    ORDER BY count DESC
");

// 3. Buscar usuários com mais posts
$authors = $wpdb->get_results("
    SELECT u.display_name, COUNT(p.ID) as post_count
    FROM {$wpdb->users} u
    INNER JOIN {$wpdb->posts} p ON u.ID = p.post_author
    WHERE p.post_type = 'post'
    AND p.post_status = 'publish'
    GROUP BY u.ID
    ORDER BY post_count DESC
    LIMIT 10
");

// 4. Atualização em massa
$wpdb->query("
    UPDATE {$wpdb->postmeta}
    SET meta_value = 'novo_valor'
    WHERE meta_key = 'campo_antigo'
");

// 5. Inserir dados personalizados
$wpdb->insert(
    $wpdb->prefix . 'custom_table',
    array(
        'name' => 'João Silva',
        'email' => 'joao@exemplo.com',
        'created_at' => current_time('mysql'),
    ),
    array('%s', '%s', '%s')
);

// 6. Evitar SQL Injection
$user_id = 1;
$wpdb->prepare("
    SELECT * FROM {$wpdb->users} WHERE ID = %d
", $user_id);

// 7. Criar tabela personalizada
function mpp_create_custom_table() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'visitors_log';
    $charset_collate = $wpdb->get_charset_collate();
    
    $sql = "CREATE TABLE $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        ip_address varchar(45) NOT NULL,
        page_url text NOT NULL,
        visit_date datetime DEFAULT CURRENT_TIMESTAMP,
        user_agent text,
        PRIMARY KEY (id)
    ) $charset_collate;";
    
    require_once ABSPATH . 'wp-admin/includes/upgrade.php';
    dbDelta($sql);
}
add_action('after_setup_theme', 'mpp_create_custom_table');

// 8. Registrar visitas
function mpp_log_visitor() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'visitors_log';
    
    $wpdb->insert(
        $table_name,
        array(
            'ip_address' => $_SERVER['REMOTE_ADDR'],
            'page_url' => $_SERVER['REQUEST_URI'],
            'user_agent' => $_SERVER['HTTP_USER_AGENT'],
        ),
        array('%s', '%s', '%s')
    );
}
add_action('wp', 'mpp_log_visitor');
```

### 19.2 Otimização do Banco de Dados

```php
<?php
// Limpeza de dados desnecessários

// Remover revisões antigas
function mpp_clean_revisions() {
    global $wpdb;
    $wpdb->query("
        DELETE FROM {$wpdb->posts}
        WHERE post_type = 'revision'
        AND post_date < DATE_SUB(NOW(), INTERVAL 30 DAY)
    ");
}

// Remover transientes expirados
function mpp_clean_expired_transients() {
    global $wpdb;
    $wpdb->query("
        DELETE FROM {$wpdb->options}
        WHERE option_name LIKE '_transient_%'
        AND option_value < NOW()
    ");
}

// Otimizar tabelas
function mpp_optimize_tables() {
    global $wpdb;
    $tables = $wpdb->get_results("SHOW TABLES", ARRAY_N);
    foreach ($tables as $table) {
        $wpdb->query("OPTIMIZE TABLE {$table[0]}");
    }
}
```

---

## 20. WP-CLI (COMMAND LINE INTERFACE)

### 20.1 Comandos Básicos

```bash
# Instalação do WordPress
wp core download --locale=pt_BR
wp config create --dbname=wordpress --dbuser=root --dbpass=senha
wp core install --url=meusite.com --title="Meu Site" --admin_user=admin --admin_password=senha --admin_email=admin@meusite.com

# Atualizações
wp core update
wp plugin update --all
wp theme update --all
wp core update-db

# Plugins
wp plugin list
wp plugin install elementor --activate
wp plugin activate woocommerce
wp plugin deactivate hello-dolly
wp plugin delete hello-dolly

# Temas
wp theme list
wp theme install twentytwentyfour --activate
wp theme activate meu-tema

# Posts
wp post list
wp post create --post_title="Meu Post" --post_content="Conteúdo" --post_status=publish
wp post update 1 --post_title="Título Atualizado"
wp post delete 1

# Usuários
wp user list
wp user create joao joao@meusite.com --user_pass=senha --role=administrator
wp user update 1 --user_pass=nova_senha

# Banco de Dados
wp db export backup.sql
wp db import backup.sql
wp db optimize
wp db repair

# Importar/Exportar conteúdo
wp export --dir=/tmp --post_type=post
wp import /tmp/export.xml --authors=create

# Cache
wp cache flush

# Buscar e substituir (migrações)
wp search-replace 'http://old.com' 'https://new.com' --all-tables

# Geração de conteúdo
wp post generate --count=10 --post_type=post

# Verificar status
wp core check-update
wp plugin status
wp theme status

# Opções
wp option get blogname
wp option update blogname "Novo Nome"
wp option delete blogdescription

# Cron
wp cron event list
wp cron event run wp_version_check

# Transcrições (rewrites)
wp rewrite structure '/%postname%/'
wp rewrite flush
```

### 20.2 Scripts com WP-CLI

```bash
#!/bin/bash
# backup.sh - Script de backup automático

# Configurações
SITE_PATH="/var/www/meusite"
BACKUP_PATH="/backups"
DATE=$(date +%Y%m%d_%H%M%S)

# Navegar para o site
cd $SITE_PATH

# Backup do banco de dados
wp db export $BACKUP_PATH/db_backup_$DATE.sql

# Backup dos arquivos
tar -czf $BACKUP_PATH/files_backup_$DATE.tar.gz wp-content

# Manter apenas últimos 7 backups
find $BACKUP_PATH -name "*.sql" -mtime +7 -delete
find $BACKUP_PATH -name "*.tar.gz" -mtime +7 -delete

echo "Backup concluído em $DATE"
```

---

## 21. MULTISITE NETWORK

### 21.1 Configuração do Multisite

```php
<?php
// wp-config.php - Ativar Multisite
define('WP_ALLOW_MULTISITE', true);

// Após instalação, adicionar:
define('MULTISITE', true);
define('SUBDOMAIN_INSTALL', false);  // true para subdomínios
define('DOMAIN_CURRENT_SITE', 'meusite.com');
define('PATH_CURRENT_SITE', '/');
define('SITE_ID_CURRENT_SITE', 1);
define('BLOG_ID_CURRENT_SITE', 1);
```

### 21.2 Funções Multisite

```php
<?php
// Funções para Multisite

// Verificar se é Multisite
if (is_multisite()) {
    echo "Site é Multisite";
}

// Obter sites da rede
$sites = get_sites();
foreach ($sites as $site) {
    echo $site->blogname;
    echo get_blog_details($site->blog_id)->siteurl;
}

// Alternar entre sites
switch_to_blog(2);
// Código para o site 2
restore_current_blog();

// Criar novo site
wpmu_create_blog('novo-site.meusite.com', '', 'Novo Site', 1);

// Obter usuários da rede
$users = get_users(array('blog_id' => 0));

// Funções específicas
get_current_blog_id();
get_blog_details(1);
is_main_site();
get_blogaddress_by_id(1);
```

---

## 22. GUTENBERG E BLOCK EDITOR

### 22.1 Criar Bloco Personalizado

```javascript
// block.js - Bloco personalizado para Gutenberg
import { registerBlockType } from '@wordpress/blocks';
import { useBlockProps, RichText } from '@wordpress/block-editor';
import { __ } from '@wordpress/i18n';

registerBlockType('meu-plugin/custom-box', {
    title: __('Caixa Personalizada', 'meu-plugin'),
    icon: 'admin-comments',
    category: 'common',
    attributes: {
        content: {
            type: 'string',
            source: 'html',
            selector: '.box-content',
        },
        title: {
            type: 'string',
            source: 'text',
            selector: 'h3',
        },
    },
    
    edit: ({ attributes, setAttributes }) => {
        const blockProps = useBlockProps();
        
        return (
            <div {...blockProps} className="custom-box">
                <RichText
                    tagName="h3"
                    value={attributes.title}
                    onChange={(title) => setAttributes({ title })}
                    placeholder={__('Título', 'meu-plugin')}
                />
                <RichText
                    tagName="div"
                    className="box-content"
                    value={attributes.content}
                    onChange={(content) => setAttributes({ content })}
                    placeholder={__('Conteúdo', 'meu-plugin')}
                />
            </div>
        );
    },
    
    save: ({ attributes }) => {
        return (
            <div className="custom-box">
                <RichText.Content tagName="h3" value={attributes.title} />
                <RichText.Content tagName="div" className="box-content" value={attributes.content} />
            </div>
        );
    },
});
```

### 22.2 Adicionar Suporte a Blocos no Tema

```php
<?php
// functions.php - Suporte a blocos

// Estilos do editor
add_theme_support('editor-styles');
add_editor_style('assets/css/editor-style.css');

// Cores personalizadas no editor
add_theme_support('editor-color-palette', array(
    array(
        'name'  => __('Azul', 'meu-tema'),
        'slug'  => 'azul',
        'color' => '#0073aa',
    ),
    array(
        'name'  => __('Vermelho', 'meu-tema'),
        'slug'  => 'vermelho',
        'color' => '#dc3232',
    ),
));

// Tamanhos de fonte personalizados
add_theme_support('editor-font-sizes', array(
    array(
        'name' => __('Pequeno', 'meu-tema'),
        'size' => 12,
        'slug' => 'small',
    ),
    array(
        'name' => __('Normal', 'meu-tema'),
        'size' => 16,
        'slug' => 'normal',
    ),
    array(
        'name' => __('Grande', 'meu-tema'),
        'size' => 20,
        'slug' => 'large',
    ),
));

// Alinhamento amplo
add_theme_support('align-wide');

// Estilos de bloco personalizados
add_theme_support('wp-block-styles');

// Responsive embeds
add_theme_support('responsive-embeds');
```

---

## 23. MANUTENÇÃO E BACKUP

### 23.1 Modo de Manutenção

```php
<?php
// functions.php - Modo de manutenção

// Ativar modo de manutenção
function mpp_maintenance_mode() {
    if (!current_user_can('edit_themes') || !is_user_logged_in()) {
        wp_die('<h1>Site em Manutenção</h1><p>Voltaremos em breve. Agradecemos a compreensão.</p>');
    }
}
add_action('get_header', 'mpp_maintenance_mode');

// Melhor: usar arquivo .maintenance
// Criar arquivo: /wp-content/.maintenance
$upgrading = time(); // Colocar timestamp
```

### 23.2 Backup Automático

```php
<?php
// functions.php - Backup automático agendado

function mpp_auto_backup() {
    // Backup do banco de dados
    $backup_dir = WP_CONTENT_DIR . '/backups/';
    if (!file_exists($backup_dir)) {
        wp_mkdir_p($backup_dir);
    }
    
    $filename = $backup_dir . 'backup-' . date('Y-m-d-H-i-s') . '.sql';
    exec("wp db export $filename");
    
    // Backup dos uploads
    $uploads_dir = WP_CONTENT_DIR . '/uploads/';
    $uploads_backup = $backup_dir . 'uploads-' . date('Y-m-d-H-i-s') . '.tar.gz';
    exec("tar -czf $uploads_backup -C $uploads_dir .");
    
    // Enviar para email ou serviço de nuvem
    // wp_mail(...);
}

// Agendar backup semanal
if (!wp_next_scheduled('mpp_weekly_backup')) {
    wp_schedule_event(time(), 'weekly', 'mpp_weekly_backup');
}
add_action('mpp_weekly_backup', 'mpp_auto_backup');
```

---

## 24. RECURSOS E COMUNIDADE

### 24.1 Documentação Oficial

```text
RECURSOS OFICIAIS:
├── WordPress Codex: https://codex.wordpress.org
├── WordPress Developer Resources: https://developer.wordpress.org
├── WordPress API Reference: https://developer.wordpress.org/reference
├── WordPress Theme Handbook: https://developer.wordpress.org/themes
├── WordPress Plugin Handbook: https://developer.wordpress.org/plugins
├── REST API Handbook: https://developer.wordpress.org/rest-api
└── Block Editor Handbook: https://developer.wordpress.org/block-editor

COMUNIDADE:
├── WordPress Stack Exchange: https://wordpress.stackexchange.com
├── WordPress.org Forums: https://wordpress.org/support
├── Make WordPress: https://make.wordpress.org
├── WordPress Meetups: https://www.meetup.com/topics/wordpress
├── WordCamps: https://central.wordcamp.org
├── Slack: https://wordpress.slack.com
└── GitHub: https://github.com/wordpress

RECURSOS EM PORTUGUÊS:
├── Brasil WordPress: https://brasil.wordpress.org
├── WordPress Brasil Comunidade: https://www.facebook.com/groups/wordpressbr
├── WP Café: https://wpcafe.com.br
└── Tables: https://tables.com.br
```

### 24.2 Principais Ferramentas

```text
FERRAMENTAS PARA DESENVOLVEDORES:

LOCAL DEVELOPMENT:
├── Local by Flywheel: https://localwp.com
├── XAMPP: https://www.apachefriends.org
├── MAMP: https://www.mamp.info
├── Laragon: https://laragon.org
└── Docker: https://www.docker.com

DEBUGGING:
├── Query Monitor: Plugin de debug
├── Debug Bar: Plugin de debug
├── WP_DEBUG: constante no wp-config.php
├── Kint Debugger: var_dump melhorado
└── Xdebug: Debugger PHP

CODE QUALITY:
├── PHP_CodeSniffer: Padrões de código
├── WordPress Coding Standards: https://github.com/WordPress/WordPress-Coding-Standards
├── WP-CLI: Linha de comando
└── Composer: Gerenciador de dependências

DEPLOYMENT:
├── Git: Versionamento
├── WP Migrate DB: Migração de banco
├── Deployer: Deploy automatizado
└── GitHub Actions: CI/CD
```

---

## 📊 TABELA RESUMO - FUNÇÕES ESSENCIAIS

| Categoria | Função | Descrição |
|-----------|--------|-----------|
| **Posts** | `the_title()` | Exibe título do post |
| | `the_content()` | Exibe conteúdo |
| | `the_permalink()` | Link permanente |
| | `the_category()` | Categorias do post |
| | `the_tags()` | Tags do post |
| **Condições** | `is_single()` | É post único? |
| | `is_page()` | É página? |
| | `is_home()` | É página inicial? |
| | `is_category()` | É arquivo de categoria? |
| | `is_user_logged_in()` | Usuário logado? |
| **Loops** | `have_posts()` | Verifica posts |
| | `the_post()` | Configura post |
| | `wp_reset_postdata()` | Reseta dados |
| | `WP_Query` | Query personalizada |
| **Banco** | `$wpdb->get_results()` | Consulta SQL |
| | `get_option()` | Opção do site |
| | `update_option()` | Atualiza opção |
| | `get_post_meta()` | Meta do post |
| **Hooks** | `add_action()` | Adiciona action |
| | `add_filter()` | Adiciona filter |
| | `do_action()` | Executa action |
| | `apply_filters()` | Aplica filter |
| **Segurança** | `esc_html()` | Escapa HTML |
| | `esc_url()` | Escapa URL |
| | `wp_nonce_field()` | Campo nonce |
| | `current_user_can()` | Verifica permissão |
| **Internacionalização** | `__()` | Traduz string |
| | `_e()` | Exibe string traduzida |
| | `_n()` | Pluralização |

---

## 🎯 CONCLUSÃO

Este cheat sheet cobre todos os aspectos fundamentais do WordPress, desde a instalação básica até o desenvolvimento avançado de temas e plugins. WordPress é uma plataforma extremamente versátil que pode ser usada tanto por iniciantes quanto por desenvolvedores experientes.

**Lembre-se sempre:**
- Nunca modifique arquivos do core do WordPress
- Mantenha tudo atualizado (core, plugins, temas)
- Faça backups regularmente
- Use práticas de segurança desde o início
- Consulte a documentação oficial sempre que tiver dúvidas
- Participe da comunidade para aprender mais

**Próximos passos para aprofundamento:**
1. Explore a documentação oficial do WordPress
2. Participe de fóruns e grupos da comunidade
3. Pratique criando temas e plugins personalizados
4. Contribua com projetos open source
5. Participe de WordCamps e meetups locais

---

*Este cheat sheet é um guia de referência rápida. Para informações mais detalhadas, consulte a documentação oficial em developer.wordpress.org.*


Perfeito! Vou criar um **Cheat Sheet MEGA COMPLETO** para **Desenvolvimento de Plugins WordPress** e **WordPress em Docker/Virtualização**, no mesmo estilo detalhado dos anteriores.

---

# 🔌 WORDPRESS - DESENVOLVIMENTO DE PLUGINS
## *Guia Definitivo para Criar Plugins Profissionais*

---

## 📚 SUMÁRIO PLUGINS

1. [Fundamentos de Plugins](#1-fundamentos-de-plugins)
2. [Estrutura de Plugin](#2-estrutura-de-plugin)
3. [API de Plugins (Hooks)](#3-api-de-plugins-hooks)
4. [Admin Pages e Settings](#4-admin-pages-e-settings)
5. [Shortcodes](#5-shortcodes)
6. [Widgets](#6-widgets)
7. [Custom Post Types e Taxonomias](#7-custom-post-types-e-taxonomias)
8. [APIs REST Personalizadas](#8-apis-rest-personalizadas)
9. [Banco de Dados em Plugins](#9-banco-de-dados-em-plugins)
10. [Internacionalização (i18n)](#10-internacionalização-i18n)
11. [Segurança em Plugins](#11-segurança-em-plugins)
12. [Testes e Debugging](#12-testes-e-debugging)
13. [Boas Práticas e Padrões](#13-boas-práticas-e-padrões)
14. [Publicação no WordPress.org](#14-publicação-no-wordpressorg)

---

## 1. FUNDAMENTOS DE PLUGINS

### 1.1 O que é um Plugin WordPress?

```text
PLUGIN = Conjunto de arquivos que estende a funcionalidade do WordPress

CARACTERÍSTICAS:
├── Autônomo (não depende do tema)
├── Pode ser ativado/desativado sem perder dados
├── Pode ser instalado/desinstalado com limpeza
├── Pode conter funcionalidades complexas
└── Pode ser distribuído gratuitamente ou comercialmente

TIPOS DE PLUGINS:
├── Plugins Simples: Uma função ou shortcode
├── Plugins de Funcionalidade: Adicionam recursos específicos
├── Plugins de Integração: Conectam com serviços externos
├── Plugins de E-commerce: Extensões para WooCommerce
├── Plugins de Segurança: Proteção e monitoramento
└── Plugins Complexos: Sistemas completos (CRM, LMS, etc.)
```

### 1.2 Arquivos Mínimos de um Plugin

```php
<?php
/*
Plugin Name: Meu Primeiro Plugin
Plugin URI: https://meusite.com/meu-plugin
Description: Uma breve descrição do que o plugin faz
Version: 1.0.0
Author: Seu Nome
Author URI: https://meusite.com
License: GPL v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: meu-plugin
Domain Path: /languages
*/

// Prevenir acesso direto
if (!defined('ABSPATH')) {
    exit; // Saída se acessado diretamente
}

// Definir constantes úteis
define('MPP_VERSION', '1.0.0');
define('MPP_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('MPP_PLUGIN_URL', plugin_dir_url(__FILE__));
define('MPP_PLUGIN_BASENAME', plugin_basename(__FILE__));

// Classe principal do plugin
class MeuPrimeiroPlugin {
    
    private static $instance = null;
    
    public static function get_instance() {
        if (null === self::$instance) {
            self::$instance = new self();
        }
        return self::$instance;
    }
    
    private function __construct() {
        $this->init_hooks();
    }
    
    private function init_hooks() {
        add_action('init', array($this, 'init'));
        add_action('wp_enqueue_scripts', array($this, 'enqueue_scripts'));
    }
    
    public function init() {
        // Inicialização do plugin
        load_plugin_textdomain('meu-plugin', false, dirname(MPP_PLUGIN_BASENAME) . '/languages');
    }
    
    public function enqueue_scripts() {
        wp_enqueue_style('mpp-styles', MPP_PLUGIN_URL . 'assets/css/styles.css', array(), MPP_VERSION);
        wp_enqueue_script('mpp-scripts', MPP_PLUGIN_URL . 'assets/js/scripts.js', array('jquery'), MPP_VERSION, true);
    }
}

// Inicializar plugin
MeuPrimeiroPlugin::get_instance();
```

---

## 2. ESTRUTURA DE PLUGIN

### 2.1 Estrutura de Diretórios Recomendada

```text
meu-plugin/
├── meu-plugin.php                 (Arquivo principal)
├── uninstall.php                  (Desinstalação)
├── readme.txt                     (Para WordPress.org)
├── languages/                     (Traduções)
│   └── meu-plugin-pt_BR.po
│   └── meu-plugin-pt_BR.mo
├── includes/                      (Classes principais)
│   ├── class-main.php
│   ├── class-admin.php
│   ├── class-frontend.php
│   └── class-db.php
├── admin/                         (Arquivos do admin)
│   ├── css/
│   │   └── admin-styles.css
│   ├── js/
│   │   └── admin-scripts.js
│   └── views/
│       ├── settings-page.php
│       └── metabox.php
├── public/                        (Arquivos públicos)
│   ├── css/
│   │   └── public-styles.css
│   ├── js/
│   │   └── public-scripts.js
│   └── partials/
│       └── template.php
├── assets/                        (Arquivos estáticos)
│   ├── images/
│   └── fonts/
├── vendor/                        (Dependências Composer)
├── tests/                         (Testes unitários)
│   ├── bootstrap.php
│   └── test-sample.php
└── .gitignore
```

### 2.2 Arquivo Principal Avançado

```php
<?php
/**
 * Plugin Name: Plugin Avançado
 * Plugin URI: https://meusite.com/plugin-avancado
 * Description: Plugin com estrutura profissional
 * Version: 1.0.0
 * Author: Seu Nome
 * Author URI: https://meusite.com
 * License: GPL v2 or later
 * Requires at least: 5.0
 * Tested up to: 6.4
 * Requires PHP: 7.4
 * Text Domain: plugin-avancado
 * Domain Path: /languages
 * 
 * @package PluginAvancado
 */

// Prevenir acesso direto
if (!defined('ABSPATH')) {
    exit;
}

// Definir constantes
define('PLUGIN_AVANCADO_VERSION', '1.0.0');
define('PLUGIN_AVANCADO_FILE', __FILE__);
define('PLUGIN_AVANCADO_PATH', plugin_dir_path(__FILE__));
define('PLUGIN_AVANCADO_URL', plugin_dir_url(__FILE__));
define('PLUGIN_AVANCADO_BASENAME', plugin_basename(__FILE__));

// Autoload de classes (PSR-4)
spl_autoload_register(function ($class) {
    $prefix = 'PluginAvancado\\';
    $base_dir = PLUGIN_AVANCADO_PATH . 'includes/';
    
    $len = strlen($prefix);
    if (strncmp($prefix, $class, $len) !== 0) {
        return;
    }
    
    $relative_class = substr($class, $len);
    $file = $base_dir . str_replace('\\', '/', $relative_class) . '.php';
    
    if (file_exists($file)) {
        require $file;
    }
});

// Verificar requisitos
function plugin_avancado_check_requirements() {
    if (version_compare(PHP_VERSION, '7.4', '<')) {
        add_action('admin_notices', function() {
            echo '<div class="error"><p>Plugin Avançado requer PHP 7.4 ou superior.</p></div>';
        });
        return false;
    }
    return true;
}

// Inicializar plugin
if (plugin_avancado_check_requirements()) {
    $plugin = PluginAvancado\Main::get_instance();
    register_activation_hook(__FILE__, array($plugin, 'activate'));
    register_deactivation_hook(__FILE__, array($plugin, 'deactivate'));
    register_uninstall_hook(__FILE__, array('PluginAvancado\Main', 'uninstall'));
}
```

### 2.3 Classe Principal (Singleton)

```php
<?php
namespace PluginAvancado;

class Main {
    
    private static $instance = null;
    private $admin;
    private $frontend;
    
    private function __construct() {
        $this->load_dependencies();
        $this->init_hooks();
    }
    
    public static function get_instance() {
        if (null === self::$instance) {
            self::$instance = new self();
        }
        return self::$instance;
    }
    
    private function load_dependencies() {
        $this->admin = new Admin();
        $this->frontend = new Frontend();
    }
    
    private function init_hooks() {
        add_action('init', array($this, 'init'));
        add_action('plugins_loaded', array($this, 'load_textdomain'));
    }
    
    public function init() {
        // Inicializar post types, taxonomias, etc.
        $this->register_post_types();
        $this->register_taxonomies();
    }
    
    public function load_textdomain() {
        load_plugin_textdomain(
            'plugin-avancado',
            false,
            dirname(PLUGIN_AVANCADO_BASENAME) . '/languages'
        );
    }
    
    private function register_post_types() {
        // Registrar CPTs
    }
    
    private function register_taxonomies() {
        // Registrar taxonomias
    }
    
    public function activate() {
        // Criar tabelas, definir opções padrão, etc.
        $this->create_tables();
        $this->set_default_options();
        
        // Limpar rewrite rules
        flush_rewrite_rules();
    }
    
    public function deactivate() {
        // Limpar agendamentos, etc.
        wp_clear_scheduled_hook('plugin_avancado_daily_event');
        
        // Limpar rewrite rules
        flush_rewrite_rules();
    }
    
    public static function uninstall() {
        // Remover tabelas, opções, etc.
        delete_option('plugin_avancado_options');
        
        global $wpdb;
        $wpdb->query("DROP TABLE IF EXISTS {$wpdb->prefix}plugin_avancado_data");
    }
    
    private function create_tables() {
        global $wpdb;
        $charset_collate = $wpdb->get_charset_collate();
        
        $table_name = $wpdb->prefix . 'plugin_avancado_data';
        
        $sql = "CREATE TABLE IF NOT EXISTS $table_name (
            id mediumint(9) NOT NULL AUTO_INCREMENT,
            data longtext NOT NULL,
            created_at datetime DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        ) $charset_collate;";
        
        require_once ABSPATH . 'wp-admin/includes/upgrade.php';
        dbDelta($sql);
    }
    
    private function set_default_options() {
        add_option('plugin_avancado_options', array(
            'version' => PLUGIN_AVANCADO_VERSION,
            'enable_feature' => true,
        ));
    }
}
```

---

## 3. API DE PLUGINS (HOOKS)

### 3.1 Actions - Onde e Quando Executar

```php
<?php
// Actions mais comuns em plugins

// 1. Plugin carregado
add_action('plugins_loaded', 'meu_plugin_init');
function meu_plugin_init() {
    // Código executado quando todos plugins estão carregados
    // Ideal para inicializações
}

// 2. WordPress inicializado
add_action('init', 'meu_plugin_register_post_type');
function meu_plugin_register_post_type() {
    // Registrar CPTs, taxonomias, shortcodes
    register_post_type('meu_cpt', $args);
}

// 3. Admin carregado
add_action('admin_init', 'meu_plugin_admin_init');
function meu_plugin_admin_init() {
    // Registrar configurações, scripts, etc.
    register_setting('meu_plugin_settings', 'meu_plugin_option');
}

// 4. Menu admin
add_action('admin_menu', 'meu_plugin_add_admin_menu');
function meu_plugin_add_admin_menu() {
    add_menu_page(
        'Meu Plugin',
        'Meu Plugin',
        'manage_options',
        'meu-plugin',
        'meu_plugin_admin_page',
        'dashicons-admin-plugins',
        80
    );
}

// 5. Widgets inicializados
add_action('widgets_init', 'meu_plugin_register_widget');
function meu_plugin_register_widget() {
    register_widget('Meu_Plugin_Widget');
}

// 6. Carregar scripts
add_action('wp_enqueue_scripts', 'meu_plugin_enqueue_scripts');
function meu_plugin_enqueue_scripts() {
    wp_enqueue_script('meu-plugin-script', plugin_dir_url(__FILE__) . 'js/script.js', array('jquery'), '1.0.0', true);
    wp_localize_script('meu-plugin-script', 'meu_plugin_ajax', array(
        'ajax_url' => admin_url('admin-ajax.php'),
        'nonce' => wp_create_nonce('meu_plugin_nonce')
    ));
}

// 7. AJAX
add_action('wp_ajax_meu_plugin_action', 'meu_plugin_ajax_handler');
add_action('wp_ajax_nopriv_meu_plugin_action', 'meu_plugin_ajax_handler');
function meu_plugin_ajax_handler() {
    check_ajax_referer('meu_plugin_nonce', 'nonce');
    
    // Processar requisição
    $result = array('success' => true, 'data' => 'Resposta');
    wp_send_json($result);
}

// 8. Salvar post
add_action('save_post', 'meu_plugin_save_post', 10, 3);
function meu_plugin_save_post($post_id, $post, $update) {
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) return;
    if (!current_user_can('edit_post', $post_id)) return;
    
    // Salvar meta dados
    if (isset($_POST['meu_plugin_field'])) {
        update_post_meta($post_id, '_meu_plugin_field', sanitize_text_field($_POST['meu_plugin_field']));
    }
}

// 9. Login do usuário
add_action('wp_login', 'meu_plugin_user_login', 10, 2);
function meu_plugin_user_login($user_login, $user) {
    update_user_meta($user->ID, 'last_login', current_time('mysql'));
}

// 10. Cron jobs
add_action('meu_plugin_daily_event', 'meu_plugin_daily_task');
function meu_plugin_daily_task() {
    // Executar tarefa diária
    wp_schedule_event(time(), 'daily', 'meu_plugin_daily_event');
}
```

### 3.2 Filters - Modificando Dados

```php
<?php
// Filters mais comuns

// 1. Modificar título
add_filter('the_title', 'meu_plugin_custom_title', 10, 2);
function meu_plugin_custom_title($title, $id) {
    if (get_post_type($id) == 'meu_cpt') {
        $prefix = get_post_meta($id, '_prefix', true);
        if ($prefix) {
            return $prefix . ': ' . $title;
        }
    }
    return $title;
}

// 2. Modificar conteúdo
add_filter('the_content', 'meu_plugin_add_after_content');
function meu_plugin_add_after_content($content) {
    if (is_single() && get_post_type() == 'meu_cpt') {
        $extra = '<div class="plugin-extra">' . get_option('meu_plugin_extra') . '</div>';
        return $content . $extra;
    }
    return $content;
}

// 3. Modificar excerpt length
add_filter('excerpt_length', 'meu_plugin_custom_excerpt_length');
function meu_plugin_custom_excerpt_length($length) {
    return 30; // 30 palavras
}

// 4. Adicionar campos ao perfil de usuário
add_filter('user_contactmethods', 'meu_plugin_user_contact_methods');
function meu_plugin_user_contact_methods($methods) {
    $methods['twitter'] = __('Twitter', 'meu-plugin');
    $methods['linkedin'] = __('LinkedIn', 'meu-plugin');
    return $methods;
}

// 5. Modificar query principal
add_action('pre_get_posts', 'meu_plugin_modify_query');
function meu_plugin_modify_query($query) {
    if (!is_admin() && $query->is_main_query() && $query->is_category()) {
        $query->set('posts_per_page', 12);
        $query->set('meta_key', 'destaque');
        $query->set('orderby', 'meta_value_num');
    }
}

// 6. Adicionar classes ao body
add_filter('body_class', 'meu_plugin_add_body_class');
function meu_plugin_add_body_class($classes) {
    if (is_singular('meu_cpt')) {
        $classes[] = 'meu-cpt-single';
    }
    return $classes;
}

// 7. Modificar colunas no admin
add_filter('manage_posts_columns', 'meu_plugin_add_admin_columns');
function meu_plugin_add_admin_columns($columns) {
    $columns['views'] = __('Visualizações', 'meu-plugin');
    return $columns;
}

add_action('manage_posts_custom_column', 'meu_plugin_display_admin_columns', 10, 2);
function meu_plugin_display_admin_columns($column, $post_id) {
    if ($column == 'views') {
        $views = get_post_meta($post_id, 'views', true);
        echo $views ? $views : 0;
    }
}

// 8. Modificar URL de login
add_filter('login_url', 'meu_plugin_custom_login_url', 10, 2);
function meu_plugin_custom_login_url($login_url, $redirect) {
    return home_url('/entrar/');
}

// 9. Modificar mensagem de erro de login
add_filter('login_errors', 'meu_plugin_custom_login_errors');
function meu_plugin_custom_login_errors($error) {
    return 'Credenciais inválidas. Tente novamente.';
}

// 10. Adicionar opções de ordenação
add_filter('woocommerce_catalog_orderby', 'meu_plugin_add_orderby_options');
function meu_plugin_add_orderby_options($options) {
    $options['popularidade'] = __('Popularidade', 'meu-plugin');
    return $options;
}
```

### 3.3 Criar Hooks Personalizados

```php
<?php
// Plugin que permite outros plugins se conectarem

// Definir action personalizada
do_action('meu_plugin_before_process', $data);

// Definir filter personalizado
$result = apply_filters('meu_plugin_process_data', $data, $context);

// Exemplo completo
class MeuPlugin {
    
    public function process_data($data) {
        // Action antes
        do_action('meu_plugin_before_process', $data);
        
        // Processamento
        $result = $this->do_process($data);
        
        // Filter para modificar resultado
        $result = apply_filters('meu_plugin_after_process', $result, $data);
        
        // Action depois
        do_action('meu_plugin_after_process', $result);
        
        return $result;
    }
}

// Outros plugins podem se conectar:
add_action('meu_plugin_before_process', function($data) {
    error_log('Processando: ' . print_r($data, true));
});

add_filter('meu_plugin_after_process', function($result, $data) {
    return $result . ' - Modificado por outro plugin';
}, 10, 2);
```

---

## 4. ADMIN PAGES E SETTINGS

### 4.1 Páginas de Administração

```php
<?php
// Adicionar página de menu
add_action('admin_menu', 'meu_plugin_add_admin_menu');

function meu_plugin_add_admin_menu() {
    // Página principal
    add_menu_page(
        __('Meu Plugin', 'meu-plugin'),          // Título da página
        __('Meu Plugin', 'meu-plugin'),          // Título do menu
        'manage_options',                         // Capacidade
        'meu-plugin',                             // Slug
        'meu_plugin_main_page',                   // Callback
        'dashicons-admin-plugins',                // Ícone
        80                                        // Posição
    );
    
    // Submenu: Configurações
    add_submenu_page(
        'meu-plugin',                             // Slug pai
        __('Configurações', 'meu-plugin'),        // Título da página
        __('Configurações', 'meu-plugin'),        // Título do menu
        'manage_options',                         // Capacidade
        'meu-plugin-settings',                    // Slug
        'meu_plugin_settings_page'                // Callback
    );
    
    // Submenu: Sobre
    add_submenu_page(
        'meu-plugin',
        __('Sobre', 'meu-plugin'),
        __('Sobre', 'meu-plugin'),
        'manage_options',
        'meu-plugin-about',
        'meu_plugin_about_page'
    );
    
    // Página oculta (sem menu)
    add_submenu_page(
        null,                                      // Sem menu pai
        __('Importar Dados', 'meu-plugin'),
        __('Importar Dados', 'meu-plugin'),
        'manage_options',
        'meu-plugin-import',
        'meu_plugin_import_page'
    );
}

// Página principal
function meu_plugin_main_page() {
    ?>
    <div class="wrap">
        <h1><?php echo esc_html(get_admin_page_title()); ?></h1>
        
        <div class="meu-plugin-dashboard">
            <div class="dashboard-card">
                <h2>Bem-vindo ao Meu Plugin</h2>
                <p>Versão: <?php echo MPP_VERSION; ?></p>
            </div>
            
            <div class="dashboard-stats">
                <div class="stat-box">
                    <span class="stat-number"><?php echo meu_plugin_get_total_items(); ?></span>
                    <span class="stat-label">Itens Cadastrados</span>
                </div>
            </div>
        </div>
    </div>
    
    <style>
        .meu-plugin-dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .dashboard-card {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .stat-box {
            background: #fff;
            padding: 20px;
            text-align: center;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .stat-number {
            font-size: 32px;
            font-weight: bold;
            display: block;
            color: #0073aa;
        }
    </style>
    <?php
}

// Página de configurações
function meu_plugin_settings_page() {
    ?>
    <div class="wrap">
        <h1><?php echo esc_html(get_admin_page_title()); ?></h1>
        <form method="post" action="options.php">
            <?php
            settings_fields('meu_plugin_settings');
            do_settings_sections('meu-plugin-settings');
            submit_button();
            ?>
        </form>
    </div>
    <?php
}

// Página sobre
function meu_plugin_about_page() {
    ?>
    <div class="wrap">
        <h1><?php echo esc_html(get_admin_page_title()); ?></h1>
        <div class="card">
            <h2>Sobre o Plugin</h2>
            <p>Plugin desenvolvido por <a href="https://meusite.com" target="_blank">Seu Nome</a></p>
            <p>Versão: <?php echo MPP_VERSION; ?></p>
            <h3>Documentação</h3>
            <p>Visite o site oficial para documentação completa.</p>
        </div>
    </div>
    <?php
}
```

### 4.2 Configurações com Settings API

```php
<?php
// Registrar configurações
add_action('admin_init', 'meu_plugin_register_settings');

function meu_plugin_register_settings() {
    // Grupo de configurações
    register_setting(
        'meu_plugin_settings',                    // Grupo de opções
        'meu_plugin_options',                     // Nome da opção
        'meu_plugin_sanitize_options'             // Callback de sanitização
    );
    
    // Seção de configurações
    add_settings_section(
        'meu_plugin_main_section',                // ID da seção
        __('Configurações Gerais', 'meu-plugin'), // Título
        'meu_plugin_section_callback',            // Callback
        'meu-plugin-settings'                     // Página
    );
    
    // Campo: Texto
    add_settings_field(
        'api_key',                                 // ID do campo
        __('Chave da API', 'meu-plugin'),          // Label
        'meu_plugin_api_key_field',                // Callback
        'meu-plugin-settings',                     // Página
        'meu_plugin_main_section'                  // Seção
    );
    
    // Campo: Checkbox
    add_settings_field(
        'enable_feature',
        __('Ativar Funcionalidade', 'meu-plugin'),
        'meu_plugin_enable_feature_field',
        'meu-plugin-settings',
        'meu_plugin_main_section'
    );
    
    // Campo: Select
    add_settings_field(
        'display_mode',
        __('Modo de Exibição', 'meu-plugin'),
        'meu_plugin_display_mode_field',
        'meu-plugin-settings',
        'meu_plugin_main_section'
    );
    
    // Campo: Textarea
    add_settings_field(
        'custom_css',
        __('CSS Personalizado', 'meu-plugin'),
        'meu_plugin_custom_css_field',
        'meu-plugin-settings',
        'meu_plugin_main_section'
    );
}

function meu_plugin_section_callback() {
    echo '<p>' . __('Configure as opções do plugin abaixo.', 'meu-plugin') . '</p>';
}

// Callbacks dos campos
function meu_plugin_api_key_field() {
    $options = get_option('meu_plugin_options');
    $value = isset($options['api_key']) ? $options['api_key'] : '';
    ?>
    <input type="text" name="meu_plugin_options[api_key]" 
           value="<?php echo esc_attr($value); ?>" 
           class="regular-text">
    <p class="description"><?php _e('Digite sua chave de API.', 'meu-plugin'); ?></p>
    <?php
}

function meu_plugin_enable_feature_field() {
    $options = get_option('meu_plugin_options');
    $checked = isset($options['enable_feature']) && $options['enable_feature'];
    ?>
    <label>
        <input type="checkbox" name="meu_plugin_options[enable_feature]" 
               value="1" <?php checked($checked); ?>>
        <?php _e('Ativar funcionalidade principal', 'meu-plugin'); ?>
    </label>
    <?php
}

function meu_plugin_display_mode_field() {
    $options = get_option('meu_plugin_options');
    $mode = isset($options['display_mode']) ? $options['display_mode'] : 'grid';
    ?>
    <select name="meu_plugin_options[display_mode]">
        <option value="grid" <?php selected($mode, 'grid'); ?>>
            <?php _e('Grade', 'meu-plugin'); ?>
        </option>
        <option value="list" <?php selected($mode, 'list'); ?>>
            <?php _e('Lista', 'meu-plugin'); ?>
        </option>
        <option value="carousel" <?php selected($mode, 'carousel'); ?>>
            <?php _e('Carrossel', 'meu-plugin'); ?>
        </option>
    </select>
    <?php
}

function meu_plugin_custom_css_field() {
    $options = get_option('meu_plugin_options');
    $css = isset($options['custom_css']) ? $options['custom_css'] : '';
    ?>
    <textarea name="meu_plugin_options[custom_css]" rows="10" cols="50" 
              class="large-text code"><?php echo esc_textarea($css); ?></textarea>
    <p class="description"><?php _e('CSS personalizado para o frontend.', 'meu-plugin'); ?></p>
    <?php
}

// Sanitização
function meu_plugin_sanitize_options($input) {
    $sanitized = array();
    
    if (isset($input['api_key'])) {
        $sanitized['api_key'] = sanitize_text_field($input['api_key']);
    }
    
    if (isset($input['enable_feature'])) {
        $sanitized['enable_feature'] = (bool) $input['enable_feature'];
    } else {
        $sanitized['enable_feature'] = false;
    }
    
    if (isset($input['display_mode'])) {
        $allowed_modes = array('grid', 'list', 'carousel');
        if (in_array($input['display_mode'], $allowed_modes)) {
            $sanitized['display_mode'] = $input['display_mode'];
        }
    }
    
    if (isset($input['custom_css'])) {
        $sanitized['custom_css'] = wp_strip_all_tags($input['custom_css']);
    }
    
    return $sanitized;
}

// Adicionar CSS personalizado ao frontend
add_action('wp_head', 'meu_plugin_custom_css_output');
function meu_plugin_custom_css_output() {
    $options = get_option('meu_plugin_options');
    if (!empty($options['custom_css'])) {
        echo '<style type="text/css">' . wp_strip_all_tags($options['custom_css']) . '</style>';
    }
}
```

### 4.3 Metaboxes e Campos Personalizados

```php
<?php
// Adicionar metabox para CPT
add_action('add_meta_boxes', 'meu_plugin_add_metabox');
add_action('save_post', 'meu_plugin_save_metabox');

function meu_plugin_add_metabox() {
    add_meta_box(
        'meu_plugin_data',                        // ID
        __('Dados Adicionais', 'meu-plugin'),     // Título
        'meu_plugin_metabox_callback',            // Callback
        array('post', 'page', 'meu_cpt'),         // Post types
        'normal',                                 // Contexto
        'high'                                    // Prioridade
    );
}

function meu_plugin_metabox_callback($post) {
    // Nonce para segurança
    wp_nonce_field('meu_plugin_metabox', 'meu_plugin_metabox_nonce');
    
    // Recuperar valores salvos
    $subtitle = get_post_meta($post->ID, '_meu_plugin_subtitle', true);
    $featured = get_post_meta($post->ID, '_meu_plugin_featured', true);
    $color = get_post_meta($post->ID, '_meu_plugin_color', true);
    ?>
    <table class="form-table">
        <tr>
            <th><label for="meu_plugin_subtitle"><?php _e('Subtítulo', 'meu-plugin'); ?></label></th>
            <td>
                <input type="text" id="meu_plugin_subtitle" name="meu_plugin_subtitle" 
                       value="<?php echo esc_attr($subtitle); ?>" class="widefat">
                <p class="description"><?php _e('Subtítulo do post.', 'meu-plugin'); ?></p>
            </td>
        </tr>
        <tr>
            <th><label for="meu_plugin_featured"><?php _e('Destaque', 'meu-plugin'); ?></label></th>
            <td>
                <label>
                    <input type="checkbox" id="meu_plugin_featured" name="meu_plugin_featured" 
                           value="1" <?php checked($featured, '1'); ?>>
                    <?php _e('Marcar como destaque', 'meu-plugin'); ?>
                </label>
            </td>
        </tr>
        <tr>
            <th><label for="meu_plugin_color"><?php _e('Cor de Destaque', 'meu-plugin'); ?></label></th>
            <td>
                <input type="color" id="meu_plugin_color" name="meu_plugin_color" 
                       value="<?php echo esc_attr($color); ?>">
            </td>
        </tr>
    </table>
    <?php
}

function meu_plugin_save_metabox($post_id) {
    // Verificar nonce
    if (!isset($_POST['meu_plugin_metabox_nonce']) || 
        !wp_verify_nonce($_POST['meu_plugin_metabox_nonce'], 'meu_plugin_metabox')) {
        return;
    }
    
    // Verificar autosave
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }
    
    // Verificar permissões
    if (!current_user_can('edit_post', $post_id)) {
        return;
    }
    
    // Salvar subtítulo
    if (isset($_POST['meu_plugin_subtitle'])) {
        update_post_meta($post_id, '_meu_plugin_subtitle', 
                         sanitize_text_field($_POST['meu_plugin_subtitle']));
    }
    
    // Salvar destaque
    $featured = isset($_POST['meu_plugin_featured']) ? '1' : '0';
    update_post_meta($post_id, '_meu_plugin_featured', $featured);
    
    // Salvar cor
    if (isset($_POST['meu_plugin_color'])) {
        update_post_meta($post_id, '_meu_plugin_color', 
                         sanitize_hex_color($_POST['meu_plugin_color']));
    }
}
```

---

## 5. SHORTCODES

### 5.1 Shortcode Básico

```php
<?php
// Registrar shortcode
add_shortcode('meu_plugin_box', 'meu_plugin_box_shortcode');

function meu_plugin_box_shortcode($atts, $content = null) {
    // Atributos padrão
    $atts = shortcode_atts(array(
        'title' => __('Título', 'meu-plugin'),
        'color' => '#0073aa',
        'class' => '',
    ), $atts, 'meu_plugin_box');
    
    // Sanitizar
    $title = esc_html($atts['title']);
    $color = esc_attr($atts['color']);
    $class = esc_attr($atts['class']);
    $content = do_shortcode($content);
    
    // Retornar HTML
    return '<div class="plugin-box ' . $class . '" style="border-color: ' . $color . ';">
                <h3 style="background-color: ' . $color . ';">' . $title . '</h3>
                <div class="box-content">' . $content . '</div>
            </div>';
}

// Uso: [meu_plugin_box title="Meu Título" color="#ff0000"]Conteúdo[/meu_plugin_box]
```

### 5.2 Shortcode com Banco de Dados

```php
<?php
// Shortcode para listar itens
add_shortcode('meu_plugin_list', 'meu_plugin_list_shortcode');

function meu_plugin_list_shortcode($atts) {
    global $wpdb;
    
    $atts = shortcode_atts(array(
        'limit' => 10,
        'category' => '',
        'orderby' => 'date',
        'order' => 'DESC',
    ), $atts, 'meu_plugin_list');
    
    // Construir query
    $table_name = $wpdb->prefix . 'meu_plugin_items';
    $limit = intval($atts['limit']);
    $orderby = sanitize_sql_orderby($atts['orderby']);
    $order = strtoupper($atts['order']) === 'ASC' ? 'ASC' : 'DESC';
    
    $where = '';
    if (!empty($atts['category'])) {
        $category = esc_sql($atts['category']);
        $where = "WHERE category = '$category'";
    }
    
    $items = $wpdb->get_results("
        SELECT * FROM $table_name 
        $where 
        ORDER BY $orderby $order 
        LIMIT $limit
    ");
    
    if (empty($items)) {
        return '<p>' . __('Nenhum item encontrado.', 'meu-plugin') . '</p>';
    }
    
    ob_start();
    ?>
    <div class="plugin-items-list">
        <?php foreach ($items as $item) : ?>
            <div class="plugin-item">
                <h3><?php echo esc_html($item->title); ?></h3>
                <p><?php echo esc_html($item->description); ?></p>
                <?php if ($item->link) : ?>
                    <a href="<?php echo esc_url($item->link); ?>" class="item-link">
                        <?php _e('Saiba mais', 'meu-plugin'); ?>
                    </a>
                <?php endif; ?>
            </div>
        <?php endforeach; ?>
    </div>
    <?php
    return ob_get_clean();
}
```

### 5.3 Shortcode com Parâmetros Avançados

```php
<?php
// Shortcode com suporte a atributos dinâmicos
add_shortcode('meu_plugin_dynamic', 'meu_plugin_dynamic_shortcode');

function meu_plugin_dynamic_shortcode($atts, $content = null) {
    // Atributos com validação
    $atts = shortcode_atts(array(
        'type' => 'post',
        'id' => 0,
        'field' => 'title',
        'default' => '',
    ), $atts, 'meu_plugin_dynamic');
    
    $type = sanitize_key($atts['type']);
    $id = intval($atts['id']);
    $field = sanitize_key($atts['field']);
    $default = esc_html($atts['default']);
    
    if ($type === 'post' && $id > 0) {
        $post = get_post($id);
        if ($post) {
            switch ($field) {
                case 'title':
                    return get_the_title($post);
                case 'content':
                    return get_the_content(null, false, $post);
                case 'excerpt':
                    return get_the_excerpt($post);
                case 'permalink':
                    return get_permalink($post);
                default:
                    return get_post_meta($id, $field, true) ?: $default;
            }
        }
    }
    
    if ($type === 'option') {
        return get_option($field, $default);
    }
    
    return $default;
}

// Uso: [meu_plugin_dynamic type="post" id="123" field="title"]
// Uso: [meu_plugin_dynamic type="option" field="blogname"]
```

---

## 6. WIDGETS

### 6.1 Widget Básico

```php
<?php
// Registrar widget
add_action('widgets_init', 'meu_plugin_register_widget');

function meu_plugin_register_widget() {
    register_widget('Meu_Plugin_Widget');
}

class Meu_Plugin_Widget extends WP_Widget {
    
    public function __construct() {
        parent::__construct(
            'meu_plugin_widget',
            __('Meu Plugin Widget', 'meu-plugin'),
            array(
                'description' => __('Widget personalizado do Meu Plugin', 'meu-plugin'),
                'classname' => 'meu-plugin-widget',
            )
        );
    }
    
    // Frontend
    public function widget($args, $instance) {
        $title = apply_filters('widget_title', $instance['title']);
        $text = $instance['text'];
        $show_author = $instance['show_author'];
        
        echo $args['before_widget'];
        
        if (!empty($title)) {
            echo $args['before_title'] . esc_html($title) . $args['after_title'];
        }
        
        echo '<div class="widget-content">';
        echo wp_kses_post($text);
        
        if ($show_author) {
            echo '<p class="widget-author">' . __('Por: ', 'meu-plugin') . get_the_author() . '</p>';
        }
        
        echo '</div>';
        
        echo $args['after_widget'];
    }
    
    // Admin form
    public function form($instance) {
        $title = !empty($instance['title']) ? $instance['title'] : '';
        $text = !empty($instance['text']) ? $instance['text'] : '';
        $show_author = !empty($instance['show_author']) ? $instance['show_author'] : false;
        ?>
        <p>
            <label for="<?php echo $this->get_field_id('title'); ?>">
                <?php _e('Título:', 'meu-plugin'); ?>
            </label>
            <input type="text" id="<?php echo $this->get_field_id('title'); ?>" 
                   name="<?php echo $this->get_field_name('title'); ?>" 
                   value="<?php echo esc_attr($title); ?>" class="widefat">
        </p>
        <p>
            <label for="<?php echo $this->get_field_id('text'); ?>">
                <?php _e('Texto:', 'meu-plugin'); ?>
            </label>
            <textarea id="<?php echo $this->get_field_id('text'); ?>" 
                      name="<?php echo $this->get_field_name('text'); ?>" 
                      class="widefat" rows="5"><?php echo esc_textarea($text); ?></textarea>
        </p>
        <p>
            <input type="checkbox" id="<?php echo $this->get_field_id('show_author'); ?>" 
                   name="<?php echo $this->get_field_name('show_author'); ?>" 
                   value="1" <?php checked($show_author, '1'); ?>>
            <label for="<?php echo $this->get_field_id('show_author'); ?>">
                <?php _e('Exibir autor', 'meu-plugin'); ?>
            </label>
        </p>
        <?php
    }
    
    // Salvar configurações
    public function update($new_instance, $old_instance) {
        $instance = array();
        $instance['title'] = sanitize_text_field($new_instance['title']);
        $instance['text'] = wp_kses_post($new_instance['text']);
        $instance['show_author'] = !empty($new_instance['show_author']) ? '1' : '0';
        return $instance;
    }
}
```

### 6.2 Widget com Configurações Avançadas

```php
<?php
class Meu_Plugin_Advanced_Widget extends WP_Widget {
    
    public function __construct() {
        parent::__construct(
            'meu_plugin_advanced_widget',
            __('Widget Avançado', 'meu-plugin'),
            array(
                'description' => __('Widget com opções avançadas', 'meu-plugin'),
            )
        );
    }
    
    public function widget($args, $instance) {
        $title = apply_filters('widget_title', $instance['title']);
        $post_type = $instance['post_type'];
        $posts_per_page = intval($instance['posts_per_page']);
        $show_image = !empty($instance['show_image']);
        $show_excerpt = !empty($instance['show_excerpt']);
        
        $query = new WP_Query(array(
            'post_type' => $post_type,
            'posts_per_page' => $posts_per_page,
            'orderby' => $instance['orderby'],
            'order' => $instance['order'],
        ));
        
        echo $args['before_widget'];
        
        if (!empty($title)) {
            echo $args['before_title'] . esc_html($title) . $args['after_title'];
        }
        
        if ($query->have_posts()) {
            echo '<ul class="widget-posts">';
            while ($query->have_posts()) {
                $query->the_post();
                echo '<li>';
                
                if ($show_image && has_post_thumbnail()) {
                    echo '<div class="widget-post-thumb">';
                    the_post_thumbnail('thumbnail');
                    echo '</div>';
                }
                
                echo '<div class="widget-post-content">';
                echo '<a href="' . get_permalink() . '">' . get_the_title() . '</a>';
                
                if ($show_excerpt) {
                    echo '<p>' . get_the_excerpt() . '</p>';
                }
                
                echo '</div>';
                echo '</li>';
            }
            echo '</ul>';
            wp_reset_postdata();
        } else {
            echo '<p>' . __('Nenhum post encontrado.', 'meu-plugin') . '</p>';
        }
        
        echo $args['after_widget'];
    }
    
    public function form($instance) {
        $title = isset($instance['title']) ? $instance['title'] : '';
        $post_type = isset($instance['post_type']) ? $instance['post_type'] : 'post';
        $posts_per_page = isset($instance['posts_per_page']) ? $instance['posts_per_page'] : 5;
        $orderby = isset($instance['orderby']) ? $instance['orderby'] : 'date';
        $order = isset($instance['order']) ? $instance['order'] : 'DESC';
        $show_image = !empty($instance['show_image']);
        $show_excerpt = !empty($instance['show_excerpt']);
        
        $post_types = get_post_types(array('public' => true), 'objects');
        $orderby_options = array(
            'date' => __('Data', 'meu-plugin'),
            'title' => __('Título', 'meu-plugin'),
            'comment_count' => __('Comentários', 'meu-plugin'),
            'rand' => __('Aleatório', 'meu-plugin'),
        );
        ?>
        <p>
            <label for="<?php echo $this->get_field_id('title'); ?>">
                <?php _e('Título:', 'meu-plugin'); ?>
            </label>
            <input type="text" id="<?php echo $this->get_field_id('title'); ?>" 
                   name="<?php echo $this->get_field_name('title'); ?>" 
                   value="<?php echo esc_attr($title); ?>" class="widefat">
        </p>
        <p>
            <label for="<?php echo $this->get_field_id('post_type'); ?>">
                <?php _e('Tipo de Conteúdo:', 'meu-plugin'); ?>
            </label>
            <select id="<?php echo $this->get_field_id('post_type'); ?>" 
                    name="<?php echo $this->get_field_name('post_type'); ?>" class="widefat">
                <?php foreach ($post_types as $pt) : ?>
                    <option value="<?php echo $pt->name; ?>" <?php selected($post_type, $pt->name); ?>>
                        <?php echo $pt->label; ?>
                    </option>
                <?php endforeach; ?>
            </select>
        </p>
        <p>
            <label for="<?php echo $this->get_field_id('posts_per_page'); ?>">
                <?php _e('Número de Posts:', 'meu-plugin'); ?>
            </label>
            <input type="number" id="<?php echo $this->get_field_id('posts_per_page'); ?>" 
                   name="<?php echo $this->get_field_name('posts_per_page'); ?>" 
                   value="<?php echo esc_attr($posts_per_page); ?>" 
                   min="1" max="20" class="small-text">
        </p>
        <p>
            <label for="<?php echo $this->get_field_id('orderby'); ?>">
                <?php _e('Ordenar por:', 'meu-plugin'); ?>
            </label>
            <select id="<?php echo $this->get_field_id('orderby'); ?>" 
                    name="<?php echo $this->get_field_name('orderby'); ?>" class="widefat">
                <?php foreach ($orderby_options as $key => $label) : ?>
                    <option value="<?php echo $key; ?>" <?php selected($orderby, $key); ?>>
                        <?php echo $label; ?>
                    </option>
                <?php endforeach; ?>
            </select>
        </p>
        <p>
            <select id="<?php echo $this->get_field_id('order'); ?>" 
                    name="<?php echo $this->get_field_name('order'); ?>" class="widefat">
                <option value="DESC" <?php selected($order, 'DESC'); ?>>
                    <?php _e('Descendente', 'meu-plugin'); ?>
                </option>
                <option value="ASC" <?php selected($order, 'ASC'); ?>>
                    <?php _e('Ascendente', 'meu-plugin'); ?>
                </option>
            </select>
        </p>
        <p>
            <input type="checkbox" id="<?php echo $this->get_field_id('show_image'); ?>" 
                   name="<?php echo $this->get_field_name('show_image'); ?>" 
                   value="1" <?php checked($show_image, '1'); ?>>
            <label for="<?php echo $this->get_field_id('show_image'); ?>">
                <?php _e('Exibir imagem destacada', 'meu-plugin'); ?>
            </label>
        </p>
        <p>
            <input type="checkbox" id="<?php echo $this->get_field_id('show_excerpt'); ?>" 
                   name="<?php echo $this->get_field_name('show_excerpt'); ?>" 
                   value="1" <?php checked($show_excerpt, '1'); ?>>
            <label for="<?php echo $this->get_field_id('show_excerpt'); ?>">
                <?php _e('Exibir resumo', 'meu-plugin'); ?>
            </label>
        </p>
        <?php
    }
    
    public function update($new_instance, $old_instance) {
        $instance = array();
        $instance['title'] = sanitize_text_field($new_instance['title']);
        $instance['post_type'] = sanitize_key($new_instance['post_type']);
        $instance['posts_per_page'] = intval($new_instance['posts_per_page']);
        $instance['orderby'] = sanitize_key($new_instance['orderby']);
        $instance['order'] = $new_instance['order'] === 'ASC' ? 'ASC' : 'DESC';
        $instance['show_image'] = !empty($new_instance['show_image']) ? '1' : '0';
        $instance['show_excerpt'] = !empty($new_instance['show_excerpt']) ? '1' : '0';
        return $instance;
    }
}
```

---

## 7. CUSTOM POST TYPES E TAXONOMIAS

### 7.1 Registro de CPT em Plugin

```php
<?php
// Registrar CPT com suporte a Gutenberg
function meu_plugin_register_cpt() {
    $labels = array(
        'name' => __('Produtos', 'meu-plugin'),
        'singular_name' => __('Produto', 'meu-plugin'),
        'menu_name' => __('Produtos', 'meu-plugin'),
        'add_new' => __('Adicionar Novo', 'meu-plugin'),
        'add_new_item' => __('Adicionar Novo Produto', 'meu-plugin'),
        'edit_item' => __('Editar Produto', 'meu-plugin'),
        'new_item' => __('Novo Produto', 'meu-plugin'),
        'view_item' => __('Ver Produto', 'meu-plugin'),
        'search_items' => __('Buscar Produtos', 'meu-plugin'),
        'not_found' => __('Nenhum produto encontrado', 'meu-plugin'),
        'not_found_in_trash' => __('Nenhum produto na lixeira', 'meu-plugin'),
    );
    
    $args = array(
        'labels' => $labels,
        'public' => true,
        'publicly_queryable' => true,
        'show_ui' => true,
        'show_in_menu' => true,
        'query_var' => true,
        'rewrite' => array('slug' => 'produtos', 'with_front' => false),
        'capability_type' => 'post',
        'has_archive' => true,
        'hierarchical' => false,
        'menu_position' => 5,
        'menu_icon' => 'dashicons-cart',
        'supports' => array('title', 'editor', 'thumbnail', 'excerpt', 'revisions'),
        'show_in_rest' => true, // Gutenberg
        'rest_base' => 'produtos',
    );
    
    register_post_type('produto', $args);
}
add_action('init', 'meu_plugin_register_cpt');

// Registrar taxonomia
function meu_plugin_register_taxonomies() {
    $labels = array(
        'name' => __('Categorias de Produtos', 'meu-plugin'),
        'singular_name' => __('Categoria', 'meu-plugin'),
        'search_items' => __('Buscar Categorias', 'meu-plugin'),
        'all_items' => __('Todas Categorias', 'meu-plugin'),
        'parent_item' => __('Categoria Pai', 'meu-plugin'),
        'parent_item_colon' => __('Categoria Pai:', 'meu-plugin'),
        'edit_item' => __('Editar Categoria', 'meu-plugin'),
        'update_item' => __('Atualizar Categoria', 'meu-plugin'),
        'add_new_item' => __('Adicionar Nova Categoria', 'meu-plugin'),
        'new_item_name' => __('Nova Categoria', 'meu-plugin'),
        'menu_name' => __('Categorias', 'meu-plugin'),
    );
    
    $args = array(
        'labels' => $labels,
        'hierarchical' => true,
        'public' => true,
        'show_ui' => true,
        'show_admin_column' => true,
        'query_var' => true,
        'rewrite' => array('slug' => 'categoria-produto'),
        'show_in_rest' => true,
    );
    
    register_taxonomy('produto_categoria', array('produto'), $args);
}
add_action('init', 'meu_plugin_register_taxonomies');
```

---

## 8. APIS REST PERSONALIZADAS

### 8.1 Criar Endpoints REST

```php
<?php
// Registrar endpoints REST
add_action('rest_api_init', 'meu_plugin_register_rest_routes');

function meu_plugin_register_rest_routes() {
    register_rest_route('meu-plugin/v1', '/items', array(
        'methods' => 'GET',
        'callback' => 'meu_plugin_get_items',
        'permission_callback' => '__return_true',
        'args' => array(
            'page' => array(
                'validate_callback' => function($param) {
                    return is_numeric($param);
                },
                'default' => 1,
            ),
            'per_page' => array(
                'validate_callback' => function($param) {
                    return is_numeric($param) && $param <= 100;
                },
                'default' => 10,
            ),
        ),
    ));
    
    register_rest_route('meu-plugin/v1', '/items/(?P<id>\d+)', array(
        'methods' => 'GET',
        'callback' => 'meu_plugin_get_item',
        'permission_callback' => '__return_true',
        'args' => array(
            'id' => array(
                'validate_callback' => function($param) {
                    return is_numeric($param);
                },
            ),
        ),
    ));
    
    register_rest_route('meu-plugin/v1', '/items', array(
        'methods' => 'POST',
        'callback' => 'meu_plugin_create_item',
        'permission_callback' => 'meu_plugin_check_admin_permission',
        'args' => array(
            'title' => array(
                'required' => true,
                'validate_callback' => function($param) {
                    return !empty($param);
                },
            ),
            'content' => array(
                'required' => true,
            ),
        ),
    ));
}

function meu_plugin_get_items($request) {
    global $wpdb;
    
    $page = $request->get_param('page');
    $per_page = $request->get_param('per_page');
    $offset = ($page - 1) * $per_page;
    
    $table_name = $wpdb->prefix . 'meu_plugin_items';
    
    $items = $wpdb->get_results($wpdb->prepare("
        SELECT * FROM $table_name 
        LIMIT %d OFFSET %d
    ", $per_page, $offset));
    
    $total = $wpdb->get_var("SELECT COUNT(*) FROM $table_name");
    
    $response = new WP_REST_Response($items);
    $response->header('X-WP-Total', $total);
    $response->header('X-WP-TotalPages', ceil($total / $per_page));
    
    return $response;
}

function meu_plugin_get_item($request) {
    global $wpdb;
    $id = $request->get_param('id');
    
    $table_name = $wpdb->prefix . 'meu_plugin_items';
    $item = $wpdb->get_row($wpdb->prepare("SELECT * FROM $table_name WHERE id = %d", $id));
    
    if (!$item) {
        return new WP_Error('not_found', 'Item não encontrado', array('status' => 404));
    }
    
    return rest_ensure_response($item);
}

function meu_plugin_create_item($request) {
    global $wpdb;
    
    $title = sanitize_text_field($request->get_param('title'));
    $content = wp_kses_post($request->get_param('content'));
    
    $table_name = $wpdb->prefix . 'meu_plugin_items';
    
    $inserted = $wpdb->insert(
        $table_name,
        array(
            'title' => $title,
            'content' => $content,
            'created_at' => current_time('mysql'),
        ),
        array('%s', '%s', '%s')
    );
    
    if (!$inserted) {
        return new WP_Error('insert_error', 'Erro ao criar item', array('status' => 500));
    }
    
    $item_id = $wpdb->insert_id;
    $item = $wpdb->get_row($wpdb->prepare("SELECT * FROM $table_name WHERE id = %d", $item_id));
    
    return rest_ensure_response($item);
}

function meu_plugin_check_admin_permission() {
    return current_user_can('manage_options');
}
```

---

## 9. BANCO DE DADOS EM PLUGINS

### 9.1 Estrutura de Tabelas

```php
<?php
// Criar tabelas na ativação
register_activation_hook(__FILE__, 'meu_plugin_create_tables');

function meu_plugin_create_tables() {
    global $wpdb;
    
    $charset_collate = $wpdb->get_charset_collate();
    
    // Tabela de itens
    $table_items = $wpdb->prefix . 'meu_plugin_items';
    $sql_items = "CREATE TABLE IF NOT EXISTS $table_items (
        id bigint(20) NOT NULL AUTO_INCREMENT,
        title varchar(255) NOT NULL,
        content longtext NOT NULL,
        status varchar(20) DEFAULT 'draft',
        created_at datetime DEFAULT CURRENT_TIMESTAMP,
        updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        KEY status (status),
        KEY created_at (created_at)
    ) $charset_collate;";
    
    // Tabela de metadados
    $table_meta = $wpdb->prefix . 'meu_plugin_meta';
    $sql_meta = "CREATE TABLE IF NOT EXISTS $table_meta (
        id bigint(20) NOT NULL AUTO_INCREMENT,
        item_id bigint(20) NOT NULL,
        meta_key varchar(255) NOT NULL,
        meta_value longtext,
        PRIMARY KEY (id),
        KEY item_id (item_id),
        KEY meta_key (meta_key)
    ) $charset_collate;";
    
    // Tabela de logs
    $table_logs = $wpdb->prefix . 'meu_plugin_logs';
    $sql_logs = "CREATE TABLE IF NOT EXISTS $table_logs (
        id bigint(20) NOT NULL AUTO_INCREMENT,
        user_id bigint(20) DEFAULT 0,
        action varchar(100) NOT NULL,
        data longtext,
        ip_address varchar(45),
        created_at datetime DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        KEY user_id (user_id),
        KEY action (action),
        KEY created_at (created_at)
    ) $charset_collate;";
    
    require_once ABSPATH . 'wp-admin/includes/upgrade.php';
    dbDelta($sql_items);
    dbDelta($sql_meta);
    dbDelta($sql_logs);
    
    // Opção de versão do banco
    add_option('meu_plugin_db_version', '1.0.0');
}

// Atualizar tabelas quando necessário
add_action('plugins_loaded', 'meu_plugin_update_db');

function meu_plugin_update_db() {
    $current_version = get_option('meu_plugin_db_version', '0');
    
    if (version_compare($current_version, '1.1.0', '<')) {
        // Atualizações para versão 1.1.0
        global $wpdb;
        $table_items = $wpdb->prefix . 'meu_plugin_items';
        $wpdb->query("ALTER TABLE $table_items ADD COLUMN user_id bigint(20) DEFAULT 0 AFTER content");
        update_option('meu_plugin_db_version', '1.1.0');
    }
}
```

### 9.2 Funções de CRUD

```php
<?php
// CRUD para itens
class Meu_Plugin_DB {
    
    private static $table_items;
    private static $table_meta;
    
    public static function init() {
        global $wpdb;
        self::$table_items = $wpdb->prefix . 'meu_plugin_items';
        self::$table_meta = $wpdb->prefix . 'meu_plugin_meta';
    }
    
    // Create
    public static function create_item($data) {
        global $wpdb;
        
        $defaults = array(
            'title' => '',
            'content' => '',
            'status' => 'draft',
            'user_id' => get_current_user_id(),
        );
        
        $data = wp_parse_args($data, $defaults);
        
        $result = $wpdb->insert(
            self::$table_items,
            array(
                'title' => sanitize_text_field($data['title']),
                'content' => wp_kses_post($data['content']),
                'status' => sanitize_key($data['status']),
                'user_id' => intval($data['user_id']),
            ),
            array('%s', '%s', '%s', '%d')
        );
        
        if (!$result) {
            return false;
        }
        
        return $wpdb->insert_id;
    }
    
    // Read (single)
    public static function get_item($id) {
        global $wpdb;
        
        $item = $wpdb->get_row($wpdb->prepare(
            "SELECT * FROM " . self::$table_items . " WHERE id = %d",
            $id
        ));
        
        if ($item) {
            $item->meta = self::get_meta($id);
        }
        
        return $item;
    }
    
    // Read (multiple)
    public static function get_items($args = array()) {
        global $wpdb;
        
        $defaults = array(
            'status' => 'publish',
            'user_id' => 0,
            'orderby' => 'created_at',
            'order' => 'DESC',
            'limit' => 20,
            'offset' => 0,
        );
        
        $args = wp_parse_args($args, $defaults);
        $where = array();
        $values = array();
        
        if ($args['status'] !== 'all') {
            $where[] = "status = %s";
            $values[] = sanitize_key($args['status']);
        }
        
        if ($args['user_id'] > 0) {
            $where[] = "user_id = %d";
            $values[] = intval($args['user_id']);
        }
        
        $where_sql = !empty($where) ? "WHERE " . implode(" AND ", $where) : "";
        $order_sql = "ORDER BY {$args['orderby']} {$args['order']}";
        $limit_sql = "LIMIT %d OFFSET %d";
        
        $values[] = intval($args['limit']);
        $values[] = intval($args['offset']);
        
        $sql = $wpdb->prepare(
            "SELECT * FROM " . self::$table_items . " $where_sql $order_sql $limit_sql",
            $values
        );
        
        $items = $wpdb->get_results($sql);
        
        foreach ($items as $item) {
            $item->meta = self::get_meta($item->id);
        }
        
        // Contar total
        $count_sql = "SELECT COUNT(*) FROM " . self::$table_items . " $where_sql";
        if (!empty($values)) {
            // Remover os valores de limit/offset
            array_pop($values);
            array_pop($values);
            $total = $wpdb->get_var($wpdb->prepare($count_sql, $values));
        } else {
            $total = $wpdb->get_var($count_sql);
        }
        
        return array(
            'items' => $items,
            'total' => intval($total),
        );
    }
    
    // Update
    public static function update_item($id, $data) {
        global $wpdb;
        
        $update_data = array();
        $update_format = array();
        
        $allowed_fields = array('title', 'content', 'status');
        foreach ($allowed_fields as $field) {
            if (isset($data[$field])) {
                $update_data[$field] = $data[$field];
                $update_format[] = '%s';
            }
        }
        
        if (empty($update_data)) {
            return false;
        }
        
        $result = $wpdb->update(
            self::$table_items,
            $update_data,
            array('id' => $id),
            $update_format,
            array('%d')
        );
        
        return $result !== false;
    }
    
    // Delete
    public static function delete_item($id) {
        global $wpdb;
        
        // Deletar metadados primeiro
        self::delete_meta($id);
        
        $result = $wpdb->delete(
            self::$table_items,
            array('id' => $id),
            array('%d')
        );
        
        return $result !== false;
    }
    
    // Meta functions
    public static function add_meta($item_id, $meta_key, $meta_value) {
        global $wpdb;
        
        return $wpdb->insert(
            self::$table_meta,
            array(
                'item_id' => $item_id,
                'meta_key' => $meta_key,
                'meta_value' => maybe_serialize($meta_value),
            ),
            array('%d', '%s', '%s')
        );
    }
    
    public static function get_meta($item_id, $meta_key = null) {
        global $wpdb;
        
        if ($meta_key) {
            $result = $wpdb->get_var($wpdb->prepare(
                "SELECT meta_value FROM " . self::$table_meta . " 
                 WHERE item_id = %d AND meta_key = %s",
                $item_id, $meta_key
            ));
            return maybe_unserialize($result);
        }
        
        $results = $wpdb->get_results($wpdb->prepare(
            "SELECT meta_key, meta_value FROM " . self::$table_meta . " 
             WHERE item_id = %d",
            $item_id
        ), ARRAY_A);
        
        $meta = array();
        foreach ($results as $row) {
            $meta[$row['meta_key']] = maybe_unserialize($row['meta_value']);
        }
        
        return $meta;
    }
    
    public static function update_meta($item_id, $meta_key, $meta_value) {
        global $wpdb;
        
        $exists = $wpdb->get_var($wpdb->prepare(
            "SELECT COUNT(*) FROM " . self::$table_meta . " 
             WHERE item_id = %d AND meta_key = %s",
            $item_id, $meta_key
        ));
        
        if ($exists) {
            return $wpdb->update(
                self::$table_meta,
                array('meta_value' => maybe_serialize($meta_value)),
                array('item_id' => $item_id, 'meta_key' => $meta_key),
                array('%s'),
                array('%d', '%s')
            );
        } else {
            return self::add_meta($item_id, $meta_key, $meta_value);
        }
    }
    
    public static function delete_meta($item_id, $meta_key = null) {
        global $wpdb;
        
        if ($meta_key) {
            return $wpdb->delete(
                self::$table_meta,
                array('item_id' => $item_id, 'meta_key' => $meta_key),
                array('%d', '%s')
            );
        } else {
            return $wpdb->delete(
                self::$table_meta,
                array('item_id' => $item_id),
                array('%d')
            );
        }
    }
}

// Inicializar
Meu_Plugin_DB::init();
```

---

## 10. INTERNACIONALIZAÇÃO (i18n)

### 10.1 Preparando o Plugin para Tradução

```php
<?php
// No arquivo principal
add_action('plugins_loaded', 'meu_plugin_load_textdomain');

function meu_plugin_load_textdomain() {
    load_plugin_textdomain(
        'meu-plugin',
        false,
        dirname(plugin_basename(__FILE__)) . '/languages'
    );
}

// Uso das funções de tradução
function meu_plugin_example() {
    // __() - Retorna string traduzida
    $title = __('Meu Plugin', 'meu-plugin');
    
    // _e() - Exibe string traduzida
    _e('Olá Mundo', 'meu-plugin');
    
    // _n() - Pluralização
    $count = 5;
    $message = _n(
        'Existe %d item',           // Singular
        'Existem %d itens',         // Plural
        $count,                     // Número
        'meu-plugin'                // Domínio
    );
    echo sprintf($message, $count);
    
    // _x() - Contexto
    $label = _x(
        'Date',                     // Texto
        'Post date',                // Contexto
        'meu-plugin'                // Domínio
    );
    
    // _ex() - Exibe com contexto
    _ex('Read', 'Read more link', 'meu-plugin');
    
    // esc_html__() - Escapa e traduz
    $safe_title = esc_html__('Título', 'meu-plugin');
    
    // esc_attr__() - Escapa atributo e traduz
    $placeholder = esc_attr__('Digite seu nome', 'meu-plugin');
}
```

### 10.2 Gerando Arquivos .pot

```bash
# Comando WP-CLI para gerar arquivo .pot
wp i18n make-pot . languages/meu-plugin.pot --slug=meu-plugin

# Extrair strings manualmente (Linux)
find . -name "*.php" | xargs xgettext --from-code=UTF-8 -o languages/meu-plugin.pot

# Criar arquivo .po para português
msginit -i languages/meu-plugin.pot -o languages/meu-plugin-pt_BR.po -l pt_BR.UTF-8

# Compilar .po para .mo
msgfmt languages/meu-plugin-pt_BR.po -o languages/meu-plugin-pt_BR.mo
```

---

## 11. SEGURANÇA EM PLUGINS

### 11.1 Validação e Sanitização

```php
<?php
// Validação de dados de entrada
function meu_plugin_validate_input($input) {
    // Sanitizar campos de texto
    $sanitized = array();
    
    if (isset($input['name'])) {
        $sanitized['name'] = sanitize_text_field($input['name']);
    }
    
    if (isset($input['email'])) {
        $sanitized['email'] = sanitize_email($input['email']);
    }
    
    if (isset($input['url'])) {
        $sanitized['url'] = esc_url_raw($input['url']);
    }
    
    if (isset($input['color'])) {
        $sanitized['color'] = sanitize_hex_color($input['color']);
    }
    
    if (isset($input['html'])) {
        $sanitized['html'] = wp_kses_post($input['html']);
    }
    
    if (isset($input['integer'])) {
        $sanitized['integer'] = intval($input['integer']);
    }
    
    if (isset($input['checkbox'])) {
        $sanitized['checkbox'] = $input['checkbox'] ? '1' : '0';
    }
    
    return $sanitized;
}

// Nonce para segurança
function meu_plugin_form_handler() {
    // Verificar nonce
    if (!isset($_POST['meu_plugin_nonce']) || 
        !wp_verify_nonce($_POST['meu_plugin_nonce'], 'meu_plugin_action')) {
        wp_die('Ação não autorizada');
    }
    
    // Verificar capacidade
    if (!current_user_can('manage_options')) {
        wp_die('Permissão negada');
    }
    
    // Processar formulário
    $data = meu_plugin_validate_input($_POST);
    update_option('meu_plugin_options', $data);
    
    wp_redirect(add_query_arg('updated', 'true', wp_get_referer()));
    exit;
}
add_action('admin_post_meu_plugin_save', 'meu_plugin_form_handler');
```

### 11.2 Prevenção de SQL Injection

```php
<?php
// Consultas seguras com $wpdb
global $wpdb;

// Usando prepare()
$id = 5;
$name = "João";

$result = $wpdb->get_results($wpdb->prepare(
    "SELECT * FROM {$wpdb->prefix}my_table WHERE id = %d AND name = %s",
    $id,
    $name
));

// Inserção segura
$wpdb->insert(
    $wpdb->prefix . 'my_table',
    array(
        'name' => $name,
        'email' => $email,
    ),
    array('%s', '%s')
);

// Atualização segura
$wpdb->update(
    $wpdb->prefix . 'my_table',
    array('name' => $new_name),
    array('id' => $id),
    array('%s'),
    array('%d')
);

// Nunca fazer:
// $wpdb->query("SELECT * FROM {$wpdb->prefix}table WHERE id = $id");
```

### 11.3 Escapando Saída

```php
<?php
// Escapar saída corretamente

// HTML
echo '<h1>' . esc_html($title) . '</h1>';
echo '<div>' . wp_kses_post($content) . '</div>';

// Atributos
echo '<input type="text" value="' . esc_attr($value) . '">';
echo '<a href="' . esc_url($url) . '">Link</a>';
echo '<img src="' . esc_url_raw($image_url) . '">';

// JavaScript
echo '<script>var data = ' . wp_json_encode($data) . ';</script>';

// SQL
$wpdb->prepare("SELECT * FROM table WHERE id = %d", $id);
```

### 11.4 Validação de Capacidades

```php
<?php
// Verificar permissões
function meu_plugin_check_capabilities() {
    if (!current_user_can('manage_options')) {
        wp_die(__('Você não tem permissão para acessar esta página.', 'meu-plugin'));
    }
}

// Verificar se é administrador
if (current_user_can('administrator')) {
    // Código para admin
}

// Verificar se é editor ou superior
if (current_user_can('edit_others_posts')) {
    // Código para editores
}

// Verificar permissões específicas
if (current_user_can('meu_plugin_custom_capability')) {
    // Código
}

// Adicionar capacidade customizada
add_action('admin_init', 'meu_plugin_add_caps');
function meu_plugin_add_caps() {
    $role = get_role('administrator');
    $role->add_cap('meu_plugin_manage');
}

// Uso
if (current_user_can('meu_plugin_manage')) {
    // Exibir menu admin
}
```

---

## 12. TESTES E DEBUGGING

### 12.1 Debug com WP_DEBUG

```php
<?php
// Ativar debug no wp-config.php
define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);
define('WP_DEBUG_DISPLAY', false);
define('SCRIPT_DEBUG', true);

// Logs
function meu_plugin_log($message, $type = 'info') {
    if (defined('WP_DEBUG') && WP_DEBUG) {
        $log_message = sprintf(
            '[%s] [%s] %s',
            current_time('mysql'),
            strtoupper($type),
            print_r($message, true)
        );
        
        error_log($log_message);
    }
}

// Uso
meu_plugin_log('Plugin inicializado');
meu_plugin_log($data, 'debug');
```

### 12.2 Testes Unitários com PHPUnit

```php
<?php
// tests/bootstrap.php
<?php
$_tests_dir = getenv('WP_TESTS_DIR');
if (!$_tests_dir) {
    $_tests_dir = '/tmp/wordpress-tests-lib';
}

require_once $_tests_dir . '/includes/functions.php';

function _manually_load_plugin() {
    require dirname(__DIR__) . '/meu-plugin.php';
}
tests_add_filter('muplugins_loaded', '_manually_load_plugin');

require $_tests_dir . '/includes/bootstrap.php';

// tests/test-sample.php
class SampleTest extends WP_UnitTestCase {
    
    public function setUp() {
        parent::setUp();
        // Setup antes de cada teste
    }
    
    public function tearDown() {
        // Cleanup após cada teste
        parent::tearDown();
    }
    
    public function test_plugin_activated() {
        $this->assertTrue(is_plugin_active('meu-plugin/meu-plugin.php'));
    }
    
    public function test_cpt_registered() {
        $this->assertTrue(post_type_exists('meu_cpt'));
    }
    
    public function test_shortcode_exists() {
        $this->assertTrue(shortcode_exists('meu_shortcode'));
    }
    
    public function test_database_table_created() {
        global $wpdb;
        $table_name = $wpdb->prefix . 'meu_plugin_items';
        $this->assertEquals($table_name, $wpdb->get_var("SHOW TABLES LIKE '$table_name'"));
    }
    
    public function test_add_item() {
        $id = meu_plugin_create_item('Teste', 'Conteúdo');
        $this->assertGreaterThan(0, $id);
        
        $item = get_post($id);
        $this->assertEquals('Teste', $item->post_title);
    }
}

// Executar testes
// phpunit
```

---

## 13. BOAS PRÁTICAS E PADRÕES

### 13.1 Padrões de Código WordPress

```php
<?php
// 1. Nomenclatura
// Prefixar tudo (funções, classes, variáveis)
$my_plugin_option = get_option('my_plugin_option');

function my_plugin_do_something() {}

class My_Plugin_Class {}

// 2. Documentação
/**
 * Breve descrição do que a função faz.
 *
 * Descrição mais detalhada se necessário.
 *
 * @since 1.0.0
 * @param string $param1 Descrição do parâmetro
 * @param int    $param2 Descrição do parâmetro
 * @return string|bool Descrição do retorno
 */
function my_plugin_function($param1, $param2 = 0) {
    // Código
}

// 3. Espaçamento
// Corrigir:
if ($condition) {
    do_something();
}

// Errado:
if($condition){
    do_something();
}

// 4. Chaves
// Corrigir:
function my_function() {
    // código
}

// Errado:
function my_function(){
    // código
}

// 5. Abreviações
// Evitar abreviações desnecessárias
$description = '';  // Bom
$desc = '';         // Ruim
```

### 13.2 Estrutura de Arquivos PSR-4

```php
<?php
// composer.json
{
    "name": "meu-plugin/meu-plugin",
    "description": "Descrição do plugin",
    "type": "wordpress-plugin",
    "require": {
        "php": ">=7.4"
    },
    "autoload": {
        "psr-4": {
            "MeuPlugin\\": "includes/"
        }
    }
}

// Executar composer dump-autoload

// includes/Admin/AdminPage.php
namespace MeuPlugin\Admin;

class AdminPage {
    public function render() {
        // Código
    }
}

// meu-plugin.php
require_once __DIR__ . '/vendor/autoload.php';

use MeuPlugin\Admin\AdminPage;

$admin_page = new AdminPage();
```

### 13.3 Checklist de Publicação

```text
CHECKLIST PARA PUBLICAR PLUGIN:

CÓDIGO:
├── Prefixar todas as funções, classes e variáveis
├── Verificar se há conflitos de nome
├── Documentar todas as funções
├── Usar WordPress Coding Standards
├── Remover debug codes (var_dump, error_log)
├── Verificar compatibilidade com versões recentes
└── Testar com WordPress Debug ativado

SEGURANÇA:
├── Escapar todas as saídas (esc_html, esc_attr, etc.)
├── Validar todas as entradas
├── Usar nonces em formulários
├── Verificar capacidades do usuário
├── Usar prepared statements no banco
└── Sanitizar antes de salvar no banco

INTERNACIONALIZAÇÃO:
├── Usar __(), _e(), _n(), etc.
├── Gerar arquivo .pot
├── Testar com outros idiomas
└── Configurar Domain Path

INSTALAÇÃO/ATIVAÇÃO:
├── Criar tabelas no activation hook
├── Configurar opções padrão
├── Criar roles/capacidades se necessário
├── Limpar rewrite rules
└── Registrar uninstall hook

TESTES:
├── Testar em PHP 7.4, 8.0, 8.1, 8.2
├── Testar em WordPress versões recentes
├── Testar em diferentes temas (padrão e personalizado)
├── Testar com e sem outros plugins
├── Testar em multisite
├── Testar em diferentes navegadores
└── Testar em dispositivos móveis

DOCUMENTAÇÃO:
├── readme.txt completo
├── Documentação no código
├── FAQ no readme
├── Screenshots (mínimo 4)
├── Changelog detalhado
└── Exemplos de uso

README.TXT (WordPress.org):
=== Plugin Name ===
Contributors: username
Tags: tag1, tag2, tag3
Requires at least: 5.0
Tested up to: 6.4
Stable tag: 1.0.0
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

== Description ==
Descrição do plugin...

== Installation ==
1. Faça upload do plugin para /wp-content/plugins/
2. Ative o plugin
3. Configure em Configurações > Meu Plugin

== Frequently Asked Questions ==
= Pergunta 1 =
Resposta 1

== Screenshots ==
1. Tela principal do plugin
2. Tela de configurações

== Changelog ==
= 1.0.0 =
* Versão inicial

== Upgrade Notice ==
= 1.0.0 =
Versão inicial
```

---

## 14. PUBLICAÇÃO NO WORDPRESS.ORG

### 14.1 Preparação para Submissão

```bash
# 1. Verificar código com PHP_CodeSniffer
phpcs --standard=WordPress meu-plugin/

# 2. Corrigir problemas
phpcbf --standard=WordPress meu-plugin/

# 3. Testar com Plugin Check
# Instalar Plugin Check no WordPress

# 4. Preparar arquivos para envio
zip -r meu-plugin.zip meu-plugin/ -x "*.git*" "*.DS_Store" "node_modules/*" "tests/*"

# 5. Submeter via WordPress.org
# Acessar: https://wordpress.org/plugins/developers/add/
```

### 14.2 Submissão via SVN

```bash
# Checkout do repositório SVN
svn co https://plugins.svn.wordpress.org/meu-plugin

# Criar estrutura
cd meu-plugin
mkdir trunk
mkdir tags

# Copiar arquivos
cp -r /caminho/do/plugin/* trunk/

# Adicionar arquivos
svn add trunk/*

# Commit
svn ci -m "Versão inicial 1.0.0"

# Criar tag
svn cp trunk tags/1.0.0
svn ci -m "Tag versão 1.0.0"
```

---

# 🐳 WORDPRESS EM DOCKER - GUIA COMPLETO

## 📚 SUMÁRIO DOCKER

1. [Introdução ao Docker](#1-introdução-ao-docker)
2. [Instalação do Docker](#2-instalação-do-docker)
3. [WordPress com Docker Compose](#3-wordpress-com-docker-compose)
4. [Configurações Avançadas](#4-configurações-avançadas)
5. [Ambiente de Desenvolvimento](#5-ambiente-de-desenvolvimento)
6. [Gerenciamento de Contêineres](#6-gerenciamento-de-contêineres)
7. [Backup e Restauração](#7-backup-e-restauração)
8. [Performance e Otimização](#8-performance-e-otimização)
9. [Segurança em Docker](#9-segurança-em-docker)
10. [Deploy em Produção](#10-deploy-em-produção)

---

## 1. INTRODUÇÃO AO DOCKER

### 1.1 Conceitos Fundamentais

```text
DOCKER = Plataforma de containerização

CONCEITOS:
├── IMAGEM: Template com aplicação e dependências
├── CONTAINER: Instância em execução de uma imagem
├── DOCKERFILE: Script para construir imagens
├── DOCKER COMPOSE: Orquestração de múltiplos containers
├── VOLUME: Persistência de dados
└── NETWORK: Rede entre containers

BENEFÍCIOS PARA WORDPRESS:
├── Ambiente isolado e consistente
├── Fácil replicação entre dev/staging/prod
├── Sem necessidade de configurar PHP/MySQL localmente
├── Permite testar diferentes versões facilmente
├── Isolamento de projetos
└── Facilidade para compartilhar configurações
```

### 1.2 Arquitetura WordPress em Docker

```text
┌─────────────────────────────────────────────────────────────┐
│                     DOCKER HOST                             │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐                   │
│  │   CONTAINER     │  │   CONTAINER     │                   │
│  │   WORDPRESS     │  │    MYSQL        │                   │
│  │                 │  │                 │                   │
│  │  - Apache/Nginx │  │  - MySQL 8.0    │                   │
│  │  - PHP 8.x      │  │  - MariaDB      │                   │
│  │  - WordPress    │  │                 │                   │
│  └────────┬────────┘  └────────┬────────┘                   │
│           │                    │                            │
│           └────────┬───────────┘                            │
│                    │                                         │
│           ┌────────▼────────┐                               │
│           │    VOLUME       │                               │
│           │  /var/www/html  │                               │
│           │  /var/lib/mysql │                               │
│           └─────────────────┘                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. INSTALAÇÃO DO DOCKER

### 2.1 Ubuntu/Debian

```bash
# Atualizar sistema
sudo apt update
sudo apt upgrade -y

# Instalar dependências
sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Adicionar chave GPG do Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Adicionar repositório
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker Engine
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Adicionar usuário ao grupo docker (evitar sudo)
sudo usermod -aG docker $USER

# Verificar instalação
docker --version
docker compose version

# Reiniciar sessão ou executar:
newgrp docker
```

### 2.2 Windows (WSL2)

```bash
# 1. Instalar WSL2
wsl --install

# 2. Baixar Docker Desktop para Windows
# https://www.docker.com/products/docker-desktop

# 3. Instalar Docker Desktop, habilitar WSL2 integration

# 4. Verificar no WSL
wsl
docker --version
```

### 2.3 macOS

```bash
# 1. Baixar Docker Desktop para Mac
# https://www.docker.com/products/docker-desktop

# 2. Instalar

# 3. Verificar
docker --version
```

---

## 3. WORDPRESS COM DOCKER COMPOSE

### 3.1 Docker Compose Básico

```yaml
# docker-compose.yml
version: '3.8'

services:
  # Banco de dados MySQL
  db:
    image: mysql:8.0
    container_name: wordpress_db
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress_password
    volumes:
      - db_data:/var/lib/mysql
    ports:
      - "3306:3306"
    networks:
      - wordpress_network

  # WordPress com PHP-FPM
  wordpress:
    image: wordpress:latest
    container_name: wordpress_app
    restart: unless-stopped
    depends_on:
      - db
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress_password
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DEBUG: 1
      WORDPRESS_CONFIG_EXTRA: |
        define('WP_DEBUG', true);
        define('WP_DEBUG_LOG', true);
        define('WP_DEBUG_DISPLAY', false);
        define('WP_MEMORY_LIMIT', '256M');
    volumes:
      - wordpress_data:/var/www/html
      - ./wp-content:/var/www/html/wp-content
      - ./uploads.ini:/usr/local/etc/php/conf.d/uploads.ini
    networks:
      - wordpress_network

  # Servidor Web (Nginx)
  webserver:
    image: nginx:latest
    container_name: wordpress_nginx
    restart: unless-stopped
    depends_on:
      - wordpress
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - wordpress_data:/var/www/html
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - ./ssl:/etc/nginx/ssl
    networks:
      - wordpress_network

  # phpMyAdmin (opcional)
  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: wordpress_phpmyadmin
    restart: unless-stopped
    depends_on:
      - db
    environment:
      PMA_HOST: db
      PMA_PORT: 3306
      UPLOAD_LIMIT: 100M
    ports:
      - "8080:80"
    networks:
      - wordpress_network

volumes:
  db_data:
  wordpress_data:

networks:
  wordpress_network:
    driver: bridge
```

### 3.2 Configuração Nginx

```nginx
# nginx.conf
server {
    listen 80;
    server_name localhost;
    root /var/www/html;
    index index.php index.html;

    client_max_body_size 100M;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_pass wordpress:9000;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }

    location ~ /\.ht {
        deny all;
    }

    location = /favicon.ico {
        log_not_found off;
        access_log off;
    }

    location = /robots.txt {
        log_not_found off;
        access_log off;
    }

    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires max;
        log_not_found off;
    }
}
```

### 3.3 Configuração PHP Upload

```ini
# uploads.ini
file_uploads = On
memory_limit = 256M
upload_max_filesize = 100M
post_max_size = 100M
max_execution_time = 300
max_input_time = 300
```

---

## 4. CONFIGURAÇÕES AVANÇADAS

### 4.1 Ambiente de Desenvolvimento

```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  db:
    image: mysql:8.0
    container_name: wp_dev_db
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: wordpress_dev
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppass
    ports:
      - "3307:3306"
    volumes:
      - dev_db_data:/var/lib/mysql

  wordpress:
    image: wordpress:latest
    container_name: wp_dev_app
    depends_on:
      - db
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppass
      WORDPRESS_DB_NAME: wordpress_dev
      WORDPRESS_DEBUG: 1
      WORDPRESS_CONFIG_EXTRA: |
        define('WP_DEBUG', true);
        define('WP_DEBUG_LOG', true);
        define('WP_DEBUG_DISPLAY', true);
        define('SCRIPT_DEBUG', true);
        define('SAVEQUERIES', true);
    volumes:
      - ./wp-content:/var/www/html/wp-content
      - ./wp-config.php:/var/www/html/wp-config.php
      - ./uploads.ini:/usr/local/etc/php/conf.d/uploads.ini
    ports:
      - "8000:80"

volumes:
  dev_db_data:
```

### 4.2 WordPress com Versões Específicas

```yaml
# docker-compose.yml
services:
  wordpress:
    image: wordpress:6.4-php8.2
    # ou
    image: wordpress:6.3-php8.1
    # ou
    image: wordpress:php8.0-fpm

  db:
    image: mysql:8.0
    # ou
    image: mariadb:10.11
```

### 4.3 Ambiente Multisite

```yaml
services:
  wordpress:
    environment:
      WORDPRESS_CONFIG_EXTRA: |
        define('WP_ALLOW_MULTISITE', true);
        define('MULTISITE', true);
        define('SUBDOMAIN_INSTALL', false);
        define('DOMAIN_CURRENT_SITE', 'localhost');
        define('PATH_CURRENT_SITE', '/');
        define('SITE_ID_CURRENT_SITE', 1);
        define('BLOG_ID_CURRENT_SITE', 1);
```

---

## 5. AMBIENTE DE DESENVOLVIMENTO

### 5.1 Dockerfile Personalizado

```dockerfile
# Dockerfile
FROM wordpress:php8.2-fpm

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    zip \
    unzip \
    vim \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Instalar WP-CLI
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp

# Instalar Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Instalar Node.js (para desenvolvimento frontend)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Configurar permissões
RUN chown -R www-data:www-data /var/www/html

# Script de inicialização customizado
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["php-fpm"]
```

### 5.2 Script de Entrypoint

```bash
#!/bin/bash
# docker-entrypoint.sh

set -e

# Aguardar banco de dados
echo "Waiting for database..."
while ! nc -z db 3306; do
    sleep 1
done
echo "Database ready!"

# Instalar WordPress se não existir
if [ ! -f /var/www/html/wp-config.php ]; then
    echo "Installing WordPress..."
    wp core download --allow-root
    wp config create \
        --dbname=wordpress \
        --dbuser=wordpress \
        --dbpass=wordpress_password \
        --dbhost=db \
        --allow-root
    wp core install \
        --url="http://localhost" \
        --title="WordPress Dev" \
        --admin_user="admin" \
        --admin_password="admin" \
        --admin_email="admin@example.com" \
        --allow-root
fi

# Executar comando original
exec "$@"
```

### 5.3 Ambiente com Xdebug

```yaml
# docker-compose.dev.yml
services:
  wordpress:
    build:
      context: .
      dockerfile: Dockerfile.dev
    environment:
      XDEBUG_CONFIG: "remote_host=host.docker.internal remote_port=9003"
      PHP_IDE_CONFIG: "serverName=localhost"
    volumes:
      - ./xdebug.ini:/usr/local/etc/php/conf.d/xdebug.ini
```

```ini
# xdebug.ini
zend_extension=xdebug.so
xdebug.mode=debug
xdebug.start_with_request=yes
xdebug.client_host=host.docker.internal
xdebug.client_port=9003
xdebug.idekey=VSCODE
```

---

## 6. GERENCIAMENTO DE CONTÊINERES

### 6.1 Comandos Essenciais

```bash
# Subir containers
docker compose up -d

# Subir com rebuild
docker compose up -d --build

# Ver logs
docker compose logs -f
docker compose logs -f wordpress

# Parar containers
docker compose stop

# Parar e remover
docker compose down

# Parar e remover volumes
docker compose down -v

# Executar comando no container
docker compose exec wordpress wp plugin list
docker compose exec wordpress bash

# Acessar MySQL
docker compose exec db mysql -u wordpress -p

# Backup do banco
docker compose exec db mysqldump -u wordpress -p wordpress > backup.sql

# Restaurar banco
cat backup.sql | docker compose exec -T db mysql -u wordpress -p wordpress
```

### 6.2 Gerenciamento de Volumes

```bash
# Listar volumes
docker volume ls

# Inspecionar volume
docker volume inspect wordpress_db_data

# Remover volumes não utilizados
docker volume prune

# Backup de volume
docker run --rm -v wordpress_db_data:/data -v $(pwd):/backup alpine tar czf /backup/db_backup.tar.gz -C /data .

# Restaurar volume
docker run --rm -v wordpress_db_data:/data -v $(pwd):/backup alpine tar xzf /backup/db_backup.tar.gz -C /data
```

### 6.3 Gerenciamento de Redes

```bash
# Listar redes
docker network ls

# Criar rede
docker network create wordpress_network

# Inspecionar rede
docker network inspect wordpress_network

# Conectar container a rede
docker network connect wordpress_network container_name
```

---

## 7. BACKUP E RESTAURAÇÃO

### 7.1 Script de Backup Automático

```bash
#!/bin/bash
# backup.sh

BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
PROJECT_NAME="wordpress"

mkdir -p $BACKUP_DIR

# Backup do banco de dados
echo "Backup do banco de dados..."
docker compose exec -T db mysqldump -u wordpress -pwordpress_password wordpress > $BACKUP_DIR/${PROJECT_NAME}_db_${DATE}.sql

# Backup dos arquivos
echo "Backup dos arquivos..."
docker compose run --rm -v $(pwd):/source -v $BACKUP_DIR:/backup wordpress tar czf /backup/${PROJECT_NAME}_files_${DATE}.tar.gz -C /source .

# Remover backups antigos (30 dias)
find $BACKUP_DIR -name "*.sql" -mtime +30 -delete
find $BACKUP_DIR -name "*.tar.gz" -mtime +30 -delete

echo "Backup concluído: ${PROJECT_NAME}_${DATE}"
```

### 7.2 Script de Restauração

```bash
#!/bin/bash
# restore.sh

BACKUP_FILE=$1
PROJECT_NAME="wordpress"

if [ -z "$BACKUP_FILE" ]; then
    echo "Uso: ./restore.sh backup_file"
    exit 1
fi

# Restaurar banco
echo "Restaurando banco de dados..."
docker compose exec -T db mysql -u wordpress -pwordpress_password wordpress < $BACKUP_FILE

# Restaurar arquivos
echo "Restaurando arquivos..."
tar xzf $BACKUP_FILE -C .

echo "Restauração concluída!"
```

---

## 8. PERFORMANCE E OTIMIZAÇÃO

### 8.1 Otimizações no Docker Compose

```yaml
services:
  wordpress:
    image: wordpress:php8.2-fpm
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M

  db:
    image: mysql:8.0
    command: --max_allowed_packet=64M --innodb_buffer_pool_size=256M
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
```

### 8.2 Redis para Cache

```yaml
services:
  redis:
    image: redis:alpine
    container_name: wordpress_redis
    restart: unless-stopped
    volumes:
      - redis_data:/data
    networks:
      - wordpress_network

  wordpress:
    environment:
      WORDPRESS_CONFIG_EXTRA: |
        define('WP_REDIS_HOST', 'redis');
        define('WP_REDIS_PORT', 6379);
        define('WP_REDIS_DATABASE', 0);
        define('WP_CACHE', true);
    depends_on:
      - redis
```

### 8.3 Nginx com Cache

```nginx
# nginx.conf com cache
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=wordpress_cache:10m max_size=1g inactive=60m;

server {
    location / {
        proxy_cache wordpress_cache;
        proxy_cache_key "$scheme$request_method$host$request_uri";
        proxy_cache_valid 200 301 302 1h;
        proxy_cache_valid 404 1m;
        add_header X-Cache-Status $upstream_cache_status;
    }
}
```

---

## 9. SEGURANÇA EM DOCKER

### 9.1 Melhores Práticas

```yaml
# docker-compose.prod.yml
services:
  wordpress:
    image: wordpress:php8.2-fpm
    # Usar usuário não-root
    user: www-data
    # Read-only root filesystem
    read_only: true
    # Volumes específicos para escrita
    volumes:
      - wordpress_data:/var/www/html/wp-content
      - wordpress_uploads:/var/www/html/wp-content/uploads
      - /tmp
    # Security options
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE

  db:
    image: mysql:8.0
    # Variáveis sensíveis via secrets
    secrets:
      - db_password
    environment:
      MYSQL_ROOT_PASSWORD_FILE: /run/secrets/db_root_password
      MYSQL_PASSWORD_FILE: /run/secrets/db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### 9.2 Firewall com iptables

```bash
# Restringir acesso ao MySQL
iptables -A INPUT -p tcp --dport 3306 -s 172.16.0.0/12 -j ACCEPT
iptables -A INPUT -p tcp --dport 3306 -j DROP

# Restringir acesso ao phpMyAdmin
iptables -A INPUT -p tcp --dport 8080 -s 192.168.1.0/24 -j ACCEPT
iptables -A INPUT -p tcp --dport 8080 -j DROP
```

---

## 10. DEPLOY EM PRODUÇÃO

### 10.1 Docker Compose para Produção

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  db:
    image: mysql:8.0
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - internal

  wordpress:
    image: wordpress:php8.2-fpm
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: ${MYSQL_USER}
      WORDPRESS_DB_PASSWORD: ${MYSQL_PASSWORD}
      WORDPRESS_DB_NAME: ${MYSQL_DATABASE}
      WORDPRESS_DEBUG: 0
    volumes:
      - wordpress_data:/var/www/html
    networks:
      - internal
    depends_on:
      - db

  webserver:
    image: nginx:alpine
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - wordpress_data:/var/www/html
      - ./nginx/conf.d:/etc/nginx/conf.d
      - ./ssl:/etc/nginx/ssl
    networks:
      - internal
      - web
    depends_on:
      - wordpress

volumes:
  db_data:
  wordpress_data:

networks:
  internal:
    internal: true
  web:
    driver: bridge
```

### 10.2 .env para Variáveis Sensíveis

```bash
# .env
MYSQL_ROOT_PASSWORD=supersecretpassword
MYSQL_DATABASE=wordpress_prod
MYSQL_USER=wpuser
MYSQL_PASSWORD=wppassword123
```

### 10.3 Script de Deploy

```bash
#!/bin/bash
# deploy.sh

set -e

echo "Iniciando deploy..."

# Pull das imagens mais recentes
docker compose -f docker-compose.prod.yml pull

# Parar containers
docker compose -f docker-compose.prod.yml stop

# Backup automático
./backup.sh

# Subir novos containers
docker compose -f docker-compose.prod.yml up -d

# Limpar imagens não utilizadas
docker image prune -f

echo "Deploy concluído!"
```

---

## 📊 TABELA RESUMO - COMANDOS DOCKER

| Comando | Descrição |
|---------|-----------|
| `docker compose up -d` | Iniciar containers em background |
| `docker compose down` | Parar e remover containers |
| `docker compose logs -f` | Ver logs em tempo real |
| `docker compose exec wordpress bash` | Acessar shell do container |
| `docker compose exec db mysql -u wordpress -p` | Acessar MySQL |
| `docker compose exec wordpress wp plugin list` | Executar WP-CLI |
| `docker volume ls` | Listar volumes |
| `docker network ls` | Listar redes |

---

## 🎯 CONCLUSÃO

Este guia completo cobre desde os fundamentos de desenvolvimento de plugins WordPress até a criação de ambientes profissionais com Docker. Com essas ferramentas, você pode:

1. **Criar plugins profissionais** com estrutura moderna, segurança e internacionalização
2. **Desenvolver localmente** com Docker sem configurar PHP/MySQL manualmente
3. **Testar diferentes versões** do WordPress, PHP e MySQL facilmente
4. **Reproduzir ambientes** de desenvolvimento, staging e produção consistentes
5. **Implantar em produção** com segurança e facilidade

**Próximos passos:**
- Pratique criando um plugin simples com shortcodes
- Configure seu ambiente Docker local
- Teste com diferentes versões do WordPress
- Publique seu primeiro plugin no WordPress.org
- Implemente CI/CD com GitHub Actions e Docker

---

*Mantenha seus plugins atualizados, siga as boas práticas de segurança e participe da comunidade WordPress!*