from random import randrange, randint

from harmony import Harmony
from melody import Melody

melody_length = 10
soprano_list1 = []
for note in range(0, melody_length):
    soprano_list1.append(randrange(0, 12))

key = randint(0, 6)
minor = True

# soprano_list1 = [0,0,4,4,4,5,4,3,3,2,2,1,1,0]
# key = 4
# note_counter = 0
# for note in soprano_list1:
#     soprano_list1[note_counter] += key
#     note_counter += 1

melody1 = Melody(soprano_list1, (key, minor))

print('Melody: ' + str(soprano_list1))
print('Key: ' + str(key))
print('Chord Notes: ' + str(melody1.chord_notes))
print('\n')

harmony = Harmony(melody1)
harmony.print_notes()
