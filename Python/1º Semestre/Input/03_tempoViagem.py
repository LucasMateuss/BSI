print("\nTempo de Viagem")
distancia = float(input("\nDigite a distância que será percorrida: "))
vel = float(input("Digite a velocidade média do veículo: "))
horas = distancia / vel
min = horas * 60
h, m = divmod(min, 60)
print(f"\nA viagem irá demorar {int(h)}h{int(m)}m")