import pygame


class colisao():
    def col_tree(tree_side, dino_x, dino_side, tree_x, dino_bott, tree_y, vidas):
        if  tree_side >= dino_x and dino_side >= tree_x+40 and dino_bott >= tree_y:
            pygame.mixer.music.load('sons_dino/perdendo_vida2.wav')
            pygame.mixer.music.play(0)
            pygame.mixer.music.set_volume(0.35)
            vidas -= 1
            tree_x = -30
        return vidas, tree_x

    def col_ptero(ptero_side, dino_x, dino_side, ptero_x, dino_y, ptero_bott, vidas):
        if ptero_side >= dino_x and dino_side >= ptero_x+40 and dino_y <= ptero_bott:
            vidas -= 1
            ptero_x = -60
        return vidas, ptero_x

    def col_crystal(crystal_side, dino_x, dino_side, crystal_x, dino_bott, crystal_y, cutscene):
        if crystal_side >= dino_x and dino_side >= crystal_x and dino_bott >= crystal_y:
            cutscene = 1
        return cutscene

    def col_coracao(coracao_side, dino_x, dino_side, coracao_x, dino_y, coracao_bott, dino_bott, coracao_y, vidas, pontuacao, coracao):
        if coracao_side >= dino_x and dino_side >= coracao_x and dino_y <= coracao_bott and dino_bott >= coracao_y:
            if 0 < vidas < 3:
                vidas += 1
                coracao_x = -1
                coracao += 1
                return vidas, pontuacao, coracao_x, coracao
            else:
                pontuacao += 150
                coracao_x = -1
                coracao += 1
                return vidas, pontuacao, coracao_x, coracao
        return vidas, pontuacao, coracao_x, coracao

    def col_moeda(moeda_side, dino_x, dino_side, moeda_x, dino_y, moeda_bott, dino_bott, moeda_y, pontuacao, moeda):
        if moeda_side >= dino_x and dino_side >= moeda_x and dino_y <= moeda_bott and dino_bott >= moeda_y:
            pontuacao += 150
            moeda_x = -1
            moeda += 1
        return pontuacao, moeda_x, moeda