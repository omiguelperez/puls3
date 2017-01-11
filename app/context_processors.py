from random import choice

def frases(request):
    mis_frases = [
        'La vengaza es lucrativa',
        'Sin sacrificio no hay victoria',
        'Un buen acto de vengaza merece otro'
    ]
    return { 'frase': choice(mis_frases) }
