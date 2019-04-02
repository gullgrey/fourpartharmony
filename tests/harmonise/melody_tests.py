from random import randint, shuffle

from melody import Melody, invalid_consecutives

soprano_list1 = list(range(4, 11))
key = randint(0, 7)
shuffle(soprano_list1)

melody1 = Melody(soprano_list1, (key, True))
print(melody1.in_soprano_range(-7))

print(invalid_consecutives(4,0,9,5))