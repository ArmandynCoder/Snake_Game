import pygame
from pygame.locals import *
from sys import exit
from game import Game
from cobra import Cobra

snake = Cobra()
jogo = Game()

class Jogando:
    def Rodando(self):
        while jogo.loop:
            pygame.display.set_caption("Snake")
            pygame.display.set_icon(jogo.icon)
            jogo.screen.fill((0,0,0))
            jogo.relogio.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    jogo.loop = False
                    exit()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                snake.y_cobra = snake.y_cobra -5
            if keys[pygame.K_s]:
                snake.y_cobra = snake.y_cobra +5
            if keys[pygame.K_a]:
                snake.x_cobra = snake.x_cobra -5
            if keys[pygame.K_d]:
                snake.x_cobra = snake.x_cobra +5
            
            # self.cobra = pygame.draw.rect(jogo.screen, (0,255,0), (snake.x_cobra, snake.y_cobra, 30, 30))
            
            
            if snake.x_cobra > jogo.largura:
                snake.x_cobra = 0
            if snake.x_cobra < -10 :
                snake.x_cobra = jogo.largura
            if snake.y_cobra > jogo.altura:
                snake.y_cobra = 0
            if snake.y_cobra < 0:
                snake.y_cobra = jogo.altura
                
                
            pygame.display.flip()
