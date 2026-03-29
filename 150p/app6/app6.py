
numero = int(input("Digite um número: "))

if numero <= 1:
    print("Não é primo")
else:
    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False 
            break
    
    if primo:
        print("É primo")
    else:
        print("Não é primo")
        