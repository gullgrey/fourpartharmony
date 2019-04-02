from random import shuffle

from harmonise_exceptions import EmptyNodeError
from melody import Interval


class TenorNote:

    def __init__(self, current_note):
        self.melody = current_note.melody
        self.chord_notes = self.melody.chord_notes

        self.soprano = current_note.soprano
        self.prev_soprano = current_note.prev_soprano

        self.chord = current_note.chord.value
        self.prev_chord = None

        self.bass = current_note.bass.value
        self.prev_bass = None

        self.prev_tenor = None
        self.prev_alto = None

        self.is_first_note = current_note.is_first_note

        self.potential_degrees = []

        self.nodes = []
        self.value = None

        self._tenor_note_setup(current_note)

    def _tenor_note_setup(self, current_note):

        if self.chord is None:
            raise EmptyNodeError('No chord found during tenor note setup.')
        elif self.bass is None:
            raise EmptyNodeError('No bass note found during tenor note setup.')

        if self.is_first_note is False:
            self.prev_chord = current_note.prev_chord.value
            self.prev_bass = current_note.prev_bass.value
            self.prev_tenor = current_note.prev_tenor.value
            self.prev_alto = current_note.prev_alto.value

        self._degree_setup()

        if self.is_first_note:
            self._first_tenor_note()
        else:
            self._new_tenor_note()

        if len(self.nodes) > 0:
            self.value = self.nodes[0]

    def _degree_setup(self):
        """
        Creates a list of potential scale degrees that that the tenor note could be.
        It then removes one copy of the degree that the bass note and soprano note
        land on.
        :return: None
        """
        abs_soprano = self.soprano % Interval.octave
        abs_bass = self.bass % Interval.octave
        triad = self.chord_notes[self.chord]

        chord_root = triad[0]
        chord_third = triad[1]
        chord_fifth = triad[2]

        in_first_inversion = abs_bass == chord_third
        in_second_inversion = abs_bass == chord_fifth

        self.potential_degrees += triad

        # For chord V7, if nether the soprano or the bass is the fifth of the chord
        # then a second copy of the root of the chord is added.
        if self.chord == 'V7':
            if (abs_soprano != chord_fifth
                    and abs_bass != chord_fifth):
                self.potential_degrees.append(chord_root)

            # If the soprano and bass are the same degree (When they're both the
            # root), the fifth of the chord is removed as the chord is now incomplete.
            if abs_soprano == abs_bass:
                self.potential_degrees.remove(chord_fifth)

        # If the chord is Ic or IVc then only the fifth of the chord is doubled.
        elif in_second_inversion:
            self.potential_degrees.append(chord_fifth)

        # In chord VI the third is always doubled (The tonic of the melody).
        elif self.chord == 'VI':
            self.potential_degrees.append(chord_third)

        elif self.melody.is_minor:

            diminished_chords = ['II', 'VII']

            if self.chord in diminished_chords:
                self.potential_degrees.append(chord_third)

            elif self.chord == 'III':
                # The additional chord root allows chord III to be incomplete (No
                # 5th note.
                self.potential_degrees += [chord_root, chord_root]

                if in_first_inversion:
                    self.potential_degrees.append(chord_third)

            elif self.chord == 'V':
                self.potential_degrees += [chord_root, chord_fifth]

            # All other chords
            else:
                self.potential_degrees += triad
            # self.potential_degrees.append(chord_root)

        # If the key is major.
        else:

            # Diminished chords only double the third of the chord.
            diminished_chords = ['VII']
            if self.chord in diminished_chords:
                self.potential_degrees.append(chord_third)

            # Chord III never doubles the fifth of the chord.
            elif self.chord == 'III':
                self.potential_degrees += [chord_root, chord_third, chord_root]

            elif in_first_inversion:

                if self.chord == 'V':
                    self.potential_degrees += [chord_root, chord_fifth]

                # All other chords
                else:
                    self.potential_degrees += triad
                # self.potential_degrees.append(chord_root)

            # If the chord is in root position:
            else:

                minor_chords = ['II']
                if self.chord in minor_chords:
                    self.potential_degrees += triad

                else:
                    self.potential_degrees += [chord_root, chord_fifth]

                # self.potential_degrees.append(chord_root)

        # print('Chord: '+self.chord)
        # print('Soprano: '+str(self.soprano))
        # print('Bass: '+str(self.bass))
        # print('Potential Degrees: '+str(self.potential_degrees))
        self.potential_degrees.remove(abs_bass)
        self.potential_degrees.remove(abs_soprano)

    def _first_tenor_note(self):

        first_nodes = list(range(self.melody.tenor_lower, self.melody.tenor_upper + 1))
        self.nodes += first_nodes
        shuffle(self.nodes)

        self.nodes[:] = [note for note in self.nodes if self._note_is_valid(note)]

    def _new_tenor_note(self):

        # tenor_direction = -1
        # if self.prev_soprano >= self.soprano:
        #     tenor_direction = 1

        tenor_direction = 1

        self.nodes.append(self.prev_tenor)

        interval_counter = Interval.second
        while interval_counter <= Interval.fifth:
            first_note = self.prev_tenor + (interval_counter * tenor_direction)
            self.nodes.append(first_note)
            second_note = self.prev_tenor - (interval_counter * tenor_direction)
            self.nodes.append(second_note)
            interval_counter += 1

        self.nodes[:] = [note for note in self.nodes if self._note_is_valid(note)]

    def _note_is_valid(self, note):

        abs_note = note % Interval.octave

        if self.melody.in_tenor_range(note) is False:
            return False

        if note <= self.bass or note >= self.soprano:
            return False

        if self.is_first_note is False:
            abs_prev_tenor = self.prev_tenor % Interval.octave

            if note < self.prev_bass or note >= self.prev_alto:
                return False

            if (abs_prev_tenor == self.melody.leading_note
                    and abs_note != self.melody.tonic):
                return False

            if (abs_prev_tenor == self.melody.submediant
                    and abs_note == self.melody.leading_note):
                return False

        if Interval.invalid_consecutives(self.prev_soprano, self.prev_tenor, self.soprano, note):
            return False
        elif Interval.invalid_consecutives(self.prev_tenor, self.prev_bass, note, self.bass):
            return False

        if abs_note not in self.potential_degrees:
            return False
        else:
            return True

    def next_node(self):

        if len(self.nodes) > 0:
            self.nodes.pop(0)

        if len(self.nodes) > 0:
            self.value = self.nodes[0]
        else:
            self.value = None
