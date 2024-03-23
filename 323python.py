from random import *
import turtle

t = turtle.Turtle()
t.shape('turtle')

x = randint(0,300)
y = randint(0,300)

t.goto(x,y)

x = randint(0,300)
y = randint(0,300)

t.goto(x,y)

x = random() + randint(0,300)
y = random() + randint(0,300)

t.goto(x,y)

x = random() + randint(0,300)
y = random() + randint(0,300)

t.goto(x,y)
turtle.done()

t.circle(randint(0,100))
t.dot(randint(0,20))
t.pensize(randint(1,10))
t.setheading(randint(0,360))
t.fd(randint(0,100))
t.bk(randint(0,100))
t.setx(randint(0,300))
t.sety(randint(0,300))

