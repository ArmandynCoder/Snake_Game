import pygame
from pygame.locals import *
# from cobra import Cobra
# from jogando import Jogando

class Game:
    def __init__(self) :
        pygame.init()
        self.altura = 420
        self.largura = 800
        self.screen = pygame.display.set_mode((self.largura, self.altura))
        self.icon = pygame.image.load("icone/icone_cobra.png")
        self.relogio = pygame.time.Clock()
        self.loop = True
