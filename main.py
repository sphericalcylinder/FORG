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

pygame.event.set_allowed(
    (pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN))

font1 = pygame.font.SysFont('timesnewroman', 22)

platformgroup = pygame.sprite.Group()


player = Marlene()
platformvalues = []
supportedplatforms = []
def genmap():

    platformgroup.empty()

    for i in range(25):
        platform3 = Platform()
        platform3.generate()
        platformgroup.add(platform3)
        platformvalues.append([platform3.x, platform3.y, i, platform3])
        
    #calculate the highest y of each column
    #currenty = 500
    #for j in range(50, 600, 50):
    #    currentvalues = []
    #    for k in range(len(platformvalues)):
    #        if platformvalues[k][0] == j:
    #            currentvalues.append(platformvalues[k])

    #    currenty = 500
    #    currenthighestplatform = None
    #    for l in range(len(currentvalues)):
    #        currentplatform = currentvalues[l]
    #        if currentplatform[1] <= currenty:
    #            currenty = currentplatform[1]
    #            currenthighestplatform = currentplatform
    #    if currenthighestplatform != None:
    #        supportedplatforms.append(currenthighestplatform)

    ##spawn the LEGS
    #for selectedplatform in supportedplatforms:
    #    legy = selectedplatform[1]
    #    for i in range(20):
    #        legs = PlatformLegs(selectedplatform[0], legy)
    #        platlegsgroup.add(legs)
    #        legy += 25

genmap()

grass = pygame.image.load('assets/grass.png')
button = pygame.image.load('assets/button-1.png')
exclaim = pygame.image.load('assets/exclamatorypunctuation.png')
button = pygame.transform.scale(button, (80, 40))
buttonrect = pygame.Rect(0, 0, button.get_width(), button.get_height())
trophy = pygame.image.load('assets/trophy.png')
trophyrect = pygame.Rect((WIDTH/2)-(trophy.get_width()/2), 0, trophy.get_width(), trophy.get_height())

a = False
d = False
jump = False
jumpable = False

gravity = 0.05
yvelocity = 0
godown = False
xvelocity = 0
xvcap = 5

bcount = 10

gravel = False
ungravel = False
nofloor = False
gravelcount = random.randint(300, 500)
gravelcount2 = 200

level = 1

while True:


    SCREEN.fill('#ffffff')

    bcount += 1
    gravelcount -= 1
    if ungravel:
        gravelcount2 -= 1


    if 0 <= gravelcount <= 100:
        SCREEN.blit(exclaim, (player.x+(exclaim.get_width()/2), player.y-17, exclaim.get_width(), exclaim.get_height()))
    if gravelcount == 0:
        ungravel = True
        gravel = True
    if gravelcount2 == 0:
        ungravel = False
        gravelcount2 = 200
        gravelcount = random.randint(300, 700)
        nofloor = False
        platformgroup.add(toremove)

    if bcount >= 10:
        button = pygame.image.load('assets/button-1.png')
        button = pygame.transform.scale(button, (80, 40))
        bcount = 10

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
            mousex, mousey = pygame.mouse.get_pos()
            if mousex < buttonrect.right and mousey < buttonrect.bottom and bcount >= 10:
                button = pygame.image.load('assets/button-2.png')
                button = pygame.transform.scale(button, (80, 40))
                bcount = 0
                genmap()
                player.x = 5
                player.y = 499 - player.image.get_height()
                gravel = False
                nofloor = False
                gravelcount = random.randint(100, 500)
                gravelcount2 = 200
                ungravel = False
                toremove = None

    godown = True

    for platform in platformgroup:

        if player.rect.bottom > platform.rect.top and \
                player.rect.right > platform.rect.left and \
                player.rect.left < platform.rect.right and \
                player.rect.bottom < platform.rect.bottom:
            godown = False
            yvelocity = 0
            jumpable = True
            if player.rect.bottom < platform.rect.bottom:
                player.y = platform.rect.top - player.image.get_height() + 1

    if player.y >= 449 - player.image.get_height() and not nofloor:
        yvelocity = 0
        godown = False
        jumpable = True
        if player.y > 449 - player.image.get_height():
            player.y = 449 - player.image.get_height()

    if player.rect.colliderect(trophyrect):
        genmap()
        player.x = 5
        player.y = 499 - player.image.get_height()
        gravel = False
        nofloor = False
        gravelcount = random.randint(100, 500)
        gravelcount2 = 200
        ungravel = False
        toremove = None
        level += 1

    if godown == True:
        yvelocity += gravity
        yvelocity = round(yvelocity, 2)

    if player.rect.left <= 0:
        a = False
        xvelocity = 0
    if player.rect.right >= WIDTH-10:
        d = False
        xvelocity = 0
    if player.rect.top - 50 >= HEIGHT:
        genmap()
        player.x = 5
        player.y = 499 - player.image.get_height()
        gravel = False
        nofloor = False
        gravelcount = random.randint(100, 500)
        gravelcount2 = 200
        ungravel = False
        toremove = None
        level -= 1

    if a and abs(xvelocity) < xvcap:
        xvelocity -= 0.2
        xvelocity = round(xvelocity, 1)
    if d and abs(xvelocity) < xvcap:
        xvelocity += 0.2
        xvelocity = round(xvelocity, 1)
    if ((a == False and d == False) or (a == True and d == True)) and jump == False:
        for z in range(4):
            if xvelocity < 0:
                xvelocity += 0.1
                xvelocity = round(xvelocity, 1)
            elif xvelocity > 0:
                xvelocity -= 0.1
                xvelocity = round(xvelocity, 1)

    player.x += xvelocity

    if not jumpable:
        jump = False

    if jump and jumpable:
        yvelocity = -2
        jump = False
        jumpable = False

    player.y += yvelocity

    if gravel and not nofloor:
        sprites = platformgroup.sprites()
        toremove = random.choices(sprites, k=10)
        platformgroup.remove(toremove)
        nofloor = True
        gravel = False

    platformgroup.update()
    platformgroup.draw(SCREEN)
    #platlegsgroup.draw(SCREEN)
    player.update()

    SCREEN.blit(grass, (0, 450, grass.get_width(), grass.get_height()))
    SCREEN.blit(button, buttonrect)
    SCREEN.blit(player.image, player.rect)
    SCREEN.blit(trophy, trophyrect)

    leveltext = font1.render(f'Level {str(level)}', True, '#000000')
    SCREEN.blit(leveltext, (WIDTH-leveltext.get_width(), 0, leveltext.get_width(), leveltext.get_height()))

    pygame.display.flip()
    CLOCK.tick(60)
