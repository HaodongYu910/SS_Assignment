import time

from PIL import Image, ImageTk, ImageSequence
import random
from Function.gl import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class snakeAndLadder_game_board(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.top1 = ttk.Toplevel(master)
        # image = Image.open('D:\Phthon_code\Assignment\map.jpg')
        bg_image = self.image_resize('/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_python_assignment/Image/bg.jpeg',
                                   700,
                                   700)
        img1 = ImageTk.PhotoImage(bg_image)
        bg_canvas = ttk.Canvas(self.top1, width=bg_image.width, height=bg_image.height, bg='white')
        bg_canvas.create_image(0, 0, image=img1, anchor="nw")
        bg_canvas.grid(row=1, column=1)

        dice_image1 = self.image_resize('/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_python_assignment/Image/1.jpeg', 100,
                                   100)
        dice_init = ImageTk.PhotoImage(dice_image1)
        self.dice_canvas1 = ttk.Canvas(self.top1, width=dice_image1.width, height=dice_image1.height, bg='white')
        self.dice_canvas1.create_image(0, 0, image=dice_init, anchor="nw")
        self.dice_canvas1.grid(row=1, column=2, pady=70, sticky=S)

        b_roll = ttk.Button(
            self.top1,
            text='Roll',
            command=self.player_move,
            width=10,
            bootstyle="success")
        b_roll.grid(row=1, column=2, pady=20, sticky=S)
        self.top1.update()
        self.top1.mainloop()

    def pick(self):
        # 开始摇骰子
        canvas_gif = ttk.Canvas(self.top1, width=200, height=250)
        canvas_gif.grid(row=1, column=2, pady=65, sticky=S)
        num = 0
        while (num < 2):
            im = Image.open(
                '/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_python_assignment/Image/Dice_GIF.gif')
            # GIF图片流的迭代器
            iter = ImageSequence.Iterator(im)
            # frame就是gif的每一帧，转换一下格式就能显示了
            for frame in iter:
                pic = ImageTk.PhotoImage(frame)
                canvas_gif.create_image((100, 150), image=pic)
                time.sleep(0.05)
                canvas_gif.update_idletasks()  # 刷新
                canvas_gif.update()
            num += 1
        canvas_gif.destroy()

    def createDice(self):
        # 造新的骰子点数图片
        dice_number = game.current_player.number
        print(dice_number)
        dice_image = self.image_resize(
            '/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_python_assignment/Image/{}.jpeg'.format(dice_number), 100,
            100)
        dice = ImageTk.PhotoImage(dice_image)
        self.dice_canvas1 = ttk.Canvas(self.top1, width=dice_image.width, height=dice_image.height, bg='white')
        self.dice_canvas1.create_image(0, 0, image=dice, anchor="nw")
        self.dice_canvas1.grid(row=1, column=2, pady=70, sticky=S)
        print("创建成功")
        # self.top1.update()


    def player_move(self):
        """
        TODO: 做三个界面！！！
        """
        print("\n")
        game.current_player.dice()
        # 投骰子画面
        self.pick()
        self.createDice()
        previous_position = game.current_player.current_position
        game.move()
        if not game.isGameEnd():
            # 小人移动界面
            previous_position = game.current_player.current_position
            game.triggerWhat()
            # 小人再次移动
            game.current_player = game.pool.__next__()
            if game.current_player.attribute == "Robot":
                self.player_move()
        else:
            # 游戏结束界面
            print("game is end")


    def image_resize(self, path, width, height):
        print(path)
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




