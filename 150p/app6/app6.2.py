import math

# -----------------------------
# Função: verificar se é primo
# -----------------------------

def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
        
    return True

# -----------------------------
# Função: listar divisores
# -----------------------------

def listar_divisores(numero):
    divisores = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    
    return divisores

# -----------------------------
# Função: contar primos até N
# -----------------------------

def contar_primos(limite):
    contador = 0

    for i in range(2, limite + 1):
        if eh_primo(i):
            contador += 1

    return contador

# -----------------------------
# MENU PRINCIPAL
# -----------------------------

def menu():
    while True:
        print("\n===== VERIFICADOR DE NÚMEROS PRIMOS =====")
        print("1 - Verificar um número")
        print("2 - Verificar vários números")
        print("3 - Contar primos até N")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        # -----------------------------
        # OPÇÃO 1
        # -----------------------------

        if opcao == "1":
            numero = int(input("Digite um número:"))

            if eh_primo(numero):
                print(f"{numero} é PRIMO ✅")
            else:
                print(f"{numero} NÃO é primo ❌")

            divisores = listar_divisores(numero)
            print(f"Divisores: {divisores}")

        # -----------------------------
        # OPÇÃO 2
        # -----------------------------
        elif opcao == "2":
            entrada = input("Digite números separados por vírgula: ")
            numeros = [int(n.strip()) for n in entrada.split(",")]

            for numero in numeros:
                if eh_primo(numero):
                    resultado = "PRIMO ✅"
                else:
                    resultado = "NÃO primo ❌"

                divisores = listar_divisores(numero)
                print(f"\nNúmero: {numero}")
                print(f"Resultado: {resultado}")
                print(f"Divisores: {divisores}")

       # -----------------------------
        # OPÇÃO 3
        # -----------------------------
        elif opcao == "3":
            limite = int(input("Contar primos até: "))
            total = contar_primos(limite)

            print(f"Existem {total} números primos até {limite}")

        # -----------------------------
        # SAIR
        # -----------------------------
        elif opcao == "0":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida!")


# -----------------------------
# EXECUÇÃO
# -----------------------------
menu()