def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisção por zero!"
    return a / b
    
print("=== CALCULADOR ===")
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
operacao = input("Escolah a operação (+, -, *, /)")

if operacao == "+":
    resultado = somar(num1, num2)
elif operacao == "-":
    resultado = subtrair(num1, num2)
elif operacao == "*":
    resultado = multiplicar(num1, num2)
elif operacao == "/":
    resultado = dividir(num1, num2)
else:
    resultado = "Operação inválida!"

print("Resultado:", resultado)
