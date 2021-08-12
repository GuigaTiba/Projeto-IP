from sys import exit

import pygame
from pygame.locals import *

pygame.init()

largura = 640
altura = 480
x = 0
y = altura / 2 - 25

vidas = 3
fonte = pygame.font.SysFont('arial', 25, False, False)

display_tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Teste Jogo 1')
relogio = pygame.time.Clock()

while True:
    relogio.tick(25)
    display_tela.fill((0, 0, 0))
    mensagem = f'Vidas: {vidas}'
    placar_vidas = fonte.render(mensagem, False, (255, 255, 255))
    if not (0 <= y <= 480):
        if y < 0:
            y += 480
        else:
            y -= 480
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_w]:
        y -= 25
    if pygame.key.get_pressed()[K_s]:
        y += 25
    dino = pygame.draw.rect(display_tela, (0, 0, 200), (x, y, 40, 50))
    obstaculo = pygame.draw.rect(display_tela, (250, 0, 0), (250, 215, 40, 50))

    if dino.colliderect(obstaculo):
        vidas -= 1
        print('-1 vida')
        x = 0
    if vidas == 0:
        print('Perdeu')
        pygame.quit()
        exit()
    if x >= altura:
        x = 0
    x += 10
    display_tela.blit(placar_vidas, (450, 40))
    pygame.display.update()

'''    pygame.draw.circle(display_tela, (250, 0, 0), (300, 260), 40)
    pygame.draw.line(display_tela, (255,255,0), (390,50),(390,400),5)
if event.type == KEYDOWN and event.key == K_w:
    y -= 25
elif event.type == KEYDOWN and event.key == K_s:
    y += 25'''
