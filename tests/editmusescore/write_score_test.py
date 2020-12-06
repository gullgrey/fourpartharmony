from read_score import ReadScore
from write_score import WriteScore
from muse_melody import MuseMelody
from melody import Melody
from harmony import Harmony
from chord_constructor import ChordConstructor
from three_part_harmony import ThreePartHarmony
from measure_chord import MeasureChord

# score = ReadScore("test.mscx")
# score = ReadScore("four part test.mscx")
# score = ReadScore("Twinkle_Twinkle_Test_2.mscx")
score = ReadScore("Mary Lamb Test.mscx")
minor = False
three_part = True

muse_melody = MuseMelody(minor, score.key_sig, score.measure_chords)
melody = Melody(muse_melody.soprano_list, muse_melody.key)
harmony = Harmony(melody)
# harmony.set_three_part()
if three_part:
    ThreePartHarmony(harmony, 'Staff 1', muse_melody.transpose_up)
ChordConstructor(score, harmony)

# for x in range(10):
#     note = score.measure_chords[x]
#     note.alto_leading_note = True
#     note.alto_pitch = '56'
#     note.alto_tpc = '22'

write_score = WriteScore(score)
print(write_score.anacrusis_length)
print(write_score.measure_length)
