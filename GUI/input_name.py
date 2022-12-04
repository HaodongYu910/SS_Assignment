from GUI.game_board import *
from GUI.game_board_new import *


class NameEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.p1 = ttk.StringVar(value="")
        self.p1_attribute = ttk.StringVar(value="")
        self.p1_colour = ttk.StringVar(value="")

        self.p2 = ttk.StringVar(value="")
        self.p2_attribute = ttk.StringVar(value="")
        self.p2_colour = ttk.StringVar(value="")

        self.p3 = ttk.StringVar(value="")
        self.p3_attribute = ttk.StringVar(value="")
        self.p3_colour = ttk.StringVar(value="")

        self.p4 = ttk.StringVar(value="")
        self.p4_attribute = ttk.StringVar(value="")
        self.p4_colour = ttk.StringVar(value="")

        # form header
        hdr_txt = "Please enter the name of different User\n(Hint: blank name will auto create a robot!!)"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("Player1", self.p1, self.p1_colour, self.p1_attribute)
        self.create_form_entry("Player2", self.p2, self.p2_colour, self.p2_attribute)
        self.create_form_entry("Player3", self.p3, self.p3_colour, self.p3_attribute)
        self.create_form_entry("Player4", self.p4, self.p4_colour, self.p4_attribute)
        self.create_buttonbox()

    def create_form_entry(self, label, variable, colour, attribute):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        # this player's label
        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        # this player's entry
        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        # is this player is a robot?
        combobox_attribute = ttk.Combobox(master=container, textvariable=attribute)
        combobox_attribute.pack(side=LEFT, padx=5, fill=X, expand=YES)
        combobox_attribute['value'] = ('Robot', 'Player')
        combobox_attribute.current(0)

        # this player's colour
        combobox = ttk.Combobox(master=container, textvariable=colour)
        combobox.pack(side=LEFT, padx=5, fill=X, expand=YES)
        combobox['value'] = ('Red', 'Blue', 'Green', 'Yellow')
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
        print(
            "Player1:{}, Colour:{}, attribute:{}".format(self.p1.get(), self.p1_colour.get(), self.p1_attribute.get()))
        print(
            "Player2:{}, Colour:{}, attribute:{}".format(self.p2.get(), self.p2_colour.get(), self.p2_attribute.get()))
        print(
            "Player3:{}, Colour:{}, attribute:{}".format(self.p3.get(), self.p3_colour.get(), self.p3_attribute.get()))
        print(
            "Player4:{}, Colour:{}, attribute:{}".format(self.p4.get(), self.p4_colour.get(), self.p4_attribute.get()))
        list_player = [self.p1.get(), self.p2.get(), self.p3.get(), self.p4.get()]
        list_colour = [self.p1_colour.get(), self.p2_colour.get(), self.p3_colour.get(), self.p4_colour.get()]
        list_attribute = [self.p1_attribute.get(), self.p2_attribute.get(), self.p3_attribute.get(),
                          self.p4_attribute.get()]
        # snakeAndLadder.addPlayer(list_player)
        game.addPlayer(list_player)
        game.addColour_2_player(list_colour)
        game.addAttribute_2_player(list_attribute)
        # return self.p1.get(), self.p2.get(), self.p3.get(), self.p4.get()

    def onStart(self):
        """Cancel and close the application."""
        self.destroy()
        snakeAndLadder_game_board_new(self.master)
        # snakeAndLadder_game_board(self.master)


if __name__ == "__main__":
    app = ttk.Window("Data Entry", "superhero", resizable=(False, False))
    NameEntryForm(app)
    app.mainloop()
