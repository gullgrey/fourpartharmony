from read_score import ReadScore
from write_score import WriteScore
from write_three_part import WriteThreePart
from muse_melody import MuseMelody
from melody import Melody
from harmony import Harmony
from chord_constructor import ChordConstructor
from three_part_harmony import ThreePartHarmony
from os import startfile
from measure_chord import MeasureChord

score = ReadScore("test.mscx")
# score = ReadScore("four part test.mscx")
# score = ReadScore("Twinkle_Twinkle_Test_2.mscx")
# score = ReadScore("Mary Lamb Test.mscx")
minor = False
three_part = True
instrument = 'Choir'
melody_position = 'Staff 1'

muse_melody = MuseMelody(minor, score.key_sig, score.measure_chords)
melody = Melody(muse_melody.soprano_list, muse_melody.key)
harmony = Harmony(melody)
# harmony.set_three_part()
if three_part:
    ThreePartHarmony(harmony, melody_position, muse_melody.transpose_up)
ChordConstructor(score, harmony)

# for x in range(10):
#     note = score.measure_chords[x]
#     note.alto_leading_note = True
#     note.alto_pitch = '56'
#     note.alto_tpc = '22'

if three_part:
    write_score = WriteThreePart(score, instrument, melody_position)
else:
    write_score = WriteScore(score, instrument)

startfile(write_score.file_name)
print(write_score.anacrusis_length)
print(write_score.measure_length)
