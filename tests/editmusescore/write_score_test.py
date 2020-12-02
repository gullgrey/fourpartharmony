from read_score import ReadScore
from write_score import WriteScore
from muse_melody import MuseMelody
from melody import Melody
from harmony import Harmony
from chord_constructor import ChordConstructor
from measure_chord import MeasureChord

# score = ReadScore("test.mscx")
# score = ReadScore("four part test.mscx")
score = ReadScore("Twinkle Twinkle Test 1.mscx")

muse_melody = MuseMelody(True, score.key_sig, score.measure_chords)
melody = Melody(muse_melody.soprano_list, muse_melody.key)
harmony = Harmony(melody)
ChordConstructor(score, harmony)

# for x in range(10):
#     note = score.measure_chords[x]
#     note.alto_leading_note = True
#     note.alto_pitch = '56'
#     note.alto_tpc = '22'

write_score = WriteScore(score)
print(write_score.anacrusis_length)
print(write_score.measure_length)
