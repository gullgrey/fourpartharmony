from random import shuffle, random
from harmonise_exceptions import EmptyNodeError
from melody import Interval


class Chord:

    def __init__(self, current_note):

        self.melody = current_note.melody
        self.chord_notes = self.melody.chord_notes

        self.soprano = current_note.soprano
        self.prev_soprano = current_note.prev_soprano

        self.is_second_note = current_note.is_second_note
        self.is_penultimate_note = current_note.is_penultimate_note
        self.is_final_note = current_note.is_final_note

        self._third_apart = False
        self.lenient_rules = current_note.lenient_rules

        # Keeps track of number of chords removed from nodes.
        # Used for final cadences.
        self.cadence_nodes_empty = True
        self.perfect_attempt_failed = False

        self.nodes = []
        self.cadence_nodes = []
        self.value = None

        self._chord_setup(current_note)

    def _chord_setup(self, current_note):

        if current_note.is_first_note is False:
            self.prev_chord = current_note.prev_chord.value
            self.prev_bass = current_note.prev_bass.value
            if self.is_second_note is False:
                self.prev_prev_chord = current_note.prev_prev_chord.value

        if self.prev_soprano is not None:
            if abs(self.soprano - self.prev_soprano) == Interval.third:
                self._third_apart = True

        if current_note.is_first_note:
            self.first_chord()
        elif self.is_final_note:
            self.perfect_attempt_failed = current_note.prev_chord.perfect_attempt_failed
            self.cadence_nodes_empty = current_note.prev_chord.cadence_nodes_empty
            self.final_chord()
        else:
            self.new_chord()

        self.nodes = self.remove_invalid_chords(self.nodes)
        if self.is_penultimate_note:
            self.penultimate_chord()

        if len(self.cadence_nodes) > 0:
            self.value = self.cadence_nodes[0]

        elif len(self.nodes) > 0:
            self.value = self.nodes[0]

    def first_chord(self):
        self.nodes.append('I')
        second_priority = ['V', 'V7']
        shuffle(second_priority)
        self.nodes += second_priority
        third_priority = ['IV', 'II']
        self.nodes += third_priority

    def new_chord(self):
        roman = self.prev_chord
        if roman == 'I':
            self._tonic_progression()
        elif roman == 'II':
            self._supertonic_progression()
        elif roman == 'III':
            self._mediant_progression()
        elif roman == 'IV':
            self._subdominant_progression()
        elif roman == 'V':
            self._dominant_progression()
        elif roman == 'VI':
            self._submediant_progression()
        elif roman == 'VII':
            self._leading_note_progression()
        elif roman == 'V7':
            self._dominant_7_progression()
        else:
            raise EmptyNodeError("Previous chord value is None or invalid.")

    def _tonic_progression(self):

        # Checks if previous chord is Ic then sets nodes to contain just chord V.
        abs_prev_bass = self.prev_bass % Interval.octave
        if (abs_prev_bass == self.chord_notes['I'][2]
                and self.is_second_note is False):

            # If chord progression went IV, Ic then set IV as first priority.
            if self.prev_prev_chord == 'IV':
                self.nodes.append('IV')
            self.nodes.append('V')
            return

        self.nodes.append('V')
        second_priority = ['II', 'III', 'IV', 'VI', 'V7']
        shuffle(second_priority)
        self.nodes += second_priority

        # This sets repeating chord I as a priority if sopranos are a 3rd apart.
        if self._third_apart:
            self.nodes.insert(0, 'I')
        else:
            self.nodes.append('I')

        # This sets chord VII and V as a priority if sopranos are a 2nd apart.
        if self.prev_soprano is not None:
            if abs(self.soprano - self.prev_soprano) == Interval.second:
                self.nodes.insert(0, 'VII')

                if random() < 0.5:
                    self.nodes.remove('V')
                    self.nodes.insert(0, 'V')

    def _supertonic_progression(self):

        self.nodes.append('V')

        second_priority = ['VII', 'V7']
        shuffle(second_priority)
        self.nodes += second_priority

        third_priority = ['III', 'I']
        shuffle(third_priority)
        self.nodes += third_priority

        # This sets repeating chord II as a priority if sopranos are a 3rd apart.
        if self._third_apart:
            self.nodes.insert(0, 'II')
        else:
            self.nodes.append('II')

    def _mediant_progression(self):

        first_priority = ['I', 'IV', 'VI']
        shuffle(first_priority)
        self.nodes += first_priority

        abs_soprano = self.soprano % Interval.octave
        abs_prev_soprano = self.prev_soprano % Interval.octave
        if abs_prev_soprano == abs_soprano == self.melody.leading_note:
            self.nodes.append('V')

    def _subdominant_progression(self):

        # Checks if previous chord is IVc then sets nodes to contain just chord I.
        abs_prev_bass = self.prev_bass % Interval.octave
        if abs_prev_bass == self.chord_notes['IV'][2]:
            self.nodes.append('I')
            return

        # First priority is shuffled unless second note where a plagal cadence is prioritised.
        first_priority = ['I', 'V']
        if self.is_second_note:
            self.nodes += first_priority
        else:
            shuffle(first_priority)
            self.nodes += first_priority

        second_priority = ['II', 'VII', 'V7']
        shuffle(second_priority)
        self.nodes += second_priority

        # This sets repeating chord IV as a priority if sopranos are a 3rd apart.
        # The exception is if it is the second note, in which case a cadence should be prioritised.
        if self.is_second_note:
            self.nodes.append('IV')
        elif self._third_apart:
            new_position = 2
            self.nodes.insert(new_position, 'IV')
        else:
            self.nodes.append('IV')

    def _dominant_progression(self):
        self.nodes.append('VI')

        # Prioritises a perfect cadence on second note of melody.
        # Otherwise prioritises an interrupted cadence.
        if self.is_second_note:
            self.nodes.insert(0, 'I')
        else:
            self.nodes.append('I')

        self.nodes.append('IV')
        if self.lenient_rules:
            third_priority = ['V', 'III', 'II']
            self.nodes += third_priority

    def _submediant_progression(self):

        first_priority = ['II', 'IV', 'V', 'V7']
        shuffle(first_priority)
        self.nodes += first_priority

        # This sets repeating chord VI as a priority if sopranos are a 3rd apart.
        if self._third_apart:
            self.nodes.insert(0, 'VI')
        else:
            self.nodes.append('VI')

    def _leading_note_progression(self):

        self.nodes.append('I')

    def _dominant_7_progression(self):

        # Prioritises a perfect cadence on second note of melody.
        first_priority = ['I', 'VI']
        if self.is_second_note:
            self.nodes += first_priority
        else:
            shuffle(first_priority)
            self.nodes += first_priority

    def remove_invalid_chords(self, nodes):

        # creates a list of chord values that should be removed from Chord.nodes
        invalid_chords = []
        abs_soprano = self.soprano % Interval.octave
        for value in nodes:
            if abs_soprano not in self.chord_notes[value]:
                invalid_chords.append(value)

        if self.melody.is_minor and abs_soprano == self.melody.leading_note:
            invalid_chords.append('III')

        # Removes all chord values in Chord.nodes that are in invalid chords
        nodes = [value for value in nodes if value not in invalid_chords]
        return nodes

    def penultimate_chord(self):

        cadence_values = ['V', 'V7', 'IV', 'V', 'I']
        self.cadence_nodes = self.remove_invalid_chords(cadence_values)

        if len(self.cadence_nodes) > 0:
            self.cadence_nodes_empty = False

    def final_chord(self):

        if self.cadence_nodes_empty:
            self.new_chord()
            return
        if self.prev_chord == 'I':
            self.nodes.append('V')
            return

        if self.prev_chord == 'V' and self.perfect_attempt_failed:
            self.nodes.append('VI')
        else:
            self.nodes.append('I')

    def next_node(self):

        if len(self.cadence_nodes) > 0:
            self.cadence_nodes.pop(0)
            self.perfect_attempt_failed = True
        elif len(self.nodes) > 0:
            self.nodes.pop(0)

        if len(self.cadence_nodes) > 0:
            self.value = self.cadence_nodes[0]
        elif len(self.nodes) > 0:
            self.value = self.nodes[0]
        else:
            self.value = None

        if len(self.cadence_nodes) == 0:
            self.cadence_nodes_empty = True
