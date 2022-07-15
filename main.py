import pygame
import sys
import random
from marlene import Marlene
from scaffold import Platform

RESOLUTION = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("FORG")
CLOCK = pygame.time.Clock()

pygame.event.set_allowed((pygame.KEYDOWN, pygame.KEYUP))

platformgroup = pygame.sprite.Group()

player = Marlene()
platform1 = Platform()
platform1.y = 250
platform1.x = 295

platformgroup.add(platform1)

grass = pygame.image.load('assets/grass.png')

a = False
d = False
jump = False
jumpable = False

gravity = 0.02
velocity = 0
godown = False

while True:

    SCREEN.fill('#ffffff')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_a:
                    a = True
                case pygame.K_d:
                    d = True
                case pygame.K_SPACE:
                    jump = True
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_a:
                    a = False
                case pygame.K_d:
                    d = False

    godown = True

    for platform in platformgroup:
        if player.rect.bottom > platform.rect.top and \
                player.rect.right > platform.rect.left and \
                player.rect.left < platform.rect.right and \
                player.rect.top < platform.rect.bottom:
            godown = False
            velocity = 0
            jumpable = True

    if player.y >= 449 - player.image.get_height():
        velocity = 0
        godown = False
        jumpable = True
        if player.y > 449 - player.image.get_height():
            player.y = 449 - player.image.get_height()

    if godown == True:
        velocity += gravity
        velocity = round(velocity, 2)

    if a:
        player.x -= 1
    if d:
        player.x += 1
    if not jumpable:
        jump = False
    if jump:
        velocity = -1
        jump = False
        jumpable = False

    player.y += velocity



    platformgroup.update()
    platformgroup.draw(SCREEN)
    player.update()
    SCREEN.blit(player.image, player.rect)
    SCREEN.blit(grass, (0, 450, grass.get_width(), grass.get_height()))

    pygame.display.flip()
    CLOCK.tick(60)
