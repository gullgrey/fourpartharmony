from harmony import Harmony
from melody import Melody

# soprano_list1 = [0,0,4,4,4,5,4,3,3,2,2,1,1,0]
soprano_list1 = [8,2,2]
key = 2
minor = True

melody1 = Melody(soprano_list1, (key, minor))

print('Melody: ' + str(soprano_list1))
print('Key: ' + str(key))
print('Chord Notes: ' + str(melody1.chord_notes))
print('\n')

harmony = Harmony(melody1)
harmony.print_notes()
