import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from PIL import Image, ImageTk

from GUI.input_name import *


# def snakeAndLadder_bg():
#     mytoplevel = ttk.Toplevel(root)
#     image = Image.open('/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_assignment/Image/bg.jpeg')
#     img = ImageTk.PhotoImage(image)
#     canvas1 = ttk.Canvas(mytoplevel, width=image.width / 2, height=image.height / 2, bg='white')
#     canvas1.create_image(0, 0, image=img, anchor="nw")
#     canvas1.create_image(image.width, 0, image=img, anchor="nw")
#     canvas1.pack()
#     mytoplevel.mainloop()


# def sup_window2():
#     top1 = ttk.Toplevel()
#     image = Image.open('/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_assignment/Image/bg.jpeg')
#     img = ImageTk.PhotoImage(image)
#     canvas = ttk.Canvas(top1, width=image.width, height=image.height, bg='white')
#     canvas.create_image(0, 0, image=img, anchor="nw")
#     canvas.pack()
#     top1.mainloop()


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title("my window")
        self.root.geometry("600x300+0+0")  # 400wight, 200height
        self.root.resizable(False, False)  # 不可拖动窗口改变大小
        # root.wm_attributes('-topmost', 1) #让主窗口置顶
        initface(self.root)


class initface():
    def __init__(self, master):
        self.master = master
        self.master.config(bg='white')
        # 基准界面initface
        self.initface = ttk.Frame(self.master, )
        self.initface.pack()

        btn = ttk.Button(
            self.initface, text='Go',
            command=self.change,
            width=10,
            bootstyle="success")
        btn.grid(pady=60)

    def change(self, ):
        self.initface.destroy()
        # face1(self.master)
        NameEntryForm(self.master)


# class face1():
#     def __init__(self, master):
#         self.master = master
#         self.master.config(bg='white')
#         self.face1 = ttk.Frame(self.master)
#         self.face1.pack()
#         btn_back = ttk.Button(
#             self.face1, text='back',
#             # command=self.back,
#             width=10,
#             bootstyle="success")
#         btn_back.pack()
#         bt_back1 = ttk.Button(
#             self.face1,
#             text="Test1",
#             command=snakeAndLadder_bg,
#             width=10,
#             bootstyle="success-outline")
#         bt_back1.pack()
#         # bt_back2 = ttk.Button(
#         #     self.face1,
#         #     text="Test2",
#         #     command=sup_window2,
#         #     width=10,
#         #     bootstyle="success-outline")
#         # bt_back2.pack()
#

if __name__ == '__main__':
    root = ttk.Window()
    basedesk(root)
    root.mainloop()
