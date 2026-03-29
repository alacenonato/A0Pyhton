numero = int(input("Digite um numero para ver a tabuada: ")
             )

print("\nTabuada do {numero}: \n")

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")