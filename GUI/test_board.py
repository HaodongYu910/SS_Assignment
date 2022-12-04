import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence
import time

imag_size = 800

player_size = imag_size * 0.025

initial_x1 = imag_size * 0.025
initial_x2 = imag_size * 0.055

initial_y1 = imag_size * 0.918
initial_y2 = imag_size * 0.946
initial_y3 = imag_size * 0.976

step_size = imag_size * 0.1

x_r = initial_x1
y_r = initial_y1

x_g = initial_x1
y_g = initial_y2

x_b = initial_x1
y_b = initial_y3

x_y = initial_x2
y_y = initial_y3


def imag_movement():
    global x_r, y_r, x_g, y_g, x_b, y_b, x_y, y_y
    global step_size
    global red, green, blue, yellow
    player = entry_image.get()
    step = int(entry_step.get())

    if player == 'red':
        canvas_set.delete(red_set)
        y_r = initial_y1 - step_size * (step // 10)
        x_r = initial_x1 + step_size * (step % 10 - 1)
        if (step % 10 == 0):
            y_r = initial_y1 - step_size * (step // 10 - 1)
            x_r = initial_x1 + step_size * 9
        canvas.delete(red)
        red = canvas.create_image(x_r, y_r, image=img_red)
        print(player, step, x_r, y_r)

    if player == 'green':
        canvas_set.delete(green_set)
        y_g = initial_y2 - step_size * (step // 10)
        x_g = initial_x1 + step_size * (step % 10 - 1)
        if (step % 10 == 0):
            y_g = initial_y2 - step_size * (step // 10 - 1)
            x_g = initial_x1 + step_size * 9
        canvas.delete(green)
        green = canvas.create_image(x_g, y_g, image=img_green)
        print(player, step, x_g, y_g)

    if player == 'blue':
        canvas_set.delete(blue_set)
        y_b = initial_y3 - step_size * (step // 10)
        x_b = initial_x1 + step_size * (step % 10 - 1)
        if (step % 10 == 0):
            y_b = initial_y3 - step_size * (step // 10 - 1)
            x_b = initial_x1 + step_size * 9
        canvas.delete(blue)
        blue = canvas.create_image(x_b, y_b, image=img_blue)
        print(player, step, x_b, y_b)

    if player == 'yellow':
        canvas_set.delete(yellow_set)
        y_y = initial_y1 - step_size * (step // 10)
        x_y = initial_x2 + step_size * (step % 10 - 1)
        if (step % 10 == 0):
            y_y = initial_y1 - step_size * (step // 10 - 1)
            x_y = initial_x2 + step_size * 9
        canvas.delete(yellow)
        yellow = canvas.create_image(x_y, y_y, image=img_yellow)
        print(player, step, x_y, y_y)


def image_resize(path, width, height):
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


top1 = ttk.Toplevel()

image1 = image_resize('../Image/bg.jpeg', imag_size, imag_size)
photo = ImageTk.PhotoImage(image1)
# 创建背景画布
canvas = ttk.Canvas(top1, width=image1.width, height=image1.height, bg='white')
canvas.create_image(0, 0, image=photo, anchor="nw")
canvas.pack()

# 窗口插入
entry_image = ttk.Entry(top1)
entry_image.pack()
canvas.create_window(100, 50, width=100, height=30, window=entry_image)

entry_step = ttk.Entry(top1)
entry_step.pack()
canvas.create_window(100, 100, width=100, height=30, window=entry_step)

# 按钮插入
btn = ttk.Button(
    top1, text='Go',
    command=imag_movement,
    width=10,
    bootstyle="success")
btn.pack()
canvas.create_window(100, 150, window=btn)

# 图片插入
image_red = image_resize('../Image/player/Red.jpg', player_size, player_size)
img_red = ImageTk.PhotoImage(image_red)

image_green = image_resize('../Image/player/Green.jpg', player_size, player_size)
img_green = ImageTk.PhotoImage(image_green)

image_blue = image_resize('../Image/player/Blue.jpg', player_size, player_size)
img_blue = ImageTk.PhotoImage(image_blue)

image_yellow = image_resize('../Image/player/Yellow.jpg', player_size, player_size)
img_yellow = ImageTk.PhotoImage(image_yellow)

# 创建出发区画布
canvas_set = ttk.Canvas(top1, width=200, height=80)
canvas_set.pack(side=LEFT)
text_set = ttk.Label(top1, text="Departure area", bootstyle="dark")
text_set.pack()
canvas_set.create_window(50, 40, window=text_set)
red_set = canvas_set.create_image(15, 15, image=img_red)
green_set = canvas_set.create_image(45, 15, image=img_green)
blue_set = canvas_set.create_image(75, 15, image=img_blue)
yellow_set = canvas_set.create_image(105, 15, image=img_yellow)

# 创建初始模块
red = canvas.create_image(-60, -60, image=img_red)
green = canvas.create_image(-60, -60, image=img_green)
blue = canvas.create_image(-60, -60, image=img_blue)
yellow = canvas.create_image(-60, -60, image=img_yellow)

# 顺序移动


top1.mainloop()
