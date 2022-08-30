# Crie um jogo que embaralhe uma palavra e a mostre ao jogador. O objetivo é acertar a palavra em até 5 tentativas. Informe sempre quantas tentativas ele ainda tem. Se ele acertar, dê os parabéns; se errar dê uma palavra de ânimo (que mude de forma aleatória). Ao final, mostre a palavra correta e o número de tentativas que ele utilizou.

from random import sample
from random import choice

palavras = ['Banana', 'Morango', 'Uva', 'Kiwi', 'Melancia', 'Laranja', 'Tangerina']
animo = ['Não Desista', 'Você Consegue na Próxima', 'Continue Tentando', 'A única forma de chegar ao impossível é acreditar que é possível', 'Você é capaz', 'Você é capaz', 'Continue firme', 'Busque sempre o progresso, não a perfeição', 'Não tenha medo, cada falha é um novo aprendizado, é uma forma de você fazer melhor da próxima vez', 'A tentação de desistir será um pouco maior antes de você estar prestes a conseguir', 'Se você pode sonhar, você pode realizar']
p = choice(palavras).lower()
e = ''.join(sample(p, len(p)))  
tentativas = 0
chances = 5
chute = ''
print('=' * 40)
print(f'A palavra embaralhada é "{e}"')
print('=' * 40)
while chances > 0 and chute != p:
    print(f'\nVocê Possui {chances} Chances')
    chute = str(input('\nDigite seu chute: ')).lower().strip()
    if chute == p:
        tentativas += 1
        if tentativas == 5:
            print(f'\nUFA, Essa foi por pouco\nA palavra era {p}\nVocê acertou em {tentativas} tentativas')
        else:
            print(f'\nParabéns!!!!\nA palavra era {p}\nVocê acertou em {tentativas} tentativa(s)')
    else:
        tentativas += 1
        chances -= 1
        if chances > 0:
            print(f"\n{''.join(sample(animo, k=1))}")
if chances == 0:
    print(f'\nInfelizmente Você Perdeu :(\nA palavra era {p}')
