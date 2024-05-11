i=1
while i<11:
    print(i,end = ' ')
    i+=1

List = ['a','b','c']
for s in List:
    print(s)

num_List = [1,2,3,4,5]
sum = 0
for num in num_List:
    sum+=num
print("avg:%d" % (sum//5))

alist = [1,2,3,]
blist = [10,100,1000]
for a in alist :
    for b in blist :
        print(a*b,end=' ' )
    print()

for i in range(10):
    print(i, end=' ')

for i in range(10,21):
    print(i, end=' ')

for i in range(1 ,10, 2):
    print(i, end=' ')

List = ['Noah','Minsu','Keily','Yuri']
for name in List :
    print(f'{name} , Congratulation!')

n = int(input("몇단?"))
for i in range (1,10) :
    print(" %d * %d = %d" % (n, i,n*i))

for i in range(1,11):
    print(i, end = ' ')

n = int (input(" "))
for i in range(n):
    print(i+1, end = ' ')

for i in range(1,100,2):
    print(i+1, end = ' ')

n = str(input(" "))
for i in range(5):
    print(n, end = ' ')

n = int (input(" "))
for i in range(n,51):
    print(i, end = ' ')

h_List = [159,163,173,158,169]
sum = 0
for h in h_List:
    sum+=h
print("sum:%d" % sum)
print("avg:%.2f" % (sum/len(h_List)))

h_List = []
for i in range (5):
    h_List.append (int(input(' ')))    
sum = 0
for h in h_List:
    sum+=h
print("sum:%d" % sum)
print("avg:%.2f" % (sum/len(h_List)))

for i in range(3):
    for j in range(1,6):
        print(j,end = ' ')
    print()

for i in range(5):
    for j in range(5):
        print('*',end = '')
    print()

for i in range(2,10):
    print(f"< {i}단 >")
    for j in range(1,10):
        print(" %d * %d = %2d" % (i,j,i*j))
    print()

import sys
import pygame
from pygame.locals import *

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
CLOCK = pygame.time.Clock()
BLACK=(   0,   0,   0)
WHITE=(255, 255, 255)
RED=(255,   0,    0)
GREEN=(    0, 255,    0)
BLUE=(    0,    0, 255)
while True:
    for event in pygame.event.get() :
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SURFACE.fill(WHITE)
    rec=Rect(20,10,60,40)
    pygame.draw.rect(SURFACE,RED,rec)
    pygame.draw.circle(SURFACE,GREEN,(120,50),10)
    pygame.draw.polygon(SURFACE,BLUE, [[50,50],[0,100],[100,100]])
    pygame.draw.line(SURFACE,BLACK,[120,0],[120,120])
    pygame.display.update()
    CLOCK.tick(1)

n = int(input())
a=0
for i in range (0,n,3):
    a +=i
print(a)

M = 0
for i in range (10):
    n = int(input())
    if n>M:
        M=n
print(M)

m = 0
for i in range (10):
    n = int(input())
    if i == 0:
        m=n
        continue
    elif n<m:
        m=n
print(m)
        
n = int(input('n:'))
for i in range (n):
    for j in range(i+1):
        print('*', end ='')
    print()

n = int(input('n:'))
for i in range (n):
    for j in range(n-i-1):
        print(' ' ,end = '')
    for j in range(i+1):
        print('*' ,end = '')
    print()
