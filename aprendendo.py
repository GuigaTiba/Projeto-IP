import pygame
from pygame.locals import *

from sys import exit
from random import randint

pygame.init()

pygame.display.set_caption('roda-do-skate')
fonte = pygame.font.SysFont('arial', 20, True, True)

altura = 600
largura = 600
x = altura/2
y = largura/2
z = randint(50,550)
w = randint(50,550)
pontos = 0

tela = pygame.display.set_mode((largura,altura))
tempo = pygame.time.Clock()

while True:
    tempo.tick(50)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                y = y-10
            if event.key == K_d:
                y = y+10
            if event.key == K_w:
                x = x-10
            if event.key == K_s:
                x = x+10
    
    if pygame.key.get_pressed()[K_a]:
        y = y-20
    if pygame.key.get_pressed()[K_d]:
        y = y+20
    if pygame.key.get_pressed()[K_w]:
        x = x-10
    if pygame.key.get_pressed()[K_s]:
        x = x+10

    movendo = pygame.draw.rect(tela, (90,90,90), (y/3,x,60,60))
    parado = pygame.draw.rect(tela, (0,0,255), (z,w,50,50))

    if parado.colliderect(movendo):
        z = randint(50,550)
        w = randint(50,550)
        pontos += 1
    
    tela.blit(texto, (450,40))
    pygame.display.update()