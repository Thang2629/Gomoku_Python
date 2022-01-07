from os import popen
import tkinter as tk
from functools import partial
from tkinter import StringVar, Toplevel, messagebox
from PIL import Image, ImageTk

class Player(tk.Frame):
    def __init__(self):
        super().__init__()
        player1 = tk.StringVar(self,"Player 1")
        player2 = tk.StringVar(self,"Player 2")
        loadO = Image.open("./assets/O.PNG")
        loadX = Image.open("./assets/X.PNG")
        renderO = ImageTk.PhotoImage(loadO)
        renderX = ImageTk.PhotoImage(loadX)
        imgO = tk.Label(self, image=renderO,height=15,width=19)
        imgX = tk.Label(self, image=renderX,height=15,width=19)
        imgO.image = renderO
        imgX.image = renderX
        label = tk.Label(self,textvariable=player1,font=('arial', 15, 'bold'))
        label.grid(row=0,column=1,padx=10)
        imgX.grid(row=0,column=2, padx=7)
        label2 = tk.Label(self,textvariable=player2,font=('arial', 15, 'bold'))
        label2.grid(row=0,column=3,padx=10)
        imgO.grid(row=0,column=4,padx=7)
        # Banner
        # loadBanner = Image.open("./assets/banner.png")
        # renderBanner = ImageTk.PhotoImage(loadBanner)
        # imgBanner = tk.Label(self, image=renderBanner,height=150,width=550)
        # imgBanner.image = renderBanner
        # imgBanner.grid(row=0,column=3,sticky="nsew")

        

class Game(tk.Frame):
    def __init__(self):
        super().__init__()
        self.Buttons = {}
        self.memory = []
        for x in range(Ox):
            for y in range(Oy):
                self.Buttons[x, y] = tk.Button(self, font=('arial', 15, 'bold'), height=1, width=2,borderwidth=2, command=partial(self.handleButton, x=x, y=y), bg='light gray')
                self.Buttons[x, y].grid(row=x, column=y)
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




class TestMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.game = Game()
        self.player.grid(row=0,column=0,sticky='nsew')
        self.game.grid(row=1,column=0,sticky='nsew')
    

if __name__ == "__main__":
    Ox = 10  # số ô theo chiều ngang
    Oy = 20  # số ô theo chiều dọc
    TestMain().mainloop()
