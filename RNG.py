from random import *
import pygame
import sys
from pygame.locals import *

pygame.init()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((200,200))
sysfont = pygame.font.SysFont(None,30)
while True:
    SCREEN.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                print("hello")
                

pygame.display.update()
CLOCK.tick(60)

