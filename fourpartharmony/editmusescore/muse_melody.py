from note_conversions import NoteConversions


class MuseMelody:

    def __init__(self, minor, key_sig, measure_chords):

        self.minor = minor
        self.key_sig = key_sig
        self.measure_chords = measure_chords

        self.key = [None, minor]

        self.soprano_list = []

        self._set_key()
        self._create_soprano_list()

    def _set_key(self):

        if self.minor:
            minor_key = NoteConversions.minor_keys[self.key_sig]
            self.key[0] = NoteConversions.note_letter_values[minor_key]
        else:
            major_key = NoteConversions.major_keys[self.key_sig]
            self.key[0] = NoteConversions.note_letter_values[major_key]

    def _create_soprano_list(self):

        c_double_flat = 70
        g_note = 4

        for chord in self.measure_chords:

            tpc_natural = (int(chord.soprano_tpc) + 1) % NoteConversions.scale_length
            soprano_note = NoteConversions.tpc_to_scale[tpc_natural]

            pitch = int(chord.soprano_pitch)
            if soprano_note <= g_note and pitch >= c_double_flat:
                soprano_note = soprano_note + NoteConversions.scale_length

            self.soprano_list.append(soprano_note)

