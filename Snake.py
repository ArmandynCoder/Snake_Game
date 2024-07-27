import pygame
from pygame.locals import *


pygame.init()

loop = True

altura = 420
largura = 800


screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")
icon = pygame.image.load("icone/icone_cobra.png")
pygame.display.set_icon(icon)

relogio = pygame.time.Clock()

x_cobra = (largura/2) 
y_cobra = (altura/2) 


while loop:
    screen.fill((0,0,0))
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            loop = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y_cobra = y_cobra -5
    if keys[pygame.K_s]:
        y_cobra = y_cobra +5
    if keys[pygame.K_a]:
        x_cobra = x_cobra -5
    if keys[pygame.K_d]:
        x_cobra = x_cobra +5
    
                
    cobra = pygame.draw.rect(screen, (0,255,0), (x_cobra, y_cobra, 30, 30))
    
    pygame.display.flip()
