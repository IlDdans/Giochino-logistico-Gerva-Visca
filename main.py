import pygame, sys

pygame.init()
sfondo=pygame.image.load("foresta.png")
WIDTH, HEIGHT = 600, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
boscaiolo=pygame.image.load("boscaiolo.png").convert_alpha()
larghezzautile=boscaiolo.get_width()
altezzautile=boscaiolo.get_height()
boscaiolo = pygame.transform.scale(boscaiolo, (boscaiolo.get_width()*0.3, boscaiolo.get_height() * 0.3))
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
    screen.blit(boscaiolo,(WIDTH-480,HEIGHT-180))
    clock.tick(fps)
    pygame.display.flip()