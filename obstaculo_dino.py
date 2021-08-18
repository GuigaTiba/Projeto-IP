from random import randint

def obstaculo_type(MAX_WIDTH, pontuacao, crystal_flag):
    tipo_obstaculo = randint(0,1)
    if tipo_obstaculo == 0 and (pontuacao < 1900 or crystal_flag == 1):
        tree_x = MAX_WIDTH + randint(0, 200)
        ptero_x = 5000
        crystal_x = 5000
        return [tree_x, ptero_x, crystal_x]
    elif tipo_obstaculo == 1 and (pontuacao < 1900 or crystal_flag == 1):
        ptero_x = MAX_WIDTH + randint(0,200)
        tree_x = 5000
        crystal_x = 5000
        return [tree_x, ptero_x, crystal_x]
    elif pontuacao > 1500 and crystal_flag == 0:
        ptero_x = 5000
        tree_x = 5000
        crystal_x = MAX_WIDTH + randint(0,200)
        crystal_flag = 1
        return [tree_x, ptero_x, crystal_x, crystal_flag]