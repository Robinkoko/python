def average(n,tot):
    avg=tot/n
    return avg
def total():
    tot=0
    score=input("score :").split()
    for i in score:
        tot +=int(i)
    avg = average(len(score),tot)
    print(f"total score : {tot}")
    print("average score : %.2f" % avg)
total()

def even(n):
    if n == 0:
        return n
    if n%2==0:
        print(n)
        even(n-1)
even(10)

from tkinter import*
win = Tk()
lbl1= Label(win,text ='orange',width = 20, height = 3,relief = 'solid')
lbl2= Label(win,text ='banana',font = ("Elephant",20),bg ="yellow")
lbl3=Label(win,text = "apple", fg="red")
lbl1.pack()
lbl2.pack()
lbl3.pack()
win.mainloop()

from tkinter import*
win = Tk()
img = PhotoImage(file ='pizza.png')
lbl = Label(win,image = img)
lbl2 = Label(win,text = "pizza",fg = 'red',bg='yellow')
lbl.pack()
lbl2.pack()
win.mainloop()

from tkinter import*
win = Tk()
def click():
    if lbl['text']=="hello" :
        lbl['text'] = "python"
        lbl['bg']="green"
    else:
        lbl['text'] = "hello"
        lbl['bg']="orange"
btn = Button(win,text = "Button",command = click)
lbl = Label(win,text = "hello" ,fg = 'white', bg = 'orange')
lbl.pack()
btn.pack()

from tkinter import *
win =Tk()
def message(event):
    lbl['text']=entry.get()
entry = Entry(win)
entry.bind("<Return>",message)
entry.pack()
lbl = Label(win,text= '')
lbl.pack()
win.mainloop()

