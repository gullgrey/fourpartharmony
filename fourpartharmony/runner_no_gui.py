from read_score import ReadScore
from write_score import WriteScore
from write_three_part import WriteThreePart
from muse_melody import MuseMelody
from melody import Melody
from harmony import Harmony
from three_part_harmony import ThreePartHarmony
from chord_constructor import ChordConstructor


def main():

    file = input('File Name: ')
    major_minor = input('Is the melody Major (M) or minor (m)? ')
    instrument = input('Is the instrument a piano (p) or choir (c)? ')
    three_part = input('Is this a Four Part Harmony (4) or a Three Part Harmony (3)? ')

    if instrument == 'p':
        instrument = 'piano'
    if instrument == 'c':
        instrument = 'choir'

    file_type = '.mscx'
    if file.endswith(file_type) is False:
        file += file_type

    is_minor = False
    if major_minor in ['minor', 'Minor', 'm']:
        is_minor = True

    if three_part in ['Three Part Harmony', 'three part harmony', '3']:
        melody_position = input('What staff is the melody in?: ')
        score = ReadScore(file)
        muse_melody = MuseMelody(is_minor, score.key_sig, score.measure_chords)
        melody = Melody(muse_melody.soprano_list, muse_melody.key)
        harmony = Harmony(melody)
        ThreePartHarmony(harmony, melody_position, muse_melody.transpose_up)
        ChordConstructor(score, harmony)
        WriteThreePart(score, instrument, melody_position)
    elif three_part in ['Four Part Harmony', 'four part harmony', '4']:
        score = ReadScore(file)
        muse_melody = MuseMelody(is_minor, score.key_sig, score.measure_chords)
        melody = Melody(muse_melody.soprano_list, muse_melody.key)
        harmony = Harmony(melody)
        ChordConstructor(score, harmony)
        WriteScore(score, instrument)


if __name__ == "__main__":
    main()
