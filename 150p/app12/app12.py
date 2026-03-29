nome = input("Digite o nome do aluno:")

nota1 = float(input("Digite a primeia nota: " ))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

print(f"\Aluno: {nome}")
print(f"Média: {media:.2f}")

if media >= 7:
    print("Status: Aprovado ✅")
elif media >= 5:
    print("Status: Recuperação ⚠️")
else:
    print("Status: Reprovado ❌")