import pygame


class Movimentação():
    def pteromov(velocidade, pterox):
        pterox -= velocidade
        return pterox

    def cactomov(velocidade, cactox):
        cactox -= velocidade
        return cactox
    
    def crystal(velocidade, crystalx):
        crystalx -= velocidade
        return crystalx