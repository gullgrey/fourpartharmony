from error_window import ErrorWindow
from harmonise_exceptions import EmptyMelodyError
from read_score import ReadScore
from write_score import WriteScore
from write_three_part import WriteThreePart
from muse_melody import MuseMelody
from melody import Melody
from harmony import Harmony
from three_part_harmony import ThreePartHarmony
from chord_constructor import ChordConstructor


class MainConsole:

    def __init__(self):

        self.file = None
        self.score = None
        self.is_minor = None
        self.instrument = None
        self.is_three_part = None
        self.melody_position = None

        self._setup()

    def _set_score(self):

        while True:
            self.file = input('File Name: \n')
            file_type = '.mscx'
            if self.file.endswith(file_type) is False:
                self.file += file_type
            try:
                self.score = ReadScore(self.file)
            except (FileNotFoundError, PermissionError, TypeError):
                error_message = ErrorWindow.set_error_message('FileNotFound')
                print(error_message.format(self.file) + '\n')
            else:
                break

    def _set_is_minor(self):

        major_list = ['major', 'Major', 'M']
        minor_list = ['minor', 'Minor', 'm']
        while True:
            major_minor = input('Is the melody Major (M) or minor (m)? \n')
            if major_minor in major_list:
                self.is_minor = False
                break
            elif major_minor in minor_list:
                self.is_minor = True
                break
            else:
                print('Please input ' + str(major_list) + ' if the melody is Major. \n'
                      + 'Please input ' + str(minor_list) + ' if the melody is minor.\n')

    def _set_instrument(self):

        piano_list = ['p', 'P', 'piano', 'Piano']
        choir_list = ['c', 'C', 'choir', 'Choir']
        while True:
            instrument_input = input('Will the instrument be a piano (p) or choir (c)? \n')
            if instrument_input in piano_list:
                self.instrument = 'Piano'
                break
            elif instrument_input in choir_list:
                self.instrument = 'Choir'
                break
            else:
                print('Please input ' + str(piano_list) + ' if the instrument is a piano. \n'
                      + 'Please input ' + str(choir_list) + ' if the instrument is a choir.\n')

    def _set_is_three_part(self):

        four_part = ['Four Part Harmony', 'four part harmony', '4']
        three_part = ['Three Part Harmony', 'three part harmony', '3']
        while True:
            part_number = input('Is this a Four Part Harmony (4) or a Three Part Harmony (3)? \n')
            if part_number in four_part:
                self.is_three_part = False
                break
            elif part_number in three_part:
                self.is_three_part = True
                break
            else:
                print('Please input ' + str(four_part) + ' if it is a Four Part Harmony. \n'
                      + 'Please input ' + str(three_part) + ' if it is a Three Part Harmony.\n')

    def _set_melody_position(self):

        staff_one = ['1', 'Staff 1', 'staff 1']
        staff_two = ['2', 'Staff 2', 'staff 2']
        staff_three = ['3', 'Staff 3', 'staff 3']
        while True:
            staff_input = input('What staff will the melody be in? (Staff 1, Staff 2, Staff 3)\n')
            if staff_input in staff_one:
                self.melody_position = 'Staff 1'
                break
            elif staff_input in staff_two:
                self.melody_position = 'Staff 2'
                break
            elif staff_input in staff_three:
                self.melody_position = 'Staff 3'
                break
            else:
                print('Please input ' + str(staff_one) + ' if the melody is in Staff 1. \n'
                      + 'Please input ' + str(staff_two) + ' if the melody is in Staff 2. \n'
                      + 'Please input ' + str(staff_three) + ' if the melody is in Staff 3.\n')

    def _setup(self):

        self._set_score()
        self._set_is_minor()
        self._set_instrument()
        self._set_is_three_part()

        if self.is_three_part:
            self._set_melody_position()

        muse_melody = MuseMelody(self.is_minor, self.score.key_sig, self.score.measure_chords)

        try:
            melody = Melody(muse_melody.soprano_list, muse_melody.key)
        except EmptyMelodyError:
            error_message = ErrorWindow.set_error_message('EmptyMelody')
            input(error_message.format(self.file))
            return

        harmony = Harmony(melody)

        if self.is_three_part:
            ThreePartHarmony(harmony, self.melody_position, muse_melody.transpose_up)
            ChordConstructor(self.score, harmony)
            WriteThreePart(self.score, self.instrument, self.melody_position)
        else:
            ChordConstructor(self.score, harmony)
            WriteScore(self.score, self.instrument)
