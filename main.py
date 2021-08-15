import random
import sys

import pygame

# Iniciar Pygame
pygame.init()
pygame.display.set_caption('images/Calegaur.io')
icon = pygame.image.load('images/logodinosaur.png')
pygame.display.set_icon(icon)
MAX_WIDTH = 800
MAX_HEIGHT = 400



def main():
    # Screen, FPS
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps.tick(25)

    # Placar de vidas
    vidas = 3
    moedas = 0
    fonte = pygame.font.SysFont('arial', 25, False, False)

    # Placar de moedas
    mensagem2 = f'Moedas: {moedas}'
    placar_moedas = fonte.render(mensagem2, False, (0, 0, 0))

    # dinosaur
    imgDino1 = pygame.image.load('images/dinosaur1.png')
    imgDino2 = pygame.image.load('images/dinosaur2.png')
    dino_width, dino_height = imgDino1.get_size()
    dino_bottom = 205
    dino_x = 75
    dino_y = dino_bottom
    jump_top = 50
    leg_swap = True
    is_bottom = True
    is_go_up = False

    # tree
    imgTree = pygame.image.load('images/cacti.png')
    tree_width, tree_height = imgTree.get_size()
    tree_x = MAX_WIDTH
    tree_y = 205

    while True:
        screen.fill((255, 255, 255))

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

        # tree movement
        tree_x -= 12
        if tree_x <= 0:
            tree_x = MAX_WIDTH + random.randint(0, 300)

        # draw tree
        #screen.blit(imgTree, (tree_x, tree_y))
        obstaculo = pygame.draw.rect(screen, (0, 0, 0), (tree_x, tree_y, 40, tree_height))

        # draw dinosaur
        dino = pygame.draw.rect(screen, (0, 0, 0), (dino_x, dino_y, dino_width, dino_height))

        if dino.colliderect(obstaculo):
            vidas -= 1
            print('-1 vida')
            tree_x = MAX_WIDTH + random.randint(0, 300)
        if vidas ==0:
            print('Perdeu')
            pygame.quit()
            exit()
        '''if leg_swap:
            screen.blit(imgDino1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(imgDino2, (dino_x, dino_y))
            leg_swap = True'''

        # update
        mensagem = f'Vidas: {vidas}'
        placar_vidas = fonte.render(mensagem, False, (0, 0, 0))
        screen.blit(placar_vidas, (20, 20))
        screen.blit(placar_moedas, (680, 20))

        pygame.display.update()
        fps.tick(30)


main()
