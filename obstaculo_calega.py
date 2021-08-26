from random import randint

def obstaculo_type(MAX_WIDTH, pontuacao):
    tipo_obstaculo = randint(0,1)
    if tipo_obstaculo == 0:
        tronco_x = MAX_WIDTH + randint(0, 200)
        nave_x = 5000
        return [tronco_x, nave_x]
    elif tipo_obstaculo == 1:
        nave_x = MAX_WIDTH + randint(0,200)
        tronco_x = 5000
        return [tronco_x, nave_x,]