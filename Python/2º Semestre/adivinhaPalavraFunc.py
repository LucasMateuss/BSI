from random import sample
from random import choice

palavras = ["Banana", "Morango", "Uva", "Kiwi", "Melancia", "Laranja", "Tangerina"]
animo = [
    "Não Desista",
    "Você Consegue na Próxima",
    "Continue Tentando",
    "A única forma de chegar ao impossível é acreditar que é possível",
    "Você é capaz",
    "Você é capaz",
    "Continue firme",
    "Busque sempre o progresso, não a perfeição",
    "Não tenha medo, cada falha é um novo aprendizado, é uma forma de você fazer melhor da próxima vez",
    "A tentação de desistir será um pouco maior antes de você estar prestes a conseguir",
    "Se você pode sonhar, você pode realizar",
]


def escolhe(p):
    p = choice(p).lower()
    return p


def embaralha(e):
    e = "".join(sample(e, len(e)))
    return e


palavraSort = escolhe(palavras)
palavraMistu = embaralha(palavraSort)
tentativas = 0
chances = 5
chute = ""
print("=" * 40)
print(f'A palavra embaralhada é "{palavraMistu}"')
print("=" * 40)
while chances > 0 and chute != palavraSort:
    print(f"\nVocê Possui {chances} Chance(s)")
    chute = str(input("\nDigite seu chute: ")).lower().strip()
    if chute == palavraSort:
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
            print(f"\n{escolhe(animo)}")
if chances == 0:
    print(f"\nInfelizmente Você Perdeu :(\nA palavra era {palavraSort}")
