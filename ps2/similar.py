#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import glob
from datetime import datetime

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

def pausar():
    print()
    input(f"{Cores.AMARELO}▶ Pressione ENTER para continuar...{Cores.NC}")
    print()

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def cabecalho():
    limpar_tela()
    print(f"{Cores.AZUL}╔══════════════════════════════════════════════════════════════════════════════╗{Cores.NC}")
    print(f"{Cores.AZUL}║{Cores.NC}      {Cores.MAGENTA}RENOMEADOR DE VCD PARA POPSTARTER (SMB) - v2.0{Cores.NC}                               {Cores.AZUL}║{Cores.NC}")
    print(f"{Cores.AZUL}╚══════════════════════════════════════════════════════════════════════════════╝{Cores.NC}")
    print()

def formatar_tamanho(tamanho_bytes):
    """Formata o tamanho em bytes para KB/MB/GB"""
    if tamanho_bytes < 1024:
        return f"{tamanho_bytes} B"
    elif tamanho_bytes < 1024 * 1024:
        return f"{tamanho_bytes / 1024:.2f} KB"
    elif tamanho_bytes < 1024 * 1024 * 1024:
        return f"{tamanho_bytes / (1024 * 1024):.2f} MB"
    else:
        return f"{tamanho_bytes / (1024 * 1024 * 1024):.2f} GB"

def gerar_nome_com_prefixo(nome_original):
    """Gera o nome com prefixo SB. a partir do nome original"""
    return f"SB.{nome_original}"

def verificar_conflito(diretorio, nome_destino, tamanho_original):
    """
    Verifica se há conflito com arquivo existente.
    Retorna: (nome_final, acao, tamanho_existente)
    acao pode ser: 'ok' (pode sobrescrever), 'renomear', 'pular'
    """
    caminho_destino = os.path.join(diretorio, nome_destino)
    
    # Se não existe, pode criar
    if not os.path.exists(caminho_destino):
        return nome_destino, 'criar', None
    
    # Se existe, compara tamanho
    tamanho_existente = os.path.getsize(caminho_destino)
    
    if tamanho_existente == tamanho_original:
        return nome_destino, 'pular', tamanho_existente
    else:
        return None, 'renomear', tamanho_existente

def gerar_nome_com_numero(diretorio, nome_base, extensao, contador_inicial=2):
    """Gera um nome com número no final até encontrar um disponível"""
    contador = contador_inicial
    while True:
        nome_novo = f"{nome_base}({contador}){extensao}"
        caminho_novo = os.path.join(diretorio, nome_novo)
        
        if not os.path.exists(caminho_novo):
            return nome_novo
        contador += 1

def exibir_lista_detalhada(titulo, itens, cor, mostrar_tamanhos=False):
    """Exibe uma lista detalhada de itens"""
    if not itens:
        return
    
    print(f"{cor}{titulo}{Cores.NC}")
    print(f"{cor}{'─' * 70}{Cores.NC}")
    
    for i, item in enumerate(itens, 1):
        if mostrar_tamanhos and len(item) == 3:
            origem, destino, tamanho = item
            tamanho_fmt = formatar_tamanho(tamanho)
            print(f"   {cor}{i:3d}{Cores.NC}. {origem}")
            print(f"        → {destino} ({cor}{tamanho_fmt}{Cores.NC})")
        else:
            origem, destino = item[:2]
            print(f"   {cor}{i:3d}{Cores.NC}. {origem}")
            print(f"        → {destino}")
    print()

def exibir_resumo_final(acoes):
    """Exibe um resumo final com todas as ações"""
    limpar_tela()
    print(f"{Cores.AZUL}╔══════════════════════════════════════════════════════════════════════════════╗{Cores.NC}")
    print(f"{Cores.AZUL}║{Cores.NC}                         {Cores.VERDE}📋 RESUMO FINAL DAS OPERAÇÕES{Cores.NC}                              {Cores.AZUL}║{Cores.NC}")
    print(f"{Cores.AZUL}╚══════════════════════════════════════════════════════════════════════════════╝{Cores.NC}")
    print()
    
    # Arquivos que serão criados
    if acoes['criar']:
        print(f"{Cores.VERDE}✅ ARQUIVOS QUE SERÃO CRIADOS (sem conflito):{Cores.NC}")
        print(f"{Cores.VERDE}{'─' * 60}{Cores.NC}")
        for origem, destino in acoes['criar']:
            tamanho = os.path.getsize(origem)
            tamanho_fmt = formatar_tamanho(tamanho)
            print(f"   📁 {origem}")
            print(f"      → {destino} ({tamanho_fmt})")
        print()
    
    # Arquivos que serão renomeados com número
    if acoes['renomear']:
        print(f"{Cores.AMARELO}⚠ ARQUIVOS QUE SERÃO RENOMEADOS COM NÚMERO (conflito de tamanho):{Cores.NC}")
        print(f"{Cores.AMARELO}{'─' * 60}{Cores.NC}")
        for origem, destino, tamanho_orig, tamanho_dest in acoes['renomear']:
            print(f"   📁 {origem} ({formatar_tamanho(tamanho_orig)})")
            print(f"      → {destino}")
            print(f"      ⚠ Conflito com: SB.{origem} ({formatar_tamanho(tamanho_dest)}) - tamanhos diferentes")
        print()
    
    # Arquivos que já existem e são idênticos (não precisam ser renomeados)
    if acoes['pular']:
        print(f"{Cores.CIANO}⏭ ARQUIVOS QUE JÁ EXISTEM E SÃO IDÊNTICOS (não serão modificados):{Cores.NC}")
        print(f"{Cores.CIANO}{'─' * 60}{Cores.NC}")
        for origem, destino, tamanho in acoes['pular']:
            tamanho_fmt = formatar_tamanho(tamanho)
            print(f"   📁 {origem} ({tamanho_fmt})")
            print(f"      → {destino} ({tamanho_fmt}) - já existe e é idêntico")
        print()
    
    # Totais
    print(f"{Cores.BRANCO}{'═' * 60}{Cores.NC}")
    print(f"{Cores.VERDE}📊 TOTAL DE ARQUIVOS PROCESSADOS: {len(acoes['criar']) + len(acoes['renomear'])}{Cores.NC}")
    print(f"{Cores.CIANO}⏭ ARQUIVOS IGNORADOS (já existem): {len(acoes['pular'])}{Cores.NC}")
    print(f"{Cores.BRANCO}{'═' * 60}{Cores.NC}")

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
    
    # Listar os arquivos sem prefixo
    if vcd_files_sem_prefixo:
        print(f"{Cores.AMARELO}📋 Arquivos que serão analisados:{Cores.NC}")
        for i, vcd in enumerate(vcd_files_sem_prefixo[:20], 1):
            tamanho = os.path.getsize(vcd)
            print(f"   {i:3d}. {vcd} ({formatar_tamanho(tamanho)})")
        if len(vcd_files_sem_prefixo) > 20:
            print(f"   ... e mais {len(vcd_files_sem_prefixo) - 20} arquivos")
    else:
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
        'criar': [],      # (origem, destino)
        'renomear': [],   # (origem, destino, tamanho_original, tamanho_existente)
        'pular': []       # (origem, destino, tamanho)
    }
    
    for vcd in vcd_files_sem_prefixo:
        tamanho_original = os.path.getsize(vcd)
        nome_destino = gerar_nome_com_prefixo(vcd)
        
        resultado, acao, tamanho_existente = verificar_conflito(".", nome_destino, tamanho_original)
        
        if acao == 'pular':
            print(f"{Cores.CIANO}⏭{Cores.NC} {vcd} -> {nome_destino} {Cores.VERDE}(já existe e é idêntico){Cores.NC}")
            acoes['pular'].append((vcd, nome_destino, tamanho_original))
        
        elif acao == 'criar':
            print(f"{Cores.VERDE}✅{Cores.NC} {vcd} -> {nome_destino}")
            acoes['criar'].append((vcd, nome_destino))
        
        elif acao == 'renomear':
            # Conflito de tamanho: precisa gerar número
            nome_base = nome_destino[:-4]  # Remove .VCD
            nome_com_numero = gerar_nome_com_numero(".", nome_base, ".VCD")
            print(f"{Cores.AMARELO}⚠{Cores.NC} {vcd} -> {nome_com_numero} {Cores.AMARELO}(conflito de tamanho: {formatar_tamanho(tamanho_original)} ≠ {formatar_tamanho(tamanho_existente)}){Cores.NC}")
            acoes['renomear'].append((vcd, nome_com_numero, tamanho_original, tamanho_existente))
    
    print()
    print(f"{Cores.VERDE}✓ Análise concluída!{Cores.NC}")
    pausar()
    
    # ============================================
    # PASSO 3: Exibir resumo detalhado
    # ============================================
    exibir_resumo_final(acoes)
    
    if len(acoes['criar']) == 0 and len(acoes['renomear']) == 0:
        print(f"\n{Cores.VERDE}🎉 Nada para fazer! Todos os arquivos já estão corretos.{Cores.NC}")
        sys.exit(0)
    
    # Perguntar se deseja continuar
    print()
    resposta = input(f"{Cores.AMARELO}▶ Deseja executar as renomeações? (S/N): {Cores.NC}")
    if resposta.lower() != 's':
        print(f"{Cores.VERMELHO}✗ Operação cancelada pelo usuário.{Cores.NC}")
        sys.exit(0)
    
    # ============================================
    # PASSO 4: Executar renomeações
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}⚙️ PASSO 4: Executando renomeações{Cores.NC}")
    print()
    
    total = len(acoes['criar']) + len(acoes['renomear'])
    processados = 0
    
    # Criar arquivos sem conflito
    for origem, destino in acoes['criar']:
        processados += 1
        print(f"   [{processados}/{total}] Renomeando: {origem} -> {destino}... ", end="")
        try:
            os.rename(origem, destino)
            print(f"{Cores.VERDE}OK{Cores.NC}")
        except Exception as e:
            print(f"{Cores.VERMELHO}FALHOU - {e}{Cores.NC}")
    
    # Renomear com número (conflito de tamanho)
    for origem, destino, _, _ in acoes['renomear']:
        processados += 1
        print(f"   [{processados}/{total}] Renomeando: {origem} -> {destino}... ", end="")
        try:
            os.rename(origem, destino)
            print(f"{Cores.AMARELO}RENOMEADO COM NÚMERO{Cores.NC}")
        except Exception as e:
            print(f"{Cores.VERMELHO}FALHOU - {e}{Cores.NC}")
    
    print()
    print(f"{Cores.VERDE}✓ {total} arquivos processados com sucesso!{Cores.NC}")
    pausar()
    
    # ============================================
    # PASSO 5: Verificação final
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}✅ PASSO 5: Verificação final{Cores.NC}")
    print()
    
    # Lista todos os arquivos .VCD agora
    todos_vcd = glob.glob("*.VCD")
    vcd_com_prefixo = [f for f in todos_vcd if f.startswith("SB.")]
    vcd_sem_prefixo = [f for f in todos_vcd if not f.startswith("SB.")]
    
    print(f"📊 Status final:")
    print(f"   {Cores.VERDE}✓ Arquivos com prefixo SB.: {len(vcd_com_prefixo)}{Cores.NC}")
    print(f"   {Cores.AMARELO}⚠ Arquivos sem prefixo: {len(vcd_sem_prefixo)}{Cores.NC}")
    
    if len(vcd_sem_prefixo) == 0:
        print(f"\n{Cores.VERDE}╔══════════════════════════════════════════════════════════════════════════════╗{Cores.NC}")
        print(f"{Cores.VERDE}║{Cores.NC}      🎉 TUDO PRONTO! Todos os VCDs foram renomeados! 🎉                        {Cores.VERDE}║{Cores.NC}")
        print(f"{Cores.VERDE}╚══════════════════════════════════════════════════════════════════════════════╝{Cores.NC}")
    else:
        print(f"\n{Cores.AMARELO}⚠ Ainda existem {len(vcd_sem_prefixo)} arquivos sem prefixo.{Cores.NC}")
        print(f"{Cores.AMARELO}   Execute o script novamente para processá-los.{Cores.NC}")
    
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