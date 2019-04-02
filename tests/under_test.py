from general_test import *

note1 = FirstNote(1)
print(note1.melody)
note1.print_info()
print()
note2 = CurrentNote(note1)
note2.print_info()
print()
note3 = CurrentNote(note2)
note3.print_info()
print()
note4 = CurrentNote(note1)
note4.print_info()

print( note2._get_melody())
print( _under_test())
