from note_conversions import NoteConversions


class ChordConstructor:

    def __init__(self, read_score, harmony):

        self.key_sig = int(read_score.key_sig)
        self.is_minor = harmony.melody.is_minor

        self.harmonised_notes = harmony.harmonised_notes
        self.measure_chords = read_score.measure_chords

        self.tpc_scale = []
        self.natural_key = None

        self.current_values = None
        self.current_mc = None

        self._set_tpc_scale()
        self._construct_chords()

    def _set_tpc_scale(self):

        scale_length = 7
        minor_adjust = 17
        major_adjust = 14
        minor_tpc_jumps = [0, 2, -3, -1, 1, -4, 5]
        major_tpc_jumps = [0, 2, 4, -1, 1, 3, 5]
        tpc_tonic = self.key_sig

        if self.is_minor:
            tpc_tonic += minor_adjust
            for jump in minor_tpc_jumps:
                self.tpc_scale.append(tpc_tonic + jump)

        else:
            tpc_tonic += major_adjust
            for jump in major_tpc_jumps:
                self.tpc_scale.append(tpc_tonic + jump)

        natural_tpc = (self.tpc_scale[0] + 1) % scale_length
        self.natural_key = NoteConversions.tpc_to_scale[natural_tpc]

    def _pitch_tpc_values(self, chord_position):

        note = self.current_values[chord_position]

        # converts note to its equivalent natural pitch.
        natural_pitch = NoteConversions.note_to_pitch[note]

        abs_note = note % NoteConversions.scale_length

        # finds where the position of the note is on the current key's scale
        tpc_position = (abs_note - self.natural_key) % NoteConversions.scale_length

        leading_note = False
        leading_note_position = 6
        if self.is_minor and tpc_position == leading_note_position:
            leading_note = True

        # the actual tpc value of the note.
        tpc = self.tpc_scale[tpc_position]

        # finds the true pitch of the note by checking if the tpc is flat, sharp or natural.
        pitch_adjust = 0
        natural_tpc_start = 13
        natural_tpc_end = 19
        flat_tpc_start = 6
        sharp_tpc_end = 26
        if tpc < natural_tpc_start:
            pitch_adjust -= 1
            # in case of double flat. *Note: should never occur
            if tpc < flat_tpc_start:
                pitch_adjust -= 1
        elif tpc > natural_tpc_end:
            pitch_adjust += 1
            # additional jump for double sharp for some minor leading notes.
            if tpc > sharp_tpc_end:
                pitch_adjust += 1
        pitch = natural_pitch + pitch_adjust

        return [str(pitch), str(tpc), leading_note]

    def _construct_chords(self):

        for position in range(len(self.measure_chords)):
            self.current_values = self.harmonised_notes[position].get_harmonies()
            self.current_mc = self.measure_chords[position]

            self.current_mc.chord = self.current_values[0]

            alto_values = self._pitch_tpc_values(1)
            self.current_mc.alto_pitch = alto_values[0]
            self.current_mc.alto_tpc = alto_values[1]
            self.current_mc.alto_leading_note = alto_values[2]

            tenor_values = self._pitch_tpc_values(2)
            self.current_mc.tenor_pitch = tenor_values[0]
            self.current_mc.tenor_tpc = tenor_values[1]
            self.current_mc.tenor_leading_note = alto_values[2]

            bass_values = self._pitch_tpc_values(3)
            self.current_mc.bass_pitch = bass_values[0]
            self.current_mc.bass_tpc = bass_values[1]
            self.current_mc.bass_leading_note = alto_values[2]

            print(self.current_mc.chord)
            print(alto_values)
            print(tenor_values)
            print(bass_values)
