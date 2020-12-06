
class NoteConversions:

    scale_length = 7

    # converts a key signature accidental value to the natural of the major scale.
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

    # converts a key signature accidental value to the natural of the minor scale.
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

    # coverts a note letter to a C scale number used in harmonisation algorithm.
    note_letter_values = {
        'C': 0,
        'D': 1,
        'E': 2,
        'F': 3,
        'G': 4,
        'A': 5,
        'B': 6
    }

    # converts a naturalised tpc value (moved into the range 0-7) to its equivalent C scale number.
    tpc_to_scale = {
        0: 3,
        1: 0,
        2: 4,
        3: 1,
        4: 5,
        5: 2,
        6: 6
    }

    # converts a harmony note value to its equivalent natural pitch.
    note_to_pitch = {
        -11: 41,
        -10: 43,
        -9: 45,
        -8: 47,
        -7: 48,
        -6: 50,
        -5: 52,
        -4: 53,
        -3: 55,
        -2: 57,
        -1: 59,
        0: 60,
        1: 62,
        2: 64,
        3: 65,
        4: 67,
        5: 69,
        6: 71,
        7: 72,
        8: 74,
        9: 76,
        10: 77,
        11: 79,
        12: 81,
        13: 83,
        14: 84,
        15: 86,
        16: 88,
    }
