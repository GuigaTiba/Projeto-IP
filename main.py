import pygame
import sys
import random

# Iniciar Pygame
pygame.init()
pygame.display.set_caption('images/Calegaur.io')
icon = pygame.image.load('images/logodinosaur.png')
pygame.display.set_icon(icon)
MAX_WIDTH = 800
MAX_HEIGHT = 400

def main():
    # Screen, FPS
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # dinosaur
    imgDino1 = pygame.image.load('images/dinosaur1.png')
    imgDino2 = pygame.image.load('images/dinosaur2.png')
    dino_height = imgDino1.get_size()[1]
    dino_bottom = MAX_HEIGHT - dino_height
    dino_x = 75
    dino_y = dino_bottom
    jump_top = 180
    leg_swap = True
    is_bottom = True
    is_go_up = False

    #pterodatyl
    imgPtero = pygame.image.load('images/pterodatyl.png')
    pterodatyl_height = imgPtero.get_size()[1]
    pterodatyl_x = MAX_WIDTH
    pterodatyl_y = (MAX_HEIGHT - pterodatyl_height) - 100

    # tree
    imgTree = pygame.image.load('images/cacti.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

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

        # pterodatyl movement
        pterodatyl_x -= 12
        if pterodatyl_x <=0:
            pterodatyl_x = MAX_WIDTH + random.randint(0,500)

        # draw pterodatyl
        screen.blit(imgPtero, (pterodatyl_x, pterodatyl_y))

        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))

        # draw dinosaur
        if leg_swap:
            screen.blit(imgDino1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(imgDino2, (dino_x, dino_y))
            leg_swap = True
        
        
        
        # update
        pygame.display.update()
        fps.tick(30)

main()
