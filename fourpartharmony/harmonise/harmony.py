from alto_note import AltoNote
from bass_note import BassNote
from chord import Chord
from current_note import FirstNote, CurrentNote
from harmonise_exceptions import HarmonisationError
from tenor_note import TenorNote


class Harmony:

    def __init__(self, melody):
        self.melody = melody

        self.harmonised_notes = []

        self.prev_note = None
        self.current_note = None

        self.current_chord = None
        self.current_bass = None
        self.current_tenor = None
        self.current_alto = None

        self.create_harmony()

    def create_harmony(self):

        # check melody is "new"?

        furthest_note = 0
        max_prev_notes = 6

        final_note_harmonised = False
        while final_note_harmonised is False:
            if self.current_note is None:
                if self.melody.current_soprano is None:
                    self.current_note = FirstNote(self.melody)
                else:
                    self.current_note = CurrentNote(self.prev_note)

            if self.current_chord is None:
                self.current_chord = Chord(self.current_note)
                self.current_note.chord = self.current_chord

            if self.current_chord.value is None:
                self._prev_next_chord()
                continue

            # print('Chord: ', self.current_chord.nodes, self.melody.current_position)

            if self.current_bass is None:
                self.current_bass = BassNote(self.current_note)
                self.current_note.bass = self.current_bass

            if self.current_bass.value is None:
                self._next_chord()
                continue

            # print('Chord: ', self.current_chord.nodes, 'Bass: ',
            #       self.current_bass.nodes, 'Position: ', self.melody.current_position)

            if self.current_tenor is None:
                self.current_tenor = TenorNote(self.current_note)
                self.current_note.tenor = self.current_tenor

            if self.current_tenor.value is None:
                self._next_bass()
                continue

            if self.current_alto is None:
                self.current_alto = AltoNote(self.current_note)
                self.current_note.alto = self.current_alto

            if self.current_alto.value is None:
                self._next_tenor()
                continue

            # self.current_note.print_notes()

            self.harmonised_notes.append(self.current_note)
            self.prev_note = self.current_note
            self.current_note = None
            self.current_chord = None
            self.current_bass = None
            self.current_tenor = None
            self.current_alto = None

            furthest_note = max(furthest_note, self.melody.current_position)
            if (furthest_note - self.melody.current_position) > max_prev_notes:
                raise HarmonisationError('Unable to harmonise current melody.')

            if self.melody.is_final_note:
                final_note_harmonised = True

    def _next_chord(self):

        self.current_bass = None
        self.current_chord.next_node()

    def _next_bass(self):

        self.current_tenor = None
        self.current_bass.next_node()

    def _next_tenor(self):

        self.current_alto = None
        self.current_tenor.next_node()

    def _prev_next_chord(self):

        self.melody.prev_note()

        self.current_note = self.harmonised_notes.pop()
        self.current_chord = self.current_note.chord
        self.current_bass = self.current_note.bass
        self.current_tenor = self.current_note.tenor
        self.current_alto = None

        self.current_tenor.next_node()

    def print_notes(self):

        for note in self.harmonised_notes:
            note.print_notes()
