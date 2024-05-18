import pygame
from random import randint
class Sfondo:
    def __init__(self, screen, size, pos):
        self.screen=screen
        self.size=size
        self.pos=pos

        self.boscaiolo=pygame.image.load("montagna2.png").convert_alpha()
        self.rect=self.boscaiolo.get_rect
        self.velocita=[randint(4,8)]