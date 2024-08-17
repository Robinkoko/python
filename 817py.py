##from tkinter import *
##win =Tk()
##canvas = Canvas(win,width =200,height = 100,bg = "white")
##canvas.pack()
##canvas.create_oval(10,10,60,60,fill = "blue")
##canvas.create_rectangle(100,10,160,60,fill = "yellow", outline='red')
##win.mainloop()
###--------------------------------------------------------------------------------------------------------------------------------------------
##from tkinter import *
##win =Tk()
##canvas = Canvas(win,width =200,height = 100,bg = "white")
##canvas.pack()
##canvas.create_polygon(100,10,30,90,160,90,fill = "red")
##win.mainloop()
###--------------------------------------------------------------------------------------------------------------------------------------------
##from tkinter import *
##win =Tk()
##canvas = Canvas(win,width =200,height = 200,bg = "white")
##x1,x2 = 0,0
##y1,y2 = 0,200
##for i in range(9):
##    x1+=20
##    x2 = x1
##    canvas.create_line(x1,y1,x2,y2)
##x1,x2 = 0,200
##y1,y2 = 0,0
##for j in range(9):
##    y1+=20
##    y2 = y1
##    canvas.create_line(x1,y1,x2,y2)
##canvas.pack()
##canvas.create_oval(40,40,160,160,fill = "blue")
###--------------------------------------------------------------------------------------------------------------------------------------------
##from tkinter import *
##win =Tk()
##canvas = Canvas(win,width =200,height = 200,bg = "white")
##x1,x2 = 0,0
##y1,y2 = 0,200
##for i in range(9):
##    x1+=20
##    x2 = x1
##    canvas.create_line(x1,y1,x2,y2)
##x1,x2 = 0,200
##y1,y2 = 0,0
##for j in range(9):
##    y1+=20
##    y2 = y1
##    canvas.create_line(x1,y1,x2,y2)
##canvas.pack()
##canvas.create_oval(60,60,140,100,fill = "blue")
###--------------------------------------------------------------------------------------------------------------------------------------------
##from tkinter import *
##win =Tk()
##canvas = Canvas(win,width =200,height = 200,bg = "white")
##x1,x2 = 0,0
##y1,y2 = 0,200
##for i in range(9):
##    x1+=20
##    x2 = x1
##    canvas.create_line(x1,y1,x2,y2)
##x1,x2 = 0,200
##y1,y2 = 0,0
##for j in range(9):
##    y1+=20
##    y2 = y1
##    canvas.create_line(x1,y1,x2,y2)
##canvas.pack()
##canvas.create_rectangle(20,20,160,100,fill = "yellow")
###--------------------------------------------------------------------------------------------------------------------------------------------
##from tkinter import *
##win =Tk()
##canvas = Canvas(win,width =200,height = 200,bg = "white")
##x1,x2 = 0,0
##y1,y2 = 0,200
##for i in range(9):
##    x1+=20
##    x2 = x1
##    canvas.create_line(x1,y1,x2,y2)
##x1,x2 = 0,200
##y1,y2 = 0,0
##for j in range(9):
##    y1+=20
##    y2 = y1
##    canvas.create_line(x1,y1,x2,y2)
##canvas.pack()
##canvas.create_rectangle(60,20,120,180,fill = "yellow")
###--------------------------------------------------------------------------------------------------------------------------------------------
##from tkinter import *
##win =Tk()
##canvas = Canvas(win,width =200,height = 200,bg = "white")
##x1,x2 = 0,0
##y1,y2 = 0,200
##for i in range(9):
##    x1+=20
##    x2 = x1
##    canvas.create_line(x1,y1,x2,y2)
##x1,x2 = 0,200
##y1,y2 = 0,0
##for j in range(9):
##    y1+=20
##    y2 = y1
##    canvas.create_line(x1,y1,x2,y2)
##canvas.pack()
##canvas.create_polygon(20,180,100,20,180,180,fill = "red")
##--------------------------------------------------------------------------------------------------------------------------------------------
##from tkinter import *
##win =Tk()
##canvas = Canvas(win,width =200,height = 200,bg = "white")
##x1,x2 = 0,0
##y1,y2 = 0,200
##for i in range(9):
##    x1+=20
##    x2 = x1
##    canvas.create_line(x1,y1,x2,y2)
##x1,x2 = 0,200
##y1,y2 = 0,0
##for j in range(9):
##    y1+=20
##    y2 = y1
##    canvas.create_line(x1,y1,x2,y2)
##canvas.pack()
##canvas.create_polygon(40,20,40,180,160,180,fill = "red")
##--------------------------------------------------------------------------------------------------------------------------------------------
##from tkinter import *
##from random import *
##def draw_shape(event):
##    color = ['black','white','blue','red','green','yellow']
##    x1,y1 = event.x,event.y
##    x2,y2=x1+randint(10,70),y1+randint(10,70)
##    canvas.create_rectangle(x1,y1,x2,y2,fill = color[randint(0,5)])
##win = Tk()
##canvas = Canvas(win,width = 300,height = 300, bg="white")
##canvas.pack()
##canvas.bind("<Double-Button-1>",draw_shape)
##win.mainloop()
##--------------------------------------------------------------------------------------------------------------------------------------------
##from tkinter import *
##def draw_shape(event):
##    x1,y1 = event.x,event.y
##    x2,y2=x1-25,y1
##    x3,y3 = x1+25,y1+50
##    canvas.create_oval(x2,y2,x3,y3,fill = "yellow")
##win = Tk()
##canvas = Canvas(win,width = 300,height = 300, bg="white")
##canvas.pack()
##canvas.bind("<Double-Button-1>",draw_shape)
##win.mainloop()
##--------------------------------------------------------------------------------------------------------------------------------------------
##from tkinter import *
##def draw_shape(event):
##    x1,y1 = event.x,event.y
##    x2,y2=x1-25,y1+25
##    x3,y3 = x1+25,y1+25
##    canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill = "green")
##win = Tk()
##canvas = Canvas(win,width = 300,height = 300, bg="white")
##canvas.pack()
##canvas.bind("<Double-Button-1>",draw_shape)
##win.mainloop()
##--------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
pen_col = "black"
pen_width = 2
mode = "pen"
canvas_col = "white"
fill_color = "white"
shape_width = 10
def paint(event):
    global pen_col
    x1,y1 = event.x,event.y
    x2,y2 = x1+5,y1+5
    canvas.create_line(x1,y1,x2,y2,width = pen_width,fill = pen_col)
def change_color(color):
    global mode
    global pen_col
    global fill_color
    if mode == "pen":
        pen_color['bg'] = color
        pen_col = color
    elif mode == "canvas":
        canvas_color['bg']=color
        canvas['bg'] = color
    elif mode == "fill":
        fill_color = color
        fill['bg'] = color
def draw_shape(event):
    global mode
    global fill_color
    if mode == "cir":
        x1,y1 = event.x - shape_width,event.y - shape_width
        x2,y2 = event.x + shape_width,event.y + shape_width
        canvas.create_oval(x1,y1,x2,y2,fill= fill_color)
    elif mode == "rect":
        x1,y1 = event.x - shape_width,event.y - shape_width
        x2,y2 = event.x + shape_width,event.y + shape_width
        canvas.create_rectangle(x1,y1,x2,y2,fill= fill_color)
    elif mode == "poly":
        x1,y1 = event.x,event.y
        x2,y2 = event.x + shape_width,event.y + shape_width
        x3,y3 = event.x - shape_width,event.y + shape_width
        canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill= fill_color)
def change_width(change):
    global pen_width
    if change == '+':
        pen_width +=1
    elif change == '-':
        if pen_width > 0:
            pen_width -=1
def modes(cc):
    global mode
    mode = cc
def clear():
    canvas.delete("all")
win = Tk()
canvas = Canvas(win,bg = 'white',width = 500, height = 500)
red = Button(win,text = "red",bg = "red",fg = "white",width = 8,command = lambda : change_color("red"))
green = Button(win,text = "green",bg = "green",fg = "white",width = 8,command = lambda : change_color("green"))
black = Button(win,text = "black",bg = "black",fg = "white",width = 8,command = lambda : change_color("black"))
blue = Button(win,text = "blue",bg = "blue",fg = "white",width = 8,command = lambda : change_color("blue"))
yellow = Button(win,text = "yellow",bg = "yellow",fg = "black",width = 8,command = lambda : change_color("yellow"))
white = Button(win,text = "white",bg = "white",fg = "black",width = 8,command =lambda : change_color("white"))
plus = Button(win,text = "+",width = 8,command = lambda :  change_width("+"))
minous = Button(win,text = "-",width = 8,command =  lambda : change_width("-"))
clear = Button(win,text = "clear",width = 8,command = clear)
canvas_color = Button(win,text = "canvas\ncolor",width = 8,bg = canvas_col,fg = "black",command = lambda : modes("canvas"))
pen_color = Button(win,text = "pen\ncolor",width = 8,bg = pen_col,fg = "white",command = lambda : modes("pen"))
fill = Button(win,text = "fill\ncolor",width = 8,bg = fill_color,fg = "black",command = lambda : modes("fill"))
circle = Button(win,text = "○",bg = "white",fg = "black",width = 8,command = lambda : modes("cir"))
rectangle = Button(win,text = "□",bg = "white",fg = "black",width = 8,command = lambda : modes("rect"))
polygon = Button(win,text = "△",bg = "white",fg = "black",width = 8,command = lambda : modes("poly"))
canvas.grid(row =0,column = 0,columnspan = 4)
white.grid(row = 2,column = 1)
black.grid(row = 1,column = 1)
blue.grid(row = 1,column = 2)
green.grid(row = 1,column = 3)
yellow.grid(row = 2,column = 3)
red.grid(row = 2,column = 2)
plus.grid(row = 1,column = 4)
minous.grid(row = 2,column = 4)
clear.grid(row = 3,column = 4)
fill.grid(row = 3,column = 0)
circle.grid(row = 3,column = 1)
rectangle.grid(row = 3,column = 2)
polygon.grid(row = 3,column = 3)
canvas_color.grid(row = 1,column = 0)
pen_color.grid(row = 2,column = 0)
win.bind("<B1-Motion>",paint)
win.bind("<Double-Button-1>",draw_shape)
win.mainloop()
