remains = lambda a,b:a%b
#--------------------------------------------------------------------------------------------------------------------
say = lambda name : print("Hello" + name)
#--------------------------------------------------------------------------------------------------------------------
from tkinter import *
def Click(shape):
    if shape == 'circle':
        img= PhotoImage(file  = "circle.png")
    if shape == 'triange':
        img= PhotoImage(file  = "triangle.png")
    if shape == 'star':
        img =PhotoImage(file  = "star.png")
    lbl ['image'] =img
    lbl.image = img
win = Tk()
img = PhotoImage(file = "circle.png")
lbl = Label(win,image = img)
btn1 = Button(win,text = 'circle', command = lambda:Click('circle'))
btn2 = Button(win,text = 'triangle' ,command = lambda:Click('triange'))
btn3 = Button(win,text = 'star' ,command = lambda:Click('star'))
lbl.grid(row = 0,column = 0,columnspan = 3)
btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
win.mainloop()
#--------------------------------------------------------------------------------------------------------------------
from tkinter import *
from random import *
win = Tk()
def Click(user):
    List = ['scissors.png','rock.png','paper.png']
    com = randint(0,2)
    user_img = PhotoImage(file = List[user])
    com_img = PhotoImage(file =  List[com])
    lbl_com['image'] = com_img
    lbl_com.image = com_img
    lbl_user['image'] = user_img
    lbl_user.image = user_img
    game(com,user)
def game(com,user):
    if user == 0:
        if com == 1:
            lbl_res['text'] = "computer wins!"
        elif com == 2:
            lbl_res['text'] = "user wins!"
    if user == 1:
        if com == 2:
            lbl_res['text'] = "computer wins!"
        elif com == 0:
            lbl_res['text'] = "user wins!"
    if user == 2:
        if com == 0:
            lbl_res['text'] = "computer wins!"
        elif com == 1:
            lbl_res['text'] = "user wins!"
    if user == com:
        lbl_res['text'] = "draw!"
win.title("Rock Paper Scissors Game")
basic_img =PhotoImage(file = "Ready.png")
lbl_com=Label(win,image = basic_img,relief= 'solid')
lbl_user = Label(win,image=basic_img,relief= 'solid')
lbl_res = Label(win,text=' ' ,width = 15,bg = "lightyellow",fg = "brown")
lbl_name1 = Label(win,text='computer',font = 20)
lbl_name2 = Label(win,text='user',font = 20)
btn_scissor = Button(win,text = "scissors" ,width =15 ,fg = "black", bg = 'skyblue',command  = lambda : Click(0))
btn_rock = Button(win,text = "rock" ,width =15 ,fg = "black", bg = 'pink',command  = lambda : Click(1))
btn_paper = Button(win,text = "paper",width =15 , fg = "black" ,bg = 'lightgreen',command  = lambda : Click(2))
lbl_com.grid(row = 0 ,column = 0)
lbl_user.grid(row=0,column=2)
lbl_res.grid(row = 0,column=1)
lbl_name1.grid(row =  1,column=0)
lbl_name2.grid(row =  1,column=2)
btn_scissor.grid(row =  2,column=0)
btn_rock.grid(row =  2,column=1)
btn_paper.grid(row =  2,column=2)
win.mainloop()
