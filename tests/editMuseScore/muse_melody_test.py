from read_score import ReadScore
from muse_melody import MuseMelody

# score = ReadScore("test.mscx")
score = ReadScore("four part test 2.mscx")

melody = MuseMelody(False, score.key_sig, score.measure_chords)
print(melody.key)
print(melody.soprano_list)