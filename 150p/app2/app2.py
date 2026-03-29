print("=== Conversor de Temperatura ===")
temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K:) ").upper()
destino = input("Converter para (C/F/K): ").upper()

resultado = None

if origem == "C" and destino == "F":
    resultado = (temp * 9/5) + 32
elif origem == "F" and destino == "C":
    resultado = (temp -32) * 5/9
elif origem == "C" and destino == "K":
    resultado = temp + 273.15
elif origem == "K" and destino == "C":
    resultado == temp - 273.15
elif origem == "F" and destino == "K":
    resultado = (temp - 32) * 5/9 + 273.15
elif origem == "K" and destino =="F":
    resultado == (temp - 273.15) * 9/5 + 32
else:
    print("Conversão inválida")

if resultado is not None:
    print(f"Resultado: {resultado:.2f} {destino}")