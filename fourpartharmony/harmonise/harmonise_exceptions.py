
class EmptyNodeError(Exception):

    def __init__(self, message):
        super().__init__(message)


class SopranoRangeError(Exception):

    def __init__(self, message):
        super().__init__(message)


class HarmonisationError(Exception):

    def __init__(self, message):
        super().__init__(message)


class EmptyMelodyError(Exception):

    def __init__(self, message):
        super().__init__(message)
