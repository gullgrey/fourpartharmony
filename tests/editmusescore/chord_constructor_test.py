from read_score import ReadScore
from muse_melody import MuseMelody
from chord_constructor import ChordConstructor
from melody import Melody
from harmony import Harmony

# score = ReadScore("test.mscx")
score = ReadScore("four part test 2.mscx")

muse_melody = MuseMelody(True, score.key_sig, score.measure_chords)
melody = Melody(muse_melody.soprano_list, muse_melody.key)
harmony = Harmony(melody)
ChordConstructor(score, harmony)
harmony.print_notes()
