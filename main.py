import pygame, sys
from random import choice as rand
pygame.init()
from lumberjack import Boscaiolo
from rami import Ramo

WIDTH, HEIGHT = 600, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
perso=False
sfondo=pygame.image.load("foresta.png")


tronco=pygame.image.load("tronco.jpg").convert_alpha()
tronco=pygame.transform.scale(tronco, (100, 550))
tronco_rect=tronco.get_rect(midtop=(WIDTH/2, 0))


boscaiolo=Boscaiolo(screen)

supporto=[i for i in range(0,9)]
stati=[]
rami=[]
stati.append(None)
stati.append(1)
stati.append(rand([0,2]))
while len(stati)<9:
    supporto=[i for i in range(0,9)]
    n=rand(supporto)
    if n<8:
        stato=stati[-1]
    else:
        if stati[-1]==0:
            stato=2
        if stati[-1]==2:
            stato=0
        stati.append(1)
    stati.append(stato)
for i, stato in enumerate(stati[1::]):
    rami.append(Ramo(screen, stato, 9-i))


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
                if boscaiolo.pos==0:
                    boscaiolo.pos=2
                else:
                    if len(rami)<9:
                        for i in range(len(rami)-1):
                            rami[i]=rami[i+1]
                            rami[i].y+=50
                        n=rand(supporto)
                        if n<8:
                            rami.append(Ramo(screen, rami[-1].stato, len(rami)))
                        else

            if event.key==pygame.K_LEFT:
                if boscaiolo.pos==2:
                    boscaiolo.pos=0
                else:
                    if len(rami)<9:
                        for i in range(len(rami)-1):
                            rami[i]=rami[i+1]
                            rami[i].y+=50
                        n=rand(supporto)
                        if n<8:
                            rami.append(Ramo(screen, rami[-1].stato, len(rami)))
    boscaiolo.draw()
    if rami[0]!=None:
        if rami[0].stato==boscaiolo.pos:
            perso=True
    
    for ramo in rami:
        if ramo!=None:
            ramo.draw()
    clock.tick(fps)
    pygame.display.flip()
    