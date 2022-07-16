import pygame
import random
import coordchoices
from platlegs import PlatformLegs

class Platform(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/platform3.png')
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 50, 20)

    def generate(self):
        self.rect.centerx = random.choice(coordchoices.xchoices)
        self.rect.centery = random.choice(coordchoices.ychoices)
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.platformlegs = PlatformLegs(self.x, self.y)

    def update(self) -> None:
        self.rect = pygame.Rect(self.x, self.y, 50, 20)