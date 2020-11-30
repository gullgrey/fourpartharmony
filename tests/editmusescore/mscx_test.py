from mscx import Mscx


print(Mscx.beginning)
tag_names = ["arranger", "composer", "copyright", "creationDate", "lyricist",
             "movementNumber", "movementTitle", "platform", "poet",
             "source", "translator", "workNumber", "workTitle"]
tag_text = Mscx.meta_tags.format(*tag_names)
print(tag_text)
print(Mscx.parts)

file = open("written file.mscx", "w")
file.write(Mscx.beginning)
file.write(tag_text)
file.write(Mscx.parts)
file.write(Mscx.staff_start.format("1"))
file.write(Mscx.vbox_start)
file.close()
