import sys
import pygame

from Function.gl import game

size = (600, 300)
center = (int(size[0] / 2), int(size[1] * 0.5))
position1 = (center[0] - int(size[0] / 6), center[1])
position2 = (center[0] + int(size[0] / 6), center[1])


class Button_:

    def __init__(self, ai_game, msg, position):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = int(size[1] / 2), int(size[1] / 6)
        self.button_color = (30, 144, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('cesigb13000', 30)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = position
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Label(object):
    def __init__(self, left, top, text, font_info):
        self.status = 0  # <0 :- 不显示。
        self.left = left
        self.top = top
        self.text = text
        self.display_x = left
        self.display_y = top

        if font_info is None:
            self.font = pygame.font.Font('font/msjh.ttc', 20)
            self.tc = (255, 255, 255)
            self.bc = (0, 0, 0)
            self.align = 0
            self.valign = 0
        else:
            self.font = font_info["font"]  # 字型及字体大小
            self.tc = font_info["tc"]
            self.bc = font_info["bc"]
            self.align = font_info.get("align", 0)
            self.valign = font_info.get("valign", 0)

        if text == "":
            self.text_surface = None
        else:
            self.set_text(text)

    def render(self, surface):
        if self.text != "" and self.status >= 0:
            surface.blit(self.text_surface, (self.display_x, self.display_y))

    def set_align(self, align):
        w, h = self.__get_size()
        if align == 2:
            self.display_x = self.left - w
        elif align == 1:
            self.display_x = self.left - int(w / 2)

    # def set_valign(self, valign):
    #     w, h = self.__get_size()
    #     if valign == 2:
    #         self.display_y = self.pos_y - h
    #     elif valign == 1:
    #         self.display_y = self.pos_y - int(h / 2)
    #     else:
    #         self.display_y = self.pos_y

    def __get_size(self):
        if self.text_surface is None:
            return (0, 0)
        else:
            return self.text_surface.get_size()  # return (w, h)

    def set_text(self, text, tc=None, bc=None):
        self.text = text

        if tc is not None:
            self.tc = tc

        if bc is not None:
            self.bc = bc

        self.text_surface = self.font.render(self.text, True, self.tc, self.bc)
        self.set_align(self.align)
        # self.set_valign(self.valign)

    def set_hide(self, flag):
        if flag:
            self.status = -1
        else:
            self.status = 0


class SelectPage:
    """
    TODO: 还需要展示一下是那个玩家赢得了这场比赛的胜利，我已经给game object添加好了一个属性脚winner，你可以直接调用“game.winner”就可以得到胜者。
    现在用
    print("{}".format(game.winner))
    这一行代码是可以直接出winner是谁的。
    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("SNAKE AND LADDERS")  # 游戏名显示在窗口左上角
        self.play_again_ = False
        font_info = {}
        font_info["font"] = pygame.font.Font('../Hannotate.ttc', 36)
        font_info["tc"] = (0, 0, 0)  # 文字颜色
        font_info["bc"] = (255, 255, 255)  # 背景颜色
        font_info["align"] = 0  # 靠左
        font_info["valign"] = 0  # 靠上
        message = "winner is {}!".format(game.winner)
        message2 = "Congratulations!!!"
        self.label1 = Label(10, 10, message, font_info)
        self.label2 = Label(200, 60, message2, font_info)
        self.play_again = Button_(self, 'play_again', position1)
        self.exit = Button_(self, 'exit', position2)
        self.bg_color = (240, 240, 240)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 点x就关闭
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    if self.exit.rect.collidepoint(mouse_pos):
                        sys.exit()
            if not self.play_again_:
                self.screen.fill(self.bg_color)
                self.label1.render(surface=self.screen)
                self.label2.render(surface=self.screen)
                self.play_again.draw_button()
                self.exit.draw_button()
            else:
                pygame.quit()
                break

            # 刷新界面
            pygame.display.flip()

    def _check_play_button(self, mouse_pos):
        if self.play_again.rect.collidepoint(mouse_pos) and not self.play_again_:
            self.play_again_ = True


if __name__ == "__main__":
    sp = SelectPage()
    sp.run()
