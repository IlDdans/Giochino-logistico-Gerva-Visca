import pygame
from random import randint
class Sfondo:
    def __init__(self, screen, pos,size):
        self.screen=screen
        self.pos=pos
        self.size=size

        self.sfondo=pygame.image.load("montagna2.png").convert_alpha()
        self.rect=self.sfondo.get_rect
        self.velocita=[randint(4,8)]