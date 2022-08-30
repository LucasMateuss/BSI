import math
print("\nDias perdidos de um fumante")
fum_dia = int(input("\nQuantos cigarros são fumados por dia: "))
anos = int(input("Fuma a quantos anos: "))
ano_dia = anos * 365
cigarros_fumados = fum_dia * ano_dia * 10
dias_perdidos = cigarros_fumados / 1440
print(f"\nFumando isso um fumante perderia {math.ceil(dias_perdidos,)} dias")