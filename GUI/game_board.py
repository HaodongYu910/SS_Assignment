from PIL import Image, ImageTk
import random
from tkinter.ttk import Frame
from Function.gl import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class snakeAndLadder_game_board(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        top1 = ttk.Toplevel(master)
        # image = Image.open('D:\Phthon_code\Assignment\map.jpg')
        bg_image = self.image_resize('/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_python_assignment/Image/bg.jpeg',
                                   700,
                                   700)
        img1 = ImageTk.PhotoImage(bg_image)
        bg_canvas = ttk.Canvas(top1, width=bg_image.width, height=bg_image.height, bg='white')
        bg_canvas.create_image(0, 0, image=img1, anchor="nw")
        bg_canvas.grid(row=1, column=1)

        dice_image1 = self.image_resize('/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_python_assignment/Image/1.jpeg', 100,
                                   100)
        img2 = ImageTk.PhotoImage(dice_image1)
        dice_canvas1 = ttk.Canvas(top1, width=dice_image1.width, height=dice_image1.height, bg='white')
        dice_canvas1.create_image(0, 0, image=img2, anchor="nw")
        dice_canvas1.grid(row=1, column=2, pady=70, sticky=S)

        b_roll = ttk.Button(
            top1,
            text='Roll',
            command=game.move,
            width=10,
            bootstyle="success")
        b_roll.grid(row=1, column=2, pady=20, sticky=S)

        top1.mainloop()

    def image_resize(self, path, width, height):
        screen_width = 0
        screen_height = 0
        I_WIDTH = int(width)
        I_HEIGHT = int(height)
        image = Image.open(path)
        if screen_width <= 0:
            screen_width = I_WIDTH
        if screen_height <= 0:
            screen_height = I_HEIGHT
        raw_width, raw_height = image.size[0], image.size[1]
        max_width, max_height = raw_width, screen_height
        min_width = max(raw_width, max_width)
        # 按照比例缩放
        min_height = int(raw_height * min_width / raw_width)
        # 第1次快速调整
        while min_height > screen_height:
            min_height = int(min_height * .9533)
        # 第2次精确微调
        while min_height < screen_height:
            min_height += 1
        # 按照比例缩放
        min_width = int(raw_width * min_height / raw_height)
        # 适应性调整
        while min_width > screen_width:
            min_width -= 1
        # 按照比例缩放
        min_height = int(raw_height * min_width / raw_width)
        return image.resize((min_width, min_height))

    def sup_window2(self):
        top1 = ttk.Toplevel()
        # image = Image.open('D:\Phthon_code\Assignment\map.jpg')
        image1 = self.image_resize('/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_assignment/Image', 1200,
                              1200)
        img1 = ImageTk.PhotoImage(image1)
        canvas1 = ttk.Canvas(top1, width=image1.width, height=image1.height, bg='white')
        canvas1.create_image(0, 0, image=img1, anchor="nw")
        canvas1.grid(row=1, column=1)

        image2 = self.image_resize('/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_assignment/Image', 200, 200)
        img2 = ImageTk.PhotoImage(image2)
        canvas2 = ttk.Canvas(top1, width=image2.width, height=image2.height, bg='white')
        canvas2.create_image(0, 0, image=img2, anchor="nw")
        canvas2.grid(row=1, column=2, pady=70, sticky=S)

        b_roll = ttk.Button(
            top1,
            text='Roll',
            # command=
            width=10,
            bootstyle="success")
        b_roll.grid(row=1, column=2, pady=20, sticky=S)

        top1.mainloop()
