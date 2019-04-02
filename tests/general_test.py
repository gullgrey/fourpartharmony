class CurrentNote:

    def __init__(self, current_note):

        if current_note is None:
            self.melody = None
        else:
            self.melody = current_note._get_melody()

        self.prev_note = current_note

    def print_info(self):
        print(self.melody)
        if self.prev_note is not None:
            self.prev_note.print_info()
        else:
            print(self.prev_note)

    def _get_melody(self):
        return self.melody


class FirstNote(CurrentNote):

    def __init__(self, melody):
        super().__init__(None)
        self.melody = melody


def _under_test():
    return 'It worked'
