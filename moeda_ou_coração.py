from random import randint

def choices(MAX_WIDTH):
    tipo_obstaculo = randint(0,1)
    if tipo_obstaculo == 0:
        moeda_x = MAX_WIDTH + randint(600, 2000)
        coracao_x = 5000
        return [moeda_x, coracao_x]
    elif tipo_obstaculo == 1:
        coracao_x = MAX_WIDTH + randint(600,2000)
        moeda_x = 5000
        return [moeda_x, coracao_x]