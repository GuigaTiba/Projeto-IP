import random
import sys
import pygame

# Iniciar Pygame
pygame.init()
pygame.display.set_caption('images/Calegaur.io')
icon = pygame.image.load('images/logodinosaur.png')
pygame.display.set_icon(icon)
MAX_WIDTH = 800
MAX_HEIGHT = 450



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
    dino = imgDino1.get_rect()
    dino_height = dino[3]
    dino_width = dino[2]
    dino_bottom = 305
    dino_x = 75
    dino_y = dino_bottom
    jump_top = 150
    leg_swap = True
    is_bottom = True
    is_go_up = False

    # tree
    imgTree = pygame.image.load('images/tree.png')
    tree = imgTree.get_rect()
    tree_width = tree[2]
    tree_height = tree[3]
    tree_x = MAX_WIDTH
    tree_y = 325

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

        if  tree_side >= dino_x and dino_side >= tree_x and dino_bott >= tree_y:
            print(dino_bott)
            print(tree_y)
            vidas -= 1
            print('-1 vida')
            tree_x = MAX_WIDTH + random.randint(0, 300)
        if vidas ==0:
            print('Perdeu')
            pygame.quit()
            exit()
       
        # update
        mensagem = f'Vidas: {vidas}'
        placar_vidas = fonte.render(mensagem, False, (0, 0, 0))
        screen.blit(placar_vidas, (20, 20))
        screen.blit(placar_moedas, (680, 20))

        pygame.display.update()
        fps.tick(30)


main()
