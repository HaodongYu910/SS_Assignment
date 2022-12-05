import time

from PIL import Image, ImageTk, ImageSequence
from Function.gl import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class snakeAndLadder_game_board_new(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.bg_canvas = ttk.Canvas(self, width=700, height=700, bg='white')
        self.bg_canvas.pack(side=LEFT)
        self.dice_canvas1 = ttk.Canvas(self, width=250, height=250, bg='white')
        self.dice_canvas1.pack(side=TOP)
        self.start_area_canvas = ttk.Canvas(self, width=250, height=250, bg='white')
        self.start_area_canvas.pack(side=BOTTOM)
        self.text_set = ttk.Label(self, text="Departure area", bootstyle="dark")
        self.text_set.pack(side=BOTTOM)

        self.create_board()

        ## player settings
        self.p1_set = None
        self.p2_set = None
        self.p3_set = None
        self.p4_set = None
        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.p1_I = None
        self.p2_I = None
        self.p3_I = None
        self.p4_I = None

    def pick(self):
        # 开始摇骰子
        # canvas_gif = ttk.Canvas(self, width=200, height=250)
        # canvas_gif.pack(side=BOTTOM)
        num = 0
        while num < 2:
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
            '../Image/{}.jpeg'.format(dice_number), 200, 200)
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
            self.imag_movement(game.current_player.No, game.current_player.current_position)
            previous_position = game.current_player.current_position
            game.triggerWhat()
            # 小人再次移动
            self.imag_movement(game.current_player.No, game.current_player.current_position)
            game.current_player = game.pool.__next__()
            if game.current_player.attribute == "Robot":
                self.player_move()
        else:
            self.imag_movement(game.current_player.No, game.current_player.current_position)
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
        bg_image = self.image_resize(
            '../Image/bg.jpeg',
            700,
            700)
        img1 = ImageTk.PhotoImage(bg_image)

        self.bg_canvas.create_image(0, 0, image=img1, anchor="nw")


        dice_image1 = self.image_resize(
            '../Image/0.jpeg', 200,
            200)
        dice_init = ImageTk.PhotoImage(dice_image1)
        dice_ini=self.dice_canvas1.create_image(0, 0, image=dice_init, anchor="nw")
        self.dice_canvas1.delete(dice_ini)
        roll_dice = ttk.Button(
            master=self,
            text="Play",
            command=self.player_move,
            bootstyle=SUCCESS,
            width=6,
        )
        roll_dice.pack(side=RIGHT, padx=5)

        # 图片插入
        player1_image = self.image_resize('../Image/player/{}.jpg'.format(game.players[0].colour), 700 * 0.025,
                                          700 * 0.025)
        self.p1_I = ImageTk.PhotoImage(player1_image)

        player2_image = self.image_resize('../Image/player/{}.jpg'.format(game.players[1].colour), 700 * 0.025,
                                          700 * 0.025)
        self.p2_I = ImageTk.PhotoImage(player2_image)

        player3_image = self.image_resize('../Image/player/{}.jpg'.format(game.players[2].colour), 700 * 0.025,
                                          700 * 0.025)
        self.p3_I = ImageTk.PhotoImage(player3_image)

        player4_image = self.image_resize('../Image/player/{}.jpg'.format(game.players[3].colour), 700 * 0.025,
                                          700 * 0.025)
        self.p4_I = ImageTk.PhotoImage(player4_image)

        # 出发区域画布
        self.start_area_canvas.create_window(50, 40, window=self.text_set)
        self.p1_set = self.start_area_canvas.create_image(15, 15, image=self.p1_I)
        self.p2_set = self.start_area_canvas.create_image(45, 15, image=self.p2_I)
        self.p3_set = self.start_area_canvas.create_image(75, 15, image=self.p3_I)
        self.p4_set = self.start_area_canvas.create_image(105, 15, image=self.p4_I)

        # 创建初始模块
        self.p1 = self.bg_canvas.create_image(-60, -60, image=self.p1_I)
        self.p2 = self.bg_canvas.create_image(-60, -60, image=self.p2_I)
        self.p3 = self.bg_canvas.create_image(-60, -60, image=self.p3_I)
        self.p4 = self.bg_canvas.create_image(-60, -60, image=self.p4_I)

        self.mainloop()

    def imag_movement(self, player_no, step):

        imag_size = 700

        initial_x1 = imag_size * 0.025
        initial_x2 = imag_size * 0.055

        initial_y1 = imag_size * 0.918
        initial_y2 = imag_size * 0.946
        initial_y3 = imag_size * 0.976

        step_size = imag_size * 0.1

        if player_no == 1:
            self.start_area_canvas.delete(self.p1_set)
            y_r = initial_y1 - step_size * (step // 10)
            x_r = initial_x1 + step_size * (step % 10 - 1)
            if step % 10 == 0:
                y_r = initial_y1 - step_size * (step // 10 - 1)
                x_r = initial_x1 + step_size * 9
            self.bg_canvas.delete(self.p1)
            self.p1 = self.bg_canvas.create_image(x_r, y_r, image=self.p1_I)
            print(player_no, step, x_r, y_r)

        if player_no == 2:
            self.start_area_canvas.delete(self.p2_set)
            y_g = initial_y2 - step_size * (step // 10)
            x_g = initial_x1 + step_size * (step % 10 - 1)
            if step % 10 == 0:
                y_g = initial_y2 - step_size * (step // 10 - 1)
                x_g = initial_x1 + step_size * 9
            self.bg_canvas.delete(self.p2)
            self.p2 = self.bg_canvas.create_image(x_g, y_g, image=self.p2_I)
            print(player_no, step, x_g, y_g)

        if player_no == 3:
            self.start_area_canvas.delete(self.p3_set)
            y_b = initial_y3 - step_size * (step // 10)
            x_b = initial_x1 + step_size * (step % 10 - 1)
            if step % 10 == 0:
                y_b = initial_y3 - step_size * (step // 10 - 1)
                x_b = initial_x1 + step_size * 9
            self.bg_canvas.delete(self.p3)
            self.p3 = self.bg_canvas.create_image(x_b, y_b, image=self.p3_I)
            print(player_no, step, x_b, y_b)

        if player_no == 4:
            self.start_area_canvas.delete(self.p4_set)
            y_y = initial_y1 - step_size * (step // 10)
            x_y = initial_x2 + step_size * (step % 10 - 1)
            if (step % 10 == 0):
                y_y = initial_y1 - step_size * (step // 10 - 1)
                x_y = initial_x2 + step_size * 9
            self.bg_canvas.delete(self.p4)
            self.p4 = self.bg_canvas.create_image(x_y, y_y, image=self.p4_I)
            print(player_no, step, x_y, y_y)
