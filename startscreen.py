import pygame
import random
import sys
from button import Button

def run(SCREEN, WIDTH, HEIGHT, CLOCK):
    dobreak = False
    startxv = 0
    startyv = 0
    font1 = pygame.font.Font('assets/didot.ttc', 75)
    font2 = pygame.font.Font('assets/notosans.ttf', 35)
    font3 = pygame.font.Font('assets/notosans.ttf', 20)
    white = pygame.image.load('assets/white.png')
    white.set_alpha(25)
    while startxv == 0:
        startxv = random.randint(-5, 5)
    while startyv == 0:
        startyv = random.randint(-5, 5)
    startx = 200
    starty = 200

    buttongroup = pygame.sprite.Group()

    playbutton = Button(pygame.image.load('assets/buttons/playbutton.png'))
    buttongroup.add(playbutton)
    buttongroup.update()
    credits = Button(pygame.image.load('assets/buttons/creditsbutton.png'))
    credits.y = playbutton.rect.bottom + 125
    buttongroup.add(credits)
    buttongroup.update()
    info = Button(pygame.image.load('assets/buttons/infobutton.png'))
    info.y = credits.rect.bottom + 125
    buttongroup.add(info)
    buttongroup.update()

    gamejamlogo = pygame.transform.scale(pygame.image.load('assets/jam2022.png'), (200, 110))
    

    bcount = 10
    pressed = False
    docredits = False
    doinfo = False

    while True:
        SCREEN.blit(white, (0, 0, white.get_width(), white.get_height()))

        if pressed:
            bcount -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if playbutton.rect.collidepoint(mousex, mousey):
                    pressed = True
                    playbutton.image = pygame.image.load('assets/buttons/playbuttonpressed.png')
                    dobreak = True
                if credits.rect.collidepoint(mousex, mousey):
                    pressed = True
                    credits.image = pygame.image.load('assets/buttons/creditsbuttonpressed.png')
                    docredits = True
                if info.rect.collidepoint(mousex, mousey):
                    pressed = True
                    info.image = pygame.image.load('assets/buttons/infobuttonpressed.png')
                    doinfo = True
                
        if dobreak and bcount == 0:
            break
        if docredits and bcount == 0:
            while True:

                SCREEN.fill('#ffffff')

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            dobreak = True
                
                if dobreak == True:
                    dobreak = False
                    docredits = False
                    bcount = 10
                    pressed = False
                    credits.image = pygame.image.load('assets/buttons/creditsbutton.png')
                    break

                pogam = font1.render("Programming:", True, '#000000')
                pogam2 = font2.render("sphericalcylinder and flerbyGerby37", True, '#000000')
                aart = font1.render("Art Assets:", True, '#000000')
                aart2 = font2.render("flerbyGerby37", True, '#000000')
                esc = font2.render("ESC to return to menu", True, '#000000')

                SCREEN.blit(pogam, (0, 0, pogam.get_width(), pogam.get_height()))
                SCREEN.blit(pogam2, (0, 100, pogam2.get_width(), pogam2.get_height()))
                SCREEN.blit(aart, (0, 200, aart.get_width(), aart.get_height()))
                SCREEN.blit(aart2, (0, 300, aart2.get_width(), aart2.get_height()))
                SCREEN.blit(esc, (0, 450, esc.get_width(), esc.get_height()))

                pygame.display.update()

        if doinfo and bcount == 0:
            while True:

                SCREEN.fill('#ffffff')

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            dobreak = True
                
                if dobreak == True:
                    dobreak = False
                    doinfo = False
                    bcount = 10
                    pressed = False
                    info.image = pygame.image.load('assets/buttons/infobutton.png')
                    break

                lin1 = font3.render("FORG is a game where you, Marlene the ant, have to get a trophy", True, '#000000')
                lin2 = font3.render("(An amazing game idea, I know)", True, '#000000')
                lin3 = font3.render("On each level, a timer will count down to \"gravel\", where chosen", True, '#000000')
                lin4 = font3.render("platforms (and the floor) disappear.", True, '#000000')
                lin5 = font3.render("Each level is procedurally randomly generated, the countdown", True, '#000000')
                lin6 = font3.render("is random, and the dissappearing platforms are random.", True, '#000000')
                lin7 = font3.render("If that's not a roll of the dice, I don't know what is!", True, '#000000')
                lin8 = font3.render("Controls are A, D, and SPACE", True, '#000000')
                lin9 = font3.render("This game was developed for the 2022 GMTK Game Jam", True, '#000000')
                esc = font2.render("ESC to return to menu", True, '#000000')

                SCREEN.blit(lin1, (0, 0, lin1.get_width(), lin1.get_height()))
                SCREEN.blit(lin2, (0, 25, lin2.get_width(), lin2.get_height()))
                SCREEN.blit(lin3, (0, 50, lin3.get_width(), lin3.get_height()))
                SCREEN.blit(lin4, (0, 75, lin4.get_width(), lin4.get_height()))
                SCREEN.blit(lin5, (0, 100, lin5.get_width(), lin5.get_height()))
                SCREEN.blit(lin6, (0, 125, lin6.get_width(), lin6.get_height()))
                SCREEN.blit(lin7, (0, 150, lin7.get_width(), lin7.get_height()))
                SCREEN.blit(lin8, (0, 200, lin7.get_width(), lin8.get_height()))
                SCREEN.blit(lin9, (0, 300, lin8.get_width(), lin8.get_height()))
                pygame.draw.rect(SCREEN, '#000000', (0, 350, 200, 110))
                SCREEN.blit(gamejamlogo, (0, 350, gamejamlogo.get_width(), gamejamlogo.get_height()))
                SCREEN.blit(esc, (0, 450, esc.get_width(), esc.get_height()))

                pygame.display.update()

        forgtext = font1.render('FORG', True, '#000000')

        if startx <= 0:
            startxv = -startxv
        if starty <= 0:
            startyv = -startyv
        if startx+forgtext.get_width() >= WIDTH:
            startxv = -startxv
        if starty+forgtext.get_height() >= HEIGHT:
            startyv = -startyv

        startx += startxv
        starty += startyv
        SCREEN.blit(forgtext, (startx, starty, forgtext.get_width(), forgtext.get_height()))
        buttongroup.draw(SCREEN)

        pygame.display.flip()
        CLOCK.tick(30)