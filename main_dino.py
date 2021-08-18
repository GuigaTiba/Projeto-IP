import pygame
import sys
from random import randint
from math import ceil
from pygame.constants import KEYDOWN, K_DOWN
from obstaculo_dino import obstaculo_type
from moeda_ou_coração import choices
from colisão_dino import colisao

# Iniciar Pygame
pygame.init()
pygame.display.set_caption('images_dino/Calegaur.io')
icon = pygame.image.load('images_dino/logodinosaur.png')
pygame.display.set_icon(icon)
MAX_WIDTH = 800
MAX_HEIGHT = 450

def main():
    # Screen, FPS
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # music
    pygame.mixer.music.load('sons_dino/musica_fundo_dino.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.35)

    # Placar de vidas
    vidas = 3
    pontuacao = 0
    fonte = pygame.font.SysFont('arial', 25, False, False)
    player_alive = 1

    # dinosaur
    imgDino1 = pygame.image.load('images_dino/dinosaur1.png')
    imgDino2 = pygame.image.load('images_dino/dinosaur2.png')
    dino = imgDino1.get_rect()
    dino_height = dino[3]
    dino_width = dino[2]
    dino_bottom = 240
    dino_x = 75
    dino_y = dino_bottom
    jump_top = 70
    leg_swap = 0
    is_bottom = True
    is_go_up = False

    # dinossauro morto
    imgDino3 = pygame.image.load('images_dino/dinosauromorto.png')

    # Game-over e pressanykey
    imgGameover = pygame.image.load('images_dino/gameover.png')
    imgPressanykey = pygame.image.load('images_dino/pressanykey.png')

    # Background
    imgBg = pygame.image.load('images_dino/dia3.png')
    

    # pterodatyl
    imgPtero1 = pygame.image.load('images_dino/pterodatyl.png')
    imgPtero2 = pygame.image.load('images_dino/pterodatyl0.png')
    ptero = imgPtero1.get_rect()
    ptero_height = ptero[3]
    ptero_width = ptero[2]
    ptero_x = MAX_WIDTH + 5000
    ptero_y = (MAX_HEIGHT - ptero_height) - 230
    wing_swap = 0

    # tree
    imgTree = pygame.image.load('images_dino/cacti.png')
    tree = imgTree.get_rect()
    tree_width = tree[2]
    tree_x = MAX_WIDTH
    tree_y = 270

    # crystal
    imgCrystal = pygame.image.load('images_dino/crystal.png')
    crystal = imgCrystal.get_rect()
    crystal_width = crystal[2]
    crystal_x = MAX_WIDTH + 5000
    crystal_y = 270
    crystal_flag = 0
    cutscene = 0
     
    #heart
    imgCoracao = pygame.image.load('images_dino/coracao.png')
    coracao = imgCoracao.get_rect()
    coracao_width = coracao[2]-1
    coracao_height = coracao[3]-1
    coracao_x = MAX_WIDTH + 5000
    coracao_y = randint(150, 270)

    #moeda
    imgMoeda = pygame.image.load('images_dino/Moeda.png')
    moeda = imgMoeda.get_rect()
    moeda_width = moeda[2]-1
    moeda_height = moeda[3]-1
    moeda_x = MAX_WIDTH + randint(600, 2000)
    moeda_y = randint(150, 270)


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
                        dino_y += 5
                        is_go_up = False
            if not player_alive:
                if event.type == KEYDOWN:
                    main()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # vidas check/ dino morto display
        if vidas == 0:   
            screen.blit(imgDino3, (dino_x, dino_y))
            screen.blit(imgGameover, (200, 100))
            screen.blit(imgPressanykey, (250, 250))
            player_alive = False
        # pressed
        if pygame.key.get_pressed()[K_DOWN]:
            if is_bottom == False:
                dino_y += 5

        # dinosaur movement
        if is_go_up:
            dino_y -= 10.0
        elif not is_go_up and not is_bottom:
            dino_y += 10.0

        # dinosaur position check
        if is_go_up and dino_y <= jump_top:
            is_go_up = False

        if not is_bottom and dino_y >= dino_bottom:
            is_bottom = True
            dino_y = dino_bottom

        # movimento do cacto e pterodatyl
        if not player_alive:
            velocidade = 0
        tree_x -= velocidade
        ptero_x -= velocidade
        crystal_x -= 13.5
        coracao_x -= velocidade
        moeda_x -= velocidade

        if tree_x < 0 or ptero_x < 0 or crystal_x < 0:
            obstaculo_geral = obstaculo_type(MAX_WIDTH, pontuacao, crystal_flag)
            tree_x = obstaculo_geral[0]
            ptero_x = obstaculo_geral[1]
            crystal_x = obstaculo_geral[2]
            try:
                crystal_flag = obstaculo_geral[3]
            except IndexError:
                True
        if moeda_x < 0 or coracao_x < 0:
            moeda_coracao = choices(MAX_WIDTH)
            moeda_x = moeda_coracao[0]
            coracao_x = moeda_coracao[1]

        
        # velocidade
        if velocidade <= 30 and player_alive:
            velocidade += 0.02

        # draw pterodatyl
        if wing_swap <= 12:
            screen.blit(imgPtero1, (ptero_x, ptero_y))
        elif wing_swap <= 25:
            screen.blit(imgPtero2, (ptero_x, ptero_y))
            if wing_swap == 25:
                wing_swap = 0
        wing_swap += 1
        ptero_side = ptero_x+ptero_width
        ptero_bott = ptero_y+ptero_height

        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))
        tree_side = tree_x+tree_width

        # draw dinosaur
        if leg_swap <= 8 and player_alive:
            screen.blit(imgDino1, (dino_x, dino_y))
        elif leg_swap <= 17 and player_alive:
            screen.blit(imgDino2, (dino_x, dino_y))
            if leg_swap == 17:
                leg_swap = 0
        leg_swap += 1
        dino_side = dino_x+dino_width
        dino_bott = dino_y+dino_height

        # draw crystal
        screen.blit(imgCrystal, (crystal_x, crystal_y))
        crystal_side = crystal_width+crystal_x
        
        # draw heart
        screen.blit(imgCoracao, (coracao_x, coracao_y))
        coracao_side = coracao_width+coracao_x
        coracao_bott = coracao_height+coracao_y


        # draw moeda
        screen.blit(imgMoeda, (moeda_x, moeda_y))
        moeda_side = moeda_width+moeda_x
        moeda_bott = moeda_y+moeda_height

        # collision
        vidas, tree_x = colisao.col_tree(tree_side, dino_x, dino_side, tree_x, dino_bott, tree_y, vidas)
        vidas, ptero_x = colisao.col_ptero(ptero_side, dino_x, dino_side, ptero_x, dino_y, ptero_bott, vidas)
        cutscene = colisao.col_crystal(crystal_side, dino_x, dino_side, crystal_x, dino_bott, crystal_y, cutscene)
        vidas, pontuacao, coracao_x = colisao.col_coracao(coracao_side, dino_x, dino_side, coracao_x, dino_y, coracao_bott, dino_bott, coracao_y, vidas, pontuacao)
        pontuacao, moeda_x = colisao.col_moeda(moeda_side, dino_x, dino_side, moeda_x, dino_y, moeda_bott, dino_bott, moeda_y, pontuacao)
        if cutscene == 1:
            pygame.quit()
            exit()

        # Placar
        mensagem2 = f'Pontuação: {pontuacao:07d}'
        placar_pontuacao = fonte.render(mensagem2, False, (0, 0, 0))
        pontuacao += ceil(velocidade/20)

        # update
        mensagem = f'Vidas: {vidas}'
        placar_vidas = fonte.render(mensagem, False, (0, 0, 0))
        screen.blit(placar_vidas, (20, 20))
        screen.blit(placar_pontuacao, (530, 20))
        
        # update
        pygame.display.update()
        fps.tick(30)

main()
