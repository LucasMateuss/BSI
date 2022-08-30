print("\nRecebe uma data e retorna o número de segundos")
dia = int(input("\nDigite um número de dias: "))
horas = int(input("Digite um número de horas: "))
minutos = int(input("Digite um número de minutos: "))
segundos = int(input("Digite um número de segundos:"))
ds = dia * 86400
hs = horas * 3600
ms = minutos * 60
total_segundos = ds + hs + ms + segundos 
print(f"\nO total de segundos é: {total_segundos}") 