from game import Game
import pygame

dimensao = Game()

class Cobra:
    def __init__(self, cor, altura_cobra, largura_cobra, x_cobra, y_cobra):
        pygame.init()
        self.cor = cor
        self.altura_cobra = altura_cobra
        self.largura_cobra = largura_cobra
        self.x_cobra = x_cobra
        self.y_cobra = y_cobra
        self.cobra = pygame.draw.rect(dimensao.screen, self.cor, (self.x_cobra, self.y_cobra, self.altura_cobra, self.largura_cobra))

