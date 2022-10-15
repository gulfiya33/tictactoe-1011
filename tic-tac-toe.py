from tkinter import *
from tkinter import messagebox
import sys


SIGN_X = 'X'
SIGN_O = 'O'

state = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

buttons = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

def victory_check():   
    if state[0][0]==state[1][1]==state[2][2] != None or state[2][0]==state[1][1]==state[0][2] != None:
        if state[1][1] == SIGN_X:
            result = messagebox.showinfo("Game Over", "!!!X WON!!!")
        else:
            result = messagebox.showinfo("Game Over", "!!!O WON!!!")
        sys.exit()    
            
    for i in range(3):
        if state[i][0]==state[i][1]==state[i][2] != None or state[0][i]==state[1][i]==state[2][i] != None:
            if state[i][i] == SIGN_X:
                result = messagebox.showinfo("Game Over", "!!!X WON!!!")
            else:
                result = messagebox.showinfo("Game Over", "!!!O WON!!!")
            sys.exit()
                     
    if noneCounter() == 0:
        result = messagebox.showinfo("Game Over", "DRAWN GAME")
        sys.exit()
             

def noneCounter():
    steps = 0
    for i in range(3):
        steps += state[i].count(None)
    return steps
    

def click(i,j):
    current_sign = SIGN_O if noneCounter() % 2 == 0 else SIGN_X
    title_sign = SIGN_O if current_sign == SIGN_X else SIGN_X    
    
    title = Label(gui, text= f'Ходит {title_sign}', font= ("Arial", 11, "bold")).grid(row= 3, column= 1)
    gui.update()

    buttons[i][j].configure(text = current_sign)
    buttons[i][j]["state"] = DISABLED
    state[i][j] = current_sign
    
    victory_check()
    

gui = Tk(className="tic-tac-toe")
gui.geometry("230x290")

for i in range(3):
    for j in range(3):                   
        buttons[i][j] = Button(height = 2, width = 4, bg = '#A18594',font = ("Arial", 20, "bold"), command = lambda x = i, y = j : click(x,y))
        buttons[i][j].grid(row = i, column = j)

title = Label(gui, text= "Start", font= ("Arial", 14, "bold")).grid(row= 3, column= 1)

gui.mainloop()
