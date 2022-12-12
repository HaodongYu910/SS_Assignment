import sys
import pygame

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


class SelectPage:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("SNAKE AND LADDERS")  # 游戏名显示在窗口左上角
        self.play_again_ = False
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


