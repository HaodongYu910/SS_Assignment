from GUI.input_name import *


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


if __name__ == '__main__':
    root = ttk.Window()
    basedesk(root)
    root.mainloop()
