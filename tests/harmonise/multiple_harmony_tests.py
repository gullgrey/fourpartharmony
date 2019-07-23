from random import randrange, randint

from harmonise_exceptions import HarmonisationError
from harmony import Harmony
from melody import Melody

failed_attempts = 0
melody_length = 7
for x in range(30):

    soprano_list1 = []
    for note in range(0, melody_length):
        soprano_list1.append(randrange(0, 12))

    key = randint(0, 6)
    minor = True

    # soprano_list1 = [10,9,8,8,6,5,4]
    # key = 4

    melody1 = Melody(soprano_list1, (key, minor))

    try:
        harmony = Harmony(melody1)
    except HarmonisationError:
        failed_attempts += 1
        print('Melody: ' + str(soprano_list1))
        print('Key: ' + str(key))
        print('Chord Notes: ' + str(melody1.chord_notes))
        print('\n')

print('Failed Attempts: ' + str(failed_attempts))
