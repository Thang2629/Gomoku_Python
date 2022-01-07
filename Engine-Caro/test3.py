from os import popen
import tkinter as tk
from functools import partial
from tkinter import StringVar, Toplevel, messagebox
from PIL import Image, ImageTk


Ox = 10  # số ô theo chiều ngang
Oy = 20  # số ô theo chiều dọc

class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.Buttons = {}
        self.memory = []
        for x in range(Ox):
            for y in range(Oy):
                self.Buttons[x, y] = tk.Button(self, font=('arial', 15, 'bold'), height=1, width=2,borderwidth=2, command=partial(self.handleButton, x=x, y=y), bg='light gray')
                self.Buttons[x, y].grid(row=x, column=y)
        return
    def handleButton(self, x, y):
        if self.Buttons[x, y]['text'] == "":  # kiểm tra ô có ký tự rỗng hay không
            if self.memory.count([x, y]) == 0:
                self.memory.append([x, y])
            if len(self.memory) % 2 == 1:
                self.Buttons[x, y]['text'] = 'O'
                self.Buttons[x, y].configure(bg='red')
                if(self.checkWin(x, y, "O")):
                    self.notification("Winner", "Player 2 is winner!")
                    self.newGame()
            else:
                self.Buttons[x, y]['text'] = 'X'
                self.Buttons[x, y].configure(bg='blue')
                if(self.checkWin(x, y, "X")):
                    self.notification("Winner", "Player 1 is winner")
                    self.newGame()
    def notification(self, title, msg):
        messagebox.showinfo(str(title), str(msg))

    def checkWin(self, x, y, XO):
        # check theo dòng
        count = 0
        i, j = x, y
        while(j < Ox and self.Buttons[i, j]["text"] == XO):
            count += 1
            j += 1
        j = y
        while(j >= 0 and self.Buttons[i, j]["text"] == XO):
            count += 1
            j -= 1
        if count >= 6:
            return True

        # check theo cột
        count = 0
        i, j = x, y
        while(i < Oy and self.Buttons[i, j]["text"] == XO):
            count += 1
            i += 1
        i = x
        while(i >= 0 and self.Buttons[i, j]["text"] == XO):
            count += 1
            i -= 1
        if count >= 6:
            return True

        # check chéo phải
        count = 0
        i, j = x, y
        while(i >= 0 and j < Ox and self.Buttons[i, j]["text"] == XO):
            count += 1
            i -= 1
            j += 1
        i, j = x, y
        while(i <= Oy and j >= 0 and self.Buttons[i, j]["text"] == XO):
            count += 1
            i += 1
            j -= 1
        if count >= 6:
            return True

        # check chéo trái
        count = 0
        i, j = x, y
        while(i < Ox and j < Oy and self.Buttons[i, j]["text"] == XO):
            count += 1
            i += 1
            j += 1
        i, j = x, y
        while(i >= 0 and j >= 0 and self.Buttons[i, j]["text"] == XO):
            count += 1
            i -= 1
            j -= 1
        if count >= 6:
            return True
        return False
    def newGame(self):
        self.memory.clear()
        for x in range(Ox):
            for y in range(Oy):
                self.Buttons[x, y]["text"] = ""
                self.Buttons[x, y].configure(bg='light gray')





    

