import tkinter
from functools import partial
from tkinter import messagebox


class Caro(tkinter.Tk):
    # hàm khởi tạo, với tham số truyền vào là Ox, Oy (hàng x cột) nếu không truyền vào, mặc định là 10x20
    def __init__(self, Ox=10, Oy=20):
        super().__init__()
        self.title("Caro with Python Advance")  # tên của cửa sổ là Caro
        self.geometry("685x500+700+300")
        self.resizable(0, 0)  # hàm không cho phép chỉnh sửa kích thước cửa sổ
        self.Buttons = {}  # một dict dùng để lưu thông tin của các ô
        self.memory = []  # một list dùng để lưu thứ tự của các lượt đánh
        # self.create_player()
        self.create_mainboard(Ox, Oy)  # gọi hàm tạo cửa sổ chính

    # hàm tạo player
    def create_player(self):
        player = tkinter.Frame(self)
        player.pack(side='top')
        label = tkinter.Label(player,text="Player 1",font=('arial', 15, 'bold'))
        label.grid(row=0,column=1,sticky="W")
        label2 = tkinter.Label(player,text="Player 2",font=('arial', 15, 'bold'))
        label2.grid(row=0,column=2,padx = 10, pady = 10,columnspan = 50, rowspan = 50)

    # hàm tạo cửa sổ chính của trò chơi, với tham số truyền vào là Ox, Oy
    def create_mainboard(self, Ox, Oy):
        frame = tkinter.Frame(self)
        frame.pack(side='bottom')
        # tạo ma trận các ô có Ox dòng và Oy cột (ma trận Ox*Oy)
        for x in range(Ox):
            for y in range(Oy):
                self.Buttons[x, y] = tkinter.Button(frame, font=('arial', 15, 'bold'), height=1, width=2,
                                                    borderwidth=2, command=partial(self.handleButton, x=x, y=y), bg='light gray')
                self.Buttons[x, y].grid(row=x, column=y)
        # Back = tkinter.Button(frame,text="Back",font=('arial', 15, 'bold'),bg='light gray')
        # Back.grid(row=0, column=1)

    # hàm xử lý việc đánh cờ
    # đánh O trước, X sau

    def handleButton(self, x, y):
        if self.Buttons[x, y]['text'] == "":  # kiểm tra ô có ký tự rỗng hay không
            if self.memory.count([x, y]) == 0:
                self.memory.append([x, y])
            if len(self.memory) % 2 == 1:
                self.Buttons[x, y]['text'] = 'O'
                self.Buttons[x, y].configure(bg='red')
                if(self.checkWin(x, y, "O")):
                    self.notification("Winner", "O is winner!")
                    self.newGame()
            else:
                self.Buttons[x, y]['text'] = 'X'
                self.Buttons[x, y].configure(bg='blue')
                if(self.checkWin(x, y, "X")):
                    self.notification("Winner", "X is winner")
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

    # Hàm để tạo lại trò chơi mới khi đã có người chiến thắng
    def newGame(self):
        self.memory.clear()
        for x in range(Ox):
            for y in range(Oy):
                self.Buttons[x, y]["text"] = ""
                self.Buttons[x, y].configure(bg='light gray')


if __name__ == "__main__":
    Ox = 10  # số ô theo chiều ngang
    Oy = 20  # số ô theo chiều dọc
    root = Caro(Ox, Oy)  # khởi tạo trò chơi
    root.mainloop()