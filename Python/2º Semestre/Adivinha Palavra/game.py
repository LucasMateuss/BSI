from listas import cidades
from listas import filmes
from listas import paises
from listas import frutas
from listas import animo
from sorteia import sorteia
from sorteia import format
from embaralha import embaralha

print("=" * 40)
escolha = int(
    input(
        """Digite o tema que você deseja: 
[ 1 ] Cidades
[ 2 ] Filmes
[ 3 ] Países
[ 4 ] Frutas
Escolha: """
    )
)
print("=" * 40)
dificuldade = int(
    input(
        """Digite a dificuldade que você deseja: 

[ 1 ] Fácil
[ 2 ] Normal
[ 3 ] Díficil
Escolha: """
    )
)
print("=" * 40)

if escolha == 1:
    palavra = cidades[dificuldade - 1]
elif escolha == 2:
    palavra = filmes[dificuldade - 1]
elif escolha == 3:
    palavra = paises[dificuldade - 1]
elif escolha == 4:
    palavra = frutas[dificuldade - 1]

palavraSort = sorteia(palavra)
palavraSortFormat = format(palavraSort)
palavraMistu = embaralha(palavraSortFormat)
tentativas = 0
chances = 5
chute = ""
print(palavraSortFormat)
print("=" * 40)
print(f'A palavra embaralhada é "{palavraMistu}"')
print("=" * 40)
while chances > 0 and chute != palavraSortFormat:
    print(f"\nVocê Possui {chances} Chance(s)")
    chute = str(input("\nDigite seu chute: "))
    chute = format(chute)
    if chute == palavraSortFormat:
        tentativas += 1
        if tentativas == 5:
            print(
                f"\nUFA, Essa foi por pouco\nA palavra era {palavraSort}\nVocê acertou em {tentativas} tentativas"
            )
        else:
            print(
                f"\nParabéns!!!!\nA palavra era {palavraSort}\nVocê acertou em {tentativas} tentativa(s)"
            )
    else:
        tentativas += 1
        chances -= 1
        if chances > 0:
            print(f"\n{sorteia(animo)}")
if chances == 0:
    print(f"\nInfelizmente Você Perdeu :(\nA palavra era {palavraSort}")
