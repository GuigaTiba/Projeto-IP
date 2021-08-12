import pygame
import time
from game import Game

pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

game = Game()

ct = 0

X_FACTOR = SCREEN_WIDTH / game.width
Y_FACTOR = SCREEN_HEIGHT / game.height

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


running = True
while running or ct < 2000:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            #print('Apertou')
            if event.key == pygame.K_SPACE:
                #print('Reconheceu')
                game.player_act('jump')

    game.update()

    screen.fill((255, 255, 255))

    player_pos = game.player_pos()
    #print(game.player)

    pygame.draw.rect(screen, (25, 25, 25), (player_pos[0] * X_FACTOR, player_pos[1] * Y_FACTOR, X_FACTOR, Y_FACTOR), 0)

    pygame.display.flip()
    ct += 1
    time.sleep(0.05)
    

pygame.quit()