import tkinter
from functools import partial
from tkinter import messagebox


class Caro(tkinter.Tk):
     # hàm khởi tạo, với tham số truyền vào là Ox, Oy (hàng x cột) nếu không truyền vào, mặc định là 10x20
    def __init__(self, Ox=10, Oy=20):
        super().__init__()
        self.title("Caro with Python Advance")  # tên của cửa sổ là Caro
        self.resizable(0, 0)  # hàm không cho phép chỉnh sửa kích thước cửa sổ
        self.Buttons = {}  # một dict dùng để lưu thông tin của các ô
        self.memory = []  # một list dùng để lưu thứ tự của các lượt đánh
        self.create_mainboard(Ox, Oy)  # gọi hàm tạo cửa sổ chính

    # hàm tạo cửa sổ chính của trò chơi, với tham số truyền vào là Ox, Oy    
    def create_mainboard(self, Ox, Oy):
        frame = tkinter.Frame(self)
        frame.pack()
        # tạo ma trận các ô có Ox dòng và Oy cột (ma trận Ox*Oy)
        for x in range(Ox):
            for y in range(Oy):
                self.Buttons[x, y] = tkinter.Button(frame, font=('arial', 15, 'bold'), height=1, width=2,
                                                    borderwidth=2, command=partial(self.handleButton, x=x, y=y), bg='light gray')
                self.Buttons[x, y].grid(row=x, column=y)
