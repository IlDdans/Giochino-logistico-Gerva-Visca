import pygame, sys
from random import choice as rand
pygame.init()
from lumberjack import Boscaiolo
from rami import Ramo

WIDTH, HEIGHT = 600, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
perso=False
sfondo=pygame.image.load("foresta.png")
font=pygame.font.Font(None,30)

sconfitta=pygame.image.load("perso.png")
sconfitta=pygame.transform.scale(sconfitta,(600,600))

tronco=pygame.image.load("tronco.jpg").convert_alpha()
tronco=pygame.transform.scale(tronco, (100, 550))
tronco_rect=tronco.get_rect(midtop=(WIDTH/2, 0))

ceppetto=pygame.image.load("ceppetto.png")
ceppetto=pygame.transform.scale(ceppetto, (52, 52))

punteggio=0

lista_caricamento=[]
carcica1=pygame.image.load("22.png")
carcica1=pygame.transform.scale(carcica1,(carcica1.get_width()*0.2,carcica1.get_height()*0.2))
carcica2=pygame.image.load("54.png")
carcica2=pygame.transform.scale(carcica2,(carcica2.get_width()*0.2,carcica2.get_height()*0.2))
carcica3=pygame.image.load("77.png")
carcica3=pygame.transform.scale(carcica3,(carcica3.get_width()*0.2,carcica3.get_height()*0.2))
carcica4=pygame.image.load("100.png")
carcica4=pygame.transform.scale(carcica4,(carcica4.get_width()*0.21,carcica4.get_height()*0.21))

lista_caricamento.append(carcica1)
lista_caricamento.append(carcica2)
lista_caricamento.append(carcica3)
lista_caricamento.append(carcica4)

boscaiolo=Boscaiolo(screen)

sfondo1=pygame.image.load("sfondo1.png")
sfond1=pygame.transform.scale(sfondo1,(600,600))

def caricamento():
    stato=True
    i=0
    while stato:
        for i in range(len(lista_caricamento)):
            screen.blit(sfondo1,(0,0))
            screen.blit(lista_caricamento[i],(250,530))
            pygame.display.update()
            pygame.time.delay(1200)
            if i==3:
                stato=False


def menù(screen):
    sfondomenu=pygame.image.load("menu.jpg")
    sfondomenu=pygame.transform.scale(sfondomenu, (600, 600))
    play=pygame.image.load("tastoplay.png")
    play=pygame.transform.scale(play, (150,150))
    tasto_rect=pygame.Rect(225, 370, 150, 150)
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        mouse=pygame.mouse.get_pressed()
        if mouse[0]:
            pos=pygame.mouse.get_pos()
            if tasto_rect.collidepoint(pos):
                run=False

        screen.blit(sfondomenu, (0,0))
        screen.blit(play, (225, 370))
        pygame.display.flip()

boscaiolosinistra=pygame.image.load("boscaiolo.png").convert_alpha()
boscaiolodestra=pygame.image.load("boscaiologirato.png").convert_alpha()
boscaiolodestra=pygame.transform.scale(boscaiolodestra, (150,150))
boscaiolosinistra = pygame.transform.scale(boscaiolosinistra, (150,150))
supporto=[i for i in range(0,9)]
stati=[]
rami=[]
stati.append(1)
stati.append(rand([0,2]))
while len(stati)<10:
    n=rand(supporto)
    if n<6:
        stato=stati[-1]
    else:
        if stati[-1]==0:
            stato=2
        if stati[-1]==2:
            stato=0
        stati.append(1)
    stati.append(stato)
for i, stato in enumerate(stati):
    rami.append(Ramo(screen, stato, 6-i))

for ramo in rami:
    print(ramo.stato, end=" ")
print()
for ramo in rami:
    print(ramo.n, end=" ")
print()
pygame.display.set_caption("Lumberjack Quandale Deangle")
icon=pygame.image.load("iconcina.jpg")
pygame.display.set_icon(icon)

fps=60
clock=pygame.time.Clock()
font=pygame.font.Font(None, 50)

caricamento()
menù(screen)
while True:
    
    screen.blit(sfondo, (0,0))
    screen.blit(tronco, tronco_rect)
    screen.blit(ceppetto, (525, 540))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:     
            pygame.quit()           
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                screen.blit(boscaiolosinistra,(350,400))
                pygame.time.delay(150)
                pygame.display.flip()
                punteggio+=10
                if boscaiolo.pos==0:
                    boscaiolo.pos=2
                for i in range(9):
                    rami[i]=rami[i+1]
                    rami[i].y+=50
                    rami[i].n+=1
                n=rand(supporto)
                if n<7:
                    rami[9]=Ramo(screen, rami[8].stato, -2)
                else:
                    if rami[8].stato==0:
                        rami[9]=Ramo(screen, 2, -2)
                    else:
                        rami[9]=Ramo(screen, 0, -2) 
                        
                    rami[8]=Ramo(screen, 1, -1)
                
                


            if event.key==pygame.K_LEFT:
                screen.blit(boscaiolodestra,(100,400))
                pygame.display.flip()
                punteggio+=10
                if boscaiolo.pos==2:
                    boscaiolo.pos=0
                else:
                    for i in range(9):
                        rami[i]=rami[i+1]
                        rami[i].y+=50
                        rami[i].n+=1
                    n=rand(supporto)
                if n<7:
                    rami[9]=Ramo(screen, rami[8].stato, -2)
                else:
                    if rami[8].stato==0:
                        rami[9]=Ramo(screen, 2, -2)
                    else:
                        rami[9]=Ramo(screen, 0, -2)
                        
                    rami[8]=Ramo(screen, 1, -1)
            for ramo in rami:
                print(ramo.stato, end=" ")
            print()
            for ramo in rami:
                print(ramo.n, end=" ")
            print()
    fontino=font.render(f"{punteggio}",True,(250,250,250))
    font_rect=fontino.get_rect()
    font_rect.center=(480,566)
    screen.blit(fontino,font_rect)
    boscaiolo.draw()
    if rami[0].stato==boscaiolo.pos:
        perso=True
        
    for ramo in rami[0:9:]:
        ramo.draw()
    if perso:
        screen.blit(sconfitta,(0,0))
    clock.tick(fps)
    pygame.display.flip()
    