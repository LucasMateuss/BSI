print("\nDesconto da mercadoria")
mercadoria = float(input("\nDigite o valor da mercadoria: "))
percentual = float(input("Digite o valor do desconto: "))
desconto = (mercadoria*percentual) / 100
valor_final = mercadoria - desconto
print(f"\nO desconto do produto foi de R${round(desconto, 2)} e o valor final será R${round(valor_final, 2)}")
