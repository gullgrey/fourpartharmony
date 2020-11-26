
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

        major_keys = {
            '-7': 'C',
            '-6': 'G',
            '-5': 'D',
            '-4': 'A',
            '-3': 'E',
            '-2': 'B',
            '-1': 'F',
            '0': 'C',
            '1': 'G',
            '2': 'D',
            '3': 'A',
            '4': 'E',
            '5': 'B',
            '6': 'F',
            '7': 'C'
        }

        minor_keys = {
            '-7': 'A',
            '-6': 'E',
            '-5': 'B',
            '-4': 'F',
            '-3': 'C',
            '-2': 'G',
            '-1': 'D',
            '0': 'A',
            '1': 'E',
            '2': 'B',
            '3': 'F',
            '4': 'C',
            '5': 'G',
            '6': 'D',
            '7': 'A'
        }

        key_values = {
            'C': 0,
            'D': 1,
            'E': 2,
            'F': 3,
            'G': 4,
            'A': 5,
            'B': 6
        }

        if self.minor:
            self.key[0] = key_values[minor_keys[self.key_sig]]
        else:
            self.key[0] = key_values[major_keys[self.key_sig]]

    def _create_soprano_list(self):

        scale_length = 7
        c_double_flat = 70
        g_note = 4
        tpc_to_scale = {
            0: 3,
            1: 0,
            2: 4,
            3: 1,
            4: 5,
            5: 2,
            6: 6
        }
        for chord in self.measure_chords:

            tpc_natural = (int(chord.soprano_tpc) + 1) % scale_length
            soprano_note = tpc_to_scale[tpc_natural]

            pitch = int(chord.soprano_pitch)
            if soprano_note <= g_note and pitch >= c_double_flat:
                soprano_note = soprano_note + scale_length

            self.soprano_list.append(soprano_note)

