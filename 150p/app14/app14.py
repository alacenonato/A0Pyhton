import random

def gerar_numero(minimo, maximo):
    return random.randint(minimo, maximo)

def main():
    print("=== Gerador de Números Aleatórios ===")

    try:
        minimo = int(input("Digite o valor mínimo: "))
        maximo = int(input("Digite o valor máximo: "))

        if minimo > maximo:
            print("Erro: o valor mínimo não pose ser maior que o máximo.")
            return
        
        numero = gerar_numero(minimo, maximo)
        print(f"Número gerado: {numero}")
    
    except ValueError:
        print("Erro: digite apenas números inteiros.")

if __name__ == "__main__":
    main()
