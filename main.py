import pygame, sys

pygame.init()
sfondo=pygame.image.load("foresta.png")
WIDTH, HEIGHT = 626, 626
screen=pygame.display.set_mode((WIDTH, HEIGHT))
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
    
    clock.tick(fps)
    pygame.display.flip()