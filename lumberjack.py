import pygame
from random import randint
class Boscaiolo:
    def __init__(self, screen, size, pos):
        self.screen=screen
        self.size=size
        self.pos=pos

        self.boscaiolo=pygame.image.load("boscaiolo.png").convert_alpha()
        self.rect=self.boscaiolo.get_rect
        self.velocita=[randint(4,8)]
        