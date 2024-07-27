from tkinter import *
win = Tk()
canvas = Canvas(win,bg ="white",width =300,height = 300)
canvas.pack()
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
win = Tk()
canvas = Canvas(win,bg ="yellow",width =100,height = 100)
canvas.pack()
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
win = Tk()
canvas = Canvas(win,bg ="white",width =500,height = 100)
canvas.create_line(0,50,500,50,fill = "blue",width = 5)
canvas.pack()
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------\
from tkinter import *
win = Tk()
canvas = Canvas(win,bg ="white",width =500,height = 100)
canvas.create_line(100,50,400,50,fill = "green",width = 5)
canvas.pack()
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
win = Tk()
canvas = Canvas(win,bg ="white",width =500,height = 500)
canvas.create_line(250,100,250,400,fill = "red",width = 5)
canvas.pack()
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
win = Tk()
canvas = Canvas(win,bg ="white",width =500,height = 100)
canvas.create_line(0,50,500,50,fill = "blue",width = 5)
canvas.pack(fill = 'both' ,expand = True)
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
win = Tk()
canvas = Canvas(win,bg ="white",width =500,height = 100)
canvas.pack()
x1,y1 = 0,0
x2,y2=500,0
for i in range(3):
    y1+=30
    y2=y1
    canvas.create_line(x1,y1,x2,y2,fill = "red",width = 3)
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
win = Tk()
canvas = Canvas(win,bg ="white",width =500,height = 100)
canvas.pack()
x1,y1 = 0,0
x2,y2=0,100
for i in range(10):
    x1+=45
    x2=x1
    canvas.create_line(x1,y1,x2,y2,fill = "red",width = 3)
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
win = Tk()
canvas = Canvas(win,bg ="white",width =500,height = 500)
canvas.pack()
x1,y1 = 25,25
x2,y2=475,25
for i in range(10):
    canvas.create_line(x1,y1,x2,y2,fill = "blue",width = 3)
    y1+=50
    y2=y1
x1,y1 = 25,25
x2,y2=25,475
for i in range(10):
    canvas.create_line(x1,y1,x2,y2,fill = "red",width = 3)
    x1+=50
    x2=x1
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
def paint(event):
    x1,y1 = event.x,event.y
    x2,y2 = x1+5,y1+5
    canvas.create_line(x1,y1,x2,y2,width = 3)
win = Tk()
canvas = Canvas(win,bg = "white",width = 500, height = 200)
canvas.pack()
win.bind("<B1-Motion>",paint)
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
pen_color = "black"
def paint(event):
    global pen_color
    x1,y1 = event.x,event.y
    x2,y2 = x1+5,y1+5
    canvas.create_line(x1,y1,x2,y2,width = 3,fill = pen_color)
def change_color():
    global pen_color
    pen_color = "red"
win = Tk()
canvas = Canvas(win,bg = "white",width = 500, height = 200)
red = Button(win,text = "red",command = change_color)
canvas.pack()
red.pack()
win.bind("<B1-Motion>",paint)
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
pen_color = "black"
pen_width = 3
def paint(event):
    global pen_color
    x1,y1 = event.x,event.y
    x2,y2 = x1+5,y1+5
    canvas.create_line(x1,y1,x2,y2,width = pen_width,fill = pen_color)
def change_color(color):
    global pen_color
    pen_color = color
def change_width(change):
    global pen_width
    if change == '+':
        pen_width +=1
    elif change == '-':
        if pen_width > 0:
            pen_width -=1
def clear():
    canvas.delete("all")
win = Tk()
canvas = Canvas(win,bg = "white",width = 500, height = 500)
red = Button(win,text = "red",bg = "red",fg = "white",command = lambda : change_color("red"))
green = Button(win,text = "green",bg = "green",fg = "white",command = lambda : change_color("green"))
black = Button(win,text = "black",bg = "black",fg = "white",command = lambda : change_color("black"))
blue = Button(win,text = "blue",bg = "blue",fg = "white",command = lambda : change_color("blue"))
yellow = Button(win,text = "yellow",bg = "yellow",fg = "black",command = lambda : change_color("yellow"))
white = Button(win,text = "white",bg = "white",fg = "black",command =lambda : change_color("white"))
plus = Button(win,text = "+",command = lambda :  change_width("+"))
minous = Button(win,text = "-",command =  lambda : change_width("-"))
clear = Button(win,text = "clear",command = clear)
canvas.grid(row =0,column = 0,columnspan = 9)
white.grid(row = 1,column = 0)
black.grid(row = 1,column = 1)
blue.grid(row = 1,column = 2)
green.grid(row = 1,column = 3)
yellow.grid(row = 1,column = 4)
red.grid(row = 1,column = 5)
plus.grid(row = 1,column = 6)
minous.grid(row = 1,column = 7)
clear.grid(row = 1,column = 8)
win.bind("<B1-Motion>",paint)
win.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#어딘가 고장남
from tkinter import *
pen_color = "black"
pen_width = 3
mode = "pen"
canvas_color = "white"
def paint(event):
    global pen_color
    x1,y1 = event.x,event.y
    x2,y2 = x1+5,y1+5
    canvas.create_line(x1,y1,x2,y2,width = pen_width,fill = pen_color)
def change_color(color):
    global mode
    if mode == "pen":
        global pen_color
        pen_color = color
    if mode == "canvas":
        global canvas_color
        canvas_color = color
def change_width(change):
    global pen_width
    if change == '+':
        pen_width +=1
    elif change == '-':
        if pen_width > 0:
            pen_width -=1
def mode(cc):
    global mode
    mode = cc
def clear():
    canvas.delete("all")
win = Tk()
canvas = Canvas(win,bg = canvas_color,width = 500, height = 500)
red = Button(win,text = "red",bg = "red",fg = "white",command = lambda : change_color("red"))
green = Button(win,text = "green",bg = "green",fg = "white",command = lambda : change_color("green"))
black = Button(win,text = "black",bg = "black",fg = "white",command = lambda : change_color("black"))
blue = Button(win,text = "blue",bg = "blue",fg = "white",command = lambda : change_color("blue"))
yellow = Button(win,text = "yellow",bg = "yellow",fg = "black",command = lambda : change_color("yellow"))
white = Button(win,text = "white",bg = "white",fg = "black",command =lambda : change_color("white"))
plus = Button(win,text = "+",command = lambda :  change_width("+"))
minous = Button(win,text = "-",command =  lambda : change_width("-"))
clear = Button(win,text = "clear",command = clear)
canvas_color = Button(win,text = "canvas\ncolor",bg = canvas_color,fg = "black",command = lambda : mode("canvas"))
pen_color = Button(win,text = "pen\ncolor",bg = pen_color,fg = "white",command = lambda : mode("pen"))
canvas.grid(row =0,column = 0,columnspan = 5)
white.grid(row = 2,column = 1)
black.grid(row = 1,column = 1)
blue.grid(row = 1,column = 2)
green.grid(row = 1,column = 3)
yellow.grid(row = 2,column = 3)
red.grid(row = 2,column = 2)
plus.grid(row = 1,column = 4)
minous.grid(row = 2,column = 4)
clear.grid(row = 2,column = 5)
canvas_color.grid(row = 1,column = 0)
pen_color.grid(row = 2,column = 0)
win.bind("<B1-Motion>",paint)
win.mainloop()
