#!/usr/bin/env python3
# Todo: esta quase lá, so tem que listar, os jogos antes de baixar as capas

"""
Downloader de Capas para OPL/POPStarter
Baixa capas da internet baseado no GAME_ID dos jogos
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path
import time
import re

# Configurações
ART_FOLDER_NAME = "ART"
SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.webp']

def get_game_ids_from_folder(folder_path):
    """Extrai todos os GAME_IDs de uma pasta de jogos"""
    game_ids = []
    
    for file in os.listdir(folder_path):
        if file.upper().endswith(('.VCD', '.ISO')):
            # Extrair GAME_ID (formato: XXXX_XXX.XX)
            match = re.search(r'([A-Z]{4}_\d{3,4}\.\d{2})', file, re.IGNORECASE)
            if match:
                game_id = match.group(1).upper()
                # Extrair título do jogo
                title_parts = file.split(game_id, 1)
                title = title_parts[1].strip(' ._-') if len(title_parts) > 1 else game_id
                # Limpar título
                title = re.sub(r'\.VCD$|\.ISO$', '', title, flags=re.IGNORECASE)
                title = re.sub(r'[^\w\s-]', '', title).strip()
                
                game_ids.append({
                    'id': game_id,
                    'title': title,
                    'filename': file
                })
    
    return game_ids

def download_cover_from_console_roms(game_id, dest_path):
    """Tenta baixar capa do console-roms.com"""
    try:
        # URL do console-roms (ajuste conforme necessário)
        url = f"https://console-roms.com/boxart/ps2/{game_id}.jpg"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                with open(dest_path, 'wb') as f:
                    f.write(response.read())
                return True
    except:
        pass
    return False

def download_cover_from_archive(game_id, dest_path):
    """Tenta baixar capa do Internet Archive"""
    try:
        # Buscar no archive.org
        search_url = f"https://archive.org/advancedsearch.php?q={game_id}+cover&fl[]=identifier&rows=1&page=1&output=json"
        
        with urllib.request.urlopen(search_url, timeout=10) as response:
            data = json.loads(response.read())
            if data.get('response', {}).get('docs'):
                identifier = data['response']['docs'][0]['identifier']
                cover_url = f"https://archive.org/download/{identifier}/{identifier}_itemimage.jpg"
                
                req = urllib.request.Request(cover_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as img_response:
                    if img_response.status == 200:
                        with open(dest_path, 'wb') as f:
                            f.write(img_response.read())
                        return True
    except:
        pass
    return False

def create_placeholder_cover(game, dest_path, size=(300, 420)):
    """Cria uma capa placeholder para jogos sem arte"""
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        img = Image.new('RGB', size, color=(30, 30, 50))
        draw = ImageDraw.Draw(img)
        
        # Desenhar borda
        draw.rectangle([(2, 2), (size[0]-3, size[1]-3)], outline=(80, 80, 120), width=2)
        
        # Texto do ID
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        except:
            font = ImageFont.load_default()
        
        # Centralizar texto
        text = f"{game['id']}\n{game['title'][:30]}"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (size[0] - text_width) // 2
        y = (size[1] - text_height) // 2
        
        draw.text((x, y), text, fill=(200, 200, 220), font=font)
        
        img.save(dest_path, 'JPEG', quality=85)
        return True
    except Exception as e:
        print(f"   ⚠️ Erro ao criar placeholder: {e}")
        return False

def download_all_covers(hd_path, dry_run=True, create_placeholders=False):
    """Baixa capas para todos os jogos encontrados"""
    hd_path = Path(hd_path)
    
    # Encontrar pastas de jogos
    game_folders = []
    for folder in ['POPS', 'DVD', 'CD']:
        folder_path = hd_path / folder
        if folder_path.exists():
            game_folders.append(folder_path)
    
    if not game_folders:
        print("❌ Nenhuma pasta de jogos encontrada (POPS/DVD/CD)")
        return
    
    # Criar pasta ART se não existir
    art_folder = hd_path / ART_FOLDER_NAME
    art_folder.mkdir(exist_ok=True)
    
    print(f"\n🎨 Baixando capas para: {hd_path}")
    print(f"📁 Pasta de artes: {art_folder}")
    print("=" * 70)
    
    all_games = []
    for folder in game_folders:
        games = get_game_ids_from_folder(folder)
        all_games.extend(games)
        print(f"\n📂 {folder.name}: {len(games)} jogos")
    
    print(f"\n📊 Total de jogos encontrados: {len(all_games)}")
    print("=" * 70)
    
    downloaded = 0
    existing = 0
    placeholders = 0
    
    for i, game in enumerate(all_games):
        game_id = game['id']
        cover_path = art_folder / f"{game_id}.jpg"
        
        # Pular se já existe
        if cover_path.exists():
            existing += 1
            if i % 50 == 0:
                print(f"   ⏭️ {game_id} - já existe")
            continue
        
        if dry_run:
            print(f"   🔍 {game_id} - {game['title'][:40]}")
            continue
        
        # Tentar baixar
        print(f"   📥 {game_id} - {game['title'][:40]}...", end=' ')
        
        success = False
        
        # Tentar diferentes fontes
        success = download_cover_from_console_roms(game_id, cover_path)
        
        if not success:
            success = download_cover_from_archive(game_id, cover_path)
        
        if success:
            downloaded += 1
            print("✅")
        elif create_placeholders:
            if create_placeholder_cover(game, cover_path):
                placeholders += 1
                print("🎨 (placeholder)")
            else:
                print("❌")
        else:
            print("❌")
        
        # Pequena pausa para não sobrecarregar
        time.sleep(0.5)
        
        # Mostrar progresso a cada 10 jogos
        if (i + 1) % 10 == 0:
            print(f"\n   Progresso: {i+1}/{len(all_games)} jogos processados\n")
    
    print("\n" + "=" * 70)
    print("📊 RESUMO:")
    print(f"   ✅ Jogos encontrados: {len(all_games)}")
    print(f"   📸 Capas existentes: {existing}")
    if not dry_run:
        print(f"   ⭐ Capas baixadas: {downloaded}")
        if create_placeholders:
            print(f"   🎨 Placeholders criados: {placeholders}")
        print(f"   📁 Pasta de artes: {art_folder}")
    else:
        print("\n💡 Execute com --apply para baixar as capas")
        print("💡 Execute com --placeholders para criar placeholders")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Baixa capas para jogos OPL/POPStarter usando GAME_ID',
        epilog='Exemplo: python3 download_covers.py "/media/alace/My Passport/"'
    )
    parser.add_argument('path', help='Caminho da pasta raiz do HD')
    parser.add_argument('--apply', action='store_true', 
                       help='Baixa as capas (padrão é apenas simular)')
    parser.add_argument('--placeholders', action='store_true',
                       help='Cria placeholders para jogos sem capa')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.path):
        print(f"❌ Erro: Caminho não existe: {args.path}")
        sys.exit(1)
    
    download_all_covers(args.path, 
                       dry_run=not args.apply,
                       create_placeholders=args.placeholders)

if __name__ == '__main__':
    main()