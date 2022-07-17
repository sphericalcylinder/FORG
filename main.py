import pygame
import sys
import random
from marlene import Marlene
from scaffold import Platform
import coordchoices
import startscreen, endscreen, winscreen

RESOLUTION = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("FORG")
pygame.display.set_icon(pygame.image.load('assets/trophy.ico'))
CLOCK = pygame.time.Clock()
pygame.font.init()

pygame.event.set_allowed(
    (pygame.MOUSEBUTTONDOWN))

font1 = pygame.font.SysFont('timesnewroman', 22)

platformgroup = pygame.sprite.Group()

player = Marlene()
#platformvalues = []
#supportedplatforms = []
def genmap():

    platformgroup.empty()
    for y in range(16):
        for e in range(2):
            platform3 = Platform(coordchoices.ychoices[y])
            platform3.generate()
            platformgroup.add(platform3)
        #platformvalues.append([platform3.x, platform3.y, y, platform3])

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

ANIMATIONFRAMEDURATION = 3
global animationframeposition
animationframeposition = 0
global animationcurrentframe
animationcurrentframe = 0
global lastmovement
lastmovement = None

def advanceAnimation():
    global animationframeposition
    global animationcurrentframe
    global lastmovement
    global a
    global d
    if a == True and d == False and jumpable == True:
        lastmovement = "a"
        if animationframeposition < ANIMATIONFRAMEDURATION:
            animationframeposition += 1
        else:
            if animationcurrentframe > 3:
                animationcurrentframe = 0
            else:
                player.image = player.leftwalkimages[animationcurrentframe]
                animationcurrentframe += 1
                animationframeposition = 0
            
    elif d == True and a == False and jumpable == True:
        lastmovement = "d"
        if animationframeposition < ANIMATIONFRAMEDURATION:
            animationframeposition += 1
        else:
            if animationcurrentframe > 3:
                animationcurrentframe = 0
            else:
                player.image = player.rightwalkimages[animationcurrentframe]
                animationcurrentframe += 1
                animationframeposition = 0 
            
    elif (a and d and jumpable) or (not a and not d and jumpable):
        player.image = player.forwards
        animationframeposition = 0
        animationcurrentframe = 0
        #make the thingy face forwards AND set the current frame and frame position to ZERO
    elif jumpable == False:
        #do the standing pose with the lastmovement thing and set the thingys to zero
        if lastmovement == "a":
            player.image = player.leftwalkimages[0]
        elif lastmovement == "d":
            player.image = player.rightwalkimages[0]
        else:
            player.image = player.forwards
        animationframeposition = 0
        animationcurrentframe = 0


pygame.event.set_allowed(
    (pygame.KEYDOWN, pygame.KEYUP))

grass = pygame.image.load('assets/grass2.png')
exclaim = pygame.image.load('assets/exclamatorypunctuation.png')
trophy = pygame.image.load('assets/trophy.png')
trophyrect = pygame.Rect((WIDTH/2)-(trophy.get_width()/2), 0, trophy.get_width(), trophy.get_height())

global a
global d
a = False
d = False
jump = False
jumpable = False

gravity = 0.05
yvelocity = 0
godown = False
xvelocity = 0
xvcap = 5

gravel = False
ungravel = False
nofloor = False
gravelcount = random.randint(300, 500)
gravelcount2 = 200
playerplat = None
numtoremove = 15

level = 1
lastlevel = 0
dobreak = False
runendscreen = False
runwinscreen = False

startscreen.run(SCREEN, WIDTH, HEIGHT, CLOCK)

while True:

    SCREEN.fill('#ffffff')

    if runendscreen:
        endscreen.run(SCREEN, WIDTH, HEIGHT, CLOCK)
        startscreen.run(SCREEN, WIDTH, HEIGHT, CLOCK)
        a = False
        d = False
        jump = False
        jumpable = False

        gravity = 0.05
        yvelocity = 0
        godown = False
        xvelocity = 0
        xvcap = 5

        gravel = False
        ungravel = False
        nofloor = False
        gravelcount = random.randint(300, 500)
        gravelcount2 = 200
        playerplat = None
        numtoremove = 15

        level = 1
        lastlevel = 0
        dobreak = False
        runendscreen = False
        runwinscreen = False
    
    if runwinscreen:
        winscreen.run(SCREEN, WIDTH, HEIGHT, CLOCK)
        startscreen.run(SCREEN, WIDTH, HEIGHT, CLOCK)
        a = False
        d = False
        jump = False
        jumpable = False

        gravity = 0.05
        yvelocity = 0
        godown = False
        xvelocity = 0
        xvcap = 5

        gravel = False
        ungravel = False
        nofloor = False
        gravelcount = random.randint(300, 500)
        gravelcount2 = 200
        playerplat = None
        numtoremove = 15

        level = 1
        lastlevel = 0
        dobreak = False
        runendscreen = False
        runwinscreen = False

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
        gravelcount = random.randint(200, 700)
        nofloor = False
        platformgroup.add(toremove)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dobreak = True
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_a:
                    a = True
                case pygame.K_d:
                    d = True
                case pygame.K_SPACE:
                    jump = True
                case pygame.K_ESCAPE:
                    startscreen.run(SCREEN, WIDTH, HEIGHT, CLOCK)
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_a:
                    a = False
                case pygame.K_d:
                    d = False

    if dobreak:
        break

    advanceAnimation()

    godown = True

    for platform in platformgroup:
    
        if player.rect.bottom > platform.rect.top and \
                player.rect.right > platform.rect.left and \
                player.rect.left < platform.rect.right and \
                player.rect.bottom < platform.rect.bottom:
            godown = False
            yvelocity = 0
            jumpable = True
            playerplat = platform
            if player.rect.bottom < platform.rect.bottom:
                player.y = platform.rect.top - player.image.get_height() + 1
            if gravel:
                platform.remove(platformgroup)
                godown = True
                jumpable = False

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
        gravelcount = random.randint(200, 700)
        gravelcount2 = 200
        ungravel = False
        toremove = None
        level += 1
        if level % 3 == 0:
            numtoremove += 1
        if level == 10:
            runwinscreen = True
        
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
        gravelcount = random.randint(200, 700)
        gravelcount2 = 200
        ungravel = False
        toremove = None
        level -= 1
        if level > lastlevel:
            lastlevel = level - 1
        if level == 0 or lastlevel == level:
            runendscreen = True

    if a and abs(xvelocity) < xvcap:
        xvelocity -= 0.2
        xvelocity = round(xvelocity, 1)
    if d and abs(xvelocity) < xvcap:
        xvelocity += 0.2
        xvelocity = round(xvelocity, 1)
    if ((not a and not d) or (a and d )) and not jump:
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
        toremove = random.choices(sprites, k=numtoremove)
        toremove.append(playerplat)
        platformgroup.remove(toremove)
        nofloor = True
        gravel = False

    platformgroup.update()
    platformgroup.draw(SCREEN)
    #platlegsgroup.draw(SCREEN)
    player.update()

    SCREEN.blit(grass, (0, 450, grass.get_width(), grass.get_height()))
    SCREEN.blit(player.image, player.rect)
    SCREEN.blit(trophy, trophyrect)

    leveltext = font1.render(f'Level {str(level)}', True, '#000000')
    SCREEN.blit(leveltext, (WIDTH-leveltext.get_width(), 0, leveltext.get_width(), leveltext.get_height()))

    pygame.display.flip()
    CLOCK.tick(60)
