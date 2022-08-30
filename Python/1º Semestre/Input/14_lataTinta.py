import math
print("\nLatas de Tinta")
metros = int(input("\nDigite quantos metros quadrados irão ser pintados: "))
lata = math.ceil(metros / 54)
if lata > 1:
    print(f"\nSerá preciso comprar {lata} latas de tinta")
else:
    print(f"\nSerá preciso comprar {lata} lata de tinta")