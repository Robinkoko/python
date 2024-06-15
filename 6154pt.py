def two_times():
    for i in range(1,10):
        print(f"2 * {i} = {i *2}" ,end =' ')

from random import *
def random_number():
    num = random() +10
    return num
print(random_number())

def say(name):
    print("welcome",name)
    return
say("minsu")

a= 0
def f():
    global a
    global b
    print(a)
    a=10
    b=20

def a():
    print(1)
    r =b()
    print(r)
def b():
    print(2)
    return 3
a()
print(4)

def f(n):
    print(n)
    if n >1:
        f(n-1)
f(3)

def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)
fac = factorial(4)
print("4! =", fac)

def judge(n):
    if n >0 :
        print('plus')
    elif n < 0:
        print("minous")
    else :
        print("zero")

n = int(input())
judge (n)

def season(month):
    if 3<= month <= 5:
        print("spring")
    elif 6<= month <= 8:
        print("summer")
    elif 9<= month <= 11:
        print("fall")
    elif month == 12 or month == 1 or  month == 2:
        print("winter")
    else:
        print("12 이하의 자연수를 입력하세요")

from random import *
def lotto():
    lot = []
    for i in range(6):
        lot.append(randint(1,45))
    lot.sort()
    print(lot)

from random import *
def lotto():
    lot = set()
    while len(lot) <6:
        lot.add(randint(1,45))
    lot = list(lot)
    lot.sort()
    print(lot)
lotto()

def times_table(a,b):
    if a<=b:
        t=a
        for i in range((b-a)+1):
            print(f' == {t} times ==')
            for j in range (9):
                print(f'{t} * {j+1} = {t*(j+1)}')
            t+=1
    if a>b:
        t=b
        for i in range((a-b)+1):
            print(f' == {t} times ==')
            for j in range (9):
                print(f'{t} * {j+1} = {t*(j+1)}')
            t+=1
n = input().split()
a= int(n[0])
b=int(n[1])
times_table(a,b)

def func_abs(n):
    if n >= 0:
        print(n)
    if n < 0:
        print(n * -1)
a = int(input())
func_abs(a)

a = input().split('.')
print(a[1])

def f(n):
    for i in range (n):
        for j in range(n):
            print("%2d" % ((i+1)*(j+1)), end=' ')
        print()
a = int(input())
if a<100:
    f(a)
