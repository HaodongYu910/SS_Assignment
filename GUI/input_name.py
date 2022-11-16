from GUI.game_board import *


# class snakeAndLadder_bg(ttk.Frame):
#     def __init__(self, master):
#         super().__init__(master, padding=(20, 10))
#         self.pack(fill=BOTH, expand=YES)
#         mytoplevel = ttk.Toplevel(master)
#         image = Image.open('/Users/yuhaodong/Desktop/Postgraduate/System and software/SS_assignment/Image/bg.jpeg')
#         img = ImageTk.PhotoImage(image)
#         canvas1 = ttk.Canvas(mytoplevel, width=image.width * 2, height=image.height * 2, bg='white')
#         canvas1.create_image(0, 0, image=img, anchor="nw")
#         canvas1.create_image(image.width, 0, image=img, anchor="nw")
#         canvas1.pack()
#         mytoplevel.mainloop()


class NameEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.p1 = ttk.StringVar(value="")
        self.p2 = ttk.StringVar(value="")
        self.p3 = ttk.StringVar(value="")
        self.p4 = ttk.StringVar(value="")
        self.p1_colour = ttk.StringVar(value="")
        self.p2_colour = ttk.StringVar(value="")
        self.p3_colour = ttk.StringVar(value="")
        self.p4_colour = ttk.StringVar(value="")

        # form header
        hdr_txt = "Please enter the name of different User\n(Hint: blank name will auto create a robot!!)"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("Player1", self.p1, self.p1_colour)
        self.create_form_entry("Player2", self.p2, self.p2_colour)
        self.create_form_entry("Player3", self.p3, self.p3_colour)
        self.create_form_entry("Player4", self.p4, self.p4_colour)
        self.create_buttonbox()


    def create_form_entry(self, label, variable, colour):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        # this player's label
        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        # this player's entry
        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        # this player's combobox
        combobox = ttk.Combobox(master=container, textvariable=colour)
        combobox.pack(side=LEFT, padx=5, fill=X, expand=YES)
        combobox['value'] = ('Red', 'Blue', 'Black', 'Grey')
        combobox.current(3)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        start_game = ttk.Button(
            master=container,
            text="Play",
            command=self.onStart,
            bootstyle=INFO,
            width=6,
        )
        start_game.pack(side=RIGHT, padx=5)

        submit_player_name = ttk.Button(
            master=container,
            text="Submit",
            command=self.onSubmit,
            bootstyle=SUCCESS,
            width=6,
        )
        submit_player_name.pack(side=RIGHT, padx=5)
        submit_player_name.focus_set()

    def onSubmit(self):
        """Print the contents to console and return the values."""
        print("Player1:{}, Colour:{}".format(self.p1.get(), self.p1_colour.get()))
        print("Player2:{}, Colour:{}".format(self.p1.get(), self.p2_colour.get()))
        print("Player3:{}, Colour:{}".format(self.p1.get(), self.p3_colour.get()))
        print("Player4:{}, Colour:{}".format(self.p1.get(), self.p4_colour.get()))
        list_player = [self.p1.get(), self.p2.get(), self.p3.get(), self.p4.get()]
        list_colour = [self.p1_colour.get(), self.p2_colour.get(), self.p3_colour.get(), self.p4_colour.get()]
        # snakeAndLadder.addPlayer(list_player)
        game.addPlayer(list_player)
        game.addColour_2_player(list_colour)
        # return self.p1.get(), self.p2.get(), self.p3.get(), self.p4.get()

    def onStart(self):
        """Cancel and close the application."""
        snakeAndLadder_game_board(self.master)


if __name__ == "__main__":
    app = ttk.Window("Data Entry", "superhero", resizable=(False, False))
    NameEntryForm(app)
    app.mainloop()
