import pygame
from random import randint
class Boscaiolo:
    def __init__(self, screen, pos,size):
        self.screen=screen
        self.pos=pos
        self.size=size

        self.boscaiolo=pygame.image.load("boscaiolo.png").convert_alpha()
        self.rect=self.boscaiolo.get_rect
        self.velocita=[randint(4,8)]
    def draw(self, x, y, screen):
        screen.blit(self.boscaiolo, (x, y))
        