#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import glob


# Cores para terminal (funciona no Linux)
class Cores:
    VERMELHO = '\033[0;31m'
    VERDE = '\033[0;32m'
    AMARELO = '\033[1;33m'
    AZUL = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CIANO = '\033[0;36m'
    NC = '\033[0m'  # Sem cor

def pausar():
    """Pausa e aguarda o usuário pressionar ENTER"""
    print()
    input(f"{Cores.AMARELO}▶ Pressione ENTER para continuar...{Cores.NC}")
    print()

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def cabecalho():
    """Mostra o cabeçalho do programa"""
    limpar_tela()
    print(f"{Cores.AZUL}╔══════════════════════════════════════════════════════════╗{Cores.NC}")
    print(f"{Cores.AZUL}║{Cores.NC}      {Cores.MAGENTA}CRIADOR DE ARQUIVOS ELF PARA POPSTARTER (SMB){Cores.NC}      {Cores.AZUL}║{Cores.NC}")
    print(f"{Cores.AZUL}╚══════════════════════════════════════════════════════════╝{Cores.NC}")
    print()

def barra_progresso(atual, total):
    """Mostra uma barra de progresso"""
    percent = int(atual * 100 / total) if total > 0 else 0
    preenchido = int(percent / 2)
    vazio = 50 - preenchido
    barra = "█" * preenchido + "░" * vazio
    print(f"{Cores.CIANO}[{barra}] {percent}%{Cores.NC}", end="")

def verificar_ou_mudar_pasta():
    """Verifica se está na pasta POPS ou pergunta se quer mudar"""
    pasta_atual = os.path.basename(os.getcwd())
    
    # Se já está na pasta POPS, continua
    if pasta_atual == "POPS":
        print(f"{Cores.VERDE}✓ OK: Você já está na pasta POPS!{Cores.NC}")
        return True
    
    # Se não está, pergunta o que fazer
    print(f"{Cores.AMARELO}⚠ ATENÇÃO: Você não está na pasta 'POPS'!{Cores.NC}")
    print(f"   Diretório atual: {Cores.VERMELHO}{os.getcwd()}{Cores.NC}")
    print()
    print(f"{Cores.CIANO}Opções:{Cores.NC}")
    print(f"   1 - Tentar acessar /media/alace/My Passport/POPS automaticamente")
    print(f"   2 - Digitar outro caminho manualmente")
    print(f"   3 - Continuar na pasta atual (não recomendado)")
    print(f"   0 - Sair")
    print()
    
    opcao = input(f"{Cores.AMARELO}Escolha uma opção: {Cores.NC}").strip()
    
    if opcao == "0":
        print(f"{Cores.VERMELHO}Programa encerrado.{Cores.NC}")
        sys.exit(0)
    elif opcao == "1":
        # Tenta acessar o caminho padrão
        caminho_pops = "/media/alace/My Passport/POPS"
        if os.path.exists(caminho_pops):
            os.chdir(caminho_pops)
            print(f"{Cores.VERDE}✓ Mudou para: {os.getcwd()}{Cores.NC}")
            return True
        else:
            print(f"{Cores.VERMELHO}✗ Caminho não encontrado: {caminho_pops}{Cores.NC}")
            return False
    elif opcao == "2":
        caminho_manual = input(f"{Cores.CIANO}Digite o caminho completo da pasta POPS: {Cores.NC}").strip()
        if os.path.exists(caminho_manual):
            os.chdir(caminho_manual)
            print(f"{Cores.VERDE}✓ Mudou para: {os.getcwd()}{Cores.NC}")
            return True
        else:
            print(f"{Cores.VERMELHO}✗ Caminho não encontrado: {caminho_manual}{Cores.NC}")
            return False
    elif opcao == "3":
        print(f"{Cores.AMARELO}⚠ Continuando na pasta atual... (pode dar erro){Cores.NC}")
        return True
    else:
        print(f"{Cores.VERMELHO}Opção inválida!{Cores.NC}")
        return False

def listar_elfs_criados(elfs_criados):
    """Mostra lista dos ELFs criados"""
    if not elfs_criados:
        return
    
    print(f"\n{Cores.VERDE}╔══════════════════════════════════════════════════════════╗{Cores.NC}")
    print(f"{Cores.VERDE}║{Cores.NC}           {Cores.MAGENTA}LISTA DE ARQUIVOS ELF CRIADOS{Cores.NC}              {Cores.VERDE}║{Cores.NC}")
    print(f"{Cores.VERDE}╚══════════════════════════════════════════════════════════╝{Cores.NC}")
    print()
    
    for i, elf in enumerate(elfs_criados, 1):
        # Verifica o tamanho do arquivo
        tamanho = os.path.getsize(elf) if os.path.exists(elf) else 0
        tamanho_kb = tamanho / 1024
        print(f"   {Cores.VERDE}{i:3d}{Cores.NC}. {Cores.CIANO}{elf}{Cores.NC} ({Cores.AMARELO}{tamanho_kb:.0f} KB{Cores.NC})")
    
    print()
    print(f"{Cores.VERDE}Total: {len(elfs_criados)} arquivo(s) criado(s){Cores.NC}")

def main():
    # ============================================
    # PASSO 1: Verificar/Mudar para diretório POPS
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}📁 PASSO 1: Verificando/Mudando para pasta POPS{Cores.NC}")
    print()
    
    if not verificar_ou_mudar_pasta():
        print(f"{Cores.VERMELHO}Não foi possível acessar a pasta POPS. Encerrando...{Cores.NC}")
        sys.exit(1)
    
    print(f"   Diretório atual: {Cores.VERDE}{os.getcwd()}{Cores.NC}")
    pausar()
    
    # ============================================
    # PASSO 2: Verificar POPSTARTER.ELF
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}📦 PASSO 2: Verificando arquivo POPSTARTER.ELF{Cores.NC}")
    
    if os.path.exists("POPSTARTER.ELF"):
        tamanho = os.path.getsize("POPSTARTER.ELF")
        tamanho_kb = tamanho / 1024
        print(f"{Cores.VERDE}✓ POPSTARTER.ELF encontrado!{Cores.NC}")
        print(f"   Tamanho: {Cores.AMARELO}{tamanho_kb:.0f} KB{Cores.NC}")
    else:
        print(f"{Cores.VERMELHO}✗ ERRO: POPSTARTER.ELF NÃO encontrado!{Cores.NC}")
        print("   Coloque o arquivo POPSTARTER.ELF na pasta atual e tente novamente.")
        sys.exit(1)
    
    pausar()
    
    # ============================================
    # PASSO 3: Procurar jogos .VCD
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}🎮 PASSO 3: Procurando jogos no formato .VCD{Cores.NC}")
    print()
    
    # Encontra todos os arquivos .VCD
    jogos = glob.glob("*.VCD")
    jogos.sort()
    total_jogos = len(jogos)
    
    if total_jogos == 0:
        print(f"{Cores.VERMELHO}✗ Nenhum arquivo .VCD encontrado nesta pasta!{Cores.NC}")
        sys.exit(1)
    
    print(f"{Cores.VERDE}✓ Encontrados {total_jogos} jogos!{Cores.NC}")
    print()
    print(f"{Cores.AMARELO}Lista dos primeiros 5 jogos encontrados:{Cores.NC}")
    
    for i, jogo in enumerate(jogos[:5]):
        print(f"   {Cores.VERDE}{i+1}{Cores.NC}. {jogo}")
    
    if total_jogos > 5:
        print(f"   ... e mais {total_jogos - 5} jogos")
    
    pausar()
    
    # ============================================
    # PASSO 4: Analisar ELFs existentes
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}🔍 PASSO 4: Verificando quais ELFs já existem{Cores.NC}")
    print()
    
    existentes = 0
    precisam_criar = []
    
    for vcd in jogos:
        nome_base = vcd[:-4]  # Remove .VCD
        elf_name = f"SB.{nome_base}.ELF"
        
        if os.path.exists(elf_name):
            existentes += 1
        else:
            precisam_criar.append(nome_base)
    
    novos = len(precisam_criar)
    
    print(f"📊 Resumo da análise:")
    print(f"   {Cores.VERDE}✓ ELFs já existentes: {existentes}{Cores.NC}")
    print(f"   {Cores.AMARELO}⚠ ELFs a serem criados: {novos}{Cores.NC}")
    print()
    
    if novos == 0:
        print(f"{Cores.VERDE}🎉 Todos os ELFs já existem! Nada para fazer.{Cores.NC}")
        sys.exit(0)
    
    print(f"{Cores.AMARELO}Os seguintes jogos PRECISAM de ELF:{Cores.NC}")
    for i, jogo in enumerate(precisam_criar[:10]):
        print(f"   {Cores.AMARELO}{i+1}{Cores.NC}. {jogo}")
    
    if novos > 10:
        print(f"   ... e mais {novos - 10} jogos")
    
    pausar()
    
    # ============================================
    # PASSO 5: Criar os ELFs
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}⚙️ PASSO 5: Criando arquivos ELF{Cores.NC}")
    print()
    
    criados = 0
    elfs_criados_lista = []  # Lista para armazenar os nomes dos ELFs criados
    
    for i, nome_base in enumerate(precisam_criar, 1):
        elf_name = f"SB.{nome_base}.ELF"
        
        # Mostra progresso
        print(f"   [{i}/{novos}] Criando: {elf_name[:50]}... ", end="")
        
        try:
            # Copia o arquivo
            with open("POPSTARTER.ELF", "rb") as origem:
                with open(elf_name, "wb") as destino:
                    destino.write(origem.read())
            print(f"{Cores.VERDE}OK{Cores.NC}")
            criados += 1
            elfs_criados_lista.append(elf_name)  # Adiciona à lista
        except Exception as e:
            print(f"{Cores.VERMELHO}FALHOU - {e}{Cores.NC}")
    
    print()
    barra_progresso(criados, novos)
    print()
    print(f"\n{Cores.VERDE}✓ {criados} de {novos} arquivos ELF criados com sucesso!{Cores.NC}")
    
    # Mostra a lista dos ELFs criados
    listar_elfs_criados(elfs_criados_lista)
    
    pausar()
    
    # ============================================
    # PASSO 6: Verificação final
    # ============================================
    cabecalho()
    
    print(f"{Cores.CIANO}✅ PASSO 6: Verificação final{Cores.NC}")
    print()
    
    total_elfs = len(glob.glob("SB.*.ELF"))
    
    print(f"📊 Status final:")
    print(f"   Total de jogos .VCD: {Cores.AMARELO}{total_jogos}{Cores.NC}")
    print(f"   Total de ELFs .ELF: {Cores.VERDE}{total_elfs}{Cores.NC}")
    print()
    
    # Mostra todos os ELFs existentes (criados + antigos)
    todos_elfs = glob.glob("SB.*.ELF")
    todos_elfs.sort()
    
    print(f"{Cores.CIANO}📋 Todos os arquivos ELF na pasta:{Cores.NC}")
    for i, elf in enumerate(todos_elfs, 1):
        tamanho = os.path.getsize(elf)
        tamanho_kb = tamanho / 1024
        marcador = "✓" if elf in elfs_criados_lista else "○"
        cor_marcador = Cores.VERDE if elf in elfs_criados_lista else Cores.CIANO
        print(f"   {cor_marcador}{marcador}{Cores.NC} {Cores.AMARELO}{i:3d}{Cores.NC}. {elf} ({tamanho_kb:.0f} KB)")
    
    print()
    
    if total_elfs == total_jogos:
        print(f"{Cores.VERDE}╔══════════════════════════════════════════════════════════╗{Cores.NC}")
        print(f"{Cores.VERDE}║{Cores.NC}      🎉 TUDO PRONTO! Todos os ELFs foram criados! 🎉      {Cores.VERDE}║{Cores.NC}")
        print(f"{Cores.VERDE}╚══════════════════════════════════════════════════════════╝{Cores.NC}")
    else:
        print(f"{Cores.AMARELO}⚠ ATENÇÃO: Ainda faltam {total_jogos - total_elfs} ELFs.{Cores.NC}")
    
    print()
    print(f"{Cores.CIANO}💡 Próximo passo:{Cores.NC}")
    print(f"   Teste um jogo no OPL acessando a aba {Cores.AMARELO}APPS{Cores.NC}")
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