from read_score import ReadScore
from write_score import WriteScore
from muse_melody import MuseMelody
from melody import Melody
from harmony import Harmony
from chord_constructor import ChordConstructor

if __name__ == "__main__":

    file = input('File Name: ')
    major_minor = input('Is the melody Major (M) or minor (m)? ')

    file_type = '.mscx'
    if file.endswith(file_type) is False:
        file += file_type

    is_minor = False
    if major_minor in ['minor', 'Minor', 'm']:
        is_minor = True

    score = ReadScore(file)
    muse_melody = MuseMelody(is_minor, score.key_sig, score.measure_chords)
    melody = Melody(muse_melody.soprano_list, muse_melody.key)
    harmony = Harmony(melody)
    ChordConstructor(score, harmony)
    WriteScore(score)
