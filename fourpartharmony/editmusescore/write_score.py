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

        self.current_note = None

        self.tuplet = None
        self.tuplet_flag = False
        self.tuplet_used = 0

        self.prev_leading_notes = []

        self._open_file()
        self._set_anacrusis_length()

        self._write_lines()

        self._close_file()

    def _open_file(self):
        file_type = ".mscx"
        file_end = " Harmonised"
        self.file_name = self.read_score.file_name[:-len(file_type)] + file_end + file_type
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

    def _write_tuplet(self):

        self.tuplet = self.current_note.tuplet
        tuplet_values = [self.tuplet.normal_notes, self.tuplet.actual_notes,
                         self.tuplet.base_note, self.tuplet.actual_notes]
        tuplet_lines = Mscx.tuplet.format(*tuplet_values)

        self.file.write(tuplet_lines)

        self.tuplet_flag = True
        self.tuplet_used = 0

    def _write_rest(self):

        if self.current_note.duration == 'measure':
            time_sig_string = (self.read_score.time_sig_numerator +
                               '/' + self.read_score.time_sig_denominator)
            rest_lines = Mscx.measure_rest.format(time_sig_string)

        else:
            if self.current_note.dots == '0':
                rest_lines = Mscx.rest.format(self.current_note.duration)
            else:
                rest_lines = Mscx.rest_dots.format(self.current_note.dots, self.current_note.duration)

        self.file.write(rest_lines)

    def _chord_values_start(self):

        self.file.write(Mscx.chord_start)

        if self.current_note.dots != '0':
            dots = Mscx.dots.format(self.current_note.dots)
            self.file.write(dots)

        duration_start = Mscx.duration_start.format(self.current_note.duration)
        self.file.write(duration_start)

        if self.current_note.lyric is not None:
            lyric_lines = Mscx.lyric.format(self.current_note.lyric)
            self.file.write(lyric_lines)

        if self.current_note.articulation is not None:
            articulation_lines = Mscx.articulation.format(self.current_note.articulation)
            self.file.write(articulation_lines)

    def _write_ties(self):

        if self.current_note.tie_start:
            self.file.write(Mscx.tie_next_start)
            if self.current_note.tie_start_measures is not None:
                measures = Mscx.tie_measures.format(self.current_note.tie_start_measures)
                self.file.write(measures)
            if self.current_note.tie_start_fractions is not None:
                fractions = Mscx.tie_fractions.format(self.current_note.tie_start_fractions)
                self.file.write(fractions)
            self.file.write(Mscx.tie_next_end)

        if self.current_note.tie_end:
            self.file.write(Mscx.tie_prev_start)
            if self.current_note.tie_end_measures is not None:
                measures = Mscx.tie_measures.format(self.current_note.tie_end_measures)
                self.file.write(measures)
            if self.current_note.tie_end_fractions is not None:
                fractions = Mscx.tie_fractions.format(self.current_note.tie_end_fractions)
                self.file.write(fractions)
            self.file.write(Mscx.tie_prev_end)

    def _write_voices(self, accidental_lines, note_lines):

        self.file.write(Mscx.note_start)
        if accidental_lines is not None:
            self.file.write(accidental_lines)
        self._write_ties()
        self.file.write(note_lines)
        self.file.write(Mscx.chord_end)

    def _get_soprano_values(self):

        accidental_lines = None

        harmony_lines = Mscx.harmony.format(self.current_note.chord)
        self.file.write(harmony_lines)

        self._chord_values_start()

        note_values = [self.current_note.soprano_pitch, self.current_note.soprano_tpc]
        if self.current_note.accidental is not None:
            accidental_lines = Mscx.note_accidental.format(self.current_note.accidental)
        note_lines = Mscx.note.format(*note_values)

        self._write_voices(accidental_lines, note_lines)

    def _get_voice_values(self, voice):

        leading_note_flag = False
        pitch_number = None
        tpc_number = None
        accidental_lines = None

        self._chord_values_start()

        if voice == 'alto':
            note_values = [self.current_note.alto_pitch, self.current_note.alto_tpc]
            if self.current_note.alto_leading_note:
                leading_note_flag = True
                pitch_number = int(self.current_note.alto_pitch)
                tpc_number = int(self.current_note.alto_tpc)
        elif voice == 'tenor':
            note_values = [self.current_note.tenor_pitch, self.current_note.tenor_tpc]
            if self.current_note.tenor_leading_note:
                leading_note_flag = True
                pitch_number = int(self.current_note.tenor_pitch)
                tpc_number = int(self.current_note.tenor_tpc)
        else:
            note_values = [self.current_note.bass_pitch, self.current_note.bass_tpc]
            if self.current_note.bass_leading_note:
                leading_note_flag = True
                pitch_number = int(self.current_note.bass_pitch)
                tpc_number = int(self.current_note.bass_tpc)

        if leading_note_flag and pitch_number not in self.prev_leading_notes:
            max_flat_tpc = 12
            if tpc_number > max_flat_tpc:
                accidental_value = 'accidentalSharp'
            else:
                accidental_value = 'accidentalNatural'
            accidental_lines = Mscx.note_accidental.format(accidental_value)
            self.prev_leading_notes.append(pitch_number)

        note_lines = Mscx.note.format(*note_values)

        self._write_voices(accidental_lines, note_lines)

    def _update_note_counters(self):

        if self.anacrusis_flag:
            if self.tuplet_flag:
                self.tuplet_used += self.current_note.note_length
                if self.tuplet_used == self.tuplet.actual_length:
                    self.anacrusis_used += self.tuplet.normal_length
                    self.tuplet_flag = False
                    self.tuplet_used = 0
                    self.file.write(Mscx.tuplet_end)
            else:
                self.anacrusis_used += self.current_note.note_length
        else:
            if self.tuplet_flag:
                self.tuplet_used += self.current_note.note_length
                if self.tuplet_used == self.tuplet.actual_length:
                    self.measure_used += self.tuplet.normal_length
                    self.tuplet_flag = False
                    self.tuplet_used = 0
                    self.file.write(Mscx.tuplet_end)
            else:
                self.measure_used += self.current_note.note_length

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

            self.current_note = note

            if self.new_measure:
                self.file.write(Mscx.measure_start)
                self.new_measure = False

            if self.current_note.tuplet is not None:
                self._write_tuplet()

            if type(self.current_note) is MeasureRest:
                self._write_rest()
            else:

                if voice == 'soprano':
                    self._get_soprano_values()
                else:
                    self._get_voice_values(voice)

            self._update_note_counters()

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
