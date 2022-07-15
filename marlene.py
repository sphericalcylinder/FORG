import pygame

class Marlene(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/marlene.png')
        self.x = 5
        self.y = 499 - self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, 10, self.image.get_height())

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 10, self.image.get_height())