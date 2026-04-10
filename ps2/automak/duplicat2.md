Ah, agora entendi! Você quer comparar os **arquivos `.VCD`** (os jogos em si), não os `.ELF`. E quer evitar sobrescrever arquivos `.VCD` que já tenham prefixo `SB.` mas com tamanhos diferentes, renomeando com numeração.

Vou refazer o script com essa lógica:

---

## 🐍 Script para gerenciar arquivos `.VCD` com prefixo `SB.`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import glob
import shutil
from pathlib import Path

# Cores para terminal
class Cores:
    VERMELHO = '\033[0;31m'
    VERDE = '\033[0;32m'
    AMARELO = '\033[1;33m'
    AZUL = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CIANO = '\033[0;36m'
    NC = '\033[0m'

def pausar():
    print()
    input(f"{Cores.AMARELO}▶ Pressione ENTER para continuar...{Cores.NC}")
    print()

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def cabecalho():
    limpar_tela()
    print(f"{Cores.AZUL}╔════════════════════════════════════════════════════════════════════╗{Cores.NC}")
    print(f"{Cores.AZUL}║{Cores.NC}      {Cores.MAGENTA}RENOMEADOR DE VCD PARA POPSTARTER (SMB) - v2.0{Cores.NC}                {Cores.AZUL}║{Cores.NC}")
    print(f"{Cores.AZUL}╚════════════════════════════════════════════════════════════════════╝{Cores.NC}")
    print()

def barra_progresso(atual, total, largura=50):
    percent = int(atual * 100 / total) if total > 0 else 0
    preenchido = int(percent * largura / 100)
    vazio = largura - preenchido
    barra = "█" * preenchido + "░" * vazio
    print(f"{Cores.CIANO}[{barra}] {percent}%{Cores.NC}", end="")

def gerar_nome_com_prefixo(nome_original):
    """Gera o nome com prefixo SB. a partir do nome original"""
    return f"SB.{nome_original}"

def verificar_conflito(diretorio, nome_destino, tamanho_original):
    """
    Verifica se há conflito com arquivo existente.
    Retorna: (nome_final, acao)
    acao pode ser: 'ok' (pode sobrescrever), 'renomear', 'pular'
    """
    caminho_destino = os.path.join(diretorio, nome_destino)
    
    # Se não existe, pode criar
    if not os.path.exists(caminho_destino):
        return nome_destino, 'criar'
    
    # Se existe, compara tamanho
    tamanho_existente = os.path.getsize(caminho_destino)
    
    if tamanho_existente == tamanho_original:
        return nome_destino, 'pular'  # Já existe e é igual
    else:
        return None, 'renomear'  # Precisa gerar nome com número

def gerar_nome_com_numero(diretorio, nome_base, extensao, contador_inicial=2):
    """Gera um nome com número no final até encontrar um disponível"""
    contador = contador_inicial
    while True:
        nome_novo = f"{nome_base}({contador}){extensao}"
        caminho_novo = os.path.join(diretorio, nome_novo)
        
        if not os.path.exists(caminho_novo):
            return nome_novo
        contador += 1

def main():
    # ============================================
    # PASSO 1: Verificar diretório
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}📁 PASSO 1: Verificando diretório atual{Cores.NC}")
    print(f"   Diretório: {Cores.VERDE}{os.getcwd()}{Cores.NC}")
    print()
    
    # Verifica se tem arquivos .VCD
    vcd_files = glob.glob("*.VCD")
    vcd_files_sem_prefixo = [f for f in vcd_files if not f.startswith("SB.")]
    vcd_files_com_prefixo = [f for f in vcd_files if f.startswith("SB.")]
    
    print(f"{Cores.VERDE}✓ Encontrados:{Cores.NC}")
    print(f"   - Arquivos .VCD sem prefixo: {len(vcd_files_sem_prefixo)}")
    print(f"   - Arquivos .VCD com prefixo SB.: {len(vcd_files_com_prefixo)}")
    print()
    
    if len(vcd_files_sem_prefixo) == 0:
        print(f"{Cores.VERDE}🎉 Todos os arquivos já têm o prefixo SB.! Nada para fazer.{Cores.NC}")
        sys.exit(0)
    
    pausar()
    
    # ============================================
    # PASSO 2: Analisar cada arquivo
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}🔍 PASSO 2: Analisando arquivos para renomear{Cores.NC}")
    print()
    
    acoes = {
        'criar': [],
        'renomear': [],
        'pular': []
    }
    
    for vcd in vcd_files_sem_prefixo:
        tamanho_original = os.path.getsize(vcd)
        nome_destino = gerar_nome_com_prefixo(vcd)
        
        resultado, acao = verificar_conflito(".", nome_destino, tamanho_original)
        
        if acao == 'pular':
            print(f"{Cores.VERDE}⏭ PULAR{Cores.NC}: {vcd} -> {nome_destino} (já existe e é idêntico)")
            acoes['pular'].append((vcd, nome_destino))
        
        elif acao == 'criar':
            print(f"{Cores.VERDE}✅ CRIAR{Cores.NC}: {vcd} -> {nome_destino}")
            acoes['criar'].append((vcd, nome_destino))
        
        elif acao == 'renomear':
            # Conflito de tamanho: precisa gerar número
            nome_base = nome_destino[:-4]  # Remove .VCD
            nome_com_numero = gerar_nome_com_numero(".", nome_base, ".VCD")
            print(f"{Cores.AMARELO}⚠ RENOMEAR COM NÚMERO{Cores.NC}: {vcd} -> {nome_com_numero} (conflito de tamanho)")
            acoes['renomear'].append((vcd, nome_com_numero))
    
    print()
    print(f"📊 Resumo da análise:")
    print(f"   {Cores.VERDE}✓ Arquivos para criar (sem conflito): {len(acoes['criar'])}{Cores.NC}")
    print(f"   {Cores.AMARELO}⚠ Arquivos para renomear com número: {len(acoes['renomear'])}{Cores.NC}")
    print(f"   {Cores.CIANO}⏭ Arquivos já existentes e idênticos: {len(acoes['pular'])}{Cores.NC}")
    
    if len(acoes['criar']) == 0 and len(acoes['renomear']) == 0:
        print(f"\n{Cores.VERDE}🎉 Nada para fazer! Todos os arquivos já estão corretos.{Cores.NC}")
        sys.exit(0)
    
    pausar()
    
    # ============================================
    # PASSO 3: Executar renomeações
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}⚙️ PASSO 3: Executando renomeações{Cores.NC}")
    print()
    
    total = len(acoes['criar']) + len(acoes['renomear'])
    processados = 0
    
    # Primeiro: criar arquivos sem conflito
    for origem, destino in acoes['criar']:
        processados += 1
        print(f"   [{processados}/{total}] Renomeando: {origem} -> {destino}... ", end="")
        try:
            os.rename(origem, destino)
            print(f"{Cores.VERDE}OK{Cores.NC}")
        except Exception as e:
            print(f"{Cores.VERMELHO}FALHOU - {e}{Cores.NC}")
    
    # Depois: renomear com número (conflito de tamanho)
    for origem, destino in acoes['renomear']:
        processados += 1
        print(f"   [{processados}/{total}] Renomeando: {origem} -> {destino}... ", end="")
        try:
            os.rename(origem, destino)
            print(f"{Cores.AMARELO}RENOMEADO COM NÚMERO{Cores.NC}")
        except Exception as e:
            print(f"{Cores.VERMELHO}FALHOU - {e}{Cores.NC}")
    
    print()
    barra_progresso(total, total)
    print(f"\n{Cores.VERDE}✓ {total} arquivos processados com sucesso!{Cores.NC}")
    pausar()
    
    # ============================================
    # PASSO 4: Verificação final
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}✅ PASSO 4: Verificação final{Cores.NC}")
    print()
    
    # Lista todos os arquivos .VCD agora
    todos_vcd = glob.glob("*.VCD")
    vcd_com_prefixo = [f for f in todos_vcd if f.startswith("SB.")]
    vcd_sem_prefixo = [f for f in todos_vcd if not f.startswith("SB.")]
    
    print(f"📊 Status final:")
    print(f"   {Cores.VERDE}✓ Arquivos com prefixo SB.: {len(vcd_com_prefixo)}{Cores.NC}")
    print(f"   {Cores.AMARELO}⚠ Arquivos sem prefixo: {len(vcd_sem_prefixo)}{Cores.NC}")
    
    if len(vcd_sem_prefixo) == 0:
        print(f"\n{Cores.VERDE}╔════════════════════════════════════════════════════════════════════╗{Cores.NC}")
        print(f"{Cores.VERDE}║{Cores.NC}      🎉 TUDO PRONTO! Todos os VCDs foram renomeados! 🎉            {Cores.VERDE}║{Cores.NC}")
        print(f"{Cores.VERDE}╚════════════════════════════════════════════════════════════════════╝{Cores.NC}")
    else:
        print(f"\n{Cores.AMARELO}⚠ Ainda existem {len(vcd_sem_prefixo)} arquivos sem prefixo.{Cores.NC}")
    
    print()
    print(f"{Cores.CIANO}💡 Próximo passo:{Cores.NC}")
    print(f"   Execute o script de criação de ELFs para gerar os SB.*.ELF correspondentes.")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Cores.AMARELO}⚠ Script interrompido pelo usuário.{Cores.NC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Cores.VERMELHO}✗ Erro inesperado: {e}{Cores.NC}")
        sys.exit(1)
```

---

## 📋 O que este script faz

| Situação | Ação |
|----------|------|
| Arquivo `.VCD` sem prefixo `SB.` e não existe `SB.arquivo.VCD` | Renomeia para `SB.arquivo.VCD` |
| Já existe `SB.arquivo.VCD` com **mesmo tamanho** | Pula (não faz nada, já está ok) |
| Já existe `SB.arquivo.VCD` com **tamanho diferente** | Renomeia para `SB.arquivo(2).VCD` (e assim por diante) |

---

## ▶️ Como usar

```bash
cd "/media/alace/My Passport/POPS"
python3 renomear_vcd.py
```

---

## 📊 Exemplo de saída

```
🔍 PASSO 2: Analisando arquivos para renomear

✅ CRIAR: GranTurismo.VCD -> SB.GranTurismo.VCD
⚠ RENOMEAR COM NÚMERO: BloodyRoar.VCD -> SB.BloodyRoar(2).VCD (conflito de tamanho)
⏭ PULAR: CrashBandicoot.VCD -> SB.CrashBandicoot.VCD (já existe e é idêntico)

📊 Resumo da análise:
   ✓ Arquivos para criar (sem conflito): 1
   ⚠ Arquivos para renomear com número: 1
   ⏭ Arquivos já existentes e idênticos: 1
```

---

Agora está correto? O script renomeia os `.VCD` para terem prefixo `SB.` e, se houver conflito de tamanho, adiciona `(2)`, `(3)`, etc. 🚀
