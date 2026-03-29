def c_para_f(c):
    return (c * 9/5) + 32

def f_para_c(f):
    return (f - 32) * 5/9

def c_para_k(c):
    return c + 273.15

def k_para_c(k):
    return k - 273.15

def converter(temp, origem, destino):
    if origem == "C" and destino == "F":
        return c_para_f(temp)
    elif origem == "F" and destino == "C":
        return f_para_c(temp)
    elif origem == "C" and destino == "K":
        return c_para_k(temp)
    elif origem == "K" and destino == "C":
        return k_para_c(temp)
    elif origem == "F" and destino == "K":
        return c_para_k(f_para_c(temp))
    elif origem == "K" and destino == "F":
        return c_para_f(k_para_c(temp))
    else:
        return None


print("=== Conversor de Temperatura ===")

temp = float(input("Digite a temperatura: "))
origem = input("Origem (C/F/K): ").upper()
destino = input("Destino (C/F/K): ").upper()

resultado = converter(temp, origem, destino)

if resultado is not None:
    print(f"Resultado: {resultado:.2f} {destino}")
else:
    print("Conversão inválida!")