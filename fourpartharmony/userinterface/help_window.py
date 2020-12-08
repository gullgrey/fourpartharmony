import tkinter as tk


class HelpWindow:

    def __init__(self, master):

        self.instruction_text = ("Create a melody using MuseScore 3.\n\n"
                                 "Save the melody as an uncompressed MuseScore 3 file (.mscx) in the same folder as "
                                 "the Melody Harmoniser app.\n\n"""
                                 "Type the name of the MuseScore file into the File Name section.\n\n"
                                 "Select whether the melody is in a major or minor key.\n\n"
                                 "Select whether the playback instrument will be a choir or piano sound."
                                 "Select whether the melody will be harmonised as a Four-Part Harmony or a Three-Part "
                                 "Harmony.\n\n"
                                 "If it is a Three-Part Harmony, select whether the melody is in the top, middle or "
                                 "lower voice.\n\n"
                                 "Press the “Harmonise” button and the now harmonised file will open in MuseScore 3.")

        self.note_text = ("The melody range for a four-part harmony is from C4 (middle C) to G5. The melody range for "
                          "a three-part harmony is C3 to G5. For the purposes of harmonisation, any notes outside this "
                          "range will be treated as though they are within the nearest octave in these ranges.\n\n"
                          "The melody is gathered from the top staff of the MuseScore file. Any notes from subsequent "
                          "staves will be ignored.\n\n"
                          "If Melody Harmoniser is used on a file that has already been harmonised or has the same "
                          "name as a previously harmonised file, the file containing the harmony will be overwritten. "
                          "To avoid this, either rename the file containing the harmony or save it in a different "
                          "directory.\n\n"
                          "Melody Harmoniser is compatible with MuseScore program version 3.5.2. It may work with "
                          "other versions but has currently not been tested.")

        self.master = master

        self.instruction_title = tk.Label(self.master, text='Instructions',
                                          fg='blue', font=('Helvetica', 20))
        self.instruction_frame = tk.Frame(self.master)
        self.instruction_body = tk.Text(self.instruction_frame,  wrap=tk.WORD,
                                        width=50, height=10, padx=5,
                                        font=('Helvetica', 11))
        self.instruction_body.insert('end', self.instruction_text)
        self.instruction_body.configure(state='disabled')
        self.instruction_scroll = tk.Scrollbar(self.instruction_frame)
        self.instruction_scroll.config(command=self.instruction_body.yview)

        self.internal_frame = tk.Frame(self.master)

        self.note_title = tk.Label(self.master, text='**Note**',
                                   fg='red', font=('Helvetica', 20))
        self.note_frame = tk.Frame(self.master)
        self.note_body = tk.Text(self.note_frame, wrap=tk.WORD,
                                 width=50, height=10, padx=5,
                                 font=('Helvetica', 11))
        self.note_body.insert('end', self.note_text)
        self.note_body.configure(state='disabled')
        self.note_scroll = tk.Scrollbar(self.note_frame)
        self.note_scroll.config(command=self.note_body.yview)

        self.padding_frame = tk.Frame(self.master)

        self.instruction_title.pack(pady=5)
        self.instruction_frame.pack(padx=10)
        self.instruction_body.pack(side=tk.LEFT)
        self.instruction_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.internal_frame.pack(pady=10)

        self.note_title.pack(pady=5)
        self.note_frame.pack(padx=10)
        self.note_body.pack(side=tk.LEFT)
        self.note_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.padding_frame.pack(pady=5)
