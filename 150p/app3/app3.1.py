print("=== Conversor de Moeda ===")

valor_reais = float(input("Digite o valor em reais (R$): "))

dolar = 5.00
euro = 5.50

valor_dolar = valor_reais / dolar
valor_euro = valor_reais / euro

print("\nResultado da conversão:")
print("-" * 30)
print(f"Real: R$ {valor_reais:.2f}")
print(f"Dólar: $ {valor_dolar:.2f}")
print(f"Euro: € {valor_euro:.2f}")
print("-" * 30)