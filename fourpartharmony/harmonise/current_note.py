from harmonise_exceptions import EmptyNodeError
from melody import Interval


class CurrentNote:

    def __init__(self, prev_note):

        if prev_note is not None:
            self.melody = prev_note.melody
            self.soprano = self.melody.next_note()
            self.prev_soprano = self.melody.prev_soprano

        self.alto = None
        self.tenor = None
        self.bass = None
        self.chord = None

        self.is_first_note = True
        self.is_second_note = False
        self.is_penultimate_note = False
        self.is_final_note = False

        self.prev_chord = None
        self.prev_bass = None
        self.prev_tenor = None
        self.prev_alto = None

        self.prev_prev_chord = None
        self.prev_prev_bass = None

        self._previous_note_vales(prev_note)

    def _previous_note_vales(self, prev_note):

        if (prev_note is not None
                and abs(self.soprano - self.prev_soprano) <= Interval.octave):

            self.is_first_note = False
            self.is_second_note = True
            self.prev_chord = prev_note.chord
            self.prev_bass = prev_note.bass
            self.prev_tenor = prev_note.tenor
            self.prev_alto = prev_note.alto
            self._prev_note_check()
            if prev_note.is_first_note is False:
                self.is_second_note = False
                self.prev_prev_chord = prev_note.prev_chord
                self.prev_prev_bass = prev_note.prev_bass

        # if self.is_first_note is False:
        self.is_penultimate_note = self.melody.is_penultimate_note
        self.is_final_note = self.melody.is_final_note

    def _prev_note_check(self):

        error_message = 'Previous %s value not found during new note setup.'

        if self.prev_chord.value is None:
            raise EmptyNodeError(error_message % 'chord')
        elif self.prev_bass.value is None:
            raise EmptyNodeError(error_message % 'bass')
        elif self.prev_tenor.value is None:
            raise EmptyNodeError(error_message % 'tenor')
        elif self.prev_alto.value is None:
            raise EmptyNodeError(error_message % 'alto')

    # The following 4 functions set the 3 notes and chord for the soprano note.
    # If they are called with no variable they set their respective note to None.
    def set_alto(self, new_alto=None):
        self.alto = new_alto

    def set_tenor(self, new_tenor=None):
        self.tenor = new_tenor

    def set_bass(self, new_bass=None):
        self.bass = new_bass

    def set_chord(self, new_chord=None):
        self.chord = new_chord

    def clear_notes(self):
        self.alto = None
        self.tenor = None
        self.bass = None
        self.chord = None

    def print_notes(self):
        print('Chord:' + str(self.chord.value) + str(self.bass.inversion()))
        print('Soprano:', self.soprano, '|', Interval.note_letter(self.soprano))
        print('Alto:', self.alto.value, '|', Interval.note_letter(self.alto.value))
        print('Tenor:', self.tenor.value, '|', Interval.note_letter(self.tenor.value))
        print('Bass:', self.bass.value, '|', Interval.note_letter(self.bass.value))
        print('\n')


class FirstNote(CurrentNote):

    def __init__(self, melody):
        self.melody = melody
        self.soprano = self.melody.next_note()
        self.prev_soprano = None
        super().__init__(None)
