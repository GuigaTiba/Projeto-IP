import pygame
import sys
from random import randint
from math import ceil
from pygame.constants import KEYDOWN, K_DOWN
from obstaculo_calega import obstaculo_type
from moeda_ou_coração import choices
from colisão_dino import colisao

def main_calega():
    # Screen, FPS
    MAX_WIDTH = 800
    MAX_HEIGHT = 450
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # music
    pygame.mixer.music.load('sons_dino/musica_fundo_dino.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.35)

    # Placar de vidas
    vidas = 3
    pontuacao = 0
    fonte = pygame.font.SysFont('arial', 25, False, False)
    player_alive = 1

    # calegario
    imgCalega1 = pygame.image.load('images_jetpack/calegario (2).png')
    imgCalega2 = pygame.image.load('images_jetpack/calegario (5).png')
    imgCalega3 = pygame.image.load('images_jetpack/calegario (6).png')
    imgCalega4 = pygame.image.load('images_jetpack/calegauro_pulando.png')
    calega = imgCalega1.get_rect()
    calega_height = calega[3]
    calega_width = calega[2]
    calega_bottom = 290
    calega_x = 75
    calega_y = calega_bottom
    jump_top = 130
    leg_swap = 0
    is_bottom = True
    is_go_up = False

    # Game-over e pressanykey
    imgGameover = pygame.image.load('images_dino/gameover.png')
    imgPressanykey = pygame.image.load('images_dino/pressanykey.png')

    # Background
    imgBg = pygame.image.load('images_jetpack/fundo.png')
    

    # nave
    imgNave1 = pygame.image.load('images_jetpack/pngwing.com.png')
    nave = imgNave1.get_rect()
    nave_height = nave[3]
    nave_width = nave[2]
    nave_x = MAX_WIDTH + 5000
    nave_y = (MAX_HEIGHT - nave_height) - 180

    # tronco
    imgTronco = pygame.image.load('images_jetpack/New_Piskel_1.png')
    tronco = imgTronco.get_rect()
    tronco_width = tronco[2]
    tronco_x = MAX_WIDTH
    tronco_y = 350
    
    #heart
    imgCoracao = pygame.image.load('images_dino/coracao.png')
    coracao = imgCoracao.get_rect()
    coracao_width = coracao[2]-3
    coracao_height = coracao[3]-3
    coracao_x = MAX_WIDTH + 5000
    coracao_y = randint(230, 350)
    pontuacao_vidas = 0

    #moeda
    imgMoeda = pygame.image.load('images_dino/Moeda.png')
    moeda = imgMoeda.get_rect()
    moeda_width = moeda[2]-3
    moeda_height = moeda[3]-3
    moeda_x = MAX_WIDTH + randint(600, 2000)
    moeda_y = randint(230, 350)
    pontuacao_moedas = 0


    # velocidade inicial
    velocidade = 12
    
    while True:
        screen.fill((255, 255, 255))
        screen.blit(imgBg, (0, 0))

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT and player_alive:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and player_alive:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    if is_bottom:
                        is_go_up = True
                        is_bottom = False
                elif event.key == pygame.K_DOWN:
                    if is_bottom == False:
                        calega_y += 5
                        is_go_up = False
            if not player_alive:
                if event.type == KEYDOWN:
                    main_calega()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # vidas check
        if vidas == 0:  
            screen.blit(imgGameover, (200, 100))
            screen.blit(imgPressanykey, (250, 250))
            player_alive = False
        # pressed
        if pygame.key.get_pressed()[K_DOWN]:
            if is_bottom == False:
                calega_y += 5

        # calegario movement
        if is_go_up:
            calega_y -= 10.0
        elif not is_go_up and not is_bottom:
            calega_y += 10.0

        # calegario position check
        if is_go_up and calega_y <= jump_top:
            is_go_up = False

        if not is_bottom and calega_y >= calega_bottom:
            is_bottom = True
            calega_y = calega_bottom

        # movimento do Tronco e nave
        if not player_alive:
            velocidade = 0
        tronco_x -= velocidade
        nave_x -= velocidade
        coracao_x -= velocidade
        moeda_x -= velocidade

        if tronco_x < -30 or nave_x < -60:
            obstaculo_geral = obstaculo_type(MAX_WIDTH, pontuacao)
            tronco_x = obstaculo_geral[0]
            nave_x = obstaculo_geral[1]
            
        if moeda_x < 0 or coracao_x < 0:
            moeda_coracao = choices(MAX_WIDTH)
            moeda_x = moeda_coracao[0]
            coracao_x = moeda_coracao[1]

        
        # velocidade
        if velocidade <= 35 and player_alive:
            velocidade += 0.015

        # draw nave
        screen.blit(imgNave1, (nave_x, nave_y))
        nave_side = nave_x+nave_width
        nave_bott = nave_y+nave_height

        # draw tronco
        screen.blit(imgTronco, (tronco_x, tronco_y))
        tronco_side = tronco_x+tronco_width

        # draw calegario
        if player_alive == True:
            if calega_y >= calega_bottom:
                if leg_swap <= 7:
                    screen.blit(imgCalega1, (calega_x, calega_y))
                elif leg_swap <= 11:
                    screen.blit(imgCalega2, (calega_x, calega_y))
                elif leg_swap <= 18:
                    screen.blit(imgCalega3, (calega_x, calega_y))
                elif leg_swap <= 22:
                    if leg_swap == 22:
                        leg_swap = 0   
                    screen.blit(imgCalega2, (calega_x, calega_y))
            else:
                screen.blit(imgCalega4, (calega_x, calega_y))
            
            if leg_swap > 22:
                leg_swap = 0
        
        leg_swap += 1
        calega_side = calega_x+calega_width
        calega_bott = calega_y+calega_height
        
        # draw heart
        screen.blit(imgCoracao, (coracao_x, coracao_y))
        coracao_side = coracao_width+coracao_x
        coracao_bott = coracao_height+coracao_y


        # draw moeda
        screen.blit(imgMoeda, (moeda_x, moeda_y))
        moeda_side = moeda_width+moeda_x
        moeda_bott = moeda_y+moeda_height

        # collision
        vidas_antes_colisao=vidas
        moedas_antes_colisao=pontuacao_moedas
        vidas, tronco_x = colisao.col_tree(tronco_side, calega_x, calega_side, tronco_x, calega_bott, tronco_y, vidas)
        vidas, nave_x = colisao.col_ptero(nave_side, calega_x, calega_side, nave_x, calega_y, nave_bott, vidas)
        vidas, pontuacao, coracao_x, pontuacao_vidas = colisao.col_coracao(coracao_side, calega_x, calega_side, coracao_x, calega_y, coracao_bott, calega_bott, coracao_y, vidas, pontuacao, pontuacao_vidas)
        pontuacao, moeda_x, pontuacao_moedas = colisao.col_moeda(moeda_side, calega_x, calega_side, moeda_x, calega_y, moeda_bott, calega_bott, moeda_y, pontuacao, pontuacao_moedas)
        
        if vidas_antes_colisao>vidas:
            pygame.mixer.music.load('sons_dino/perdendo_vida2.wav')
            pygame.mixer.music.play()
            pygame.mixer.music.queue ( 'sons_dino/musica_fundo_dino.wav' )
            pygame.mixer.music.set_volume(0.35)
        elif vidas_antes_colisao<vidas:
            pygame.mixer.music.load('sons_dino/pegando_vida2.wav')
            pygame.mixer.music.play()
            pygame.mixer.music.queue ( 'sons_dino/musica_fundo_dino.wav' )
            pygame.mixer.music.set_volume(0.35)
        if pontuacao_moedas>moedas_antes_colisao:
            pygame.mixer.music.load('sons_dino/coin_coleta2.wav')
            pygame.mixer.music.play()
            pygame.mixer.music.queue ( 'sons_dino/musica_fundo_dino.wav' )
            pygame.mixer.music.set_volume(0.35)

        # Placar
        mensagem2 = f'Pontuação: {pontuacao:07d}'
        mensagem_moedas = f'Moedas coletadas: {pontuacao_moedas}'
        mensagem_vidas = f'Vidas coletadas: {pontuacao_vidas}'
        placar_pontuacao = fonte.render(mensagem2, False, (180, 180, 180))
        placar_moedas = fonte.render(mensagem_moedas, False, (180, 180, 180))
        placar_de_coracao = fonte.render(mensagem_vidas, False, (180, 180, 180))
        pontuacao += ceil(velocidade/20)

        # update
        mensagem = f'Vidas: {vidas}'
        placar_vidas = fonte.render(mensagem, False, (180, 180, 180))
        screen.blit(placar_vidas, (20, 20))
        screen.blit(placar_pontuacao, (560, 20))
        screen.blit(placar_moedas, (140, 20))
        screen.blit(placar_de_coracao, (360, 20))
        
        # update
        pygame.display.update()
        fps.tick(30)