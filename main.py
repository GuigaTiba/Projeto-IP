import pygame
pygame.init()



screen = pygame.display.set_mode([500, 500])


running = True
while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (25, 25, 25), (30, 450, 50, 50), 0)

    pygame.display.flip()

pygame.quit()