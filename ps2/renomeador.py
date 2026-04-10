#!/usr/bin/env python3
"""
Extrator de GAME_ID de arquivos ISO/VCD para PS2/PS1
Útil para corrigir nomes de jogos para funcionar com OPL/POPStarter
"""

import os
import sys
import struct
from pathlib import Path

def extract_game_id_from_iso(file_path):
    """Extrai o GAME_ID de um arquivo ISO de PS2"""
    try:
        with open(file_path, 'rb') as f:
            # SYSTEM.CNF está no setor 10 do ISO (setor = 2048 bytes)
            f.seek(10 * 2048)
            data = f.read(2048)
            
            # Procurar por BOOT2 = cdrom0:\XXX_XXX.XX;1
            import re
            match = re.search(r'BOOT2 = cdrom0:\\([A-Z0-9_]+\.\d{2});1', data.decode('latin-1', errors='ignore'))
            if match:
                return match.group(1)
            
            # Fallback: procurar padrão de ID no início do arquivo
            f.seek(0)
            header = f.read(1024)
            match = re.search(r'([A-Z]{4}_\d{3,4}\.\d{2})', header.decode('latin-1', errors='ignore'))
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")
    
    return None

def extract_game_id_from_vcd(file_path):
    """Extrai o GAME_ID de um arquivo VCD de PS1"""
    try:
        with open(file_path, 'rb') as f:
            # VCD tem a estrutura do POPS
            f.seek(0)
            data = f.read(2048)
            
            import re
            # Procurar por padrão de ID PS1 (ex: SCUS_941.94)
            match = re.search(r'([A-Z]{4}_\d{3,4}\.\d{2})', data.decode('latin-1', errors='ignore'))
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")
    
    return None

def fix_game_name(file_path, dry_run=True):
    """Corrige o nome do arquivo baseado no GAME_ID extraído"""
    file_path = Path(file_path)
    
    if not file_path.exists():
        return None
    
    # Determinar tipo e extrair ID
    ext = file_path.suffix.lower()
    if ext == '.iso':
        game_id = extract_game_id_from_iso(file_path)
    elif ext == '.vcd':
        game_id = extract_game_id_from_vcd(file_path)
    else:
        return None
    
    if not game_id:
        print(f"⚠️ Não foi possível extrair ID de: {file_path.name}")
        return None
    
    # Extrair título original se disponível
    title = file_path.stem
    # Remover sufixos comuns (PT-BR, Dublado, etc)
    title = title.replace('_PT-BR', '').replace('_Dublado', '').replace('_Legendado', '')
    
    # Novo nome: GAME_ID.TITLE.ext
    new_name = f"{game_id}.{title}{ext}"
    new_path = file_path.parent / new_name
    
    if dry_run:
        print(f"📋 Simulação:")
        print(f"   Antigo: {file_path.name}")
        print(f"   Novo:   {new_name}")
        print(f"   ID:     {game_id}")
        return new_path
    
    # Renomear
    try:
        file_path.rename(new_path)
        print(f"✅ Renomeado: {file_path.name} -> {new_name}")
        return new_path
    except Exception as e:
        print(f"❌ Erro ao renomear: {e}")
        return None

def scan_and_fix_folder(folder_path, dry_run=True):
    """Escaneia uma pasta e corrige todos os jogos"""
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Pasta não encontrada: {folder_path}")
        return
    
    print(f"\n📁 Escaneando: {folder_path}")
    print("=" * 60)
    
    fixed_count = 0
    extensions = ['.iso', '.vcd']
    
    for file_path in folder.iterdir():
        if file_path.suffix.lower() in extensions:
            result = fix_game_name(file_path, dry_run)
            if result:
                fixed_count += 1
    
    print("=" * 60)
    print(f"📊 Total: {fixed_count} jogos processados")
    
    if dry_run:
        print("\n💡 Execute com --apply para aplicar as alterações")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Extrai GAME_ID e renomeia arquivos ISO/VCD')
    parser.add_argument('path', help='Caminho da pasta com os jogos')
    parser.add_argument('--apply', action='store_true', help='Aplica as alterações (dry-run padrão)')
    
    args = parser.parse_args()
    
    scan_and_fix_folder(args.path, dry_run=not args.apply)

if __name__ == '__main__':
    main()
    