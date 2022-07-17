import pygame
import sys

def run(SCREEN, WIDTH, HEIGHT, CLOCK):

    font1 = pygame.font.Font('assets/didot.ttc', 75)
    font2 = pygame.font.Font('assets/notosans.ttf', 35)
    dobreak = False

    while True:
        SCREEN.fill('#ffffff')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    dobreak = True

        if dobreak:
            break

        congra = font1.render("Congradulations!", True, '#000000')
        die = font1.render("You Died!", True, '#000000')
        lin1 = font2.render("We are pleased to inform you", True, '#000000')
        lin2 = font2.render("that you no longer exist!", True, '#000000')
        lin3 = font2.render("ESC to return to menu", True, '#000000')

        SCREEN.blit(congra, ((WIDTH/2)-(congra.get_width()/2), 50, congra.get_width(), congra.get_height()))
        SCREEN.blit(die, ((WIDTH/2)-(die.get_width()/2), 150, die.get_width(), die.get_height()))
        SCREEN.blit(lin1, ((WIDTH/2)-(lin1.get_width()/2), 350, lin1.get_width(), lin1.get_height()))
        SCREEN.blit(lin2, ((WIDTH/2)-(lin2.get_width()/2), 400, lin2.get_width(), lin2.get_height()))
        SCREEN.blit(lin3, ((WIDTH/2)-(lin3.get_width()/2), 450, lin3.get_width(), lin3.get_height()))

        pygame.display.update()