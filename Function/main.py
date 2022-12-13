# main function, program entrance
import ttkbootstrap as ttk

from Function.gl import game
from GUI import start_page, select_page
from GUI.welcom_page import basedesk

if __name__ == '__main__':
    startPage = start_page.Snake_and_Ladders()
    startPage.run_game()
    while True:
        game.__init__()
        root = ttk.Window()
        basedesk(root)
        root.mainloop()
        selectPage = select_page.SelectPage()
        selectPage.run()
