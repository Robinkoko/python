##from random import *
##a =['월','화','수','목','금','토','일']
##print (choice(a))

##a =['월','화','수','목','금']
##print(choice([True,False]))
##print(choice(a))

##a = [1,2,3,4,5]
##print(choices(a, [1,1,10,1,1],k =3))

##a = [0,1,2,3,4,5]
##r = choice(a)
##if r == 0:
##    print("Loss!")
##else:
##    print(f'NO.{r}  spot!')

from random import *
import turtle
house=turtle.Turtle()
house.up()
house.goto(350,-200)
house.down()
house.fillcolor('royalblue')
house.begin_fill()
for i in range(4):
    house. fd(100)
    house.rt(90)
house.end_fill()
house.fillcolor('blue')
house.begin_fill()
for i in range(3):
    house.fd(100)
    house.lt(120)
house.end_fill()
line=turtle.Turtle()
line.up()
line.goto(-450,-300)
line.down()
line.write("0" ,False ,font = ('Arial',5,"bold"))
line.fd(400)
line.write("50" ,False,font = ('Arial',5,"bold"))
line.fd(400)
line.write("100" ,False,font = ('Arial',5,"bold"))
t = turtle.Turtle(shape = "turtle")
t.up()
t.goto(-450,-300)
t.fillcolor('pink')
g=turtle.Turtle()
g.write("씨큐브 코딩의 타자게임!" ,True,font = ('Arial',20,"bold"))
fruit = ["apple",'banana','stawberry','watermelon','mandrain','peach','grapes','orange','pear','kiwi']
score = 0
n = randint(5,10)

for i in range (n):
    s =choice(fruit)
    word = turtle.textinput('fruit','%s(%d/%d)' % (s,i+1, n))
    if word == s:
        score += 1
rate = score / n * 100

g.up()
g.goto(0,-50)
g.down()
g.write('%d/%d번 성공!' % (score,n),True,font = ('Arial',15,"bold"))
g.up()
g.goto(0,-100)
g.down()
g.write("정확도 : %.1f%%" % rate,True,font = ('Arial',15,"bold"))

distance = t.distance(line)/100 *rate
t.speed(1)
t.forward(distance)
if rate ==100:
    t.write('집에 데려다 줘서 고마워♬',False,'center',font= ('Arial',15,"normal"))
elif rate >= 80:
    t.write('집이 코앞인데!! 한번 더 나에게 질풍같은 시도를~',False,'center',font= ('Arial',15,"normal"))
elif rate >= 50:
    t.write('집에 가고싶어!! ㅠㅇㅠ',False,'center',font= ('Arial',15,"normal"))
else:
    t.color('black')
    t.right(360)
    t.write('주거써용',False,'center',font= ('Arial',15,"normal"))
