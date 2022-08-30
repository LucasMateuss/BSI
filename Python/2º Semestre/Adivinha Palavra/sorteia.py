from random import choice
import unidecode

def sorteia(p):
    p = choice(p)
    return p

def format(p):
    p = p.lower()
    p = unidecode.unidecode(p)
    p = p.strip()
    return p


