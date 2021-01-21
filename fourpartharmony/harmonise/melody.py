from harmonise_exceptions import SopranoRangeError, HarmonisationError, EmptyMelodyError


class Melody:

    def __init__(self, soprano_list, key):
        """

        :param soprano_list:
        :param key: A tuple of 2 values -->
            key[0] is an int where 0 <= key <= 6. It represents the natural of the tonic note of the key
                0 --> C
                1 --> D
                2 --> E
                3 --> F
                4 --> G
                5 --> A
                6 --> B
            key[1] is a boolean. It represents whether the key is major (False) or minor (True).
            **NOTE: Whether the key is sharp, flat or natural is irrelevant to the operation of the harmonisation.
        """
        # Voice Ranges
        self.bass_lower = -11
        self.bass_upper = 0
        self.tenor_lower = -7
        self.tenor_upper = 4
        self.alto_lower = -3
        self.alto_upper = 7
        self.soprano_lower = 0
        self.soprano_upper = 11

        # Use kwargs to set voice ranges

        self.soprano_list = soprano_list

        self.soprano_list_check()

        self.tonic = key[0]
        self.super_tonic = (key[0] + Interval.second) % Interval.octave
        self.mediant = (key[0] + Interval.third) % Interval.octave
        self.subdominant = (key[0] + Interval.forth) % Interval.octave
        self.dominant = (key[0] + Interval.fifth) % Interval.octave
        self.submediant = (key[0] + Interval.sixth) % Interval.octave
        self.leading_note = (key[0] + Interval.seventh) % Interval.octave

        self.is_minor = key[1]

        self.current_position = -1
        self.current_soprano = None
        self.prev_soprano = None
        self.future_soprano = None
        self.is_penultimate_note = False
        self.is_final_note = False

        self.chord_notes = self.chord_construction()

    def soprano_list_check(self):

        if len(self.soprano_list) == 0:
            raise EmptyMelodyError('Melody contains no notes.')

        for note in self.soprano_list:
            if self.soprano_lower <= note <= self.soprano_upper:
                pass
            else:
                raise SopranoRangeError('Melody is out of soprano range.')

    def chord_construction(self):
        scale = []
        scale_start = 0

        while scale_start < Interval.octave:
            note = (self.tonic + scale_start) % Interval.octave
            chord_third = (note + Interval.third) % Interval.octave
            chord_fifth = (note + Interval.fifth) % Interval.octave
            triad = [note, chord_third, chord_fifth]
            scale.append(triad)
            scale_start += 1

        chord_notes = {
            'I': scale[0],
            'II': scale[1],
            'III': scale[2],
            'IV': scale[3],
            'V': scale[4],
            'VI': scale[5],
            'VII': scale[6],
            'V7': scale[4]+[self.subdominant]
        }
        return chord_notes

    def first_note(self):
        return self.soprano_list[0]

    def next_note(self):

        if self.current_soprano is not None:
            self.prev_soprano = self.soprano_list[self.current_position]

        self.current_position += 1
        self.current_soprano = self.soprano_list[self.current_position]

        self._set_final_note_checks()

        if self.is_final_note is False:
            self.future_soprano = self.soprano_list[self.current_position + 1]
        else:
            self.future_soprano = None

        return self.current_soprano

    def prev_note(self):

        self.current_position -= 1
        if self.current_position < 0:
            raise HarmonisationError('Unable to harmonise current melody.')

        self.current_soprano = self.soprano_list[self.current_position]

        if self.current_position > 0:
            self.prev_soprano = self.soprano_list[self.current_position - 1]

        self._set_final_note_checks()

        if self.is_final_note is False:
            self.future_soprano = self.soprano_list[self.current_position + 1]
        else:
            self.future_soprano = None

        return self.current_soprano

    def _set_final_note_checks(self):

        melody_length = len(self.soprano_list)
        if melody_length - self.current_position == 2:
            self.is_penultimate_note = True
        else:
            self.is_penultimate_note = False
        if melody_length - self.current_position == 1:
            self.is_final_note = True
        else:
            self.is_final_note = False

    def reset_position(self):

        self.current_position = -1
        self.current_soprano = None
        self.prev_soprano = None
        self.future_soprano = None
        self.is_penultimate_note = False
        self.is_final_note = False

    def _in_range(self, note_int, voice):

        if voice == 'soprano':
            if self.soprano_upper >= note_int >= self.soprano_lower:
                return True
            else:
                return False
        elif voice == 'alto':
            if self.alto_upper >= note_int >= self.alto_lower:
                return True
            else:
                return False
        elif voice == 'tenor':
            if self.tenor_upper >= note_int >= self.tenor_lower:
                return True
            else:
                return False
        elif voice == 'bass':
            if self.bass_upper >= note_int >= self.bass_lower:
                return True
            else:
                return False
        else:
            return False

    def in_soprano_range(self, note_int):
        return self._in_range(note_int, 'soprano')

    def in_alto_range(self, note_int):
        return self._in_range(note_int, 'alto')

    def in_tenor_range(self, note_int):
        return self._in_range(note_int, 'tenor')

    def in_bass_range(self, note_int):
        return self._in_range(note_int, 'bass')


class Interval:

    unison = 0
    second = 1
    third = 2
    forth = 3
    fifth = 4
    sixth = 5
    seventh = 6
    octave = 7

    @staticmethod
    def invalid_consecutives(prev_higher, prev_lower, higher, lower):
        """

        :param prev_higher: The highest note value of the previous chord.
        :param prev_lower: The lowest note value of the previous chord.
        :param higher: The highest note value of the current chord.
        :param lower: The lowest note value of the current chord.
        :return: True if consecutive fifth or octave is found. False if not.
        """
        if prev_higher is None or prev_lower is None:
            return False

        if prev_higher == higher and prev_lower == lower:
            return False

        prev_interval = (prev_higher - prev_lower) % Interval.octave
        new_interval = (higher - lower) % Interval.octave
        voice_unison = False
        if (prev_higher - prev_lower == Interval.unison
                or higher - lower == Interval.unison):
            voice_unison = True

        if (prev_interval == Interval.fifth
                and new_interval == Interval.fifth):
            return True

        elif (prev_interval == Interval.unison
              and new_interval == Interval.unison
              and voice_unison is False):
            return True

        else:
            return False

    @staticmethod
    def note_letter(note):

        abs_note = note % Interval.octave
        if abs_note > Interval.fifth:
            letter_value = 60
        else:
            letter_value = 67

        return chr(letter_value + abs_note)
