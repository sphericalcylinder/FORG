import pygame
import sys
import random
from marlene import Marlene
from scaffold import Platform

RESOLUTION = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("FORG")
CLOCK = pygame.time.Clock()
pygame.font.init()

pygame.event.set_allowed((pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN))

font1 = pygame.font.SysFont('timesnewroman', 50)

platformgroup = pygame.sprite.Group()

player = Marlene()

for i in range(25):
    platform3 = Platform()
    platform3.generate()
    platformgroup.add(platform3)

grass = pygame.image.load('grass.png')

a = False
d = False
jump = False
jumpable = False

gravity = 0.05
velocity = 0
godown = False
xvcurrent = 0
xvcap = 5

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    godown = True

    for platform in platformgroup:
        if player.rect.bottom > platform.rect.top and \
                player.rect.right > platform.rect.left and \
                player.rect.left < platform.rect.right and \
                player.rect.bottom < platform.rect.bottom:
            godown = False
            velocity = 0
            jumpable = True
            if player.rect.bottom < platform.rect.bottom:
                player.y = platform.rect.top - player.image.get_height() + 1

    if player.y >= 449 - player.image.get_height():
        velocity = 0
        godown = False
        jumpable = True
        if player.y > 449 - player.image.get_height():
            player.y = 449 - player.image.get_height()

    if godown == True:
        velocity += gravity
        velocity = round(velocity, 2)

    if player.rect.left <= 0:
        a = False
        xvcurrent = 0
    if player.rect.right >= WIDTH-10:
        d = False
        xvcurrent = 0

    if a and abs(xvcurrent) < xvcap:
        xvcurrent -= 0.1
        xvcurrent = round(xvcurrent, 1)
    if d and abs(xvcurrent) < xvcap:
        xvcurrent += 0.1
        xvcurrent = round(xvcurrent, 1)
    if a == False and d == False and jump == False:
        for z in range(3):
            if xvcurrent < 0:
                xvcurrent += 0.1
                xvcurrent = round(xvcurrent, 1)
            elif xvcurrent > 0:
                xvcurrent -= 0.1
                xvcurrent = round(xvcurrent, 1)
    
    player.x += xvcurrent

    if not jumpable:
        jump = False

    if jump and jumpable:
        velocity = -2
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
