import math
print("\nDúzia de Ovos")
ovo = int(input("\nDigite o número de ovos: "))
duzia = math.ceil(ovo / 12)
if duzia > 1:
    print(f"\n{ovo} ovos são {duzia} dúzias")
else:
    print(f"\n{ovo} ovos são {duzia} dúzia")