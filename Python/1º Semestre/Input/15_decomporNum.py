from random import randint
print("\nDecompõe um número inteiro")
n = randint(1, 999)
c = n // 100 % 10
d = n // 10 % 10
u = n % 10
print(f"\nO número {n} decomposto é {c,d, u}")