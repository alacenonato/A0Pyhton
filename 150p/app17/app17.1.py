import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def formatar_tempo(segundos):
    minutos = segundos // 60
    segundos_restantes = segundos % 60 
    return f"{minutos:02d}:{segundos_restantes:02d}"

def contador_regressivo(total_segundos):
    while total_segundos > 0:
        limpar_tela()
        print("CONTADOR REGRESSIVO")
        print("===================")
        print(f"Tempo restante: {formatar_tempo(total_segundos)}")
        time.sleep(1)
        total_segundos -= 1
    
    limpar_tela()
    print("TEMPO ESGOTADO!")

def main():
    try:
        tempo = int(input("Digite o tempo em segundos: "))
        if tempo <= 0:
            print("Digite um número positivo!")
            return

        contador_regressivo(tempo)

    except ValueError:
        print("Entrada inválida! Digite apenas números.")

if __name__ == "__main__":
    main()
