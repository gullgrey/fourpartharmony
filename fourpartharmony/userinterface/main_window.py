import tkinter as tk
from read_score import ReadScore
from write_score import WriteScore
from write_three_part import WriteThreePart
from muse_melody import MuseMelody
from melody import Melody
from harmony import Harmony
from three_part_harmony import ThreePartHarmony
from chord_constructor import ChordConstructor
from help_window import HelpWindow
from error_window import ErrorWindow
from harmonise_exceptions import EmptyMelodyError
from os import startfile


class MainWindow:

    def __init__(self, master):

        self.master = master
        self.master.title('Melody Harmoniser')

        self.middle_frame = tk.Frame(self.master)
        self.option_frame = tk.Frame(self.middle_frame)

        self.name_label = tk.Label(self.master, text="Melody Harmoniser", font=("Helvetica", 20))

        self.file_label = tk.Label(self.option_frame, text="File Name: ")
        self.file_entry = tk.Entry(self.option_frame)

        self.minor_label = tk.Label(self.option_frame, text="Major or Minor: ")
        self.minor_value = tk.StringVar(self.option_frame)
        self.minor_value.set('Major')
        self.minor_option = tk.OptionMenu(self.option_frame, self.minor_value, 'Major', 'Minor')

        self.instrument_label = tk.Label(self.option_frame, text="Instrument: ")
        self.instrument_value = tk.StringVar(self.option_frame)
        self.instrument_value.set('Choir')
        self.instrument_option = tk.OptionMenu(self.option_frame, self.instrument_value,
                                               'Choir', 'Piano')

        self.parts_label = tk.Label(self.option_frame,
                                    text="Number of parts: ")
        self.parts_value = tk.StringVar(self.option_frame)
        self.parts_value.set('Four Part Harmony')
        self.parts_option = tk.OptionMenu(self.option_frame, self.parts_value,
                                          'Four Part Harmony', 'Three Part Harmony',
                                          command=self._show_melody_position)

        self.position_label = tk.Label(self.option_frame,
                                       text="Melody voice: ")
        self.position_value = tk.StringVar(self.option_frame)
        self.position_value.set('Top Voice')
        self.position_option = tk.OptionMenu(self.option_frame, self.position_value,
                                             'Top Voice', 'Middle Voice', 'Bottom Voice')
        self.position_padding = tk.Frame(self.option_frame)

        self.help_button = tk.Button(self.middle_frame, text='?', font=("Helvetica", 16),
                                     fg='blue', command=self._instruction_window)

        self.harmony_button = tk.Button(self.master, text='Harmonise', font=("Helvetica", 16),
                                        fg='red', command=self._harmonise_file)

        self.file_label.grid(column=0, row=0, sticky=tk.E)
        self.file_entry.grid(column=1, row=0, sticky=tk.EW,
                             padx=2, pady=4, ipadx=22)

        self.minor_label.grid(column=0, row=1, sticky=tk.E)
        self.minor_option.grid(column=1, row=1, sticky=tk.EW)

        self.instrument_label.grid(column=0, row=2, sticky=tk.E)
        self.instrument_option.grid(column=1, row=2, sticky=tk.EW)

        self.parts_label.grid(column=0, row=3, sticky=tk.E)
        self.parts_option.grid(column=1, row=3, sticky=tk.EW)

        self.position_padding.grid(row=4, pady=15)

        self.name_label.pack(pady=20)
        self.middle_frame.pack()
        self.option_frame.pack(side=tk.LEFT, padx=10)
        self.help_button.pack(side=tk.RIGHT, ipadx=5, padx=20)
        self.harmony_button.pack(pady=30)

    def _show_melody_position(self, value):

        if value == 'Three Part Harmony':
            self.position_label.grid(column=0, row=4, sticky=tk.E)
            self.position_option.grid(column=1, row=4, sticky=tk.EW)

        else:
            self.position_label.grid_forget()
            self.position_option.grid_forget()

    def _instruction_window(self):
        self.help_window = tk.Toplevel(self.master)
        HelpWindow(self.help_window)
        self.help_window.focus_set()
        self.help_window.grab_set()

    def _get_melody_position(self):

        voice = self.position_value.get()
        if voice == 'Top Voice':
            melody_position = 'Staff 1'
        elif voice == 'Middle Voice':
            melody_position = 'Staff 2'
        # if the three part voice is Bottom Voice
        else:
            melody_position = 'Staff 3'
        return melody_position

    def _create_error_window(self, file, error_type):
        self.error_window = tk.Toplevel(self.master)
        ErrorWindow(self.error_window, file, error_type)
        self.error_window.focus_set()
        self.error_window.grab_set()

    def _harmonise_file(self):

        file = self.file_entry.get()
        major_minor = self.minor_value.get()
        instrument = self.instrument_value.get()
        three_part = self.parts_value.get()

        file_type = '.mscx'
        if file.endswith(file_type) is False:
            file += file_type

        is_minor = False
        if major_minor == 'Minor':
            is_minor = True

        try:
            score = ReadScore(file)
        except (FileNotFoundError, PermissionError):
            self._create_error_window(file, 'FileNotFound')
            return

        muse_melody = MuseMelody(is_minor, score.key_sig, score.measure_chords)

        try:
            melody = Melody(muse_melody.soprano_list, muse_melody.key)
        except EmptyMelodyError:
            self._create_error_window(file, 'EmptyMelody')
            return

        harmony = Harmony(melody)

        if three_part == 'Three Part Harmony':
            melody_position = self._get_melody_position()
            ThreePartHarmony(harmony, melody_position, muse_melody.transpose_up)
            ChordConstructor(score, harmony)
            write_score = WriteThreePart(score, instrument, melody_position)
        # if harmonisation is Four-Part Harmony
        else:
            ChordConstructor(score, harmony)
            write_score = WriteScore(score, instrument)

        startfile(write_score.file_name)
        self.master.destroy()
