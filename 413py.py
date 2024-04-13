score = 80
if score >=60 and score <= 100:
    print('pass')
else :
    print('fail')

x = 10
print(x >= 0 and x <= 10)
print(x < 0 or x > 10)
print(not x)

a = int(input())
b = int(input())
c = int(input())
print(a >=140 and b >=140 and c >= 140)

a = int(input())
if a >= 90:
    print("a")
elif a >= 80 :
    print("b")
elif a >= 70 :
    print("c")
else:
    print("f")

a = int(input())
if a%2 == 0:
    print('EVEN')
else:
    print('ODD')

y =int(input('year :  '))
if y % 4 ==0 or y%100 != 0  and y %400 == 0:
    print('leap year')
else :
    print('common year')

a = input()
if a == 'm':
    print("man")
elif a == 'w':
    print("woman")
else:
    print("what?")

m = int(input())
if m <=6 and m >0:
    print('first half')
elif m >6 and m < 13:
    print('second half')
else:
    print("월을 입력해 주세요")

print("""=====menu=====
1. burger
2. sandwitch
3. Hotdog
4. coke
5. milk
===============""")
a = int(input())
if a ==1:
    print("안돼 돌아가")
elif a ==2 or a==3:
    print("drink?")
elif a==4 :
    print(" i like coke too")
elif a==5 :
    print("hot or cold?")
else :
    print("order a menu")

from random import *

com =randint(1,3)
user =int(input('1 : 가위 ,2 : 바위 ,3 : 보'))
if com == user:
    print("Draw")
elif com == 1 and user ==2:
    print("com가위) : user (바위)\nuser wins")
elif com == 1 and user ==3:
    print("com(가위) : user (보)\ncom wins")
elif com == 2 and user ==1:
    print("com(바위) : user (가위)com wins")
elif com == 2 and user ==3:
    print("com(바위) : user (보)user wins")
elif com == 3 and user ==1:
    print("com(보) : user (가위)\nuser wins")
elif com == 3 and user ==2:
    print("com(보) : user (바위)\ncom wins")

import turtle
t = turtle.Tutrle('turtle')
t.penup()
t.setx(200)
t.write('동',font=('Arial' ,30))
t.setx(-200)
t.write('서',font=('Arial' ,30))
t.sety(-200)
t.write('남',font=('Arial' ,30))
t.sety(200)
t.write('북',font=('Arial' ,30))
t.goto(0,0)
t.pendown()
t.pencolour('bule')
a = turtle.textinput('','방향을 입력해 주세요.')
