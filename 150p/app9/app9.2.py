def gerar_tabuada(numero, inicio, fim):
    print("\n" + "="*25)
    print(f"     TABUADA DO {numero}")
    print("="*25)

    for i in range(inicio, fim + 1):
        print(f"{numero} x {i} = {numero * i}")


def tabuada_completa(inicio, fim):
    print("\n" + "="*25)
    print("   TABUADA COMPLETA (1 a 10)")
    print("="*25)

    for n in range(1, 11):
        print("\n" + "-"*20)
        print(f"Tabuada do {n}")
        print("-"*20)
        for i in range(inicio, fim + 1):
            print(f"{n} x {i} = {n * i}")


while True:
    try:
        print("\n" + "="*30)
        print("      SISTEMA DE TABUADA")
        print("="*30)
        print("1 - Tabuada de um número")
        print("2 - Tabuada completa (1 a 10)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Encerrando...")
            break

        elif opcao in ['1', '2']:
            inicio = int(input("Início da tabuada: "))
            fim = int(input("Fim da tabuada: "))

            if inicio > fim:
                print("❌ O início não pode ser maior que o fim!")
                continue

            if opcao == '1':
                numero = int(input("Digite o número: "))
                gerar_tabuada(numero, inicio, fim)

            elif opcao == '2':
                tabuada_completa(inicio, fim)

        else:
            print("❌ Opção inválida!")

        continuar = input("\nDeseja continuar? (s/n): ").lower()
        if continuar != 's':
            print("Finalizando sistema...")
            break

    except ValueError:
        print("❌ Digite apenas números válidos!")