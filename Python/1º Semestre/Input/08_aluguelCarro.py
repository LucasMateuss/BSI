print("\nAluguel do carro")
km = float(input("\nDigite quantos km foram percorridos: "))
dias = int(input("Digite quantos dias o carro ficou alugado: "))
custo_km = km * 0.15
custo_dia = dias * 60
custo_total = custo_km + custo_dia
print(f"\nO valor total a ser pago é de R${round(custo_total, 2)} reais")