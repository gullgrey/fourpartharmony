from melody import Interval


class ThreePartHarmony:

    def __init__(self, harmony, melody_position, transpose_up):

        self.harmonised_notes = harmony.harmonised_notes
        self.melody = harmony.melody
        self.melody_position = melody_position
        self.transpose_up = transpose_up

        self._set_three_part()

    def _first_voice(self):

        prev_soprano = None

        for note in self.harmonised_notes:

            chord_value = note.chord.value
            triad = note.chord.chord_notes[chord_value]
            soprano = note.actual_soprano
            abs_soprano = soprano % Interval.octave
            triad_position = triad.index(abs_soprano)

            if triad_position == 0:
                alto_shift = -Interval.forth
                tenor_shift = -Interval.sixth
            elif triad_position == 1:
                alto_shift = -Interval.third
                tenor_shift = -Interval.sixth
            else:
                alto_shift = -Interval.third
                tenor_shift = -Interval.fifth

            future_soprano = note.future_soprano
            large_jump = Interval.forth

            if (prev_soprano is not None and
                    soprano - prev_soprano >= large_jump and
                    future_soprano is not None and
                    soprano - future_soprano >= large_jump):
                alto_shift = tenor_shift
                tenor_shift = -Interval.octave

            alto_value = soprano + alto_shift
            tenor_value = soprano + tenor_shift

            note.alto.value = alto_value
            note.tenor.value = tenor_value

            prev_soprano = soprano

    def _second_voice(self):

        prev_soprano = None

        for note in self.harmonised_notes:

            chord_value = note.chord.value
            triad = note.chord.chord_notes[chord_value]
            soprano = note.actual_soprano
            abs_soprano = soprano % Interval.octave
            triad_position = triad.index(abs_soprano)

            if triad_position == 0:
                alto_shift = Interval.third
                tenor_shift = -Interval.forth
            elif triad_position == 1:
                alto_shift = Interval.third
                tenor_shift = -Interval.third
            else:
                alto_shift = Interval.forth
                tenor_shift = -Interval.third

            future_soprano = note.future_soprano
            large_jump = Interval.forth

            if (prev_soprano is not None and
                    soprano - prev_soprano >= large_jump and
                    future_soprano is not None and
                    soprano - future_soprano >= large_jump):
                tenor_shift = alto_shift - Interval.octave

            elif (prev_soprano is not None and
                    prev_soprano - soprano >= large_jump and
                    future_soprano is not None and
                    future_soprano - soprano >= large_jump):
                alto_shift = tenor_shift + Interval.octave

            alto_value = soprano + alto_shift
            tenor_value = soprano + tenor_shift

            note.alto.value = alto_value
            note.tenor.value = tenor_value

            prev_soprano = soprano

    def _third_voice(self):

        prev_soprano = None

        for note in self.harmonised_notes:

            chord_value = note.chord.value
            triad = note.chord.chord_notes[chord_value]
            soprano = note.actual_soprano
            abs_soprano = soprano % Interval.octave
            triad_position = triad.index(abs_soprano)

            if triad_position == 0:
                alto_shift = Interval.fifth
                tenor_shift = Interval.third
            elif triad_position == 1:
                alto_shift = Interval.sixth
                tenor_shift = Interval.third
            else:
                alto_shift = Interval.sixth
                tenor_shift = Interval.forth

            future_soprano = note.future_soprano
            large_jump = Interval.forth

            if (prev_soprano is not None and
                    prev_soprano - soprano >= large_jump and
                    future_soprano is not None and
                    future_soprano - soprano >= large_jump):
                tenor_shift = alto_shift
                alto_shift = Interval.octave

            alto_value = soprano + alto_shift
            tenor_value = soprano + tenor_shift

            note.alto.value = alto_value
            note.tenor.value = tenor_value

            prev_soprano = soprano

    def _set_three_part(self):

        note_position = 0
        for note in self.harmonised_notes:

            if self.transpose_up[note_position]:
                note.actual_soprano -= Interval.octave

            note_position += 1

        if self.melody_position == 'Staff 1':
            self._first_voice()
        elif self.melody_position == 'Staff 2':
            self._second_voice()
        else:
            self._third_voice()
