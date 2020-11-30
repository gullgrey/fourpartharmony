from fractions import Fraction
from mscx import Mscx


class WriteScore:

    def __init__(self, read_score):

        self.read_score = read_score
        self.file = None

        self.measure_length = read_score.time_sig_value
        self.anacrusis_length = None

        self._open_file(read_score)
        self._set_anacrusis_length()

        self._close_file()

    def _open_file(self, read_score):
        file_type = ".mscx"
        file_name = read_score.file_name[:-len(file_type)] + " Harmonised" + file_type
        self.file = open(file_name, "w")

    def _set_anacrusis_length(self):
        if self.read_score.anacrusis is not None:
            self.anacrusis_length = Fraction(self.read_score.anacrusis)

    def _close_file(self):
        self.file.close()
