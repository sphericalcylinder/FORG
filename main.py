import pygame
import sys

RESOLUTION = WIDTH, HEIGHT = 500, 600
SCREEN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("FORG")
CLOCK = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    CLOCK.tick(72)
    pygame.display.update()
