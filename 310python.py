a = int(input("몇각형을 그릴까?"))
import turtle
t = turtle.Turtle()
t.shape("turtle")
for i in range(a):
    t.rt(360 / a)
    t.fd(300 / a)
t.ht()
