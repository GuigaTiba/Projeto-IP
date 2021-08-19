import pygame
from sys import exit
from random import randint
from pygame import sprite, image

pygame.init()

musica_de_fundo = pygame.mixer.music.load('sons_jetpack/musica_fundo_jetpack.mp3')
pygame.mixer.music.play(-1)
moedacoleted = pygame.mixer.Sound('sons_jetpack/coin_coleta.wav')
pygame.mixer.music.set_volume(0.2)

class Moeda(sprite.Sprite):
    def __init__(self, xa=0, ya=0):
        super(Moeda, self).__init__()
        self.image = image.load('images_jetpack/Moeda.png')
        self.rect = self.image.get_rect(center=(xa, ya))
        self.speed = 10

    def nascer(self, xb, yb):
        grupo_colete.add(Moeda(xb, yb))

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= 0:
            self.kill()

class Calega(sprite.Sprite):
    def __init__(self):
        super(Calega, self).__init__()
        self.image = image.load('images_dino/dinosaur1.png')
        self.rect = self.image.get_rect(center=(70, 300))
        self.speed_H = 9
        self.speed_V = 8

    def update(self):
        com = pygame.key.get_pressed()
        if com[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed_H
        if com[pygame.K_RIGHT] and self.rect.x < 700:
            self.rect.x += self.speed_H
        if com[pygame.K_UP] and self.rect.y > 4:
            self.rect.y -= self.speed_V
        if com[pygame.K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed_V


class Cacto(sprite.Sprite):
    def __init__(self):
        super(Cacto, self).__init__()
        self.image = pygame.image.load('images_dino/cacti.png')
        self.rect = self.image.get_rect(center=(randint(900, 1200), randint(10, 590)))
        self.speed = 10

    def nascer(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= 0:
            self.kill()

class Pterotyl(sprite.Sprite):
    def __init__(self):
        super(Pterotyl, self).__init__()
        self.image = pygame.image.load('images_dino/pterodatyl.png')
        self.rect = self.image.get_rect(center=(randint(800, 1200), randint(10, 590)))
        self.speed = 10

    def nascer(self):
        grupo_obstaculo.add(Pterotyl())

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

cacto = Cacto()
pterodatyl = Pterotyl()
grupo_obstaculo = pygame.sprite.Group(cacto, pterodatyl)


grupo_colete = pygame.sprite.GroupSingle(Moeda())
calegario = pygame.image.load('images_dino/dinosaur1.png')
grupo_calega = pygame.sprite.GroupSingle(Calega())

screen = pygame.display.set_mode([900, 600])
clock = pygame.time.Clock()

moedas = 0
round = 0

k = -1
x = 0
y = 0

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            break

    if round % 1000 == 0:
        k = randint(100, 105)
        p = True
    if round % k > 0 and (round % k) < 5:
        x = 800
        y = randint(10, 590)
        grupo_colete.add(Moeda(x, y))

    if round % k == 0:
        grupo_obstaculo.add(Cacto())
    if round % k == 0:
        grupo_obstaculo.add(Pterotyl())

    # events
    if pygame.sprite.groupcollide(grupo_calega, grupo_colete, False, True):
        moedas += 1
        moedacoleted.play()

    if pygame.sprite.groupcollide(grupo_calega, grupo_obstaculo, False, False):
        # tela fim de game
        fim = True

    screen.fill((255, 255, 255))

    grupo_calega.draw(screen)
    grupo_obstaculo.draw(screen)
    grupo_colete.draw(screen)

    grupo_colete.update()
    grupo_obstaculo.update()
    grupo_calega.update()

    pygame.display.flip()
    round += 1

pygame.quit()
