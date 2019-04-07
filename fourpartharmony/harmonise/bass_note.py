from random import shuffle

from harmonise_exceptions import EmptyNodeError
from melody import Interval


class BassNote:

    def __init__(self, current_note):

        self.melody = current_note.melody
        self.chord_notes = self.melody.chord_notes

        self.soprano = current_note.soprano
        self.prev_soprano = current_note.prev_soprano

        self.chord = current_note.chord.value
        self.prev_chord = None
        self.prev_prev_chord = None

        self.prev_bass = None
        self.prev_prev_bass = None

        self.prev_tenor = None

        self.cadence_nodes_empty = current_note.chord.cadence_nodes_empty
        # self.is_penultimate_note = current_note.is_penultimate_note
        # self.is_final_note = current_note.is_final_note

        self.nodes = []
        self.value = None

        self._bass_note_setup(current_note)

    def _bass_note_setup(self, current_note):

        if self.chord is None:
            raise EmptyNodeError('No chord found during bass note setup.')

        if current_note.is_first_note is False:
            self.prev_chord = current_note.prev_chord.value
            self.prev_bass = current_note.prev_bass.value
            self.prev_tenor = current_note.prev_tenor.value
            if current_note.is_second_note is False:
                self.prev_prev_chord = current_note.prev_prev_chord.value
                self.prev_prev_bass = current_note.prev_prev_bass.value

        if current_note.is_first_note:
            self._first_bass_note()
        elif self.cadence_nodes_empty is False:
            self._final_bass_cadence()
        else:
            self._new_bass_note()

        if len(self.nodes) > 0:
            self.value = self.nodes[0]

    def _first_bass_note(self):

        # This randomly selects between shifting down 1 or two octaves, and makes sure shift is still in bass range.
        octave_shift = -7
        two_octave_shift = -14

        triad_note = 0
        dominant_chord = False
        while triad_note <= 1 and dominant_chord is False:
            note = self.chord_notes[self.chord][triad_note]
            if note + two_octave_shift >= self.melody.bass_lower:
                self.nodes.append(note + two_octave_shift)
            self.nodes.append(note + octave_shift)
            dominant_chord = self.chord in ['V', 'V7']
            triad_note += 1

    def _new_bass_note(self):

        abs_prev_bass = self.prev_bass % Interval.octave

        bass_interval = 0
        while bass_interval < Interval.octave:
            bass_interval += 1
            if bass_interval == Interval.seventh:
                continue
            # Bass steps down first to encourage lower bass voicing.
            interval_pair = [self.prev_bass - bass_interval, self.prev_bass + bass_interval]

            self.nodes += interval_pair
            if bass_interval == Interval.fifth:
                self.nodes.append(self.prev_bass)

        if abs_prev_bass == self.melody.leading_note:
            self.nodes.clear()
            self.nodes.append(self.prev_bass + 1)

        self.nodes[:] = [note for note in self.nodes if self._note_is_valid(note)]

    def _note_is_valid(self, note):

        abs_note = note % Interval.octave
        abs_prev_bass = self.prev_bass % Interval.octave
        abs_soprano = self.soprano % Interval.octave
        first_triad_note = self.chord_notes[self.chord][0]
        second_triad_note = self.chord_notes[self.chord][1]
        third_triad_note = self.chord_notes[self.chord][2]

        if self.melody.in_bass_range(note) is False:
            return False

        elif note > self.prev_tenor:
            return False

        # This ensures that no consecutive 5ths or octaves are created.
        elif Interval.invalid_consecutives(self.prev_soprano, self.prev_bass, self.soprano, note):
            return False

        # This ensures the mediant doesn't resolve to the leading note if the key is minor.
        elif (abs_prev_bass == self.melody.mediant
                and abs_note == self.melody.leading_note
                and self.melody.is_minor):
            return False

        # This ensures the 3rd note of chord 'V' (the leading note of the melody) is never doubled.
        elif (self.chord == 'V'
                and abs_note == second_triad_note
                and abs_soprano == second_triad_note):
            return False

        # This removes any notes not in the chosen chord.
        elif abs_note not in self.chord_notes[self.chord]:
            return False

        # This removes the possibility of 2nd inversion for all chords other then chords I, IV an V7.
        elif (self.chord not in ['I', 'IV', 'V7']
                and abs_note == third_triad_note):
            return False

        # This ensures if the chord is repeated the bass is in a different inversion.
        elif (self.chord == self.prev_chord
                and abs_note == abs_prev_bass):
            return False

        # This ensures chord VII is always in 1st inversion as it is a diminished chord.
        elif (self.chord == 'VII'
                and abs_note != second_triad_note):
            return False

        # This ensures chord II is always in second inversion when the key is minor as it is a diminished chord.
        elif (self.chord == 'II'
                and self.melody.is_minor
                and abs_note != second_triad_note):
            return False

        # This ensures only the third can be doubled in chord VI
        elif (self.chord == 'VI'
                and abs_note == abs_soprano
                and abs_note != third_triad_note):
            return False

        # This ensures only the tonic can be doubled in chord V7.
        elif (self.chord == 'V7'
                and abs_note == abs_soprano
                and abs_note != first_triad_note):
            return False

        # This ensures chord IVc always resolves to I in root position.
        elif (self.prev_chord == 'IV'
                and self.chord == 'I'
                and abs_prev_bass == first_triad_note
                and abs_note != first_triad_note):
            return False

        # This checks conditions for when the previous chord was Ic.
        elif (self.prev_chord == 'I'
                and abs_prev_bass == self.chord_notes[self.prev_chord][2]):

            abs_prev_prev_bass = self.prev_prev_bass % Interval.octave

            # This ensures Ic resolves to V in root position unless progression is
            # (IVb -> Ic -> IV root) or (IV root -> Ic -> IVb)
            if self.chord == 'V' and abs_note == first_triad_note:
                return True
            elif (self.chord == 'IV'
                    and abs_prev_prev_bass == first_triad_note
                    and abs_note == second_triad_note):
                return True
            elif (self.chord == 'IV'
                    and abs_prev_prev_bass == second_triad_note
                    and abs_note == first_triad_note):
                return True
            else:
                return False

        else:
            return True

    def _final_bass_cadence(self):
        """
        This function sets up a regular array of bass nodes but removes any note
        that is not the tonic of the chord.
        It is used in the final 2 notes of the melody.

        :return: None
        """
        self._new_bass_note()

        tonic_nodes = []
        for note in self.nodes:
            abs_note = note % Interval.octave
            if abs_note == self.chord_notes[self.chord][0]:
                tonic_nodes.append(note)

        # self.nodes = [note for note in self.nodes if note not in tonic_nodes]
        # self.nodes = tonic_nodes + self.nodes
        self.nodes = tonic_nodes

    def inversion(self):

        if self.value is None:
            return None

        abs_bass = self.value % Interval.octave
        triad = self.chord_notes[self.chord]

        if abs_bass == triad[0]:
            return ''
        elif abs_bass == triad[1]:
            return 'b'
        elif abs_bass == triad[2]:
            return 'c'
        elif (len(triad) > 3
                and abs_bass == triad[3]):
            return 'd'
        else:
            return None

    def next_node(self):

        if len(self.nodes) > 0:
            self.nodes.pop(0)

        if len(self.nodes) > 0:
            self.value = self.nodes[0]
        else:
            self.value = None
