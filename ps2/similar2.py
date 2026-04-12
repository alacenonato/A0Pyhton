#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher

# Cores para terminal
class Cores:
    VERMELHO = '\033[0;31m'
    VERDE = '\033[0;32m'
    AMARELO = '\033[1;33m'
    AZUL = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CIANO = '\033[0;36m'
    BRANCO = '\033[1;37m'
    NC = '\033[0m'

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def cabecalho():
    limpar_tela()
    print(f"{Cores.AZUL}╔══════════════════════════════════════════════════════════════════════════════╗{Cores.NC}")
    print(f"{Cores.AZUL}║{Cores.NC}      {Cores.MAGENTA}DETECTOR DE JOGOS DUPLICADOS - OpenPS2Loader{Cores.NC}                             {Cores.AZUL}║{Cores.NC}")
    print(f"{Cores.AZUL}╚══════════════════════════════════════════════════════════════════════════════╝{Cores.NC}")
    print()

def extrair_id_jogo(nome_arquivo):
    """Extrai o ID do jogo (ex: SLUS_001.15, SCUS_123.45)"""
    # Procura padrões como SLUS_123.45, SCUS_123.45, SLES_123.45, etc
    match = re.search(r'(SLUS|SCUS|SLES|SLPS|PBPX|SCCS|SCPS|SIPS|SPUS)_(\d+\.\d+)', nome_arquivo, re.IGNORECASE)
    if match:
        return f"{match.group(1)}_{match.group(2)}"
    return None

def extrair_nome_jogo(nome_arquivo):
    """Extrai o nome do jogo removendo ID, extensão, prefixos e tags"""
    # Remove extensão
    nome = re.sub(r'\.(VCD|ELF|ISO|BIN|CUE)$', '', nome_arquivo, flags=re.IGNORECASE)
    
    # Remove ID do jogo (SLUS_123.45., SCUS_123.45., etc)
    nome = re.sub(r'(SLUS|SCUS|SLES|SLPS|PBPX|SCCS|SCPS|SIPS|SPUS)_\d+\.\d+\.', '', nome, flags=re.IGNORECASE)
    
    # Remove prefixos numéricos (001., 002., etc)
    nome = re.sub(r'^\d+\.', '', nome)
    
    # Remove tags entre parênteses
    nome = re.sub(r'\([^)]*\)', '', nome)
    
    # Remove tags como [USA], [JPN], [BR]
    nome = re.sub(r'\[[^\]]*\]', '', nome)
    
    # Remove palavras comuns de versão
    nome = re.sub(r'\b(PTBR|DUBLADO|USA|JAPAN|EUROPE|VERSION|REV|DEMO)\b', '', nome, flags=re.IGNORECASE)
    
    # Remove espaços extras e caracteres especiais
    nome = re.sub(r'[._\-]', ' ', nome)
    nome = re.sub(r'\s+', ' ', nome).strip()
    
    return nome.lower()

def calcular_similaridade(nome1, nome2):
    """Calcula similaridade entre dois nomes usando SequenceMatcher"""
    return SequenceMatcher(None, nome1, nome2).ratio()

def encontrar_duplicados_por_id(arquivos_por_extensao):
    """
    Encontra duplicados baseado no ID do jogo (mesmo ID com números diferentes)
    Ex: slus_001.15.jogo1 e slus_001.15.jogo2
    """
    todos_grupos = {}
    
    for extensao, arquivos in arquivos_por_extensao.items():
        if len(arquivos) < 2:
            continue
        
        # Agrupa por ID
        grupos_por_id = defaultdict(list)
        
        for arquivo in arquivos:
            id_jogo = extrair_id_jogo(arquivo)
            if id_jogo:
                grupos_por_id[id_jogo].append(arquivo)
        
        # Filtra apenas grupos com mais de 1 arquivo
        grupos = [grupo for grupo in grupos_por_id.values() if len(grupo) > 1]
        
        if grupos:
            todos_grupos[extensao] = grupos
    
    return todos_grupos

def encontrar_duplicados_por_nome(arquivos_por_extensao, limite_similaridade=0.7, min_letras=5):
    """
    Encontra duplicados baseado no nome do jogo (ignorando IDs)
    Ex: slus_0001.18.jogo1 e slus_001.19.jogo1
    """
    todos_grupos = {}
    todos_nomes_base = {}
    
    for extensao, arquivos in arquivos_por_extensao.items():
        if len(arquivos) < 2:
            continue
        
        # Extrai nomes base (sem ID)
        nomes_base = {}
        for arquivo in arquivos:
            nome_base = extrair_nome_jogo(arquivo)
            if len(nome_base) >= min_letras:
                nomes_base[arquivo] = nome_base
        
        if len(nomes_base) < 2:
            continue
        
        # Agrupa por similaridade
        grupos = []
        ja_agrupados = set()
        arquivos_lista = list(nomes_base.keys())
        
        for i, arquivo1 in enumerate(arquivos_lista):
            if arquivo1 in ja_agrupados:
                continue
                
            nome1 = nomes_base[arquivo1]
            grupo_atual = [arquivo1]
            
            for arquivo2 in arquivos_lista[i+1:]:
                if arquivo2 in ja_agrupados:
                    continue
                    
                nome2 = nomes_base[arquivo2]
                similaridade = calcular_similaridade(nome1, nome2)
                
                # Verifica se há sequência comum
                sequencia_comum = False
                for letras in range(min_letras, min(min(len(nome1), len(nome2)) + 1, min_letras + 5)):
                    for j in range(len(nome1) - letras + 1):
                        sub = nome1[j:j+letras]
                        if sub in nome2 and len(sub) >= min_letras:
                            sequencia_comum = True
                            break
                    if sequencia_comum:
                        break
                
                if similaridade >= limite_similaridade or sequencia_comum:
                    grupo_atual.append(arquivo2)
                    ja_agrupados.add(arquivo2)
            
            if len(grupo_atual) > 1:
                grupos.append(grupo_atual)
                ja_agrupados.add(arquivo1)
        
        if grupos:
            todos_grupos[extensao] = grupos
            todos_nomes_base[extensao] = nomes_base
    
    return todos_grupos, todos_nomes_base

def formatar_tamanho(tamanho_bytes):
    """Formata o tamanho em bytes"""
    if tamanho_bytes < 1024:
        return f"{tamanho_bytes} B"
    elif tamanho_bytes < 1024 * 1024:
        return f"{tamanho_bytes / 1024:.2f} KB"
    elif tamanho_bytes < 1024 * 1024 * 1024:
        return f"{tamanho_bytes / (1024 * 1024):.2f} MB"
    else:
        return f"{tamanho_bytes / (1024 * 1024 * 1024):.2f} GB"

def analisar_pasta(caminho_pasta, nome_pasta, extensoes, modo_busca, limite_similaridade, min_letras):
    """Analisa uma pasta específica (CD, DVD, POPS)"""
    print(f"\n{Cores.AZUL}{'═' * 70}{Cores.NC}")
    print(f"{Cores.MAGENTA}📁 ANALISANDO PASTA: {nome_pasta}{Cores.NC}")
    print(f"{Cores.CIANO}   Caminho: {caminho_pasta}{Cores.NC}")
    print(f"{Cores.AZUL}{'═' * 70}{Cores.NC}")
    
    if not os.path.exists(caminho_pasta):
        print(f"{Cores.VERMELHO}   ✗ Pasta {nome_pasta} não encontrada!{Cores.NC}")
        return None, 0, 0, 0
    
    # Entra na pasta
    os.chdir(caminho_pasta)
    
    # Coleta arquivos separados por extensão
    arquivos_por_extensao = defaultdict(list)
    total_arquivos = 0
    
    for ext in extensoes:
        encontrados = [f for f in os.listdir(".") if f.upper().endswith(f".{ext}")]
        if encontrados:
            print(f"{Cores.VERDE}   ✓ .{ext}: {len(encontrados)} arquivo(s){Cores.NC}")
            arquivos_por_extensao[ext] = encontrados
            total_arquivos += len(encontrados)
        else:
            print(f"{Cores.VERMELHO}   ✗ .{ext}: nenhum arquivo encontrado{Cores.NC}")
    
    if total_arquivos == 0:
        print(f"{Cores.VERMELHO}   ✗ Nenhum arquivo encontrado em {nome_pasta}{Cores.NC}")
        return None, 0, 0, 0
    
    # Mostra lista dos arquivos encontrados
    print(f"\n{Cores.VERDE}   📋 ARQUIVOS ENCONTRADOS ({total_arquivos}):{Cores.NC}")
    print(f"{Cores.CIANO}   {'─' * 46}{Cores.NC}")
    
    for ext in extensoes:
        if ext in arquivos_por_extensao:
            print(f"{Cores.MAGENTA}      .{ext} ({len(arquivos_por_extensao[ext])} arquivos):{Cores.NC}")
            for i, arquivo in enumerate(arquivos_por_extensao[ext], 1):
                tamanho = os.path.getsize(os.path.join(caminho_pasta, arquivo))
                id_jogo = extrair_id_jogo(arquivo) or "Sem ID"
                nome_jogo = extrair_nome_jogo(arquivo) or "Sem nome"
                print(f"{Cores.CIANO}         {i:2d}.{Cores.NC} {arquivo}")
                print(f"{Cores.CIANO}             ID: {Cores.VERDE}{id_jogo}{Cores.NC}")
                print(f"{Cores.CIANO}             Nome: {Cores.VERDE}{nome_jogo[:50]}{Cores.NC}")
                print(f"{Cores.CIANO}             Tamanho: {Cores.VERDE}{formatar_tamanho(tamanho)}{Cores.NC}")
                print()
    
    # Busca por duplicados conforme modo escolhido
    print(f"{Cores.CIANO}   🔍 Buscando duplicados por {modo_busca}...{Cores.NC}")
    print()
    
    if modo_busca == "ID":
        todos_grupos = encontrar_duplicados_por_id(arquivos_por_extensao)
        
        if not todos_grupos:
            print(f"\n   {Cores.VERDE}🎉 Nenhum duplicado por ID encontrado em {nome_pasta}!{Cores.NC}")
            return None, 0, 0, 0
        
        # Exibe resultados por ID
        total_grupos = 0
        total_arquivos_dup = 0
        total_duplicatas = 0
        
        for extensao, grupos in todos_grupos.items():
            print(f"\n   {Cores.AZUL}🔍 ARQUIVOS .{extensao.upper()} - MESMO ID:{Cores.NC}")
            
            for i, grupo in enumerate(grupos, 1):
                id_jogo = extrair_id_jogo(grupo[0])
                print(f"\n   {Cores.AMARELO}   📦 GRUPO {i} - ID: {id_jogo} ({len(grupo)} arquivos .{extensao}):{Cores.NC}")
                print(f"   {Cores.AMARELO}   {'─' * 46}{Cores.NC}")
                
                for arquivo in grupo:
                    caminho_completo = os.path.join(caminho_pasta, arquivo)
                    tamanho = os.path.getsize(caminho_completo) if os.path.exists(caminho_completo) else 0
                    nome_jogo = extrair_nome_jogo(arquivo)
                    
                    print(f"      {Cores.VERDE}▶{Cores.NC} {arquivo}")
                    print(f"         {Cores.CIANO}Nome:{Cores.NC} {nome_jogo}")
                    print(f"         {Cores.CIANO}Tamanho:{Cores.NC} {formatar_tamanho(tamanho)}")
                
                total_grupos += 1
                total_arquivos_dup += len(grupo)
                total_duplicatas += (len(grupo) - 1)
        
        return todos_grupos, total_grupos, total_arquivos_dup, total_duplicatas
    
    else:  # Modo NOME
        todos_grupos, todos_nomes_base = encontrar_duplicados_por_nome(arquivos_por_extensao, limite_similaridade, min_letras)
        
        if not todos_grupos:
            print(f"\n   {Cores.VERDE}🎉 Nenhum duplicado por nome encontrado em {nome_pasta}!{Cores.NC}")
            return None, 0, 0, 0
        
        # Exibe resultados por nome
        total_grupos = 0
        total_arquivos_dup = 0
        total_duplicatas = 0
        
        for extensao, grupos in todos_grupos.items():
            print(f"\n   {Cores.AZUL}🔍 ARQUIVOS .{extensao.upper()} - NOMES SIMILARES:{Cores.NC}")
            
            nomes_base = todos_nomes_base[extensao]
            
            for i, grupo in enumerate(grupos, 1):
                print(f"\n   {Cores.AMARELO}   📦 GRUPO {i} ({len(grupo)} arquivos .{extensao}):{Cores.NC}")
                print(f"   {Cores.AMARELO}   {'─' * 46}{Cores.NC}")
                
                for arquivo in grupo:
                    caminho_completo = os.path.join(caminho_pasta, arquivo)
                    tamanho = os.path.getsize(caminho_completo) if os.path.exists(caminho_completo) else 0
                    nome_base = nomes_base.get(arquivo, "não detectado")
                    id_jogo = extrair_id_jogo(arquivo) or "Sem ID"
                    
                    print(f"      {Cores.VERDE}▶{Cores.NC} {arquivo}")
                    print(f"         {Cores.CIANO}ID:{Cores.NC} {id_jogo}")
                    print(f"         {Cores.CIANO}Nome detectado:{Cores.NC} {nome_base}")
                    print(f"         {Cores.CIANO}Tamanho:{Cores.NC} {formatar_tamanho(tamanho)}")
                
                total_grupos += 1
                total_arquivos_dup += len(grupo)
                total_duplicatas += (len(grupo) - 1)
        
        return todos_grupos, total_grupos, total_arquivos_dup, total_duplicatas

def main():
    cabecalho()
    
    # DEFINE O DIRETÓRIO PADRÃO DO HD
    hd_base = "/media/alace/My Passport"
    
    # Define as subpastas do OpenPS2Loader
    subpastas = {
        "CD": ["ISO", "BIN"],      # Jogos de PS2 em CD
        "DVD": ["ISO"],             # Jogos de PS2 em DVD
        "POPS": ["VCD", "ELF"]      # Jogos de PS1
    }
    
    print(f"{Cores.VERDE}📂 HD BASE: {hd_base}{Cores.NC}")
    print(f"{Cores.CIANO}   Estrutura do OpenPS2Loader:{Cores.NC}")
    print(f"{Cores.CIANO}   ├── /CD    - Jogos PS2 CD (ISO, BIN){Cores.NC}")
    print(f"{Cores.CIANO}   ├── /DVD   - Jogos PS2 DVD (ISO){Cores.NC}")
    print(f"{Cores.CIANO}   └── /POPS  - Jogos PS1 (VCD, ELF){Cores.NC}")
    print()
    
    # Verifica se o HD existe
    if not os.path.exists(hd_base):
        print(f"{Cores.VERMELHO}✗ HD não encontrado: {hd_base}{Cores.NC}")
        print(f"{Cores.AMARELO}  Deseja digitar outro caminho? (s/N){Cores.NC}")
        opcao = input().strip().lower()
        if opcao == 's':
            hd_base = input(f"{Cores.AMARELO}→ {Cores.NC}").strip()
            if not os.path.exists(hd_base):
                print(f"{Cores.VERMELHO}✗ Diretório não encontrado!{Cores.NC}")
                sys.exit(1)
        else:
            sys.exit(1)
    
    # Escolhe o modo de busca
    print(f"{Cores.CIANO}🔍 MODO DE BUSCA:{Cores.NC}")
    print(f"   1 - Buscar por ID do jogo (ex: SLUS_001.15.jogo1 e SLUS_001.15.jogo2)")
    print(f"   2 - Buscar por nome do jogo (ex: slus_0001.18.jogo1 e slus_001.19.jogo1)")
    print()
    
    modo_opcao = input(f"{Cores.AMARELO}→ {Cores.NC}").strip()
    
    if modo_opcao == '1':
        modo_busca = "ID"
        print(f"\n{Cores.VERDE}✅ Modo selecionado: BUSCA POR ID{Cores.NC}")
    else:
        modo_busca = "NOME"
        print(f"\n{Cores.VERDE}✅ Modo selecionado: BUSCA POR NOME{Cores.NC}")
    
    # Pergunta quais pastas analisar
    print(f"\n{Cores.CIANO}📁 Quais pastas analisar?{Cores.NC}")
    print(f"   1 - Apenas CD")
    print(f"   2 - Apenas DVD")
    print(f"   3 - Apenas POPS")
    print(f"   4 - CD + DVD")
    print(f"   5 - CD + POPS")
    print(f"   6 - DVD + POPS")
    print(f"   7 - Todas (CD, DVD, POPS)")
    print()
    
    opcao_pastas = input(f"{Cores.AMARELO}→ {Cores.NC}").strip()
    
    pastas_para_analisar = []
    if opcao_pastas == '1':
        pastas_para_analisar = ["CD"]
    elif opcao_pastas == '2':
        pastas_para_analisar = ["DVD"]
    elif opcao_pastas == '3':
        pastas_para_analisar = ["POPS"]
    elif opcao_pastas == '4':
        pastas_para_analisar = ["CD", "DVD"]
    elif opcao_pastas == '5':
        pastas_para_analisar = ["CD", "POPS"]
    elif opcao_pastas == '6':
        pastas_para_analisar = ["DVD", "POPS"]
    else:
        pastas_para_analisar = ["CD", "DVD", "POPS"]
    
    # Configurações para modo NOME
    limite_similaridade = 0.7
    min_letras = 5
    
    if modo_busca == "NOME":
        print()
        print(f"{Cores.CIANO}⚙️ CONFIGURAÇÕES DE SIMILARIDADE (para busca por NOME):{Cores.NC}")
        print(f"   Similaridade mínima (0.0 a 1.0) - padrão: 0.7")
        print(f"   Número mínimo de letras coincidentes - padrão: 5")
        print()
        
        similaridade_input = input(f"{Cores.AMARELO}Similaridade (ENTER para 0.7): {Cores.NC}").strip()
        limite_similaridade = float(similaridade_input) if similaridade_input else 0.7
        
        min_letras_input = input(f"{Cores.AMARELO}Mínimo de letras coincidentes (ENTER para 5): {Cores.NC}").strip()
        min_letras = int(min_letras_input) if min_letras_input else 5
    
    # Mostra configurações
    print()
    print(f"{Cores.VERDE}⚙️ CONFIGURAÇÕES APLICADAS:{Cores.NC}")
    print(f"   HD Base: {hd_base}")
    print(f"   Modo de busca: {modo_busca}")
    print(f"   Pastas a analisar: {', '.join(pastas_para_analisar)}")
    if modo_busca == "NOME":
        print(f"   Similaridade mínima: {limite_similaridade * 100:.0f}%")
        print(f"   Mínimo de letras coincidentes: {min_letras}")
    print(f"   Comparação: apenas arquivos com a MESMA extensão")
    print()
    
    input(f"{Cores.CIANO}Pressione ENTER para iniciar a análise...{Cores.NC}")
    
    # Analisa cada pasta selecionada
    total_geral_grupos = 0
    total_geral_arquivos = 0
    total_geral_duplicatas = 0
    
    for pasta in pastas_para_analisar:
        caminho_pasta = os.path.join(hd_base, pasta)
        extensoes = subpastas[pasta]
        
        resultado = analisar_pasta(caminho_pasta, pasta, extensoes, modo_busca, limite_similaridade, min_letras)
        
        if resultado[0] is not None:
            total_geral_grupos += resultado[1]
            total_geral_arquivos += resultado[2]
            total_geral_duplicatas += resultado[3]
    
    # Resumo final
    if total_geral_grupos > 0:
        print(f"\n{Cores.AZUL}{'═' * 70}{Cores.NC}")
        print(f"{Cores.VERDE}📊 RESUMO GERAL:{Cores.NC}")
        print(f"   Modo de busca: {modo_busca}")
        print(f"   Total de grupos com duplicatas: {total_geral_grupos}")
        print(f"   Total de arquivos envolvidos: {total_geral_arquivos}")
        print(f"   Total de arquivos duplicados (excedentes): {total_geral_duplicatas}")
        print(f"{Cores.AZUL}{'═' * 70}{Cores.NC}")
    else:
        print(f"\n{Cores.VERDE}{'═' * 70}{Cores.NC}")
        print(f"{Cores.VERDE}🎉 NENHUMA DUPLICATA ENCONTRADA EM NENHUMA PASTA!{Cores.NC}")
        print(f"{Cores.VERDE}{'═' * 70}{Cores.NC}")
    
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Cores.AMARELO}⚠ Script interrompido pelo usuário.{Cores.NC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Cores.VERMELHO}✗ Erro: {e}{Cores.NC}")
        sys.exit(1)