from tkinter import *
from court import *
from ball import *
win = Tk()
width, height = 745, 374
win.title("tennis game")
win.geometry("745x374+150+150")
win.resizable(False,False)
court = Court(win,745,374,"court.png")
x1,y1 = width/2,height/2
x2,y2 = x1+30,y1+30
ball = Ball(court,x1,y1,x2,y2)
def play_game() :
    ball.move_ball()
    win.after(50, play_game)
play_game()
win.mainloop()
