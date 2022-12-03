import time

from PIL import Image, ImageTk, ImageSequence
import random
from Function.gl import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class snakeAndLadder_game_board_new(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.bg_canvas = ttk.Canvas(self, width=700, height=700,bg='white')
        self.bg_canvas.pack(side=LEFT)
        self.dice_canvas1 = ttk.Canvas(self, width=250, height=250, bg='white')
        self.dice_canvas1.pack(side=LEFT)

        self.create_board()
        # self.createDice()
        self.create_rolling_button()


    def pick(self):
        # 开始摇骰子
        # canvas_gif = ttk.Canvas(self, width=200, height=250)
        # canvas_gif.pack(side=BOTTOM)
        num = 0
        while (num < 2):
            im = Image.open(
                '../Image/Dice_GIF.gif')
            # GIF图片流的迭代器
            iter = ImageSequence.Iterator(im)
            # frame就是gif的每一帧，转换一下格式就能显示了
            for frame in iter:
                pic = ImageTk.PhotoImage(frame)
                self.dice_canvas1.create_image((100, 100), image=pic)
                time.sleep(0.05)
                self.dice_canvas1.update_idletasks()  # 刷新
                self.dice_canvas1.update()
            num += 1
        # canvas_gif.destroy()



    def createDice(self):
        # 造新的骰子点数图片
        dice_number = game.current_player.number
        print(dice_number)
        dice_image = self.image_resize(
            '../Image/{}.jpeg'.format(dice_number),200,200)
        dice = ImageTk.PhotoImage(dice_image)

        self.dice_canvas1.create_image(0, 0, image=dice, anchor="nw")

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
            if game.current_player.name.split("-")[0] == "robot":
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

    def create_board(self):
        # 创建游戏界面，骰子初始图标
        # container = ttk.Frame(self)
        # container.pack(fill=X, expand=YES, pady=(15, 10))

        # image = Image.open('D:\Phthon_code\Assignment\map.jpg')

        bg_image = self.image_resize(
            '../Image/bg.jpeg',
            700,
            700)
        img1 = ImageTk.PhotoImage(bg_image)

        # bg_canvas.create_image(0, 0, image=img1, anchor="nw")
        self.bg_canvas.create_image(0, 0, image=img1,anchor="nw")
        self.bg_canvas.pack(side=LEFT)

        dice_image1 = self.image_resize(
            '../Image/0.jpeg', 200,
            200)
        dice_init = ImageTk.PhotoImage(dice_image1)
        self.dice_canvas1.create_image(0, 0, image=dice_init, anchor="nw")
        self.dice_canvas1.pack(side=TOP)

        # image1 = self.image_resize('../Image/bg.jpeg', 700, 700)
        # photo = ImageTk.PhotoImage(image1)
        # # 创建背景画布
        # canvas = ttk.Canvas(self, width=image1.width, height=image1.height, bg='white')
        # canvas.create_image(0, 0, image=photo, anchor="nw")
        # canvas.pack()


        roll_dice = ttk.Button(
            master=self,
            text="Play",
            command=self.player_move,
            bootstyle=SUCCESS,
            width=6,
        )
        roll_dice.pack(side=RIGHT, padx=5)
        self.mainloop()


        # canvas = ttk.Canvas(self,width=500,height=500)
        # entry_step = ttk.Entry(self)
        # entry_step.pack(side=BOTTOM)
        # canvas.create_image(0,0,image=image1)





    def create_rolling_button(self):
        """Create the dice rolling buttonbox"""
        # 创建投骰子的按钮，这个OK
        # container = ttk.Frame(self)
        # container.pack(fill=X, expand=YES, pady=(15, 10))



        # submit_player_name = ttk.Button(
        #     master=container,
        #     text="Submit",
        #     command=self.onSubmit,
        #     bootstyle=SUCCESS,
        #     width=6,
        # )
        # submit_player_name.pack(side=RIGHT, padx=5)
        # roll_dice.focus_set()
        # self.mainloop()