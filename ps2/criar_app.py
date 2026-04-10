#!/usr/bin/env python3
import os
import glob

# Pasta raiz do HD (onde ficam POPS e APPS)
raiz = "/media/alace/My Passport"

# Pasta APPS
apps_dir = os.path.join(raiz, "APPS")
os.makedirs(apps_dir, exist_ok=True)

# Pega todos os arquivos .VCD
vcd_files = glob.glob("*.VCD")

print(f"📂 Criando estrutura APPS para {len(vcd_files)} jogos...")
print()

criados = 0
for vcd in vcd_files:
    # Nome base do jogo (sem extensão)
    nome_base = vcd[:-4]  # remove .VCD
    
    # Nome do ELF correspondente
    elf_name = f"SB.{nome_base}.ELF"
    
    # Verifica se o ELF existe
    if not os.path.exists(elf_name):
        print(f"⚠ Aviso: {elf_name} não encontrado para {vcd}")
        continue
    
    # Nome amigável para a pasta (remove o código do jogo)
    # Ex: "SCUS_941.94.Gran Turismo" -> "Gran Turismo"
    partes = nome_base.split('.', 2)
    if len(partes) >= 3:
        nome_jogo = partes[2].strip()
    else:
        nome_jogo = nome_base
    
    # Remove caracteres problemáticos para nome de pasta
    nome_jogo = nome_jogo.replace('/', '_').replace('\\', '_')
    
    # Pasta do jogo em APPS
    jogo_dir = os.path.join(apps_dir, nome_jogo)
    os.makedirs(jogo_dir, exist_ok=True)
    
    # Copia o ELF para a pasta
    import shutil
    shutil.copy2(elf_name, os.path.join(jogo_dir, elf_name))
    
    # Cria o title.cfg
    with open(os.path.join(jogo_dir, "title.cfg"), "w") as f:
        f.write(f"title={nome_jogo}\n")
        f.write(f"boot={elf_name}\n")
    
    print(f"✅ {nome_jogo}")
    criados += 1

print()
print(f"🎉 {criados} jogos configurados na pasta APPS!")
print(f"📁 Local: {apps_dir}")
