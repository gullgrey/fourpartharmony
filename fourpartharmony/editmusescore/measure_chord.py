
class MeasureRest:

    def __init__(self):

        self.dots = '0'
        self.duration = None

        self.note_length = None

    def set_note_length(self, time_sig):

        durations_dict = {
            'whole': 1,
            'half': 0.5,
            'quarter': 0.25,
            'eighth': 0.125,
            '16th': 0.0625,
            '32nd': 0.03125,
            '64th': 0.015625,
            '128th': 0.0078125
        }

        if self.duration == 'measure':
            self.note_length = time_sig
        else:
            self.note_length = durations_dict[self.duration]

        dot_num = int(self.dots)
        current_length = self.note_length
        dot_lengths = [current_length]
        while dot_num > 0:
            dot_modifier = 0.5
            current_length = current_length * dot_modifier
            dot_lengths.append(current_length)
            dot_num -= 1

        self.note_length = sum(dot_lengths)


class MeasureChord(MeasureRest):

    def __init__(self):

        super().__init__()
        self.lyric = None
        self.accidental = None

        self.soprano_pitch = None
        self.soprano_tpc = None

        self.chord = None

        self.alto_pitch = None
        self.alto_tpc = None
        self.alto_leading_note = False

        self.tenor_pitch = None
        self.tenor_tpc = None
        self.tenor_leading_note = False

        self.bass_pitch = None
        self.bass_tpc = None
        self.bass_leading_note = False
