from read_score import ReadScore
from measure_chord import MeasureChord

score = ReadScore("test.mscx")
# score = ReadScore("four part test 2.mscx")

print(score.tag_values)
print(score.anacrusis)
print(score.key_sig)
print(score.time_sig_numerator)
print(score.time_sig_denominator)
print()

for value in score.measure_values:
    print(value.dots)
    print(value.duration)
    print(value.note_length)
    if isinstance(value, MeasureChord):
        print(value.accidental)
        print(value.soprano_pitch)
        print(value.soprano_tpc)
    print()
