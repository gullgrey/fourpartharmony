from read_score import ReadScore
from write_score import WriteScore
from measure_chord import MeasureChord

# score = ReadScore("test.mscx")
score = ReadScore("four part test.mscx")

write_score = WriteScore(score)
print(write_score.anacrusis_length)
