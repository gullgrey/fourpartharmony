import tkinter as tk


class HelpWindow:

    def __init__(self, master):

        self.instruction_text = """blah"""

        self.note_text = """foo"""

        self.master = master

        self.instruction_title = tk.Label(self.master, text='Instructions')
        self.instruction_body = tk.Label(self.master, text=self.instruction_text)
        self.note_title = tk.Label(self.master, text='**Note**')
        self.note_body = tk.Label(self.master, text=self.note_text)

        self.instruction_title.pack()
        self.instruction_body.pack()
        self.note_title.pack()
        self.note_body.pack()
