print("\nNota final do aluno")
p1 = float(input("\nDigite a nota da primeira prova: "))
p2 = float(input("Digite a nota da segunda prova: "))
e1 = float(input("Digite a nota do primeiro exercício: "))
e2 = float(input("Digite a nota do segundo exercício: "))
media_final = (p1 * 7 + p2 * 7 + e1 * 3 + e2 * 3) / (7 + 7 +3 + 3)
if media_final >= 7:
    print(f"\nO aluno foi aprovado com uma média de {round(media_final, 1)}")
else:
    print(f"\nO aluno foi reprovado com uma média de {round(media_final, 1)}") 
