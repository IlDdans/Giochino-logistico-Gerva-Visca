import pygame, sys
pygame.init()




WIDTH, HEIGHT = 800, 600
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


    clock.tick(fps)
    pygame.display.flip()