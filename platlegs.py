import pygame

class PlatformLegs(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/platformlegs.png'), (60, 25))
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 60, 25)