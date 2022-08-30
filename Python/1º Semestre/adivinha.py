from random import randint
print("\nAdivinha número")
numero = randint(1, 100)
chute = 0
nr_tentativas = 7
tentativas = 1
while numero != chute and tentativas <= nr_tentativas:
    chute = int(input("\nQue número eu pensei? "))
    if chute == numero:
        print("Acertou")
    else:
        if numero > chute: 
            print("Número é maior.")
        else:
            print("Número é menor.")
    tentativas = tentativas + 1 
print("\nO número que eu pensei é: ", numero)