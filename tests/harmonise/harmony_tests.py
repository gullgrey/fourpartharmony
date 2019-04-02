from random import shuffle, randint, randrange

from alto_note import AltoNote
from melody import Melody, Interval
from chord import Chord
from current_note import CurrentNote, FirstNote
from bass_note import BassNote
from tenor_note import TenorNote

melody_length = 7
soprano_list1 = []
for note in range(0, melody_length):
    soprano_list1.append(randrange(0, 12))

key = randint(0, 6)

# soprano_list1 = [2, 1, 0, 1,2,3]
# key = 0

melody1 = Melody(soprano_list1, (key, True))

bass_list1 = list(range(melody1.bass_lower, melody1.bass_upper + 1))
tenor_list1 = list(range(melody1.tenor_lower, melody1.tenor_upper + 1))
alto_list1 = list(range(melody1.alto_lower, melody1.alto_upper + 1))  \
             + [randint(melody1.alto_lower, melody1.alto_upper)]
# bass_list1 = [-11, -1, -10, -5, -4, 0, -6, -7, -8, -2, -9, -3]

shuffle(bass_list1)
shuffle(alto_list1)
shuffle(tenor_list1)

print('Melody: ' + str(soprano_list1))
print('Bass List: ' + str(bass_list1))
print('Key: ' + str(key))
print('Chord Notes: ' + str(melody1.chord_notes))
print('\n')


harmony_list1 = []
note_counter = 0
for note in soprano_list1:
    if note_counter == 0:
        new_note = FirstNote(melody1)
    else:
        new_note = CurrentNote(harmony_list1[-1])
    new_chord = Chord(new_note)
    new_note.chord = new_chord

    print('Chord Nodes: ' + str(new_chord.nodes))
    print('Chord: ' + str(new_chord.value))
    print('Soprano: ' + str(new_note.soprano))

    new_bass = BassNote(new_note)
    # new_bass.value = bass_list1[note_counter]
    new_note.bass = new_bass

    print('Bass Nodes: ' + str(new_bass.nodes))
    print('Bass: ' + str(new_note.bass.value) + ' | '
          + str(new_note.bass.chord) + str(new_note.bass.inversion()))

    new_tenor = TenorNote(new_note)
    # new_tenor.value = tenor_list1[note_counter]
    new_note.set_tenor(new_tenor)

    print('Tenor Nodes: ' + str(new_tenor.nodes))
    print('Tenor: ' + str(new_note.tenor.value))
    print('Potential Degrees: ' + str(new_tenor.potential_degrees))

    new_alto = AltoNote(new_note)
    # new_alto.value = alto_list1[note_counter]
    new_note.set_alto(new_alto)

    print('Alto: '+ str(new_alto.value))

    print('\n')

    harmony_list1.append(new_note)
    note_counter += 1
