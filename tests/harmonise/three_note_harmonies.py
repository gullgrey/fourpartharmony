from random import randint

from harmonise_exceptions import HarmonisationError
from harmony import Harmony
from melody import Melody

failed_attempts = 0
soprano_range = list(range(12))
for first_note in soprano_range:
    for second_note in soprano_range:
        for third_note in soprano_range:
            soprano_list = [first_note, second_note, third_note]
            # key = randint(0, 6)
            key = 0
            minor = False

            # soprano_list1 = [10,9,8,8,6,5,4]
            # key = 4

            melody1 = Melody(soprano_list, (key, minor))

            try:
                harmony = Harmony(melody1)
            except HarmonisationError:
                failed_attempts += 1
                print('Melody: ' + str(soprano_list))
                print('Key: ' + str(key))
                print('Chord Notes: ' + str(melody1.chord_notes))
                print('\n')

            # print(soprano_list)
print('Failed Attempts: ' + str(failed_attempts))
