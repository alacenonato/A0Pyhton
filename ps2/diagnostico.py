#!/usr/bin/env python3
import os
from pathlib import Path

def verificar_estrutura(pasta):
    """Verifica a estrutura de pastas e procura jogos"""
    print(f"\n🔍 ANALISANDO: {pasta}")
    print("=" * 60)
    
    if not os.path.exists(pasta):
        print(f"❌ Pasta não existe: {pasta}")
        return
    
    print(f"✅ Pasta existe: {pasta}")
    print(f"🔓 Permissão de leitura: {os.access(pasta, os.R_OK)}\n")
    
    # Listar tudo na pasta
    try:
        itens = os.listdir(pasta)
        print(f"📁 Conteúdo da pasta ({len(itens)} itens):")
        for item in sorted(itens):
            full_path = os.path.join(pasta, item)
            if os.path.isdir(full_path):
                print(f"   📂 {item}/")
                # Verificar subpastas comuns de jogos
                if item.upper() in ['POPS', 'DVD', 'CD', 'GAMES', 'ISO', 'PS2', 'PS1']:
                    print(f"      🎮 Pasta de jogos detectada!")
                    # Contar arquivos dentro
                    try:
                        sub_itens = os.listdir(full_path)
                        jogos = [x for x in sub_itens if x.lower().endswith(('.iso', '.vcd', '.bin', '.img'))]
                        print(f"      📊 Encontrados {len(jogos)} arquivos de jogo")
                        for jogo in jogos[:5]:  # Mostrar 5 primeiros
                            print(f"         - {jogo}")
                        if len(jogos) > 5:
                            print(f"         ... e mais {len(jogos)-5} jogos")
                    except:
                        pass
            else:
                # Verificar se é arquivo de jogo na raiz
                if item.lower().endswith(('.iso', '.vcd', '.bin', '.img')):
                    print(f"   🎮 {item} (JOGO NA RAIZ)")
                else:
                    print(f"   📄 {item}")
    except PermissionError:
        print("❌ Sem permissão para ler a pasta!")
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    # Analisar o caminho que você usou
    caminho = "/media/alace/My Passport/"
    verificar_estrutura(caminho)
    
    # Também analisar subpastas comuns
    print("\n" + "=" * 60)
    print("🔍 VERIFICANDO SUBPASTAS COMUNS:")
    
    subpastas = ["POPS", "DVD", "CD", "GAMES", "ISO", "PS2", "PS1"]
    for sub in subpastas:
        sub_path = os.path.join(caminho, sub)
        if os.path.exists(sub_path):
            verificar_estrutura(sub_path)