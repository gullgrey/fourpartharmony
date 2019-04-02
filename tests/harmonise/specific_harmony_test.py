from harmony import Harmony
from melody import Melody

soprano_list1 = [0, 6, 0]
key = 0
minor = False

melody1 = Melody(soprano_list1, (key, minor))

print('Melody: ' + str(soprano_list1))
print('Key: ' + str(key))
print('Chord Notes: ' + str(melody1.chord_notes))
print('\n')

harmony = Harmony(melody1)
harmony.print_notes()