import pygame
from random import randint
class Boscaiolo:
    def __init__(self, screen, x, y):
        self.screen=screen
        self.x=x
        self.y=y
        self.pos=0

        self.boscaiolo=pygame.image.load("boscaiolo.png").convert_alpha()
        self.boscaiolodestra=pygame.image.load("boscaiologirato.png").convert_alpha()
        self.boscaiolodestra=pygame.transform.scale(self.boscaiolodestra, (self.boscaiolodestra.get_width()*0.3, self.boscaiolodestra.get_height()*0.3))
        self.boscaiolo = pygame.transform.scale(self.boscaiolo, (self.boscaiolo.get_width()*0.3, self.boscaiolo.get_height() * 0.3))
        self.w=self.boscaiolo.get_width()
        self.h=self.boscaiolo.get_height()

        self.rect=self.boscaiolo.get_rect()
    def draw(self):
        if self.pos==0:
            self.screen.blit(self.boscaiolo, (self.x, self.y))
        else:
            self.screen.blit(self.boscaiolodestra, (self.x+250, self.y))
        