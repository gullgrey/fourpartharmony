import tkinter as tk


class ErrorWindow:

    def __init__(self, master, file, error_type):

        self.error_message = self.set_error_message(error_type)

        self.master = master
        self.file = file

        self.file_error_title = tk.Label(self.master,
                                         text='File Error',
                                         fg='red',
                                         font=("Helvetica", 16))
        self.file_error_body = tk.Label(self.master,
                                        text=self.error_message.format(self.file))

        self.ok_button = tk.Button(self.master,
                                   text='OK',
                                   command=self.master.destroy)

        self.file_error_title.pack()
        self.file_error_body.pack()
        self.ok_button.pack(pady=10, ipadx=20)

    @staticmethod
    def set_error_message(error_type):

        if error_type == 'FileNotFound':
            error_message = """The file "{}" cannot be found in this directory. 
Make sure the file name is spelled correctly and has been
saved as an Uncompressed MuseScore 3 File (.mscx)."""
        # The error type is EmptyMelody
        else:
            error_message = """Harmony cannot be created. The file "{}" has no notes on the top staff."""
        return error_message
