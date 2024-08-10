from tkinter import *
from random import *
win  = Tk()
g = 0
L= ['평범한 검','덜 평범한 검','약한 검','조금 강한 검','강한 검','매우 강한 검']
def Roll(pro):
    a = ['성공','실패']
    b = (choices(a, [int(pro),int(100)-int(pro)]))
    if b == '성공':
        if g < 5:
            g+=1
            lbl['text'] = L[int(g)]
UPG=Button(win,text = '강화' , command = lambda : Roll(int(90)-int(g)*5))
lbl=Label(win,text = L[int(g)])
lbl.pack()
UPG.pack()
win.mainloop()
