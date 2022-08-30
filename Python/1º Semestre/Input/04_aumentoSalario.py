print("\nAumento salarial")
salario = float(input("\nDigite seu salário: "))
porcentagem = float(input("Digite a porcentagem de aumento: "))
aumento = (salario * porcentagem) / 100
nv_salario = salario + aumento
print(f"\nO salário aumentou R${aumento} e o novo salário será R${nv_salario}")