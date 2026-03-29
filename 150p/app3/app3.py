# Conversor de Moeda

# Entrada
valor_reais = float(input("Digite o valor em reais: R$ "))

# Cotações fixas
dolar = 5.00
euro = 5.50

# Conversão
valor_dolar = valor_reais / dolar
valor_euro = valor_reais / euro

# Saída
print("\n=== Conversão ===")
print(f"Dólar: ${valor_dolar:.2f}")
print(f"Euro: €{valor_euro:.2f}")