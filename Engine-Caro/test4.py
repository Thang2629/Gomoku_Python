import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
from functools import partial
from test3 import Game

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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
        # load = Image.open("./assets/banner.png")
        # photo = ImageTk.PhotoImage(load)
        # label = tk.Label(self, image=photo)
        # label.image=photo
        # label.place(x=0,y=0)
        
        # border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        # border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        # L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        # L1.place(x=50, y=20)
        # T1 = tk.Entry(border, width = 30, bd = 5)
        # T1.place(x=180, y=20)
        
        # L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        # L2.place(x=50, y=80)
        # T2 = tk.Entry(border, width = 30, show='*', bd = 5)
        # T2.place(x=180, y=80)
        
        def verify():
           controller.show_frame(Game)

         
        B1 = tk.Button(self, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)
        
        def register():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg="deep sky blue")
            window.title("Register")
            l1 = tk.Label(window, text="Username:", font=("Arial",15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x = 200, y=10)
            
            l2 = tk.Label(window, text="Password:", font=("Arial",15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x = 200, y=60)
            
            l3 = tk.Label(window, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x = 200, y=110)
            
            def check():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                        with open("credential.txt", "a") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error","Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")
                    
            b1 = tk.Button(window, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)
            
            window.geometry("470x220")
            window.mainloop()
            
        B2 = tk.Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)
        B2.place(x=650, y=20)
        
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load = Image.open("./assets/banner.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
        
        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=650, y=450)
        
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=100, y=450)
        
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='Tomato')
        
        Label = tk.Label(self, text="Store some content related to your \n project or what your application made for. \n All the best!!", bg = "orange", font=("Arial Bold", 25))
        Label.place(x=40, y=150)
        
        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=450)
        
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=100, y=450)
# Ox = 10  # số ô theo chiều ngang
# Oy = 20  # số ô theo chiều dọc       
# class Game(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.Buttons = {}
#         self.memory = []
#         for x in range(Ox):
#             for y in range(Oy):
#                 self.Buttons[x, y] = tk.Button(self, font=('arial', 15, 'bold'), height=1, width=2,borderwidth=2, command=partial(self.handleButton, x=x, y=y), bg='light gray')
#                 self.Buttons[x, y].grid(row=x, column=y)
#         Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
#         Button.place(x=100, y=450)
#     def handleButton(self, x, y):
#         if self.Buttons[x, y]['text'] == "":  # kiểm tra ô có ký tự rỗng hay không
#             if self.memory.count([x, y]) == 0:
#                 self.memory.append([x, y])
#             if len(self.memory) % 2 == 1:
#                 self.Buttons[x, y]['text'] = 'O'
#                 self.Buttons[x, y].configure(bg='red')
#                 if(self.checkWin(x, y, "O")):
#                     self.notification("Winner", "Player 2 is winner!")
#                     self.newGame()
#             else:
#                 self.Buttons[x, y]['text'] = 'X'
#                 self.Buttons[x, y].configure(bg='blue')
#                 if(self.checkWin(x, y, "X")):
#                     self.notification("Winner", "Player 1 is winner")
#                     self.newGame()
#     def notification(self, title, msg):
#         messagebox.showinfo(str(title), str(msg))

#     def checkWin(self, x, y, XO):
#         # check theo dòng
#         count = 0
#         i, j = x, y
#         while(j < Ox and self.Buttons[i, j]["text"] == XO):
#             count += 1
#             j += 1
#         j = y
#         while(j >= 0 and self.Buttons[i, j]["text"] == XO):
#             count += 1
#             j -= 1
#         if count >= 6:
#             return True

#         # check theo cột
#         count = 0
#         i, j = x, y
#         while(i < Oy and self.Buttons[i, j]["text"] == XO):
#             count += 1
#             i += 1
#         i = x
#         while(i >= 0 and self.Buttons[i, j]["text"] == XO):
#             count += 1
#             i -= 1
#         if count >= 6:
#             return True

#         # check chéo phải
#         count = 0
#         i, j = x, y
#         while(i >= 0 and j < Ox and self.Buttons[i, j]["text"] == XO):
#             count += 1
#             i -= 1
#             j += 1
#         i, j = x, y
#         while(i <= Oy and j >= 0 and self.Buttons[i, j]["text"] == XO):
#             count += 1
#             i += 1
#             j -= 1
#         if count >= 6:
#             return True

#         # check chéo trái
#         count = 0
#         i, j = x, y
#         while(i < Ox and j < Oy and self.Buttons[i, j]["text"] == XO):
#             count += 1
#             i += 1
#             j += 1
#         i, j = x, y
#         while(i >= 0 and j >= 0 and self.Buttons[i, j]["text"] == XO):
#             count += 1
#             i -= 1
#             j -= 1
#         if count >= 6:
#             return True
#         return False
#     def newGame(self):
#         self.memory.clear()
#         for x in range(Ox):
#             for y in range(Oy):
#                 self.Buttons[x, y]["text"] = ""
#                 self.Buttons[x, y].configure(bg='light gray')

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage, Game):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")
            
app = Application()
app.maxsize(800,500)
app.mainloop()