import pygame, sys
pygame.init()
from lumberjack import Boscaiolo

WIDTH, HEIGHT = 600, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))

sfondo=pygame.image.load("foresta.png")
ramo=pygame.image.load("ramo.png").convert_alpha()


tronco=pygame.image.load("tronco.jpg").convert_alpha()
tronco=pygame.transform.scale(tronco, (100, 550))
tronco_rect=tronco.get_rect(midtop=(WIDTH/2, 0))


boscaiolo=pygame.image.load("boscaiolo.png").convert_alpha()

boscaiolo=Boscaiolo(screen, 250-boscaiolo.get_width()*0.3, 550-boscaiolo.get_height()*0.3)


pygame.display.set_caption("Lumberjack Quandale Deangle")

fps=60
clock=pygame.time.Clock()
font=pygame.font.Font(None, 50)


while True:
    screen.blit(sfondo, (0,0))
    screen.blit(tronco, tronco_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:     
            pygame.quit()           
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                boscaiolo.drawdestra()
                pygame.display.flip()
                screen.blit(sfondo, (0,0))
                screen.blit(tronco, tronco_rect)
            if event.key==pygame.K_LEFT:
                boscaiolo.drawsinistra()
                pygame.display.flip()
                screen.blit(sfondo, (0,0))
                screen.blit(tronco, tronco_rect)
    clock.tick(fps)
   