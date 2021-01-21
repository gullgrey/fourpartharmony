from write_score import WriteScore
from mscx import Mscx


class WriteThreePart(WriteScore):

    def __init__(self, read_score, instrument, melody_position):
        self.melody_position = melody_position
        super().__init__(read_score, instrument)

    def _get_soprano_values(self):

        accidental_lines = None

        self._chord_values_start()

        note_values = [self.current_note.soprano_pitch, self.current_note.soprano_tpc]
        if self.current_note.accidental is not None:
            accidental_lines = Mscx.note_accidental.format(self.current_note.accidental)
        note_lines = Mscx.note.format(*note_values)

        self._write_voices(accidental_lines, note_lines)

    def _write_lines(self):

        voice_1 = '1'
        voice_2 = '2'
        voice_3 = '3'

        # If the melody is in Staff 1
        voice_order = ['soprano', 'alto', 'tenor']

        if self.melody_position == 'Staff 2':
            voice_order = ['alto', 'soprano', 'tenor']
        elif self.melody_position == 'Staff 3':
            voice_order = ['alto', 'tenor', 'soprano']

        self.file.write(Mscx.beginning)

        tags = Mscx.meta_tags.format(*self.read_score.tag_values)
        self.file.write(tags)

        if self.instrument == 'Piano':
            self.file.write(Mscx.three_piano_parts)
        # if instrument is Choir
        else:
            self.file.write(Mscx.three_choir_parts)

        self.file.write(Mscx.staff_start.format(voice_1))
        self._vbox()
        self._measure_start()
        self._write_key_sig()
        self._write_time_sig()
        self.file.write(Mscx.tempo)
        self._write_staff(voice_order[0])

        self.file.write(Mscx.staff_start.format(voice_2))
        self._measure_start()
        self._write_key_sig()
        self._write_time_sig()
        self._write_staff(voice_order[1])

        self.file.write(Mscx.staff_start.format(voice_3))
        self._measure_start()
        self._write_key_sig()
        self._write_time_sig()
        self._write_staff(voice_order[2])

        self.file.write(Mscx.end)
