from GUI.input_name import *


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title("Snake and Ladder")
        self.root.geometry("1000x800+0+0")  # 400wight, 200height
        self.root.resizable(False, False)  # 不可拖动窗口改变大小
        # root.wm_attributes('-topmost', 1) #让主窗口置顶
        # NameEntryForm(self.root)
        NameEntryForm(self.root)


if __name__ == '__main__':
    root = ttk.Window()
    basedesk(root)
    root.mainloop()
