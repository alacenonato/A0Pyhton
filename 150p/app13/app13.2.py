import time
import threading
import os

tempo = 0
rodando = False
executando = True

lock = threading.Lock()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cronometro():
    global tempo, rodando, executando
    while executando:
        if rodando:
            time.sleep(1)
            with lock:
                tempo += 1
        else:
            time.sleep(0.1)


def formatar_tempo(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def display():
    global executando
    while executando:
        limpar_tela()
        with lock:
            tempo_formatado = formatar_tempo(tempo)

        print("=== CRONÔMETRO ===\n")
        print(f"Tempo: {tempo_formatado}\n")
        print("(i) iniciar | (p) pausar | (r) resetar | (s) sair")
        print("\nDigite um comando abaixo:\n")

        time.sleep(0.3)


# Threads
thread_cronometro = threading.Thread(target=cronometro, daemon=True)
thread_display = threading.Thread(target=display, daemon=True)

thread_cronometro.start()
thread_display.start()


# Loop principal (input separado)
while True:
    comando = input("> ").lower()

    if comando == "i":
        rodando = True

    elif comando == "p":
        rodando = False

    elif comando == "r":
        with lock:
            tempo = 0

    elif comando == "s":
        executando = False
        break

# Finalização
thread_cronometro.join(timeout=1)
thread_display.join(timeout=1)

print("\nEncerrado.")