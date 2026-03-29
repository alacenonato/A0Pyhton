while True:
    try:
        numero = int(input("\nDigite um número: "))

        print("\n" + "="*20)
        print(f"Tabuada do {numero}")
        print("="*20)

        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
        
        opcao = input("\nDeseja continuar? (s/n): ").lower()

        if opcao != 's':
            break

    except ValueError:
        print("❌ Digite um número válido!")