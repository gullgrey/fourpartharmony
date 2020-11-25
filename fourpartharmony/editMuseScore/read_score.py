from fractions import Fraction


class ReadScore:

    def __init__(self, file_name):

        self.lines = None
        self.tag_values = []
        self.anacrusis = None
        self.key_sig = 0
        self.time_sig = None

        self._create_lines(file_name)
        self._collect_data()

    def _create_lines(self, file_name):

        file = open(file_name, "r")
        self.lines = file.read().splitlines()
        file.close()

    def _collect_data(self):

        tag_names = ["arranger", "composer", "copyright", "creationDate", "lyricist",
                     "movementNumber", "movementTitle", "platform", "poet",
                     "source", "translator", "workNumber", "workTitle"]
        tag_start = '<metaTag name="{}">'
        tag_end = '</metaTag>'

        key_sig_flag = False
        time_sig_flag = False

        time_sig_numerator = None

        for line in self.lines:

            line = line.strip()
            # print(line)

            if line.startswith('<metaTag'):
                for name in tag_names:
                    if line.startswith(tag_start.format(name)):
                        tag_value = line[len(tag_start.format(name)):-len(tag_end)]
                        self.tag_values.append(tag_value)

            if line.startswith('<Measure '):
                anacrusis_start = '<Measure len="'
                anacrusis_end = '">'
                anacrusis_value = line[len(anacrusis_start):-len(anacrusis_end)]
                self.anacrusis = float(Fraction(anacrusis_value))

            if line.startswith('<KeySig>'):
                key_sig_flag = True

            if key_sig_flag and line.startswith('<accidental>'):
                key_sig_start = '<accidental>'
                key_sig_end = '</accidental>'
                key_sig_value = line[len(key_sig_start):-len(key_sig_end)]
                self.key_sig = int(key_sig_value)
                key_sig_flag = False

            if line.startswith('<TimeSig>'):
                time_sig_flag = True

            if time_sig_flag:
                if line.startswith('<sigN>'):
                    time_start = '<sigN>'
                    time_end = '</sigN>'
                    time_sig_value = line[len(time_start):-len(time_end)]
                    time_sig_numerator = int(time_sig_value)
                elif line.startswith('<sigD>'):
                    time_start = '<sigD>'
                    time_end = '</sigD>'
                    time_sig_value = line[len(time_start):-len(time_end)]
                    time_sig_denominator = int(time_sig_value)
                    self.time_sig = time_sig_numerator / time_sig_denominator
                    time_sig_flag = False

        print(self.tag_values)
        print(self.key_sig)
        print(self.time_sig)



