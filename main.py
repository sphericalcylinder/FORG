import pygame
import sys
import random
from marlene import Marlene

RESOLUTION = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("FORG")
CLOCK = pygame.time.Clock()

pygame.event.set_allowed((pygame.KEYDOWN, pygame.KEYUP))

player = Marlene()

while True:
    
    SCREEN.fill('#ffffff')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        

    SCREEN.blit(player.image, player.rect)
    
    pygame.display.flip()
    CLOCK.tick(72)
