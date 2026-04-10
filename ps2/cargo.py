#!/usr/bin/env python3
"""
Script para processar arquivos .VCD de PSX usando psx-vcd
Equivalente ao script bash original
"""

import os
import subprocess
import sys
import re
from pathlib import Path

def print_step(step_num, description):
    """Função para exibir etapas do processo"""
    print(f"\n{'='*60}")
    print(f"PASSO {step_num}: {description}")
    print(f"{'='*60}")

def run_command(cmd, description):
    """Executa um comando e mostra o que está acontecendo"""
    print(f"\n▶ Executando: {cmd}")
    print(f"  → {description}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, 
                              capture_output=True, text=True)
        if result.stdout:
            print(f"  ✓ Saída: {result.stdout[:200]}...")  # Mostra apenas início
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Erro: {e}")
        if e.stderr:
            print(f"    Detalhes: {e.stderr}")
        return False

def main():
    """Função principal"""
    
    # Mostra diretório atual
    print(f"Diretório atual: {os.getcwd()}")
    
    # PASSO 1: Mudar para o diretório alvo
    print_step(1, "Mudando para o diretório '/media/alace/My Passport/POPS'")
    target_dir = "/media/alace/My Passport/POPS"
    
    if not os.path.exists(target_dir):
        print(f"✗ ERRO: Diretório '{target_dir}' não encontrado!")
        print("  Verifique se o disco está montado corretamente.")
        sys.exit(1)
    
    os.chdir(target_dir)
    print(f"✓ Mudou para: {os.getcwd()}")
    print(f"  Conteúdo atual: {len(os.listdir('.'))} arquivos/pastas")

    # PASSO 2: Instalar Rust (se necessário)
    print_step(2, "Instalando Rust (se não estiver instalado)")
    
    # Verifica se cargo/rust está instalado
    try:
        subprocess.run(["cargo", "--version"], capture_output=True, check=True)
        print("✓ Rust/Cargo já está instalado!")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠ Rust não encontrado. Instalando Rust...")
        print("  Isso pode levar alguns minutos...")
        
        # Instala Rust
        rust_install_cmd = 'curl --proto "=https" --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y'
        print(f"  Comando: {rust_install_cmd}")
        
        # Adiciona cargo ao PATH para esta sessão
        subprocess.run(rust_install_cmd, shell=True, check=True)
        
        # Carrega ambiente Rust
        home = Path.home()
        cargo_env = home / ".cargo" / "env"
        if cargo_env.exists():
            with open(cargo_env) as f:
                exec(f.read())
        
        print("✓ Rust instalado com sucesso!")
    
    # PASSO 3: Instalar psx-vcd
    print_step(3, "Instalando psx-vcd via Cargo")
    
    # Verifica se psx-vcd já está instalado
    try:
        subprocess.run(["psx-vcd", "--version"], capture_output=True, check=True)
        print("✓ psx-vcd já está instalado!")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠ Instalando psx-vcd...")
        if run_command("cargo install psx-vcd", "Instalando pacote psx-vcd"):
            print("✓ psx-vcd instalado com sucesso!")
        else:
            print("✗ Falha ao instalar psx-vcd")
            sys.exit(1)
    
    # PASSO 4: Processar arquivos .VCD
    print_step(4, "Processando arquivos .VCD")
    
    # Encontra todos os arquivos .VCD (case-sensitive)
    vcd_files = [f for f in os.listdir('.') if f.endswith('.VCD')]
    
    if not vcd_files:
        print("⚠ Nenhum arquivo .VCD encontrado no diretório atual")
        print(f"  Arquivos presentes: {os.listdir('.')[:10]}")  # Mostra primeiros 10
    else:
        print(f"✓ Encontrados {len(vcd_files)} arquivo(s) .VCD")
        
        for i, vcd_file in enumerate(vcd_files, 1):
            print(f"\n  [{i}/{len(vcd_files)}] Processando: {vcd_file}")
            print(f"  → Executando: psx-vcd auto \"{vcd_file}\" -o ./")
            
            try:
                # Executa psx-vcd para cada arquivo
                result = subprocess.run(
                    ["psx-vcd", "auto", vcd_file, "-o", "./"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                
                if result.stdout:
                    # Mostra linhas relevantes da saída
                    for line in result.stdout.split('\n')[:5]:
                        if line.strip():
                            print(f"    {line}")
                
                print(f"  ✓ {vcd_file} processado com sucesso!")
                
            except subprocess.CalledProcessError as e:
                print(f"  ✗ Erro ao processar {vcd_file}")
                if e.stderr:
                    print(f"    Mensagem: {e.stderr[:200]}")
    
    # PASSO 5: Verificar resultados
    print_step(5, "Verificando resultados - arquivos com padrões de PSX")
    
    # Padrões de nomes de jogos PSX
    psx_patterns = ['SLUS', 'SLES', 'SCUS', 'SLPS']
    
    # Lista todos os arquivos
    all_files = os.listdir('.')
    
    # Filtra arquivos que correspondem aos padrões
    matched_files = []
    for pattern in psx_patterns:
        for file in all_files:
            if pattern in file.upper():
                matched_files.append(file)
    
    if matched_files:
        print(f"\n✓ Encontrados {len(matched_files)} arquivo(s) com padrões PSX:")
        for file in matched_files:
            # Mostra detalhes do arquivo
            file_path = Path(file)
            if file_path.exists():
                size = file_path.stat().st_size
                size_mb = size / (1024 * 1024)
                print(f"  • {file} ({size_mb:.2f} MB)")
    else:
        print("\n⚠ Nenhum arquivo com padrões PSX encontrado")
        print(f"  Padrões procurados: {', '.join(psx_patterns)}")
        
        # Mostra alguns arquivos que foram criados/modificados recentemente
        print("\n  Últimos 5 arquivos modificados no diretório:")
        files_with_mtime = [(f, Path(f).stat().st_mtime) for f in all_files]
        files_with_mtime.sort(key=lambda x: x[1], reverse=True)
        
        for file, mtime in files_with_mtime[:5]:
            print(f"    - {file}")
    
    print_step(6, "Processo concluído")
    print(f"✓ Script finalizado. Diretório atual: {os.getcwd()}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Script interrompido pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Erro inesperado: {e}")
        sys.exit(1)