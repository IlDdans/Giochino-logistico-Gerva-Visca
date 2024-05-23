import pygame, sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))

sfondo=pygame.image.load("foresta.png")
ramo=pygame.image.load("ramo.png").convert_alpha()
boscaiolo=pygame.image.load("boscaiolo.png").convert_alpha()


boscaiolo = pygame.transform.scale(boscaiolo, (boscaiolo.get_width()*0.3, boscaiolo.get_height() * 0.3))
larghezzautile=boscaiolo.get_width()
altezzautile=boscaiolo.get_height()

tronco=pygame.image.load("tronco.jpg").convert_alpha()
tronco=pygame.transform.scale(tronco, (larghezzautile*0.8, 550))
tronco_rect=tronco.get_rect(midtop=(WIDTH/2, 0))

boscaiolo_rect=boscaiolo.get_rect(bottomright=(tronco_rect.left, 550))



pygame.display.set_caption("Lumberjack Quandale Deangle")

fps=60
clock=pygame.time.Clock()
font=pygame.font.Font(None, 50)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:     
            pygame.quit()           
            sys.exit()
    screen.blit(sfondo, (0,0))
    screen.blit(boscaiolo, boscaiolo_rect)
    screen.blit(tronco, tronco_rect)
    clock.tick(fps)
    pygame.display.flip()