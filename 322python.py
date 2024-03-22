import turtle
from random import *
line = turtle.Turtle()
line.speed(10)
line.pu()
line.goto(-380,240)
for i in range(3):
    line.write(i +1)
    line.right(90)
    line.fd(20)
    line.pd()
    line.fd(500)
    line.pu()
    line.bk(520)
    line.left(90)
    line.forward(300)

t1 = turtle.Turtle(shape = 'turtle')
t1.color("red")
t1.pu()
t1.goto(-400,200)
t1.pd()

t2 = turtle.Turtle(shape = 'turtle')
t2.color("pink")
t2.pu()
t2.goto(-400,50)
t2.pd()

t3 = turtle.Turtle(shape = 'turtle')
t3.color("blue")
t3.pu()
t3.goto(-400,-100)
t3.pd()

t4 = turtle.Turtle(shape = 'turtle')
t4.color("purple")
t4.pu()
t4.goto(-400,-250)
t4.pd()

t1.right(360)
t2.right(360)
t3.right(360)
t4.right(360)

t1.fd(randint(1,450))
t2.fd(randint(1,450))
t3.fd(randint(1,450))
t4.fd(randint(1,450))

t1.fd(randint(1,300))
t2.fd(randint(1,300))
t3.fd(randint(1,300))
t4.fd(randint(1,300))

t1.fd(randint(1,200))
t2.fd(randint(1,200))
t3.fd(randint(1,200))
t4.fd(randint(1,200))

##while i < 50:
##    i = i+1
##    t1.fd(randint(1,25))
##    t2.fd(randint(1,25))
##    t3.fd(randint(1,25))
##    t4.fd(randint(1,25))
