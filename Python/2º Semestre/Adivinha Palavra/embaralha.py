from random import sample

def embaralha(e):
    e = "".join(sample(e, len(e)))
    return e 