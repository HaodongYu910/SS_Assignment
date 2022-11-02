# main function, program entrance
import ttkbootstrap as ttk

from GUI.welcom_page import basedesk

if __name__ == '__main__':
    root = ttk.Window()
    basedesk(root)
    root.mainloop()
