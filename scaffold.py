import pygame
import random
import coordchoices

class Platform(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('platform3.png')
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 60, 20)

    def generate(self):
        self.rect.centerx = random.choice(coordchoices.xchoices)
        self.rect.centery = random.choice(coordchoices.ychoices)
        self.x = self.rect.centerx
        self.y = self.rect.centery

    def update(self) -> None:
        self.rect = pygame.Rect(self.x, self.y, 60, 20)