import pygame

class Marlene(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/marlene.png')
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())