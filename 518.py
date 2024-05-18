X = int(input())
N = int(input())
b=0
for i in range(N):
    a = input().split()
    b += int(a[0]) * int(a[1])
if b == X:
    print('yes')
else:
    print('no')
##-----------------------------------------------------------------------------------------------------------------------
import pygame
import sys
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((300,300))
CLOCK = pygame.time.Clock()
BLACK =(0,0,0)
WHITE =(255,255,255)
sysfont = pygame.font.SysFont(None,36)
txt = sysfont.render(" ",True,BLACK)

while True:
    SCREEN.fill(WHITE)
    for event in pygame.event.get()  :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                txt = sysfont.render("UP",True,BLACK)
            if event.key == K_DOWN:
                txt = sysfont.render("DOWN",True,BLACK)
            if event.key == K_LEFT:
                txt = sysfont.render("LEFT",True,BLACK)
            if event.key == K_RIGHT:
                txt = sysfont.render("RIGHT",True,BLACK)
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    SCREEN.blit(txt, (100,120))
    pygame.display.update()
    CLOCK.tick(60)

##-----------------------------------------------------------------------------------------------------------------------
import pygame
import sys
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((600,600))
CLOCK = pygame.time.Clock()
BLACK =(0,0,0)
WHITE =(255,255,255)
sysfont = pygame.font.SysFont(None,36)
txt = sysfont.render(" ",True,BLACK)
coord = sysfont.render(" ",True, (0,0,0))
x,y=0,0

while True:
    SCREEN.fill(WHITE)
    for event in pygame.event.get()  :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            x,y=event.pos[0] ,event.pos[1]
            coord = sysfont.render(f"{x},{y}", True , BLACK)
            if event.button == 1:
                txt = sysfont.render("1",True,BLACK)
            if event.button == 2:
                txt = sysfont.render("2",True,BLACK)
            if event.button == 3:
                txt = sysfont.render("3",True,BLACK)
            if event.button == 4:
                txt = sysfont.render("4",True,BLACK)
            if event.button == 5:
                 txt = sysfont.render("5",True,BLACK)
                 
    SCREEN.blit(txt, (285, 220))
    SCREEN.blit(coord,(x, y))
    pygame.display.update()
    CLOCK.tick(60)
##-----------------------------------------------------------------------------------------------------------------------
import pygame
import sys
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((600,600))
CLOCK = pygame.time.Clock()
BLACK =(0,0,0)
WHITE =(255,255,255)
sysfont = pygame.font.SysFont(None,36)
txt = sysfont.render(" ",True,BLACK)
n =0

while True:
    SCREEN.fill(WHITE)
    for event in pygame.event.get()  :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                n += 10
            if event.key == K_DOWN:
                n -= 10
            if event.key == K_LEFT:
                n *= 10
            if event.key == K_RIGHT:
                n //= 10
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                n = 0

    txt = sysfont.render(f"{n}",True,BLACK)              
    SCREEN.blit(txt, (100, 120))
    pygame.display.update()
    CLOCK.tick(60)
##-----------------------------------------------------------------------------------------------------------------------
import pygame
import sys
from pygame.locals import *
from random import *

pygame.init()
SCREEN = pygame.display.set_mode((600,600))
CLOCK = pygame.time.Clock()
BLACK =(0,0,0)
WHITE =(255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE= (0,0,255)
direc = ('UP','DOWN','LEFT','RIGHT')
i = 0
cnt =0
rect1 = Rect(250,200,100,60)
rect2 = Rect(250,400,100,60)
rect3= Rect(100,300,100,60)
rect4 = Rect(400,300,100,60)

COLOR1 = GREEN
COLOR2 = GREEN
COLOR3 = GREEN
COLOR4 = GREEN

sysfont = pygame.font.SysFont(None,36)
sysfont2 = pygame.font.SysFont(None,66)
u_txt = sysfont.render("UP",True,WHITE)
d_txt = sysfont.render("DOWN",True,WHITE)
l_txt = sysfont.render("LEFT",True,WHITE)
r_txt = sysfont.render("RIGHT",True,WHITE)
while True:
    SCREEN.fill(WHITE)
    cnt +=1
    if cnt >=60 :
        cnt=0
        i = randint(0,3)
    dr_txt = sysfont.render(direc[i],True,BLACK)
    SCREEN.blit(dr_txt, (250,100))
    for event in pygame.event.get()  :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if i == 0:
                    COLOR1 = BLUE
                else:
                    COLOR1 = RED
            if event.key == K_DOWN:
                 if i == 1:
                    COLOR2 = BLUE
                 else:
                    COLOR2 = RED
            if event.key == K_LEFT:
                 if i == 2:
                     COLOR3 = BLUE
                 else:
                     COLOR3 = RED
            if event.key == K_RIGHT:
                  if i == 3:
                     COLOR4 = BLUE
                  else:
                     COLOR4 = RED
        if event.type == KEYUP:
            COLOR1 = GREEN
            COLOR2 = GREEN
            COLOR3 = GREEN
            COLOR4 = GREEN

    pygame.draw.rect(SCREEN,COLOR1,rect1)
    pygame.draw.rect(SCREEN,COLOR2,rect2)
    pygame.draw.rect(SCREEN,COLOR3,rect3)
    pygame.draw.rect(SCREEN,COLOR4,rect4)


    SCREEN.blit(u_txt, (285,220))
    SCREEN.blit(d_txt, (260,420))
    SCREEN.blit(l_txt, (120,320))
    SCREEN.blit(r_txt, (410,320))
    
    pygame.display.update()
    CLOCK.tick(60)
