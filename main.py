import tkinter as tk
from tkinter import *
from functools import partial
from PIL import Image, ImageTk
from P2P import Game
from AI.board_gui import BoardFrame


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def forwardP2P():
            controller.show_frame(Game)
        def forwardP2C():
            controller.show_frame(BoardFrame)

        p2pBtn = Button(self, text="PvP", font=("Arial", 15), command=forwardP2P)
        p2pBtn.place(x=320, y=115)
        p2cBtn = Button(self, text="Play With Computer", font=("Arial", 15), command=forwardP2C)
        p2cBtn.place(x=320, y=20)
    
# class SecondPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
        
#         load = Image.open("./assets/banner.png")
#         photo = ImageTk.PhotoImage(load)
#         label = tk.Label(self, image=photo)
#         label.image=photo
#         label.place(x=0,y=0)
        
        
#         Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
#         Button.place(x=650, y=450)
        
#         Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
#         Button.place(x=100, y=450)

class Gomoku(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0,minsize=500)
        window.grid_columnconfigure(0,minsize=650)

        self.frames = {}
        for F in (StartPage,Game,BoardFrame):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Gomoku Game")

app = Gomoku()
app.maxsize(680,500)
app.mainloop()