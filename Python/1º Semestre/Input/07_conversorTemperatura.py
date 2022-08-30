print("\nConverte uma temperatura em Celsius para Fahrenheit")
c = int(input("\nDigite a temperatura: "))
c_f = (9 * c / 5) + 32
print(f"\nEssa temperatura convertida é de {round(c_f)}F")

print("\nConverte uma temperatura em Fahrenheit para Celsius")
f = int(input("\nAgora digite uma temperatura em Fahrenheit: "))
f_c = (f - 32) * (5 / 9)
print(f"\nEssa temperatura convertida é de {round(f_c)}C")