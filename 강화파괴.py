from tkinter import *
from random import *
win  = Tk()
def Roll(pro):
    a = ['성공','실패']
    b = (choices(a, [int(pro),int(int(100)-int(pro))]))
UPG=Button(win,text = '강화' , command = lambda : Roll(90))
lbl=Label(win,text = '기본')
lbl.pack()
UPG.pack()
win.mainloop()
