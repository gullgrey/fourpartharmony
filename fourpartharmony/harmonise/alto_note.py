from random import shuffle
from statistics import mean

from harmonise_exceptions import EmptyNodeError
from melody import Interval


class AltoNote:

    def __init__(self, current_note):

        self.melody = current_note.melody
        self.chord_notes = self.melody.chord_notes

        self.soprano = current_note.soprano
        self.prev_soprano = current_note.prev_soprano

        self.chord = current_note.chord.value
        self.prev_chord = None

        self.bass = current_note.bass.value
        self.prev_bass = None

        self.tenor = current_note.tenor.value
        self.prev_tenor = None
        self.prev_alto = None

        self.is_first_note = current_note.is_first_note

        self.potential_degrees = list(current_note.tenor.potential_degrees)

        self.nodes = []
        self.value = None

        self._alto_note_setup(current_note)

    def _alto_note_setup(self, current_note):

        if self.chord is None:
            raise EmptyNodeError('No chord found during alto note setup.')
        elif self.bass is None:
            raise EmptyNodeError('No bass note found during alto note setup.')
        elif self.tenor is None:
            raise EmptyNodeError('No tenor note found during alto note setup.')

        if self.is_first_note is False:
            self.prev_chord = current_note.prev_chord.value
            self.prev_bass = current_note.prev_bass.value
            self.prev_tenor = current_note.prev_tenor.value
            self.prev_alto = current_note.prev_alto.value

        self._degree_setup()

        if self.is_first_note:
            self._first_alto_note()
        else:
            self._new_alto_note()

        if len(self.nodes) > 0:
            self.value = self.nodes[0]

    def _degree_setup(self):

        abs_tenor = self.tenor % Interval.octave
        abs_soprano = self.soprano % Interval.octave
        abs_bass = self.bass % Interval.octave
        other_voices = [abs_soprano, abs_tenor, abs_bass]
        other_voices.sort()

        triad = self.chord_notes[self.chord]
        chord_root = triad[0]
        chord_third = triad[1]
        chord_fifth = triad[2]

        self.potential_degrees.remove(abs_tenor)

        if self.chord == 'V7':

            if (abs_tenor == abs_soprano
                    or abs_tenor == abs_bass
                    or abs_soprano == abs_bass):
                if chord_fifth in self.potential_degrees:
                    self.potential_degrees.remove(chord_fifth)

        elif self.chord in ['III', 'I']:

            if other_voices == [chord_root, chord_root, chord_root]:
                self.potential_degrees = [chord_third]

            elif other_voices == [chord_root, chord_root, chord_third]:
                self.potential_degrees = [chord_root, chord_fifth]

            elif other_voices == [chord_root, chord_third, chord_third]:
                self.potential_degrees = [chord_fifth]

            elif other_voices == [chord_root, chord_root, chord_fifth]:
                self.potential_degrees = [chord_third]

        else:
            if (abs_tenor == abs_soprano
                    or abs_tenor == abs_bass
                    or abs_soprano == abs_bass):
                if abs_tenor in self.potential_degrees:
                    self.potential_degrees.remove(abs_tenor)

                if abs_soprano in self.potential_degrees:
                    self.potential_degrees.remove(abs_soprano)

                if abs_bass in self.potential_degrees:
                    self.potential_degrees.remove(abs_bass)

        # This allows jumps of a seventh to be more readily harmonised by allowing the
        # doubling of the soprano note no matter what.
        if (self.is_first_note is False
                and self.soprano - self.prev_soprano == Interval.seventh):
            self.potential_degrees.append(abs_soprano)

    def _first_alto_note(self):

        middle_note = int(mean([self.soprano, self.tenor]))

        self.nodes.append(middle_note)

        interval_counter = Interval.second
        while interval_counter <= Interval.fifth:
            first_note = middle_note + interval_counter
            self.nodes.append(first_note)
            second_note = middle_note - interval_counter
            self.nodes.append(second_note)
            interval_counter += 1

        self.nodes[:] = [note for note in self.nodes if self._note_is_valid(note)]

    def _new_alto_note(self):

        middle_note = int(mean([self.soprano, self.tenor]))

        alto_direction = -1
        if middle_note >= self.prev_alto:
            alto_direction = 1

        self.nodes.append(self.prev_alto)

        interval_counter = Interval.second
        while interval_counter <= Interval.fifth:
            first_note = self.prev_alto + (interval_counter * alto_direction)
            self.nodes.append(first_note)
            second_note = self.prev_alto - (interval_counter * alto_direction)
            self.nodes.append(second_note)
            interval_counter += 1

        # Sets notes that are equal to tenor or soprano as the last priority.
        for note in self.nodes:
            if note in [self.soprano, self.tenor]:
                self.nodes.remove(note)
                self.nodes.append(note)

        self.nodes[:] = [note for note in self.nodes if self._note_is_valid(note)]

    def _note_is_valid(self, note):

        abs_note = note % Interval.octave

        if self.melody.in_alto_range(note) is False:
            return False

        if note < self.tenor or note > self.soprano:
            return False

        if (self.soprano - note > Interval.octave
                or note - self.tenor > Interval.octave):
            return False

        if self.is_first_note is False:
            abs_prev_alto = self.prev_alto % Interval.octave

            if note < self.prev_tenor or note > self.prev_soprano:
                return False

            if abs_prev_alto == self.melody.leading_note:
                non_tonic_chords = ['V', 'III', 'II']
                if (self.chord not in non_tonic_chords
                        # and self.soprano - self.prev_alto < Interval.octave
                        and abs_note != self.melody.tonic):
                    return False

            if (abs_prev_alto == self.melody.submediant
                    and abs_note == self.melody.leading_note):
                return False

        if Interval.invalid_consecutives(self.prev_soprano, self.prev_alto, self.soprano, note):
            return False
        elif Interval.invalid_consecutives(self.prev_alto, self.prev_tenor, note, self.tenor):
            return False
        elif Interval.invalid_consecutives(self.prev_alto, self.prev_bass, note, self.bass):
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


# class AltoNote:
#
#     def __init__(self, current_note):
#
#         self.soprano = current_note.soprano
#         self.tenor = current_note.tenor.value
#         if self.soprano > self.tenor:
#             self.value_list = list(range(0, 4))
#         else:
#             self.value_list = []
#         shuffle(self.value_list)
#         self.nodes = []
#         self.value = self.value_list[0]
#
#     def next_node(self):
#         if len(self.value_list) > 0:
#             self.value_list.pop(0)
#         if len(self.value_list) > 0:
#             self.value = self.value_list[0]
#         else:
#             self.value = None
