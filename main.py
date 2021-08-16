import pygame
import sys
from random import randint
from math import ceil
from pygame.constants import K_DOWN

# Iniciar Pygame
pygame.init()
pygame.display.set_caption('images/Calegaur.io')
icon = pygame.image.load('images/logodinosaur.png')
pygame.display.set_icon(icon)
MAX_WIDTH = 800
MAX_HEIGHT = 450

def main():
    # Screen, FPS
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # Placar de vidas
    vidas = 3
    pontuacao = 0
    fonte = pygame.font.SysFont('arial', 25, False, False)

    # dinosaur
    imgDino1 = pygame.image.load('images/dinosaur1.png')
    imgDino2 = pygame.image.load('images/dinosaur2.png')
    dino = imgDino1.get_rect()
    dino_height = dino[3]
    dino_width = dino[2]
    dino_bottom = 240
    dino_x = 75
    dino_y = dino_bottom
    jump_top = 70
    leg_swap = True
    is_bottom = True
    is_go_up = False

    # Background
    imgBg = pygame.image.load('images/dia3.png')
    

    # pterodatyl
    imgPtero = pygame.image.load('images/pterodatyl.png')
    ptero = imgPtero.get_rect()
    ptero_height = ptero[3]
    ptero_width = ptero[2]
    ptero_x = MAX_WIDTH + 5000
    ptero_y = (MAX_HEIGHT - ptero_height) - 230

    # tree
    imgTree = pygame.image.load('images/cacti.png')
    tree = imgTree.get_rect()
    tree_width = tree[2]
    tree_height = tree[3]
    tree_x = MAX_WIDTH
    tree_y = 270

    # crystal
    imgCrystal = pygame.image.load('images/crystal.png')
    crystal_x = MAX_WIDTH
    crystal_y = 270

    # velocidade inicial
    velocidade = 12

    while True:
        screen.fill((255, 255, 255))
        screen.blit(imgBg, (0, 0))


        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    if is_bottom:
                        is_go_up = True
                        is_bottom = False
                if event.key == pygame.K_DOWN:
                    if is_bottom == False:
                        dino_y += 5
                        is_go_up = False
        
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
        tree_x -= velocidade
        ptero_x -= velocidade
        crystal_x -= velocidade
        if tree_x <= 0 or ptero_x <=0:
            tipo_obstaculo = randint(0,1)
            if tipo_obstaculo == 0:
                tree_x = MAX_WIDTH + randint(0, 200)
                ptero_x = 5000
            else:
                ptero_x = MAX_WIDTH + randint(0,200)
                tree_x = 5000
        
        # velocidade
        if velocidade <= 30:
            velocidade += 0.01

        # draw pterodatyl
        screen.blit(imgPtero, (ptero_x, ptero_y))
        ptero_side = ptero_x+ptero_width
        ptero_bott = ptero_y+ptero_height

        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))
        tree_side = tree_x+tree_width
        tree_bott = tree_y+tree_height

        # draw dinosaur
        if leg_swap:
            screen.blit(imgDino1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(imgDino2, (dino_x, dino_y))
            leg_swap = True
        dino_side = dino_x+dino_width
        dino_bott = dino_y+dino_height

        # draw crystal
        screen.blit(imgCrystal, (crystal_x, crystal_y))

        # colission
        if  tree_side >= dino_x and dino_side >= tree_x+40 and dino_bott >= tree_y:
            vidas -= 1
            tree_x = MAX_WIDTH + randint(0, 300)

        if ptero_side >= dino_x and dino_side >= ptero_x+40 and dino_y <= ptero_y:
            vidas -= 1
            ptero_x = MAX_WIDTH + randint(0, 300)

        if vidas ==0:
            print('Perdeu')
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
