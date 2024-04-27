i = 1
while i <= 10 :
    print(i,end = " ")
    i +=1

sum = 0
i = 1
while i <= 100 :
    sum +=i
    i +=1
  print(sum)

i = 0
while i<10:
    i +=1
    if i % 2 ==0 :
        continue
    print(i, end = " ")

while True :
    ans = input("shall we close? (y/n) ")
    if ans =='y':
        print('the end')
        break

ans = ' '
while ans !="yes" :
    ans = input("are you ready? ")
print("going out")

stamp = 0
while stamp <10:
    stamp +=1
    print("스탬프 %d개 적립" % stamp)
    if stamp == 10:
        print("무료 음료 쿠폰 1개 증정")

i =1
while i <100:
    i +=1
    print(i)

a=int(input())
k =a
i =1
while i < k:
    a += i
    i +=1
print(a)

i =1
while i  <6:
    a = int(input("input : "))
    i+=1
    if a % 5 == 0:
        continue
    else:
        print(f"output : {a}")

while True:
    a = int(input())
    if a == 0:
        break
print("end")

cut = 0
n = int(input('정수 입력 :'))
while n > 0:
    cut +=1
    n //= 10
print(f"자릿수 :{cut}")

cut = 0
n = int(input('정수 입력 :'))
while True:
    cut +=1
    n //= 10
    if n == 0:
        break
print(f"자릿수 :{cut}")

import pygame
from pygame.locals import *
import sys
timer = 0
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("tick tock, timer")
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None,36)
while True:
    for  event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    timer +=1
    screen.fill((255,255,255))
    cnt_txt = sysfont.render("timer : %d" % timer, True,(0,0,0))
    screen.blit(cnt_txt, (140,140))
    pygame.display.update()
    CLOCK.tick(1)

n =1
while n <=10:
    if n %3==0:
        print("X",end = ' ')
    else:
        print(n, end =' ')
    n +=1

n =1
while n <=20:
    if n %10==3 or n %10 == 6 or n%10 == 9:
        print("X",end = ' ')
    else:
        print(n, end =' ')
    n +=1

a = int(input("몇단?:"))
i =0
while i< 9:
    i += 1
    print("%d * %d = %d" % (a, i ,a*i))

from random import *
b = randint(1,100)
while True:
    a = int(input())
    if a<b:
        print("up")
    elif a>b:
        print("down")
    elif a==b:
        print("correct!")
        break

import pygame
from pygame.locals import *
import sys
from random import *
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("pygame window")
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None,36)
while True:
    for  event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    cnt_txt = sysfont.render("hi" ,True,(0,0,0))
    screen.blit(cnt_txt, (randint(0,400),randint(0,300)))
    pygame.display.update()
    CLOCK.tick(1)       
