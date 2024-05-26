import pygame
from random import randint
class Ramo:
    def __init__(self, display, stato, n) -> None:
        self.display=display
        self.stato=stato
        self.y=50*n
        if self.stato==0:
            self.x=100
        if self.stato==2:
            self.x=350
        self.w=150
        self.h=50
        self.surf=pygame.image.load("ramo.png").convert_alpha()
        self.surf=pygame.transform.scale(self.surf, (self.w, self.h))
        if self.stato==2:
            self.surf=pygame.transform.flip(self.surf, True, False)

    def draw(self):
        if self.stato!=1:
            self.display.blit(self.surf,(self.x, self.y))