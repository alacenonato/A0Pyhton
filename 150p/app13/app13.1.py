import time
import threading
import os

tempo = 0
rodando = False

def limpar_tela():
    os.system('clear')


def cronometro():
    global tempo, rodando
    while True:
        if rodando:
            time.sleep(1)
            tempo += 1
            print(f"\rTempo: {tempo}s| Digite: ", end="")

thread = threading.Thread(target=cronometro, daemon=True)
thread.start()

while True:
    print("\nCronômetro Super-Chique....!")
    comando = input("\t\t\t | (i)niciar | (p)ausar | (r)esetar | (s)air | ").lower()
    limpar_tela()
    if comando == "i":
        print("Iniciando...")
        rodando = True

    elif comando == "p":
        print("Pausado...")
        rodando = False

    elif comando == "r":
        print("Resetado")
        tempo = 0

    elif comando == "s":
        print("Saindo...")
        break