t1 = (1,)
t2 = (4,5,6)
print(t1+t2)
print(t2*2)
print(t2[0])
print(t2[1:3])
del t2[0]

a = [1,2,3]
del a[0]
print(a)

a = "Carpe Diem!"
b = [1,2,3,4,5,6]
print(len(a))
print(len(b))

d = {'name' : 'jane', 'name' : 'Mason', 'age' : 12 , 'number' : 123456}
print(d)
print(d['age'])

d = {'a' : 1,'b' : 2}
d['c'] = 3
del d['a']
print(d)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 - s2)
print(s1 & s2)
print(s1 | s2)

a= {'a' :1 , 'b' :2 ,'c' : 3, 'd' :4}
print(a.keys())
print(a.values())
print(a.items())
a.clear()
print(a)

a = {'name' : 'Minsu','address' : 'seoul','phone' : '010-1234-1234'}
print(a.keys())

a = set([1,2,3])
a.add(4)
print(a)
a.update('abc')
print(a)
a.remove('c')
print(a)

a = set('abc')
a.update('abcde')
print(a)

n = int(input('몇단? '))
i = 0
while i <9:
    i += 1
    print(n*i)

import turtle
t = turtle.Turtle()
t.fillcolor('red')
t.begin_fill()
t.right(60)
t.circle(25,180)
t.rt(120)
t.circle(25,180)
t.rt(120)
t.circle(25,180)
t.rt(120)
t.circle(25,180)
t.rt(120)
t.circle(25,180)
t.rt(120)
t.circle(25,180)
t.end_fill()
t.fillcolor('yellow')
t.begin_fill()
t.rt(60)
t.circle(50)
t.end_fill()

s = turtle.textinput('즐거운 시큐브 코딩', '이름을 알려주세요')
t.write(f"{s}님 반갑습니다!")

s = '즐거운 시큐브 코딩'
n =turtle.numinput(s,"앞으로 얼마나 이동할까요?")
t.fd(n)
ang = turtle.numinput(s,"오른쪽으로 얼마나 회전할까요? ", default=0 ,minval = 0 ,maxval=360)
t.rt(ang)

d = {'a' :90, 'b' :85, 'c' :95}
d['e'] = 70
d['a']=100
print(d)

d = {'plus' : ['더하기 , 장점'],'minus' : ['빼기 , 적자'],'multiply' : ['곱하다 , 다양하게'],'divison' : ['나누기 , 분열']}
w = input(' 단어 : ')
print(d[w])

d = {'plus' : ['더하기 , 장점'],'minus' : ['빼기 , 적자'],'multiply' : ['곱하다 , 다양하게'],'divison' : ['나누기 , 분열']}
print(d.keys())

d = {'plus' : ['더하기 , 장점'],'minus' : ['빼기 , 적자'],'multiply' : ['곱하다 , 다양하게'],'divison' : ['나누기 , 분열']}
d['sqare'] = '제곱'
print(d.items())

d = {'plus' : ['더하기 , 장점'],'minus' : ['빼기 , 적자'],'multiply' : ['곱하다 , 다양하게'],'divison' : ['나누기 , 분열']}
d['sqare'] = '제곱'
w = input(' 단어 : ')
del d[w]
print(d)

import turtle
from random import *
t = turtle.Turtle()
c = ['red','orange','blue','green','yellow']
t.fillcolor(c[randint(0,6)])
t.begin_fill()
t.circle(randint)
t.circle(randint)
t.circle(randint)
t.circle(randint)
t.end_fill()
