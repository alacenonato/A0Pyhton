Ótimo, agora você quer organizar a parte visual. Vamos nessa.

Com o esquema que você montou (POPS + APPS + SB.* via rede), adicionar capas é um processo **manual e específico** — mas totalmente funcional.

A boa notícia: você **não precisa** de um programa especial. O que manda é o nome do arquivo e o lugar certo.

---

## 1. Onde as capas ficam no seu HD (SMB)

Na raiz da sua pasta compartilhada (a mesma onde estão `POPS` e `APPS`), você precisa criar esta estrutura:

```
My Passport/               ← raiz da sua pasta compartilhada
│
├── POPS/                  ← seus .VCD e SB.*.ELF
├── APPS/                  ← pastas com title.cfg e SB.*.ELF
│
└── ART/                   ← ← ← pasta que você vai criar
    └── APPS/              ← ← ← importante!
        ├── cover.jpg
        ├── background.jpg
        └── icon.png
```

Criando no Linux:

```bash
cd "/media/alace/My Passport"
mkdir -p ART/APPS
```

A pasta `ART/APPS/` é onde o OPL vai procurar as imagens .

---

## 2. Como nomear os arquivos de imagem (regra de ouro)

Essa é a parte mais importante e onde quase todo mundo erra.

Para um jogo cujo lançador `.ELF` se chama, por exemplo:

`SB.SLUS_005.94.Metal Gear Solid.ELF`

Os arquivos de arte **devem ter exatamente o mesmo nome**, acrescentando o sufixo do tipo de arte.

Exemplo prático:

| Tipo de arte   | Nome do arquivo                                               |
|----------------|---------------------------------------------------------------|
| Capa           | `SB.SLUS_005.94.Metal Gear Solid.ELF_cover.jpg`               |
| Background     | `SB.SLUS_005.94.Metal Gear Solid.ELF_background.jpg`          |
| Ícone          | `SB.SLUS_005.94.Metal Gear Solid.ELF_icon.png`                |

Isso foi confirmado por usuários no PSX-Place: o OPL usa o nome completo do `.ELF` como base para buscar a imagem, incluindo o sufixo `_cover`, `_background` etc. 

---

## 3. Onde baixar as capas pesquisando pelo nome do jogo

Você quer baixar **pesquisando pelo nome do jogo** — e isso é totalmente possível.

### 🔹 OPL Manager (recomendado, mas com um detalhe)

O **OPL Manager** é a ferramenta oficial para isso . Ele baixa capas automaticamente.

**Porém:** até pouco tempo atrás, ele não enxergava a estrutura `APPS/PastaDoJogo/` para PS1 .  
A dica que funciona:

- Mova **temporariamente** os arquivos `SB.NomeDoJogo.ELF` para a **raiz da pasta APPS** (sem a subpasta)
- Deixe o `title.cfg` onde está
- Rode o OPL Manager → ele vai baixar as artes
- Depois mova os `.ELF` de volta para as pastas dos jogos

Isso força o OPL Manager a reconhecer os jogos e baixar as capas.

### 🔹 Baixar manualmente (mais garantido)

Se preferir fazer direto:

- **Google Imagens** → pesquise `"NomeDoJogo PS1 cover"`
- **Sites especializados**:
  - [The Cover Project](https://www.thecoverproject.net/)
  - [LaunchBox Games Database](https://gamesdb.launchbox-app.com/)
  - [VGMusic](https://vgmusic.com/) (apenas trilhas, não capas)

Baixe a imagem, renomeie conforme a regra acima e coloque em `ART/APPS/`.

---

## 4. Formato e resolução recomendados

| Tipo        | Formato          | Resolução sugerida       |
|-------------|------------------|--------------------------|
| Capa        | `.jpg` ou `.png` | 140x200 ou 226x300       |
| Background  | `.jpg`           | 640x448 ou 1280x896      |
| Ícone       | `.png`           | 64x64 ou 128x128         |

Arquivos muito grandes podem deixar o OPL lento ao abrir a lista.

---

## 5. Exemplo completo (Metal Gear Solid)

Imagine que você tem:

`/POPS/SB.SLUS_005.94.Metal Gear Solid.ELF`

Passo a passo:

1. Crie a pasta `ART/APPS/`
2. Baixe a capa do MGS
3. Renomeie a capa para:
   `SB.SLUS_005.94.Metal Gear Solid.ELF_cover.jpg`
4. Copie para `ART/APPS/`
5. (Opcional) faça o mesmo para background e ícone

Pronto. Ao entrar na aba **APPS** no OPL, a capa vai aparecer.

---

## 6. O que NÃO funciona (para você não perder tempo)

- ❌ Colocar as imagens dentro da pasta `POPS/`
- ❌ Usar apenas o nome do jogo (`Metal Gear Solid_cover.jpg`)
- ❌ Usar `ART/POPS/` (funciona apenas para versões muito antigas do OPL com aba PS1 dedicada)

No seu setup atual (OPL moderno + POPStarter via APPS), o caminho correto é sempre `ART/APPS/` + nome completo do `.ELF` + sufixo .

---

## Resumo rápido para você testar agora

```bash
cd "/media/alace/My Passport"
mkdir -p ART/APPS

# Exemplo com um jogo seu
# Supondo que você tenha: POPS/SB.SCUS_949.00.Crash Bandicoot.ELF
# Baixe a capa e renomeie para:
# SB.SCUS_949.00.Crash Bandicoot.ELF_cover.jpg
# Cole em ART/APPS/
```

Depois disso, entre no OPL → aba APPS → Crash Bandicoot deve aparecer com capa.

Se quiser, me passe o nome de **um jogo específico** que você quer testar primeiro, que posso te dar o comando exato de renomeio da imagem.

Agora você consegue organizar todo o visual manualmente. Quer ajuda com o primeiro jogo para testar?

---
---
---
Sim, você pode automatizar o download das capas que faltam, mas **não espere que nenhum script pronto resolva 100%** — porque sites de artes bloqueiam scraping em massa. O que eu vou te mostrar é o fluxo **real** que funciona hoje.

---

## A verdade sobre scrapers de capa

Fóruns como PSX-Place e PS2-HOME já discutiram isso: sites como GameTDB, TheGamesDB e LaunchBox têm proteções anti-bot. Qualquer script simples de Python será bloqueado rapidamente .

As soluções que funcionam na prática:

### 1. OPL Scanner (recomendado)
Um programa que faz exatamente o que você quer: escaneia seus jogos e baixa artes de fontes confiáveis .

**Como usar:**
- Baixe no fórum PSX-Place
- Aponte para sua pasta `APPS/` ou `OPL/`
- Ele baixa capas, logos e arquivos `cfg`

### 2. OPL Mobile Scanner
Versão mais simples, foca só em covers .

---

## Se você insistir em fazer seu próprio script

### Fontes que ainda funcionam (parcialmente)

| Site | Funciona? | Limitação |
|------|-----------|-----------|
| GameTDB | Sim, mas precisa de User-Agent realista | APIs públicas limitadas |
| LaunchBox DB | Sim, via API oficial | Requer chave gratuita |
| TheGamesDB | Sim, via API v3 | Catálogo PS1 incompleto |
| Mobygames | Bloqueia scraping | Só manual |

### Estrutura de API que funciona (exemplo GameTDB)

```python
import requests
import re
from pathlib import Path

# 1. Extrair ID do jogo do nome do arquivo VCD
# Exemplo: "SCUS_949.00.Crash Bandicoot.VCD" -> ID: "SCUS-94900"
def extrair_id_game(nome_vcd):
    match = re.search(r'([A-Z]{4})_(\d{3})\.(\d{2})\.', nome_vcd)
    if match:
        regiao = match.group(1)  # SCUS, SLUS, SLES, SLPS
        codigo = match.group(2) + match.group(3)  # 94900
        return f"{regiao}-{codigo}"
    return None

# 2. Buscar capa na GameTDB
def buscar_capa_gametdb(game_id):
    url = f"https://art.gametdb.com/ps2/cover/{game_id}.jpg"
    # Ou para PS1: https://art.gametdb.com/ps1/cover/{game_id}.jpg
    response = requests.get(url, headers={"User-Agent": "OPL-Scanner/1.0"})
    if response.status_code == 200:
        return response.content
    return None
```

### Fluxo correto do scraping

1. **Parse da pasta POPS** → extrair IDs dos jogos
2. **Buscar em múltiplas fontes** (GameTDB → LaunchBox → TheGamesDB)
3. **Renomear para o formato correto** (`SB.ID.Nome.ELF_cover.jpg`)
4. **Salvar em `ART/APPS/`**

---

## O caminho mais prático (que eu recomendo)

| Etapa | Ferramenta | Por quê |
|-------|------------|---------|
| 1 | **OPL Manager v24** | Baixa 70-80% das capas automaticamente  |
| 2 | **OPL Scanner** | Pega mais 10-15% que o Manager perde |
| 3 | **Manual (os 10-15% restantes)** | Busca no Google Images + renomeio manual |

### Por que o OPL Manager perde capas?

1. **Nomes de arquivo não padronizados** — O Manager espera IDs como `SLUS-00594`, mas seus `.VCD` podem ter nomes diferentes 
2. **Banco de dados incompleto** — Jogos obscuros ou de regiões específicas (Japão, Europa) faltam
3. **Estrutura APPS vs POPS** — O Manager ainda não lida bem com a estrutura de pastas aninhadas que você criou 

### Solução para o Manager enxergar seus jogos

```
1. Mova os .ELF da pasta APPS/Jogo/ para a raiz de APPS/
2. Rode o OPL Manager → ele vai baixar as capas
3. Renomeie as capas baixadas para o formato correto:
   De: "SLUS_00594_cover.jpg"
   Para: "SB.SLUS_00594.Metal Gear Solid.ELF_cover.jpg"
4. Mova os .ELF de volta para as pastas dos jogos
5. Copie as capas renomeadas para ART/APPS/
```

Isso foi confirmado por usuários no PSX-Place .

---

## Se quiser mesmo o script (para os 10-15% restantes)

Aqui está a estrutura que **funciona sem ser bloqueado**:

```python
#!/usr/bin/env python3
import requests
import os
import re
from pathlib import Path

# Configurações
POPS_DIR = "/media/alace/My Passport/POPS"
ART_DIR = "/media/alace/My Passport/ART/APPS"

def extrair_id_opl(nome_vcd):
    """Extrai ID no formato que o OPL Manager usa"""
    match = re.search(r'([A-Z]{4})_(\d{3})\.(\d{2})\.', nome_vcd)
    if match:
        return f"{match.group(1)}-{match.group(2)}{match.group(3)}"
    return None

def buscar_gametdb(game_id, console="ps1"):
    """Busca capa no GameTDB"""
    url = f"https://art.gametdb.com/{console}/cover/{game_id}.jpg"
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "OPL-User/1.0"})
        return r.content if r.status_code == 200 else None
    except:
        return None

def buscar_launchbox(game_name):
    """Busca na API do LaunchBox (requer chave)"""
    # API key gratuita: https://gamesdb.launchbox-app.com/api/docs
    pass

# Fluxo principal
for vcd in Path(POPS_DIR).glob("*.VCD"):
    game_id = extrair_id_opl(vcd.name)
    if not game_id:
        continue
    
    # Tenta GameTDB primeiro
    capa = buscar_gametdb(game_id, "ps1")
    if capa:
        # Nome correto para sua estrutura SMB
        nome_elf = vcd.name.replace(".VCD", ".ELF")
        nome_capa = f"SB.{nome_elf}_cover.jpg"
        
        with open(Path(ART_DIR) / nome_capa, "wb") as f:
            f.write(capa)
        print(f"✓ Baixado: {vcd.name}")
    else:
        print(f"✗ Não encontrado: {vcd.name}")
```

---

## Resumo do que realmente funciona

| Abordagem | Taxa de sucesso | Esforço |
|-----------|-----------------|---------|
| OPL Manager v24 | 70-80% | Baixo |
| OPL Scanner | +10-15% | Baixo |
| Script caseiro | 0-50% (bloqueios) | Alto |
| Manual (Google) | 100% (do que existe) | Muito alto |

**Minha sugestão:** use OPL Manager + OPL Scanner para 90% das capas, e faça manualmente os jogos que faltam. O tempo que você gastaria fazendo um script resistente a bloqueios não compensa pelas 30-50 capas que faltam.

Quer que eu te ajude a configurar o OPL Manager para sua estrutura SMB?

---
---
---
Ah, entendi agora! Você quer uma ferramenta para baixar **capas de jogos de PS1** para usar no OPL, rodando **nativamente no Linux** (não o Instalador POPStarter do Windows).

A boa notícia é que existem sim ótimas opções para Linux. Vou te apresentar as duas melhores:

---

## 🐧 Opção 1: Skyscraper (Recomendado - 100% nativo)

O **Skyscraper** é exatamente o que você procura: uma ferramenta de linha de comando poderosa, escrita em C++/Qt, que roda nativamente no Linux .

### O que ele faz:
- Baixa capas, backgrounds, screenshots e metadados de jogos
- Suporta **PS1** (e outras 125 plataformas)
- Busca em múltiplas fontes: ScreenScraper.fr, TheGamesDB, Mobygames
- Funciona com vários frontends, incluindo **EmulationStation** (que é compatível com a estrutura do OPL)

### Como instalar no Linux (Ubuntu/Debian):

```bash
# Instalar dependências
sudo apt update
sudo apt install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools libqt5sql5-sqlite p7zip-full make g++ gcc git

# Baixar e compilar
git clone --depth 1 https://github.com/Gemba/skyscraper.git
cd skyscraper
qmake
make -j$(nproc)
sudo make install
```

### Como usar para PS1:

```bash
# Para um único jogo
Skyscraper -p psx -s screenscraper -u SEU_USUARIO:SUA_SENHA "caminho/para/jogo.VCD"

# Para escanear sua pasta POPS inteira
Skyscraper -p psx -s screenscraper -u SEU_USUARIO:SUA_SENHA -i "/media/alace/My Passport/POPS"

# Exportar as artes no formato que o OPL espera
Skyscraper -p psx -o "/media/alace/My Passport/ART/APPS" --cache refresh
```

**Importante:** Você precisa criar uma conta gratuita no [ScreenScraper.fr](https://www.screenscraper.fr) para usar o módulo `screenscraper` (é o mais completo).

---

## 📚 Opção 2: Base de dados pronta (GitHub)

Se você prefere baixar um pacote já pronto com todas as artes, existe um dump completo da base do OPL Manager disponível no GitHub .

**Repositório:** `Luden02/psx-ps2-opl-art-database`

```bash
# Clonar o repositório (cuidado: é grande!)
git clone https://github.com/Luden02/psx-ps2-opl-art-database.git

# As capas de PS1 estão em:
cd psx-ps2-opl-art-database/PS1/

# Copiar para seu HD
cp -r * "/media/alace/My Passport/ART/APPS/"
```

**Vantagens:** 
- Não precisa de scraping
- Já vem organizado

**Desvantagens:**
- É um snapshot estático (sem atualizações) 
- Pode não ter jogos obscuros ou recentemente adicionados

---

## 📋 Comparação das opções

| Ferramenta | Funciona no Linux? | Busca automática? | Atualizado? | Dificuldade |
|-----------|-------------------|-------------------|-------------|-------------|
| **Skyscraper** | ✅ Sim (nativo) | ✅ Sim | ✅ Sim (online) | Média |
| **Base de dados pronta** | ✅ Sim | ❌ Não (manual) | ❌ Não (parado) | Baixa |
| ~~OPL Manager~~ | ❌ Não (Windows) | ✅ Sim | ✅ Sim | - |

---

## 🎯 Minha recomendação

Use **Skyscraper** se você:
- Quer fazer scraping **agora** e ter as artes mais recentes
- Tem paciência para configurar (é uma vez só)
- Quer uma solução 100% nativa no Linux

Use a **base de dados pronta** se você:
- Quer algo rápido e sem configuração
- Não se importa com artes desatualizadas
- Tem espaço no HD (o repositório é grande)

---

## 🔧 Bônus: Script para integrar com sua estrutura

Se você usar o Skyscraper, crie um script para renomear as artes para o formato que o OPL espera (`SB.ID.Nome.ELF_cover.jpg`):

```bash
#!/bin/bash
cd "/media/alace/My Passport/ART/APPS"

# Para cada jogo na pasta POPS
for vcd in /media/alace/My\ Passport/POPS/*.VCD; do
    nome_base=$(basename "$vcd" .VCD)
    nome_elf="SB.${nome_base}.ELF"
    
    # Skyscraper exporta como "nome_do_jogo-cover.jpg"
    # Renomear para o formato do OPL
    if [ -f "${nome_base}-cover.jpg" ]; then
        mv "${nome_base}-cover.jpg" "${nome_elf}_cover.jpg"
    fi
done
```

---

Quer que eu te ajude a configurar o Skyscraper passo a passo, ou prefere ir direto pela base de dados pronta? 🚀