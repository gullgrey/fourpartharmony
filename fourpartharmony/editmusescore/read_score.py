from measure_chord import MeasureRest, MeasureChord


class ReadScore:

    def __init__(self, file_name):

        self.file_name = file_name

        self.lines = None
        self.tag_values = []
        self.subtitle = ''
        self.anacrusis = None
        self.key_sig = '0'

        self.time_sig_common = None
        self.time_sig_numerator = None
        self.time_sig_denominator = None

        self.time_sig_value = None

        self.measure_values = []
        self.measure_chords = []

        self.current_note_value = None
        self.rest_flag = False
        self.chord_flag = False

        self._create_lines()
        self._collect_data()

    def _create_lines(self):

        file = open(self.file_name, "r")
        self.lines = file.read().splitlines()
        file.close()

    @staticmethod
    def _extract_value(line, tag_start, tag_end):
        return line[len(tag_start):-len(tag_end)]

    def _extract_duration(self, line):
        if line.startswith('<dots>'):
            self.current_note_value.dots = self._extract_value(line, '<dots>', '</dots>')
        elif line.startswith('<durationType>'):
            duration = self._extract_value(line, '<durationType>', '</durationType>')
            self.current_note_value.duration = duration
            self.current_note_value.set_note_length(self.time_sig_value)
            self.rest_flag = False

    def _extract_pitch(self, line):

        if line.startswith('<text>'):
            self.current_note_value.lyric = self._extract_value(line, '<text>', '</text>')
        elif line.startswith('<subtype>'):
            self.current_note_value.accidental = self._extract_value(line, '<subtype>', '</subtype>')
        elif line.startswith('<pitch>'):
            self.current_note_value.soprano_pitch = self._extract_value(line, '<pitch>', '</pitch>')
        elif line.startswith('<tpc>'):
            self.current_note_value.soprano_tpc = self._extract_value(line, '<tpc>', '</tpc>')
            self.chord_flag = False

    def _set_time_sig(self):

        numerator = int(self.time_sig_numerator)
        denominator = int(self.time_sig_denominator)
        self.time_sig_value = numerator / denominator

    def _collect_data(self):

        tag_names = ["arranger", "composer", "copyright", "creationDate", "lyricist",
                     "movementNumber", "movementTitle", "platform", "poet",
                     "source", "translator", "workNumber", "workTitle"]
        meta_tag_start = '<metaTag name="{}">'
        meta_tag_end = '</metaTag>'

        subtitle_flag = False
        key_sig_flag = False
        time_sig_flag = False
        staff_flag = False

        for line in self.lines:

            line = line.strip()

            if line.startswith('<metaTag'):
                for name in tag_names:
                    if line.startswith(meta_tag_start.format(name)):
                        tag_value = line[len(meta_tag_start.format(name)):-len(meta_tag_end)]
                        self.tag_values.append(tag_value)

            if line.startswith('<style>Subtitle'):
                subtitle_flag = True

            if subtitle_flag and line.startswith('<text>'):
                self.subtitle = self._extract_value(line, '<text>', '</text>')
                subtitle_flag = False

            if line.startswith('<Measure len'):
                self.anacrusis = self._extract_value(line, '<Measure len="', '">')

            if line.startswith('<KeySig>'):
                key_sig_flag = True

            if key_sig_flag and line.startswith('<accidental>'):
                self.key_sig = self._extract_value(line, '<accidental>', '</accidental>')
                key_sig_flag = False

            if line.startswith('<TimeSig>'):
                time_sig_flag = True
                staff_flag = True

            if time_sig_flag:
                if line.startswith('<subtype>'):
                    self.time_sig_common = self._extract_value(line, '<subtype>', '</subtype>')
                elif line.startswith('<sigN>'):
                    self.time_sig_numerator = self._extract_value(line, '<sigN>', '</sigN>')
                elif line.startswith('<sigD>'):
                    self.time_sig_denominator = self._extract_value(line, '<sigD>', '</sigD>')
                    self._set_time_sig()
                    time_sig_flag = False

            if line.startswith('<Rest>'):
                self.rest_flag = True
                self.current_note_value = MeasureRest()

            if self.rest_flag:
                self._extract_duration(line)
                if not self.rest_flag:
                    self.measure_values.append(self.current_note_value)

            if line.startswith('<Chord>'):
                self.chord_flag = True
                self.current_note_value = MeasureChord()

            if self.chord_flag:
                self._extract_duration(line)
                self._extract_pitch(line)
                if not self.chord_flag:
                    self.measure_values.append(self.current_note_value)
                    self.measure_chords.append(self.current_note_value)

            if staff_flag and line.startswith('</Staff>'):
                break

        self.current_note_value = None
        self.lines = None
