print("\nSalário Liquido")
ganho_hora = float(input("\nDigite quando ganha por hora: "))
hora_trabalho = int(input("Digite quantos horas trabalha por mês: "))
salario_bruto = ganho_hora * hora_trabalho
descontos = (salario_bruto * 0.08) + (salario_bruto * 0.11) + (salario_bruto * 0.05)
salario_liquido = salario_bruto - descontos
print(f"\nO salário líquido é R${salario_liquido} reais")