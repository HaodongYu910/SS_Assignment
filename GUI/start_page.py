import sys
import pygame
from PIL import Image
import ttkbootstrap as ttk

# 设置窗口大小
from GUI.welcom_page import basedesk

size = (600, 300)
# 修改原始图片大小为窗口大小
pic_org = Image.open('../Image/start_page.jpeg')  # 把'original_bg.jpg'换成你保存的图片的路径， 下同
pic_new = pic_org.resize(size, Image.ANTIALIAS)
pic_new.save('../Image/background.jpg')
# 导入修改尺寸后的图片
picture = pygame.image.load('../Image/background.jpg')
# 估计开始键的中心坐标
center = (int(size[0] / 2), int(size[1] * 0.8))


# 这个类是用来创建一个开始键矩形，放在背景图开始键那，但是没有绘制在窗口中（所以看不到），这样点击背景图上的开始键才能有反应，具体代码不用管、不用调
class Button:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = int(size[1] / 6), int(size[1] / 6)
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


# 游戏主程序
class Snake_and_Ladders:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)  # screen屏幕大小
        pygame.display.set_caption("SNAKE AND LADDERS")  # 游戏名显示在窗口左上角
        self.game_active = False  # 初始化时，以及每轮游戏结束后，设置为“暂停”模式，要点击开始键才开始游戏
        self.play_button = Button(self, '')  # 创建的开始按钮，位置就在背景图的开始键位置，但不显示
        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 点x就关闭
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  # 点开始键就进入下一个环节，这一步设置self.game_active = True，用来指示游戏开始；注意！！！每轮游戏结束后要设置self.game_active = False 否则画不出背景图
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

            if not self.game_active:  # 游戏没有开始的话，将背景图绘制上去
                self.screen.blit(picture, (0, 0))
            else:
                pygame.quit()    # 关闭窗口
                break    # 跳出循环，结束程序

            # 刷新界面
            pygame.display.flip()

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self.game_active = True


if __name__ == "__main__":
    game1 = Snake_and_Ladders()  # 创建一个游戏对象
    game1.run_game()  # 运行游戏
    root = ttk.Window()
    basedesk(root)
    root.mainloop()

