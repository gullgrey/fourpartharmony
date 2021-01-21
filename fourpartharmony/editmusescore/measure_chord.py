from note_conversions import NoteConversions


class MeasureRest:

    def __init__(self):

        self.dots = '0'
        self.duration = None

        self.note_length = None

        self.tuplet = None

    def set_note_length(self, time_sig):

        if self.duration == 'measure':
            self.note_length = time_sig
        else:
            self.note_length = NoteConversions.durations[self.duration]

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
        self.articulation = None
        self.accidental = None

        self.tie_start = False
        self.tie_start_measures = None
        self.tie_start_fractions = None

        self.tie_end = False
        self.tie_end_measures = None
        self.tie_end_fractions = None

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


class Tuplet:

    def __init__(self):

        self.normal_notes = None
        self.actual_notes = None
        self.base_note = None

        self.normal_length = None
        self.actual_length = None

    def set_tuplet_length(self):

        base_length = NoteConversions.durations[self.base_note]
        self.normal_length = int(self.normal_notes) * base_length
        self.actual_length = int(self.actual_notes) * base_length
