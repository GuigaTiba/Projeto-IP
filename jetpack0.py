import pygame
from sys import exit
from random import randint
from pygame import sprite, image

#quando colidir com a moeda "sound_coin.play()"
#sound_coin = pygame.mixer.Sound('sons/coin_coleta.wav')
pygame.init()

musica_de_fundo = pygame.mixer.music.load('sons_jetpack/musica_fundo_jetpack.mp3')
pygame.mixer.music.play(-1)
moedacoleted = pygame.mixer.Sound('sons_jetpack/coin_coleta.wav')
pygame.mixer.music.set_volume(0.2)

#pra tocar a musica de fund0music.set_volume(0.2)
class Moeda(sprite.Sprite):
    def __init__(self, x, y):
        super(Moeda, self).__init__()
        self.image = image.load('images_jetpack/Moeda.png')
        self.rect = self.image.get_rect(x=600, y=100)
        self.speed = 10

    def mexe(self):
        self.rect.x -= self.speed

    def nasce(self):
        self.rect.x = randint(100, 300)
        self.rect.y = randint(20, 580)

    def update(self):
        moeda.mexe()

class Calega(sprite.Sprite):
    def __init__(self):
        super(Calega, self).__init__()
        self.image = image.load('images_dino/dinosaur1.png')
        self.rect = self.image.get_rect(center=(70, 300))
        self.speed_H = 12
        self.speed_V = 10

    def update(self):
        com = pygame.key.get_pressed()
        if com[pygame.K_LEFT]:
            self.rect.x -= self.speed_H
        if com[pygame.K_RIGHT]:
            self.rect.x += self.speed_H
        if com[pygame.K_UP]:
            self.rect.y -= self.speed_V
        if com[pygame.K_DOWN]:
            self.rect.y += self.speed_V
        pygame.display.flip()

class Cacto(sprite.Sprite):
    def __init__(self):
        super(Cacto, self).__init__()
        self.image = pygame.image.load('images_dino/cacti.png')
        self.rect = self.image.get_rect(center=(900, 300))
        self.speed = 10

    def mexer(self):
        self.rect.x -= self.speed
        grupo_obstaculo.draw(screen)

    def update(self):
        cacto.mexer()

class Pterotyl(sprite.Sprite):
    def __init__(self):
        super(Pterotyl, self).__init__()
        self.image = pygame.image.load('images_dino/pterodatyl.png')
        self.rect = self.image.get_rect(center=(700, 400))
        self.speed = 10

    def mexe(self):
        self.rect.x -= self.speed


    def update(self):
        pterodatyl.mexe()
        if self.rect.x < 0:
            self.rect.x = randint(700, 2000)
            self.rect.y = randint(20, 580)

cacto = Cacto()
pterodatyl = Pterotyl()
grupo_obstaculo = pygame.sprite.Group(cacto, pterodatyl)

moeda = Moeda(1, 1)
grupo_colete = pygame.sprite.GroupSingle(moeda)

imgDino1 = pygame.image.load('images_dino/dinosaur1.png')

calegario = Calega()
grupo_calega = pygame.sprite.GroupSingle(calegario)

screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()
cont = 0
moedas = 0
while True:
    clock.tick(30)
    #events
    if pygame.sprite.groupcollide(grupo_calega, grupo_colete, False, True):
        moedas += 1
        moedacoleted.play()
    if pygame.sprite.groupcollide(grupo_calega, grupo_obstaculo, False, False):
        #tela fim de game
        fim = True
        print('bateu')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            break


    screen.fill((255, 255, 255))

    grupo_calega.draw(screen)
    grupo_obstaculo.draw(screen)
    grupo_colete.draw(screen)

    grupo_colete.update()
    grupo_obstaculo.update()
    grupo_calega.update()

    pygame.display.flip()
pygame.quit()
