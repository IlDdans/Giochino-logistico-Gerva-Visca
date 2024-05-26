import pygame
from random import randint
class Boscaiolo:
    def __init__(self, screen):
        self.screen=screen
        self.pos=0
        self.w=150
        self.h=150
        self.x=100
        self.y=400
        self.boscaiolo=pygame.image.load("boscaiolo.png").convert_alpha()
        self.boscaiolodestra=pygame.image.load("boscaiologirato.png").convert_alpha()
        self.boscaiolodestra=pygame.transform.scale(self.boscaiolodestra, (150,150))
        self.boscaiolo = pygame.transform.scale(self.boscaiolo, (150,150))

        self.rect=self.boscaiolo.get_rect()
    def draw(self):
        if self.pos==0:
            self.screen.blit(self.boscaiolo, (self.x, self.y))
        else:
            self.screen.blit(self.boscaiolodestra, (self.x+250, self.y))
        