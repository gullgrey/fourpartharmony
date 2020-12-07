from fractions import Fraction
from mscx import Mscx
from measure_chord import MeasureRest


class WriteScore:

    def __init__(self, read_score, instrument):

        self.read_score = read_score
        self.instrument = instrument
        self.file_name = None
        self.file = None

        self.measure_length = read_score.time_sig_value
        self.anacrusis_length = None

        self.measure_used = 0
        self.anacrusis_used = 0
        self.anacrusis_flag = False
        self.new_measure = False

        self.prev_leading_notes = []

        self._open_file()
        self._set_anacrusis_length()

        self._write_lines()

        self._close_file()

    def _open_file(self):
        file_type = ".mscx"
        self.file_name = self.read_score.file_name[:-len(file_type)] + " Harmonised" + file_type
        self.file = open(self.file_name, "w")

    def _set_anacrusis_length(self):
        if self.read_score.anacrusis is not None:
            self.anacrusis_length = Fraction(self.read_score.anacrusis)

    def _vbox(self):

        title_position = 12
        composer_position = 1
        lyricist_position = 4
        title = self.read_score.tag_values[title_position]
        composer = self.read_score.tag_values[composer_position]
        lyricist = self.read_score.tag_values[lyricist_position]
        subtitle = self.read_score.subtitle
        if (title != '' or composer != '' or
                lyricist != '' or subtitle != ''):
            vbox = Mscx.vbox.format(title, subtitle, composer, lyricist)
            self.file.write(vbox)

    def _measure_start(self):

        if self.read_score.anacrusis is not None:
            anacrusis_lines = Mscx.anacrusis.format(self.read_score.anacrusis)
            self.file.write(anacrusis_lines)
        else:
            self.file.write(Mscx.measure_start)

    def _write_key_sig(self):

        if self.read_score.key_sig != '0':
            key_lines = Mscx.key_sig.format(self.read_score.key_sig)
            self.file.write(key_lines)

    def _write_time_sig(self):

        if self.read_score.time_sig_common is not None:
            time_sig_list = [self.read_score.time_sig_common,
                             self.read_score.time_sig_numerator,
                             self.read_score.time_sig_denominator]
            time_sig_lines = Mscx.time_sig_common.format(*time_sig_list)

        else:
            time_sig_list = [self.read_score.time_sig_numerator,
                             self.read_score.time_sig_denominator]
            time_sig_lines = Mscx.time_sig.format(*time_sig_list)

        self.file.write(time_sig_lines)

    def _write_rest(self, note):

        if note.duration == 'measure':
            time_sig_string = (self.read_score.time_sig_numerator +
                               '/' + self.read_score.time_sig_denominator)
            rest_lines = Mscx.measure_rest.format(time_sig_string)
        else:
            rest_lines = Mscx.rest.format(note.duration)
        self.file.write(rest_lines)

    def _chord_lyric_start(self, note):

        chord_start = Mscx.chord_start.format(note.duration)
        self.file.write(chord_start)

        if note.lyric is not None:
            lyric_lines = Mscx.lyric.format(note.lyric)
            self.file.write(lyric_lines)

    def _write_soprano(self, note):

        harmony_lines = Mscx.harmony.format(note.chord)
        self.file.write(harmony_lines)

        self._chord_lyric_start(note)

        note_values = [note.soprano_pitch, note.soprano_tpc]
        if note.accidental is None:
            note_lines = Mscx.note.format(*note_values)
        else:
            note_lines = Mscx.note_accidental.format(note.accidental,
                                                     *note_values)

        self.file.write(note_lines)
        self.file.write(Mscx.chord_end)

    def _write_voice(self, note, voice):

        leading_note_flag = False
        pitch_number = None
        tpc_number = None

        self._chord_lyric_start(note)

        if voice == 'alto':
            note_values = [note.alto_pitch, note.alto_tpc]
            if note.alto_leading_note:
                leading_note_flag = True
                pitch_number = int(note.alto_pitch)
                tpc_number = int(note.alto_tpc)
        elif voice == 'tenor':
            note_values = [note.tenor_pitch, note.tenor_tpc]
            if note.tenor_leading_note:
                leading_note_flag = True
                pitch_number = int(note.tenor_pitch)
                tpc_number = int(note.tenor_tpc)
        else:
            note_values = [note.bass_pitch, note.bass_tpc]
            if note.bass_leading_note:
                leading_note_flag = True
                pitch_number = int(note.bass_pitch)
                tpc_number = int(note.bass_tpc)

        if leading_note_flag and pitch_number not in self.prev_leading_notes:
            max_flat_tpc = 12
            if tpc_number > max_flat_tpc:
                accidental_value = 'accidentalSharp'
            else:
                accidental_value = 'accidentalNatural'
            note_lines = Mscx.note_accidental.format(accidental_value,
                                                     *note_values)
            self.prev_leading_notes.append(pitch_number)
        else:
            note_lines = Mscx.note.format(*note_values)

        self.file.write(note_lines)
        self.file.write(Mscx.chord_end)

    def _measure_end(self):

        if self.anacrusis_used == self.anacrusis_length:
            self.file.write(Mscx.measure_end)
            self.anacrusis_flag = False
            self.anacrusis_used = 0
            self.new_measure = True
            self.prev_leading_notes.clear()
        elif self.measure_used == self.measure_length:
            self.file.write(Mscx.measure_end)
            self.measure_used = 0
            self.new_measure = True
            self.prev_leading_notes.clear()

    def _write_staff(self, voice):

        if self.anacrusis_length is not None:
            self.anacrusis_flag = True

        for note in self.read_score.measure_values:

            if self.new_measure:
                self.file.write(Mscx.measure_start)
                self.new_measure = False

            if self.anacrusis_flag:
                self.anacrusis_used += note.note_length
            else:
                self.measure_used += note.note_length

            if type(note) is MeasureRest:
                self._write_rest(note)
            else:
                if voice == 'soprano':
                    self._write_soprano(note)
                else:
                    self._write_voice(note, voice)

            self._measure_end()

        self.file.write(Mscx.staff_end)
        self.new_measure = False

    def _write_lines(self):

        soprano = '1'
        alto = '2'
        tenor = '3'
        bass = '4'

        self.file.write(Mscx.beginning)

        tags = Mscx.meta_tags.format(*self.read_score.tag_values)
        self.file.write(tags)

        if self.instrument == 'Piano':
            self.file.write(Mscx.four_piano_parts)
        # if instrument is Choir
        else:
            self.file.write(Mscx.four_choir_parts)

        self.file.write(Mscx.staff_start.format(soprano))
        self._vbox()
        self._measure_start()
        self._write_key_sig()
        self._write_time_sig()
        self.file.write(Mscx.tempo)
        self._write_staff('soprano')

        self.file.write(Mscx.staff_start.format(alto))
        self._measure_start()
        self._write_key_sig()
        self._write_time_sig()
        self._write_staff('alto')

        self.file.write(Mscx.staff_start.format(tenor))
        self._measure_start()
        self.file.write(Mscx.bass_clef)
        self._write_key_sig()
        self._write_time_sig()
        self._write_staff('tenor')

        self.file.write(Mscx.staff_start.format(bass))
        self._measure_start()
        self._write_key_sig()
        self._write_time_sig()
        self._write_staff('bass')

        self.file.write(Mscx.end)

    def _close_file(self):
        self.file.close()
