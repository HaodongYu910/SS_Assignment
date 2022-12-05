# main function, program entrance
import ttkbootstrap as ttk

from GUI import start_page
from GUI.welcom_page import basedesk

if __name__ == '__main__':
    # startPage = start_page.Snake_and_Ladders()
    # startPage.run_game()
    root = ttk.Window()
    basedesk(root)
    root.mainloop()
