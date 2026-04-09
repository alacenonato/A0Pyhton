import time
import os
import threading
import sys

# ==================================
# CONFIG SOM (cross-platform)
# ==================================
def tocar_som():
    try:
        if os.name == 'nt':
            import winsound
            winsound.Beep(1000, 1000)
        else:
            print('\a') # beep simples no Linux

    except:
        pass

# =================================
# LIMPAR TELA 
# =================================
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# =================================
# FORMATAR TEMPO
# =================================
def formatar_tempo(segundos):
    minutos = segundos // 60
    segundos_restantes = segundos % 60
    return f"{minutos:02d}:{segundos_restantes:02d}"

# =================================
# CONTROLE DE PAUSA
# =================================
pausado = False

def escutar_tecla():
    global pausado
    while True:
        tecla = input()
        if tecla.lower() == 'p':
            pausado = not pausado

# ================================
# CONTADOR
# ================================
def contador_regressivo(total_segundos, mensagem_final):
    global pausado

    # Thread para escutar tecla
    thread = threading.Thread(targer= escutar_tecla, daemon=True)
    thread.start()

    while total_segundos > 0:
        if not pausado:
            limpar_tela()
            print("CONTADOR REGRESSIVO")
            print("-------------------")
            print(f"Tempo restante: {formatar_tempo(total_segundos)}")
            print("\nPressione 'P' + ENTER para pausar/continuar")
            time.sleep(1)
            total_segundos -= 1
        else:
            print("PAUSADO... pressione 'P' + ENTER para continuar")
            time.sleep(1)

    limpar_tela()
    print("TEMPO ESGOTADO!")
    print("* {mensagem_final}")
    tocar_som()

# ================================
# MAIN
# ================================
def main():
    try:
        minutos = int(input("Digite os minutos: "))
        segundos = int(input("Digite os segundos: "))

        total = minutos * 60 + segundos

        if total <= 0:
            print("Digite um tempo válido!")
            return

        mensagem = input("Mensagem final: ")

        contador_regressivo(total, mensagem)
    
    except ValueError:
        print("Entrada inválida! Digite números.")

if __name__ == "__main__":
    main()
